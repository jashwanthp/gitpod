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

def inputword()->str():
    output = input('enter the word -')
    print(output)
    return output

def remove_first_nchars(n):
    word = inputword()
    output = word[4:]
    return output
def remove_last_nchars(n):
    word = inputword()
    output = word[:4]
    return output

#print(remove_first_nchars(4))

def text_to_arrays(text):
    wronginputarrayelements = ['[',']',',']
    #print(text[0]+'--'+ text[-1])
    if text[0] in wronginputarrayelements:
        text = text[1:]
        #print(text)
    if text[-1] in wronginputarrayelements:
        text = text[:-1]
        #print(text)

    #print('see'+text)
    array = list(map(str.strip, text.strip().split(',')))
    print('array is', array)
    return array


def workwitharrays(what):
    
    input_array = input('input array - ')
    array = text_to_arrays(input_array)
    print(*array)
    
    if what == 'wordcount':
        wordcheck = input('word check -')
        output1 = input_array.count(wordcheck)
        output2 =0
        for i in range(len(input_array)-1):
            #print(output2)
            #print(input_array[i:i+len(wordcheck)])
            output2 += input_array[i:i+len(wordcheck)] == wordcheck
        return output1, output2

    if what == 'divisible':
        import numpy
        divisibleby =  input('divisible by number -') 
        divisibleby = int(divisibleby)
        testarray = []
        for each in array: 
            if each.isnumeric(): testarray.append(each)
        newarray = list(map(int, testarray))
        newarray = numpy.array(newarray)
        print(newarray)
        output = newarray#/divisibleby
        

    if what == 'first_last_same':
        if array[0]==array[-1]:
            print('first',str(array[0]) , 'and last element', str(array[-1]), 'of the array-' , *array , 'are same')
            output = 'first',str(array[0]) , 'and last element', str(array[-1]), 'of the array-' , *array , 'are same'
        else:
            print('first',str(array[0]) , 'and last element', str(array[-1]), 'of the array-' , *array , 'are different')
            output = 'first',str(array[0]) , 'and last element', str(array[-1]), 'of the array-' , *array , 'are different'
    
    return output
#text1 = '[10, 20, 30, 40, 10]'
#text2 = 'Emma is good developer. Emma is a writer'
#print(workwitharrays('wordcount'))

def patterns(type):
    if type == 'trainglenumbers':
        n = input('lenght of triangle-')
        intn = int(n)
        i=1
        for i in range(intn):
            for j in range(i):
                print(i, end=' ')
            print('\n')
        return output
    if type=='palindrome':
        n = input('check palindrome number-')
        intn = int(n)
        revn = n[::-1]
        if intn == int(revn): 
            output = 'yeah, its a palindrome'
        else:
            output = 'Nope, try a different number'
        return output
    if type =='revnum':
        n=input('Enter the number to be reversed with spaces in between-')
        revn = n[::-1]
        output = ' '.join(revn)
        return output

#print(patterns('revnum'))

def tax():
    income = int(input('Enter the income in Dollars-'))
    taxable = income - 10000
    tax=0
    if income<= 10000: 
        output = tax
    if taxable>=10000:
        tax = ((taxable - 10000)*20/100)+(10000*10/100)
            
    elif taxable<10000 and taxable> 0:
        tax= taxable*10/100
    output = tax
    return output

print(tax())
        