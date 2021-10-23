from typing import List


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
        





              

def create_processes(file_processes):
    
    p_list = []
    for line in file_processes:
        elements = line.split(',')
        p = Process(elements)
        p_list.append(p)
    return p_list