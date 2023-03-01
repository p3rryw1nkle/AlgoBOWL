import sys, os

class Verifier():
    def __init__(self, inputFile, outputFile):
        # self.sequence = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
        self.sequence = self.readInput(inputFile) # reads in a sequence from a group's input file
        self.sums = self.readOutput(outputFile) # reads in the series of summations from a group's output file
        self.errorLog = [] # if an output is invalid, log why
        self.result = self.checkSums() # result of the verification

    def readInput(self, filename) -> list:
        file = open(filename, 'r')
        sumCount = int(file.readline())
        nums = []

        line = file.readline()
        for number in line.split():
            nums.append(int(number))

        file.close()
        return nums

    def readOutput(self, filename) -> list:
        file = open(filename, 'r')
        sumCount = int(file.readline()) 
        sums = {1} # keep track of current numbers that have been calculated, 1 is there by default

        for operation in range(sumCount):
            line = file.readline()
            if not line:
                break
            summation = line.split(' ')
            num1 = int(summation[0])
            num2 = int(summation[1])
            if (num1 in sums) and (num2 in sums): # search through set to make sure numbers have already been calculated
                sums.add(int(summation[0]) + int(summation[1]))
            else:
                self.errorLog.append(f"ERROR: one of these numbers: {num1} or {num2}, has not yet been calculated!")
                break
  
        file.close()
        return sums

    def checkSums(self) -> bool: # ASSUMES THAT SUMMATIONS ARE CALCULATED IN-ORDER (COULD BE PROBLEMATIC)
        for summation in self.sums: # go through each sum that was calculated 
            if summation == self.sequence[0]:
                self.sequence.pop(0)
                continue
            if summation >= self.sequence[0]:
                self.errorLog.append(f"ERROR: {summation} was caclulated before {self.sequence[0]}")
                return False
        if len(self.sequence) == 0: # if all the numbers in the sequence have been found
            return True
        else:
            self.errorLog.append(f"ERROR: {self.sequence} were not calculated!")
            return False

for filename in os.listdir('./outputs'):
    groupName = filename.replace("output_","")
    V = Verifier(f"./inputs/input_{groupName}.txt", f"./outputs/{filename}")
    # print(V.result)
    f = open(f"./verification_results/results_{groupName}.txt", "w")
    f.write(str(V.result) + "\n")
    for error in V.errorLog:
        f.write(error)
    f.write(f"These were the summmations we calculated for {groupName}: {V.sums} \n")
    if V.result == False:
        f.write(f"These were the sums we were missing: {V.sequence}")