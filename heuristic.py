# PSEUDOCODE
# read in input
# create a list of calculated sums (initialize with 1)
# for each number x in the sequence, add the last number n in sums and the next largest number that is less than or equal to x - n 
# add the calculated sum to sums, store both numbers as a tuple for later
# repeat until all numbers in the sequence are calculated
# return number of sums we've calculated
import os

class Solver():
    def __init__(self, inputFile):
        self.sequence = self.readInput(inputFile) # reads in a sequence from a group's input file
        self.operations = []
        self.sums = []
        # self.differences = []
        # self.findDifferences()
        self.findSums()
        # print(len(self.operations))
        # print(self.operations)
    
    def readInput(self, filename) -> list:
        file = open(filename, 'r')
        sumCount = int(file.readline())
        nums = []

        line = file.readline()
        for number in line.split():
            nums.append(int(number))

        file.close()
        return nums

    def nextBiggestNum(self, nextNum, lastSum):
        target = nextNum - lastSum
        # self.differences.append(target)
        lo = 0
        hi = len(self.sums) - 1
        curBest = 1
        while lo < hi:
            mid = (hi + lo) // 2
            if self.sums[mid] < target:
                if self.sums[mid] > curBest:
                    curBest = self.sums[mid]
                lo = mid + 1
            elif self.sums[mid] > target:
                hi = mid
            else:
                return self.sums[mid]
        return curBest
    
    def findSums(self):
        self.sums = [1]
        for nextNum in self.sequence:
            while self.sums[-1] != nextNum:
                num1 = self.sums[-1]
                num2 = self.nextBiggestNum(nextNum,num1)
                self.operations.append((num1,num2))
                self.sums.append(num1 + num2)
        # return sums

for filename in os.listdir('./inputs'):
    groupName = filename.replace("input_","")
    H = Solver(f"./inputs/input_{groupName}")
    f = open(f"./our_outputs/output_{groupName}", "w")
    f.write(str(len(H.operations)) + "\n")
    for operation in H.operations:
        f.write(f"{operation[0]} {operation[1]} \n")
    f.close()

# groupName = filename.replace("input_","")
# H = Solver(f"./inputs/input_group568.txt")
# f = open(f"./our_outputs/output_group568.txt", "w")
# f.write(str(len(H.operations)) + "\n")
# for operation in H.operations:
#     f.write(f"{operation[0]} {operation[1]} \n")
# f.close()