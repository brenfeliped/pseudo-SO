from process import create_processes
from process import Process
from fileSys import get_blocks_inf
REAL_TIME = 64
USER = 960
N_BLOCKS= 0
OCP_BLOCKS =0 # blocos ocupados

process_list = []
files_list = []
operations_list = []

def run():
    files_so = open('files.txt','r')
    processes = open('processes.txt','r')
    process_list = create_processes(processes)
    
    N_BLOCKS,OCP_BLOCKS = get_blocks_inf(files_so)
    


run()