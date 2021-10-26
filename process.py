from typing import List
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
            self.execTime = 0
            self.pos_memory = 0

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
        if(len(data_operation)> 3):
            self.exists_blocks= True
            self.num_blocks = data_operation[3]
        else:
            self.exists_blocks= False



class Process_manager:

    def __init__(self):
        self.max_fila = MAX_SIZE
        self.fila_real_time = []
        self.fila_u0 = []
        self.fila_u1 = []
        self.fila_u2 = []
        self.fila_u3 = []


    
              

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