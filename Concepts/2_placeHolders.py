#PLACEHOLDERS IN STRINGS
name = "Jake"
sentence = "%s is 15 years old"
print(sentence % name)

sentence = "%s %s was the president of the US"
print(sentence % ("Barack","Obama"))

#format strings
print(f"Hello, {name}")
x = 10
y = 20
print(f"The sum of {x} and {y} is {x+y}")

print(x , y , sep = '\t|\t')#print whit sep
print(name + " " + sentence,end ="!\n")#print with end

sentence = "you are the best winner"
print(sentence)
print(sentence[4:20:2])#slice
print(len(sentence))
print("agua" in sentence)
print(not "c" in sentence)#primera aproximacion
print("c" not in sentence)#forma pitonica
print(sentence.split())#split is a list to separete strings
sentence = 'Red,Blue,Green,Black'
print(sentence.split(","))
#rawdata
text= r'abc\ndef'
print(text)
#partition
text = '3 + 4'
print(text.partition('+'))#returns a tuple with the part before the separator, the separator and the part next the separator
#clean strings
serial_number = '\n\t \n 48374983274832 \n\n\t  \t  \n'
print(serial_number.strip())#eliminar caracteres del principio y del final de un "string"
print(serial_number.lstrip())#left strip
print(serial_number.rstrip())#right strip
print(serial_number.strip('\n'))#eliminar caracter deseado

#Busquedas
lyrics = '''Time changes every idea I've ever had
Oh, such a heavy love, rolls out like a blanket
Why must it fold up on me?
Why must it fold up on me?
Slow replies when I'm hungry enough to give
Lust is thrown around my room, I better get out of here
You can lead me on all of the way home
You can lead me on all of the way home
Don't wait, don't wait,don't wait for too long
Don't say, don't say, don't say a word
Don't wait, don't wait,don't wait for too long
Don't say, don't say, don't say a word'''
print(lyrics.startswith('Time'))
print(lyrics.endswith('world'))
print(lyrics.find('word'))
print(lyrics.index('word'))# Find,index devuelven el indice de la primera ocurrencia
print(lyrics.find('Love'))#devuelve -1
#print(lyrics.index('Love'))#Decuelve un error
print(lyrics.count("don't"))#Numero de veces que aparece una palabra

