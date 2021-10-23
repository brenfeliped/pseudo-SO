
class File():
    def __init__(self,data_file):
        self.name = data_file[0]
        self.first_block = data_file[1]
        self.quant_block = data_file[2]




def get_blocks_inf(data_file):
     content = data_file.readlines()
     n_blocks = int(content[0])
     ocp_blocks = int(content[1])
     return (n_blocks, ocp_blocks)
