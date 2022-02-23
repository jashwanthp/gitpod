#print('hello!!')

num1 = 20
num2 = 10
def multiply(num1,num2):
    product = num1*num2
    return product

#print (multiply(num1, num2))

#for i in range(1,11):
#    print (i)


def evenindex1() -> str():
    word = input('enter the word - ') 
    print (word)
    output = '' 
    for i in range(len(word)):
        if i%2 == 0: 
            output = output+word[i]
    return output

#print (evenindex1())

def evenindex2()-> str():
    word = input('enter the word - ') 
    print (word)
    output = '' 
    for i in range(0,len(word)-1,2):
        output = output + word[i]
    return output

def evenindex3() -> str():
    word = input('enter the word -')
    print(word)
    output = ''
    #x= list(word) 
    for i in word[0:len(word)-1:2]:
        output = output + i
    return output

print(evenindex3())
    

