/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
#include <stdlib.h>
#include <string.h>

typedef struct {
    char leftChar;
    char rightChar;
    int length;
    int prefix;
    int suffix;
    int best;
} Node;

Node mergeNodes(Node left, Node right) {
    Node res;

    res.leftChar = left.leftChar;
    res.rightChar = right.rightChar;
    res.length = left.length + right.length;

    res.prefix = left.prefix;

    if (
        left.rightChar == right.leftChar &&
        left.prefix == left.length
    ) {
        res.prefix = left.length + right.prefix;
    }

    res.suffix = right.suffix;

    if (
        left.rightChar == right.leftChar &&
        right.suffix == right.length
    ) {
        res.suffix = right.length + left.suffix;
    }

    res.best = left.best > right.best
        ? left.best
        : right.best;

    if (left.rightChar == right.leftChar) {
        int combined = left.suffix + right.prefix;

        if (combined > res.best) {
            res.best = combined;
        }
    }

    return res;
}

void build(
    Node* tree,
    const char* s,
    int node,
    int start,
    int end
) {
    if (start == end) {
        tree[node] = (Node){
            s[start],
            s[start],
            1,
            1,
            1,
            1
        };
        return;
    }

    int mid = (start + end) / 2;

    build(tree, s, node * 2, start, mid);
    build(tree, s, node * 2 + 1, mid + 1, end);

    tree[node] = mergeNodes(
        tree[node * 2],
        tree[node * 2 + 1]
    );
}

void update(
    Node* tree,
    int node,
    int start,
    int end,
    int index,
    char ch
) {
    if (start == end) {
        tree[node] = (Node){
            ch,
            ch,
            1,
            1,
            1,
            1
        };
        return;
    }

    int mid = (start + end) / 2;

    if (index <= mid) {
        update(tree, node * 2, start, mid, index, ch);
    } else {
        update(tree, node * 2 + 1, mid + 1, end, index, ch);
    }

    tree[node] = mergeNodes(
        tree[node * 2],
        tree[node * 2 + 1]
    );
}

int* longestRepeating(char* s, char* queryCharacters, int* queryIndices, int queryIndicesSize, int* returnSize) {
    int n = strlen(s);
    Node* tree = (Node*)malloc(
        sizeof(Node) * 4 * n
    );

    build(tree, s, 1, 0, n - 1);
    int* answer = (int*)malloc(
        sizeof(int) * queryIndicesSize
    );

    for (int i = 0; i < queryIndicesSize; i++) {
        update(tree, 1, 0, n - 1, queryIndices[i], queryCharacters[i]);
        answer[i] = tree[1].best;
    }

    free(tree);
    *returnSize = queryIndicesSize;

    return answer;
}