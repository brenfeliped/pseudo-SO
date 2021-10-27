from process import create_processes
from process import Process, Process_manager, escalona_global
from fileSys import get_blocks_inf, get_files_list, get_operation_list, File_manager
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


def runSO():

    files_txt = open('files.txt','r').readlines()
    processes_txt = open('processes.txt','r').readlines()
    process_list = create_processes(processes_txt)

    N_BLOCKS, OCP_BLOCKS = get_blocks_inf(files_txt)
    files_list = get_files_list(files_txt)
    operations_list = get_operation_list(files_txt)

    for op in operations_list:
        for f in files_list:
            if op.name_file == f.name:
                op.dados_file =f
    
    process_list.sort(key=lambda x: x.init_time)

    pm = Process_manager()
    memory = Memory()
    contrRecursos = ControlaRecursos()
    #pm.init_process_manager(process_list, memory)
    
    escalona_global(pm, memory, process_list)

    fm = File_manager(N_BLOCKS, files_list, len(process_list))
    fm.show_disco("Disco inicialmente")
    fm.do_operation_list(operations_list)

    # memory.printM()

if __name__ == '__main__':
    runSO()