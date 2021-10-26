SIZE_MEMORY = 1024
USER_MEMORY = 960
REAL_TIME_M = 64

class Memory:
    def __init__(self):
        self.qtdOcupRT = 0
        self.qtdOcupUM = 0
        self.memory = []
        for i in range(0, SIZE_MEMORY):
            self.memory.append(None)
    
    def verifyMemory(self, process):
        countFree = 0
        if process.priority == 0:
            for i in range(0, REAL_TIME_M):
                if(self.memory[i] == None):
                    countFree += 1
                    if process.quant_memory == countFree:
                        process.pos_memory = i - process.quant_memory + 1
                        return True
                else:
                    countFree = 0
        else:
            for i in range(REAL_TIME_M, SIZE_MEMORY):
                if(self.memory[i] == None):
                    countFree += 1
                    if process.quant_memory == countFree:
                        process.pos_memory = i - process.quant_memory + 1
                        return True
                else:
                    countFree = 0
        return False

    def allocateMemory(self, process):
        if (self.verifyMemory(process) == True):
            for i in range(process.pos_memory, process.pos_memory + process.quant_memory):
                self.memory[i] = process.PID
            print("DEU BOM")
        else:
            print("DEU RUIM")

    def removeMemory(self, process):
        for i in range(process.pos_memory, process.pos_memory + process.quant_memory):
                self.memory[i] = None

    def printM(self):
        for x in range(len(self.memory)):
            print(self.memory[x], end=" ")
