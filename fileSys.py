from process import Operation
class File():
    def __init__(self,data_file):
        self.name = data_file[0]
        self.id_process = None
        self.first_block = int(data_file[1])
        self.quant_block = int(data_file[2])
    
    def __str__(self):
        return self.name + "  " + str(self.id_process) + " " + str(self.first_block) + str(self.quant_block)   


def get_blocks_inf(data_file):
     n_blocks = int(data_file[0])
     ocp_blocks = int(data_file[1])
     return (n_blocks, ocp_blocks)


def get_files_list(data_file):
    
    qtd_segmentos = int(data_file[1])
    files_list = []
    for i in range(2, qtd_segmentos+2):
        line = data_file[i].split(',')
        f = File(line)
        files_list.append(f)
    
    return files_list

# def set_file_in_disco(files_list, blocks):
#     disco = [0] * blocks
#     for i in files_list:
#         for j in range(i.first_block, i.first_block+i.quant_block):
#             disco[j] = i.name
#     return disco

def get_operation_list(data_file):
    n = int(data_file[1])
    operation_list = []
    for i in range(n+2,len(data_file)):
        line = data_file[i].split(',')
        p = Operation(line)
        operation_list.append(p)
    
    return operation_list

class File_manager:
    def __init__(self, disc_size, files_list, qt_process):
        self.disco = [0] * disc_size # Inicializa tudo com zero a partir do disc size 
        self.qt_id_process = qt_process-1

        # Inicializando disco
        for i in files_list:
            for j in range(i.first_block, i.first_block+i.quant_block):
                self.disco[j] = i.name

    def show_disco(self, message):
        print("#############", message, "#############")
        print(self.disco)

    def delete_file(self, data_file, priority, process_id):
     
        # TODO: Adicionar verificações pra vê se arquivo/processo existe
        contEntrou = 0
        for x in range(0, len(self.disco)):
            if self.disco[x] != data_file.name_file.strip():
                contEntrou = contEntrou+1
        if(contEntrou == len(self.disco)):
            return (False, "O processo "+str(process_id)+" não pode deletar o arquivo "+data_file.name_file.strip()+" porque ele não existe")
        if priority == 0:
            for x in range(0, len(self.disco)):
                while(self.disco[x] == data_file.name_file.strip()):
                    self.disco[x] = 0
                    x = x+1
                break
            return (True, "O processo "+str(process_id)+" deletou o arquivo "+data_file.name_file.strip())
        elif process_id == data_file.id_process:
            for x in range(0, len(self.disco)):
                while(self.disco[x] == data_file.name_file.strip()):
                    self.disco[x] = 0
                    x = x+1
                break
            return (True, "O processo "+str(process_id)+" deletou o arquivo "+data_file.name_file.strip())
        else:
            return (False, "")

    def create_file(self, nome, numeroBlocos):

        if (numeroBlocos <= len(self.disco)): # Checa se ha blocos o suficiente para salvar o arquivo
            hasSpace = False
            currentPosition = 0
            qtdFreeContinuous = 0
            positionWhereWillInsert = 0

            while (currentPosition < len(self.disco)): # Percorre todo o disco
                if(self.disco[currentPosition] == 0): # Verifica se o espaco esta livre
                    qtdFreeContinuous = qtdFreeContinuous + 1
                else:
                    qtdFreeContinuous = 0

                if(qtdFreeContinuous == numeroBlocos): # Verifica se achou a quantidade necessaria
                    positionWhereWillInsert = currentPosition
                    hasSpace = True
                    break
                
                currentPosition = currentPosition + 1

            if(hasSpace):
                while(numeroBlocos > 0): # Salva dado o no disco
                    self.disco[positionWhereWillInsert-1] = nome
                    positionWhereWillInsert = positionWhereWillInsert + 1
                    numeroBlocos = numeroBlocos - 1
                
                return (True, "Arquivo criado")
            else:
                return (False, "Falta espaço contiguo disponível no disco")
        else:
            return (False, "Arquivo é maior do que o disco!!!")

    def msg_sucesso_falha(self, value):
        if(value == True):
            return "Sucesso"
        else:
            return "Falha"
        
    def do_operation_list(self, operations_list, process):
        print("Sistemas de arquivos => ")
        qtd_op = 0
        for i in operations_list:
            qtd_op += 1
            print("Operação ",qtd_op," => ", end="")
            if i.id_process < 0 or i.id_process > self.qt_id_process:
                print("Falha\nO processo "+str(i.id_process)+" não existe.")
            else:
                if(i.cod_operation == 0):
                    isSucessfullCreate, msgResCreate = self.create_file(i.name_file, i.num_blocks)
                    print(self.msg_sucesso_falha(isSucessfullCreate))
                    print(msgResCreate)
                elif(i.cod_operation == 1):
                    # self.msg_sucesso_falha(self.delete_file(i, 0, process.PID))
                    isSucessfullDelete, msgResDelete = self.delete_file(i, 0, process.PID)
                    print(self.msg_sucesso_falha(isSucessfullDelete))
                    print(msgResDelete)
                
            self.show_disco("Mapa de ocupação de disco: ")

