class Solution:
    def smallestNumber(self, num: str, t: int) -> str:
        c2 = c3 = c5 = c7 = 0
        temp_t = t
        
        while temp_t % 2 == 0: temp_t //= 2; c2 += 1
        while temp_t % 3 == 0: temp_t //= 3; c3 += 1
        while temp_t % 5 == 0: temp_t //= 5; c5 += 1
        while temp_t % 7 == 0: temp_t //= 7; c7 += 1

        if temp_t > 1:
            return "-1"

        def get_factor_count(n: int, p: int) -> int:
            cnt = 0
            while n > 0 and n % p == 0:
                cnt += 1
                n //= p
            return cnt

        def get_min_digits_needed(r2: int, r3: int, r5: int, r7: int) -> int:
            c8, rem2 = divmod(r2, 3)
            c9, rem3 = divmod(r3, 2)
            c6 = c4 = c2_rem = c3_rem = 0

            if rem2 == 2:
                c4 = 1
            elif rem2 == 1:
                if rem3 == 1:
                    c6 = 1
                    rem3 = 0
                else:
                    c2_rem = 1

            if rem3 == 1:
                c3_rem = 1

            return c8 + c9 + c6 + c4 + c2_rem + c3_rem + r5 + r7

        def fill_trailing(res_chars: list[str], rem_len: int, r2: int, r3: int, r5: int, r7: int):
            for pos in range(rem_len):
                needed_for_rest = rem_len - 1 - pos
                for d in range(1, 10):
                    next2 = max(0, r2 - get_factor_count(d, 2))
                    next3 = max(0, r3 - get_factor_count(d, 3))
                    next5 = max(0, r5 - get_factor_count(d, 5))
                    next7 = max(0, r7 - get_factor_count(d, 7))

                    if get_min_digits_needed(next2, next3, next5, next7) <= needed_for_rest:
                        res_chars.append(str(d))
                        r2, r3, r5, r7 = next2, next3, next5, next7
                        break

        n = len(num)
        num_digits = [int(c) for c in num]

        max_prefix = n
        for i in range(n):
            if num_digits[i] == 0:
                max_prefix = i
                break

        pref2, pref3, pref5, pref7 = [0] * (n + 1), [0] * (n + 1), [0] * (n + 1), [0] * (n + 1)
        for i in range(max_prefix):
            d = num_digits[i]
            pref2[i + 1] = pref2[i] + get_factor_count(d, 2)
            pref3[i + 1] = pref3[i] + get_factor_count(d, 3)
            pref5[i + 1] = pref5[i] + get_factor_count(d, 5)
            pref7[i + 1] = pref7[i] + get_factor_count(d, 7)

        for L in range(max_prefix, -1, -1):
            req2 = max(0, c2 - pref2[L])
            req3 = max(0, c3 - pref3[L])
            req5 = max(0, c5 - pref5[L])
            req7 = max(0, c7 - pref7[L])

            if L == n:
                if get_min_digits_needed(req2, req3, req5, req7) == 0:
                    return num
                continue

            start_digit = num_digits[L] + 1

            for d in range(start_digit, 10):
                r2 = max(0, req2 - get_factor_count(d, 2))
                r3 = max(0, req3 - get_factor_count(d, 3))
                r5 = max(0, req5 - get_factor_count(d, 5))
                r7 = max(0, req7 - get_factor_count(d, 7))

                min_len_needed = get_min_digits_needed(r2, r3, r5, r7)
                rem_len = n - 1 - L

                if min_len_needed <= rem_len:
                    res = [str(num_digits[i]) for i in range(L)]
                    res.append(str(d))
                    fill_trailing(res, rem_len, r2, r3, r5, r7)
                    return "".join(res)

        min_len_needed = get_min_digits_needed(c2, c3, c5, c7)
        total_len = max(n + 1, min_len_needed)

        res = []
        fill_trailing(res, total_len, c2, c3, c5, c7)
        return "".join(res)