from process import create_processes
from process import Process
REAL_TIME = 64
USER = 960
process_list = []

def run():
    files_so = open('files.txt','r')
    processes = open('processes.txt','r')
    process_list = create_processes(processes)


run()