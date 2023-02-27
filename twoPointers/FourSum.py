class Problem:

    def solve(self):
        nums = [1, 0, -1, 0, -2, 2]
        target = 0

        nums.sort()
        print(nums)
        i = 0
        minDiff = 10000000000
        setValue = set()
        while i < len(nums) - 3:
            j = i + 1
            print(" [", i, j, "]")
            while j < len(nums) - 2:
                k = j + 1
                l = len(nums) - 1
                print("  [", i, j, k, l, "]")
                while k < l:
                    diff = target - nums[i] - nums[j] - nums[k] - nums[l]
                    print("   [", i, j, k, l, "]")
                    if diff == 0:
                        lst = (nums[i], nums[j], nums[k], nums[l])
                        setValue.add(lst)

                    if diff < minDiff:
                        minDiff = diff
                    t2 = target - nums[i] - nums[j]
                    if  t2 > (nums[k] + nums[l]) :
                        k += 1
                    elif t2 < (nums[k] + nums[l]):
                        l -= 1
                    else:
                        l -= 1
                        k += 1
                j += 1
            i += 1

        ans = list(map(list, setValue))
        print("ans:", ans)
        return ans