from process import create_processes
from process import Process
from fileSys import get_blocks_inf, get_files_list, get_operation_list
REAL_TIME = 64
USER = 960
N_BLOCKS= 0
OCP_BLOCKS =0 # blocos ocupados

process_list = []
files_list = []
operations_list = []

def run():
    files_txt = open('files.txt','r').readlines()
    processes_txt = open('processes.txt','r').readlines()
    process_list = create_processes(processes_txt)

    N_BLOCKS,OCP_BLOCKS = get_blocks_inf(files_txt)
    files_list = get_files_list(files_txt)
    operations_list = get_operation_list(files_txt)
    



run()