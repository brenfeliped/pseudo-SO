from typing import List
import time
MAX_SIZE = 1000 # tamanho máximo da fila de processos

class Process:

        def __init__(self, data_process):
            self.init_time = int(data_process[0])
            self.priority = int(data_process[1])
            self.cpu_time = int(data_process[2])
            self.quant_memory= int(data_process[3])
            self.cod_printer = int(data_process[4])
            self.request_scanner = int(data_process[5])
            self.request_modem = int(data_process[6])
            self.cod_disc = int(data_process[7])

            
            self.instructions = []  
            self.PID = None
            self.exec_time = 0
            self.offset = 0
            self.wait_time = 0

        def set_intructions(self, instrs):
            for instr in instrs:
                if self.PID == instr.id_process:
                    self.instructions.append(instr)
            return
        
            

        
class Operation:
    def __init__(self,data_operation):
        self.id_process = int(data_operation[0])
        self.cod_operation = int(data_operation[1])
        self.name_file = data_operation[2]
        self.dados_file = None
        if(len(data_operation)> 3):
            self.exists_blocks= True
            self.num_blocks = int(data_operation[3])
        else:
            self.exists_blocks= False
    
    def __str__(self):
        return str(self.id_process) + " " + str(self.cod_operation) + " " + self.name_file + " " + ( str(self.num_blocks) if self.exists_blocks else " ")




class Process_manager:

    def __init__(self):
        self.max_fila = MAX_SIZE
        self.executing = []
        self.ready_processes = []
        self.fila_real_time = []
        self.fila_u0 = []
        self.fila_u1 = []
        self.fila_u2 = []
        self.fila_u3 = []
        self.exec = None

    def divideProcesses(self, processes, memory):
        for p in processes:
            if p.priority == 0 and len(self.fila_real_time) < 1000:
                self.fila_real_time.append(p)
            elif p.priority == 1 and len(self.fila_u1) < 1000:
                self.fila_u1.append(p)
            elif p.priority == 2 and len(self.fila_u2) < 1000:
                self.fila_u2.append(p)
            elif p.priority == 3 and len(self.fila_u3) < 1000:
                self.fila_u3.append(p)
            else:
                print("Lista de processos cheia")

    def init_process_manager(self, processes, memory):
        self.divideProcesses(processes, memory)
    
    def enviarFimFila(self, memoria, processo):
        self.memoria.deallocateMemory(processo)
        self.ready_processes.append(processo)


    def init_process(self, process):
        if(process.PID != None):
            print("dispatcher => ")
            print("\t PID: ", process.PID)
            print("\t offset: ", process.offset) #implementar depois com a memoria
            print("\t blocks: ", process.quant_memory)
            print("\t priority: ", process.priority)
            print("\t time:", process.cpu_time)
            print("\t printers:", process.cod_printer)
            print("\t scanners: ", process.request_scanner)
            print("\t modems: ", process.request_modem)
            print("\t drives: ", process.cod_disc)
            if(process.priority == 0):
                self.exec_process_real_time(process)
            else:
                #self.exec_process_user(process)
                self.exec_process_real_time(process)
            
            return True

        else:
            return False

    def exec_process_real_time(self, process):
        
            print("P"+str(process.PID)+" STARTED")
            for i in range(1, process.cpu_time + 1):
                print("P"+str(process.PID)+" instruction " + str(process.exec_time))
                process.exec_time+=1
                time.sleep(1)
            print("P"+str(process.PID)+ " return "+ "SIGINT")
            return True
        

    def exec_process_user(self, process): 
        if(process.exec_time == 0):
            print("P"+str(process.PID)+" STARTED")
            print("P"+str(process.PID)+" instruction " + str(process.exec_time +1))
        elif(process.exec_time == process.cpu_time+1):
            print("P"+str(process.PID)+" instruction " + str(process.exec_time +1))
            print("P"+str(process.PID)+ " return "+ "SIGINT")
        else:
            print("P"+str(process.PID)+" instruction " + str(process.exec_time +1))
        
        process.exec_time+=1
        time.sleep(1)

        return True       

def create_processes(file_processes):   
    p_list = []
    count_PID = 0
    for line in file_processes:
        elements = line.split(',')
        p = Process(elements)
        p.PID = count_PID
        p_list.append(p)
        count_PID+=1;
    return p_list

def escalona_global(process_manager, memory, process_list): # funcao que vai receber todos modulos
        process_manager.init_process_manager(process_list, memory)
        TIME = 0

        for p in process_manager.fila_real_time:
            
            if memory.allocateMemory(p):
                process_manager.init_process(p)
                memory.deallocateMemory(p)
                TIME+= p.cpu_time
        
        for p in process_manager.fila_u1:
            if memory.allocateMemory(p):
                process_manager.executing.append(p)
                process_manager.fila_u1 = filter(lambda x: x!= p, process_manager.fila_u1)

        for p in process_manager.fila_u2:
            if memory.allocateMemory(p):
                process_manager.executing.append(p)
                process_manager.fila_u1 = filter(lambda x: x!= p, process_manager.fila_u1)

        for p in process_manager.fila_u3:
            if memory.allocateMemory(p):
                process_manager.executing.append(p)
                process_manager.fila_u1 = filter(lambda x: x!= p, process_manager.fila_u1)

        for p in process_manager.executing:
            if(p.exec_time==0):
                process_manager.init_process(p)
                memory.deallocateMemory(p)
            else:
                process_manager.exec_process_user(p)
                memory.deallocateMemory(p)
        
        TIME += 1