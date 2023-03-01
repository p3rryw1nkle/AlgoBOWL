# from collections import defaultdict
import sys, os

class Verifier():
    def __init__(self, filename):
        self.sequence = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
        # self.sequence = [2,5]
        # self.sequence = self.readInput(filename)
        self.sums = self.readOutput(filename)
        self.result = self.checkSums()

    def readInput(self, filename) -> list:
        file = open(filename, 'r')
        sumCount = int(file.readline()) # read in how many nodes there are from first line
        nums = []

        line = file.readline()
        for number in line.split():
            nums.append(number)

        file.close()
        return nums

    def readOutput(self, filename) -> list:
        file = open(filename, 'r')
        sumCount = int(file.readline()) # read in how many nodes there are from first line
        sums = {1}

        for operation in range(sumCount):
            line = file.readline()
            if not line:
                break
            summation = line.split(' ')
            num1 = int(summation[0])
            num2 = int(summation[1])
            if (num1 in sums) and (num2 in sums):
                sums.add(int(summation[0]) + int(summation[1]))
            else:
                print(f"ERROR: one of these numbers: {num1} or {num2}, has not yet been calculated!")
                break
  
        file.close()
        print(f"Calculated sums: {sums}")
        return sums

    def checkSums(self) -> bool:
        for summation in self.sums:
            if summation == self.sequence[0]:
                self.sequence.pop(0)
                continue
            if summation >= self.sequence[0]:
                print(f"ERROR: {summation} was caclulated before {self.sequence[0]}")
                return False
        if len(self.sequence) == 0: # if all the numbers in the sequence have been found
            return True
        else:
            print(f"ERROR: {self.sequence} were not calculated!")
            return False


import os
for filename in os.listdir('./outputs'):
    V = Verifier(f"./outputs/{filename}")
    print(V.result)

