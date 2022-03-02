def openfileread(file):
    #file = input('filepath is -')
    with open(file,'r') as f:
        lines = f.readlines()
        #print(lines)
        f.close()
    return lines

def openfilewrite(file, lines):
    #file = input('filepath is-')
    with open(file, 'w') as f:
        #lines = f.readlines()
        #write permission just helps to rewirite the whole file
        f.writelines(lines)
        f.close()
    return lines


    
file = '/workspace/template-python-django/exercises/files/textfile.txt'
lines = openfileread(file)
#print('Printing \n', *lines)
lines[-1] = lines[-1] + '\n'
#print(*lines)
lines += str('-Jash')
#print(*lines)
openfilewrite(file, lines)


