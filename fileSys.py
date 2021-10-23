
class File():
    def __init__(self,data_file):
        self.name = data_file[0]
        self.first_block = int(data_file[1])
        self.quant_block = int(data_file[2])






def get_blocks_inf(data_file):
     
     
     n_blocks = int(data_file[0])
     ocp_blocks = int(data_file[1])
     return (n_blocks, ocp_blocks)


def get_files_list(data_file):
    
    n = int(data_file[1])
    files_list = []
    for i in range(2,n+2):
        line = data_file[i].split(',')
        f = File(line)
        files_list.append(f)
    
    return files_list
