class Problem:

    def solve(self):
        print("Solving ArrangeChar")
        input = ['G','G','R','B','B','R','R','B']
        print("Provided Array:", input)

        ptR = 0
        ptG = 1
        ptB = len(input)-1

        while input[ptR]=='R':
            ptR+=1
            ptG+=1

        while input[ptB]=='B':
            ptB-=1

        while ptG <= ptB :
            if input[ptG]=='R' :
                input[ptG] = input[ptR]
                input[ptR] = 'R'
                print("   r:", ptR, ", g:", ptG, ", b:", ptB, " Array:", input)
                ptR+=1
            elif input[ptG]=='B' :
                input[ptG] = input[ptB]
                input[ptB] = 'B'
                print("   r:", ptR, ", g:", ptG, ", b:", ptB, " Array:", input)
                ptB-=1
            else:
                ptG+=1

        print("Processed Array:", input)
        return