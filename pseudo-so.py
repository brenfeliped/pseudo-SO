from process import create_processes
from process import Process, Process_manager
from fileSys import get_blocks_inf, get_files_list, get_operation_list, File_manager#, set_file_in_disco
from memory import Memory
from resources import ControlaRecursos
REAL_TIME_MEM = 64
USER_MEM = 960
N_BLOCKS= 0
OCP_BLOCKS = 0 # blocos ocupados

FILA_real_time = [] # FIFO (First In First Out), sem preempção
FILA_user = [] #Processos de usuário devem utilizar múltiplas filas de prioridades com realimentação. Para isso,devem ser mantidas três filas com prioridades distintas
FILA_ready = []

process_list = []
files_list = []
operations_list = []


def run():
    files_txt = open('files.txt','r').readlines()
    processes_txt = open('processes.txt','r').readlines()
    process_list = create_processes(processes_txt)

    N_BLOCKS, OCP_BLOCKS = get_blocks_inf(files_txt)
    files_list = get_files_list(files_txt)
    operations_list = get_operation_list(files_txt)

    # for p in process_list:
    #     #print(p.PID)
    #     p.set_intructions(operations_list)
    
    # print("########## CRIA DISCO ##############")
    # fm = File_manager(N_BLOCKS, files_list)
    # fm.show_disco()
    # print("########## DELETA Y DO DISCO ##############")
    # fm.delete_file(files_list[1], 0, 0)
    # fm.show_disco()
    # print("########## ADICIONA F NO DISCO ##############")
    # fm.create_file("f", 2)
    # fm.show_disco()
    memory = Memory()
    pm = Process_manager()

    

    #pm.init_process_manager(process_list, memory)
    
    # for p in process_list:
    #     pm.init_process(p)

    # test = set_file_in_disco(files_list, N_BLOCKS)

    # pm = Process_manager() # sugestao futura: colocar principais classes em uma classe chamda SO
    # memory = Memory()
    # memory.allocateMemory(process_list[0])
    # memory.allocateMemory(process_list[1])
    # for p in process_list:
    #     cond = pm.init_process(p)
    #         
    # memory.printM()
    # memory.printM()
    # memory.printM()

    # recursos = ControlaRecursos()
    # recursos.solicitaRecurso(process_list[0].cod_printer,process_list[0].request_scanner
    # ,process_list[0].request_modem,process_list[0].cod_disc)
    # recursos.liberaScanner()
    # recursos.liberaDisco(process_list[0].cod_disc)
run()  

run()