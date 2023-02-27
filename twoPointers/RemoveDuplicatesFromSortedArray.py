class Problem:

    def solve(self):
        '''
        lst = [0,0,1,1,1,2,2,3,3,4]
        2 pointers i, j = 0, 1

        '''
        nums = [0,0,1,1,1,2,2,3,3,4]

        i, j = 0, 1
        while j < len(nums):

            # Condition for identifying duplicates
            # Condition for identifying unique elements
            if nums[j] != nums[j - 1]:
                i += 1
                nums[i] = nums[j]

            j += 1

        return i + 1