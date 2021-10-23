
filesSO = open('files.txt','r')
processes = open('processes.txt','r')

content = filesSO.read()
print(content)

print()
content = processes.read()
print(content)