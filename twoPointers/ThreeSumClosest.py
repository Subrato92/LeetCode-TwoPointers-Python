class Problem:
    def solve(self):
        nums = [-576, 743, 630, 477, -728, 750, 756, -243, 57, -828, -567, 132, -464, -281, 334, -553, 666, -193, -726,
                514, 83, 282, -32, -852, -513, -469, 100, -813, -528, -959, 758, -155, 195, 780, -963, 561, 177, 185,
                -98, -23, -541, -801, 801, 158, -925, -731, -89, 490, 278, 75, 122, 632, -805, -529, 748, -27, 869,
                -730, 859, 71, -621, 693, 298, 383, -315, -342, 244, -103, -588, 5, 318, -291, -206, -460, 188, -495,
                -550, 170, -939, 119, -479, 818, -441, -530, 222, -253, 265, 395, -718, -70, 133, 425, -41, -543, -309,
                -391, 481, 355, -999, 623, 667, -242, -461, -714, 823, -8, -346, 340, -642, -740, -866, -368, -850,
                -313, -336, 402, 698, -144, -577, 774, 56, -602, 940, 549, 754, -376, -57, 9, -238, 205, 678, -199, 529,
                -503, -974, -867, 409, 534, 576, -649, 951, 155, 530, 304, -674, 479, -603, 958, 264, -535, 730, -727,
                506, -191, 476, 776, -596, -216, -173, -21, -249, -6, 684, 559, -961, 557, -967, -157, 354, -340, -423,
                -918, 773, -625, -636, 970, -843, -840, -218, -746, -498, 767, 533, -117, 280, -995, -239, -254, 198,
                -174, -354, 38, 638, 301, 262, 149, -44, 896, -108, -330, 453, 462, 157, -299, 279, -829, 876, -186,
                -240, -660, -880, 622, 802, -488, -857, 434, -465, 868, 972, -691, -252, 669, 93, 850, 891, -823, -298,
                -873, 64, -473, -491, -574, -507, 646, 882, 489, -399, 564, 415, 788, 300, 62, -695, 625, -439, 147,
                913, -392, -421, 610, -632, -643, -819, -303, 87, -800, -942, 13, 154, 90, -113, -928, 839, -712, 637,
                -768, -234, 39, -295, -51, -587, -770, 161, 760, -130, -92, -451, -445, -926, 153, 497, -26, -725, -458,
                -11, -656, 973, 143, 982, 160, 414, 396, 733, 96, 211, 254, 796, 440, 220, 50, 499, -386, 292, 574, 317,
                -276, -133, -547, -264, -817, -411, -938, 98, 35, -384, -763, 208, 906, 88, 647, 194, 947, 496, 711,
                -162, 704, -48, 116, 551, -181, 651, 364, -105, -633, 175, -177, -992, 665, -954, 76, -841, 69, 193,
                -703, -902, -413, -922, -855, 975, -548, 260, 617, 797, 654, -767, -300, -987, -334, 445, 642, 105, 952,
                350, -115, 676, -487, -533, 892, 732, -721, -572, -20, -419, 602, 749, -463, -911, 812, -706, 319, 115,
                -589, 104, 266, -609, 142, -154, 828, 45, -872, -416, -774, -43, 528, -80, -422, -429, -986, -970, 953,
                626, -215, 214, 136, 190, 431, 204, -128, 311, 854, -810, -323, -915, -472, 186, 619, 79, 875, -779,
                -534, 611, 682, 531, -614, -581, -524, -414, 939, 565, -49, 535, -241, 467, 313, -1, 679, 43, 606, 270,
                -431, -832, -522, 0, 697, -287, 19, 948, -147, -601, -729, -362, -753, -145, 518, -75, -777, 12, 252,
                114, -759, -179, -584, -212, 173, -141, 361, -142, -858, -772, -250, -151, 694, 867, 138, -29, -466,
                -77, -374, -201, -778, 135, 890, -662, -457, 151, 790, 956, -459, 68, -784, 437, 217, -927, 993, -290,
                899, -183, -10, 795, 257]
        target = 4815
        self.revApproach(nums, target)

    def revApproach(self, nums, target):
        isNeg = False
        if target < 0:
            nums = list(map(lambda x: (-1) * x, nums))
            target *= -1
            isNeg = True

        nums.sort()

        i = 0
        minDiff = 1000000
        sum = 0
        while i < len(nums) - 2:
            j = i + 1
            k = len(nums) - 1
            t2 = target - nums[i]
            while j < k:
                diff = abs(t2 - nums[j] - nums[k])
                if diff < minDiff:
                    minDiff = diff
                    sum = (nums[i] + nums[j] + nums[k])
                    if isNeg:
                        sum *= -1
                    if diff == 0:
                        print("Ans:", sum)
                        return sum

                if abs(t2 - nums[j + 1] - nums[k]) < diff:
                    j += 1
                elif abs(t2 - nums[j] - nums[k - 1]) < diff:
                    k -= 1
                else:
                    j += 1
                    k -= 1
            i += 1

        print("Ans:", sum)
        return sum

    def bsApproach(self, nums, target):
        minDiff = 10000
        sum = 0
        i = 0

        nums.sort()
        print(nums)

        while i < len(nums) - 1:
            j = i + 1
            while j < len(nums):
                t2 = target - nums[i] - nums[j]
                k = self.bs(nums, t2, i, j)
                if t2 == nums[k]:
                    sum = nums[i] + nums[j] + nums[k]
                    print("Ans:", sum)
                    return sum
                elif minDiff > abs(t2 - nums[k]):
                    minDiff = abs(t2 - nums[k])
                    sum = nums[i] + nums[j] + nums[k]
                j += 1
            i += 1

        print("Ans:", sum)
        return sum

    def bs(self, nums, ele, i, j):
        start = 0
        end = len(nums)

        if start == i:
            start+=1

        if end == j:
            end-=1

        if end == i:
            end-=1

        diff = 1000000
        indx = -1

        while start<end :
            mid = (int)((end + start) / 2)

            if abs(nums[mid] - ele) < diff and mid!=i and mid!=j:
                diff = abs(nums[mid] - ele)
                indx = mid

            if nums[mid] < ele :
                start = mid+1
            elif nums[mid] == ele and mid != i and mid != j:
                return mid
            else :
                end = mid-1

            if start == i or start == j:
                start += 1

            if end == i or end == j:
                end -= 1

        return indx
