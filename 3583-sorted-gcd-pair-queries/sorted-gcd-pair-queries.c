#include <stdlib.h>

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* gcdValues(int* nums, int numsSize, long long* queries, int queriesSize, int* returnSize) {
    // Determine the maximum element in the dataset to set limits for our sieve array sizes
    int maxVal = 0;
    for (int i = 0; i < numsSize; i++) {
        if (nums[i] > maxVal) {
            maxVal = nums[i];
        }
    }

    // Allocate an array to count the occurrence frequency of each number up to maxVal
    int* counts = (int*)calloc(maxVal + 1, sizeof(int));
    for (int i = 0; i < numsSize; i++) {
        counts[nums[i]]++;
    }

    // Allocate space to store the exact number of pairs yielding a specific GCD value
    long long* exactGcdPairs = (long long*)calloc(maxVal + 1, sizeof(long long));
    
    // Process backwards to easily filter out contributions belonging to higher multiples
    for (int i = maxVal; i >= 1; i--) {
        long long multiplesCount = 0;
        
        // Sum up frequencies of all numbers that are perfectly divisible by 'i'
        for (int j = i; j <= maxVal; j += i) {
            multiplesCount += counts[j];
        }
        
        // Compute total combination choices of pairs that share 'i' as a common divisor
        long long totalPairsWithDivisor = (multiplesCount * (multiplesCount - 1)) / 2;
        
        // Subtract counts belonging to larger multiples of 'i' to isolate pairs where GCD is exactly 'i'
        for (int j = 2 * i; j <= maxVal; j += i) {
            totalPairsWithDivisor -= exactGcdPairs[j];
        }
        exactGcdPairs[i] = totalPairsWithDivisor;
    }

    // Build a prefix sum array to keep track of the cumulative number of pairs up to GCD 'i'
    long long* prefixSum = (long long*)calloc(maxVal + 1, sizeof(long long));
    for (int i = 1; i <= maxVal; i++) {
        prefixSum[i] = prefixSum[i - 1] + exactGcdPairs[i];
    }

    // Allocate memory for the final output array that will hold the answers for each query index
    int* answer = (int*)malloc(queriesSize * sizeof(int));
    *returnSize = queriesSize; // Tell the caller the absolute size of the returned array

    // Process each query position via a custom upper_bound binary search over our distribution table
    for (int i = 0; i < queriesSize; i++) {
        long long targetIndex = queries[i];
        
        int low = 1, high = maxVal, result = maxVal;
        while (low <= high) {
            int mid = low + (high - low) / 2;
            
            // If prefix sum is strictly greater, it covers the index. Record it and try to search left.
            if (prefixSum[mid] > targetIndex) {
                result = mid;
                high = mid - 1; 
            } else {
                // Otherwise, the current prefix window isn't big enough yet. Search right.
                low = mid + 1;
            }
        }
        answer[i] = result;
    }

    // Free local dynamic storage buffers to prevent memory leaks before returning the response
    free(counts);
    free(exactGcdPairs);
    free(prefixSum);

    return answer;
}