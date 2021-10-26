SIZE_MEMORY = 1024
USER_MEMORY = 960
REAL_TIME_M = 64

class Memory:
    def initMemory(self):
        self.qtdOcupRT = 0
        self.qtdOcupUM = 0
        for i in range(0, SIZE_MEMORY):
            self.memory = None
    
    def verifyMemory(self, process):
        countFree = 0
        if process.priority == 0:
            for i in range(0, REAL_TIME_M):
                if(self.memory[i] == None):
                    countFree += 1
                    if process.quant_memory == countFree:
                        return True
                else:
                    countFree = 0
        else:
            for i in range(REAL_TIME_M, SIZE_MEMORY):
                if(self.memory[i] == None):
                    countFree += 1
                    if process.quant_memory == countFree:
                        return True
                else:
                    countFree = 0
        return False

    def allocateMemory(self, process):
        if verifyMemomy(self, process):

