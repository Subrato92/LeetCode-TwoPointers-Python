class Problem:
    def solve(self):
        height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
        print("heit:", height)
        nlvl = []
        nlvr = []
        lvl = 0
        nlvl.append(lvl)
        for i in range(len(height)-1) :
            if height[i] > height[lvl] :
                lvl = i
            nlvl.append(lvl)

        print("nlvl:", nlvl)

        lvr = len(height) - 1
        nlvr.append(lvr)
        for i in range(len(height)-2, -1, -1) :
            if height[i] > height[lvr] :
                lvr = i
            nlvr.append(lvr)

        nlvr.reverse()
        print("nlvr:", nlvr)

        sum = 0
        for i in range(len(height)-2) :
            lhl = height[nlvl[i]]
            lhr = height[nlvr[i]]

            if lhl==height[i] or lhr==height[i] :
                pass

            minHt = min(lhl, lhr)

            diffHt = minHt - height[i]
            if diffHt > 0 :
                sum += diffHt
                print("   Added Water:", diffHt,", i:", i)
        print("totalWater:", sum)

        return sum