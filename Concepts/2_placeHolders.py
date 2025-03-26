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
#print(lyrics.index('Love'))#Devuelve un error
print(lyrics.count("don't"))#Numero de veces que aparece una palabra
#Replace
proverb = "quien  mal Anda, mal Acaba"
print(proverb.replace("mal", "bien"))#reemplaza todos los mal
print(proverb.replace("mal","bien",1)+"\n")#1 reemplazo

print(proverb.capitalize())#capitalize devuelve una cadena con la primera letra en mayuscula y el resto en minusculas
print(proverb.title())#title devuelve una cadena con la primera letra de cada palabra en mayusculas
print(proverb.upper())#upper devuelve una cadena con todas las letras en mayusculas
print(proverb.lower())#lower devuelve una cadena con todas las letras en minusculas
print(proverb.swapcase())#swapcase intercambia una cadena con las letras en minusculas y mayusculas
print(proverb.casefold()+'\n')#casefold devuelve una cadena con todas las letras en minusculas

#Identificar caracteres
print('D2D2'.isalnum())#Alpha-numeric
print('D2-D2'.isalnum())
print('314'.isnumeric())#Is Numeric
print('3.14'.isnumeric())
print("ABC".isalpha())#letra
print("a-b-c".isalpha())
print("ABC".isupper())
print("abc".islower())
print("Hola Mundo".istitle())

#Interpolacion de cadenas / f-string
name = "Cristofer"
age = 25
print(f"\nHola, me llamo {name} y tengo {age} años")#Actuall py 3
value =0b10010011#bin
print(value)#decimal
print(f"{value:b}")#binario
print(f"{value:o}")#octal
print(f'{value:x}')#hexadecimal
pi = 3.14159265
print(f"{pi:f}")#6 decimals default
print(f"{pi:.2f}")#2 decimals
print(f"{pi:12f}")#6 decimals, total width of 12 characters
print(f"{pi:7.2f}")#2 decimals, total width of 7 characters
print(f"{pi:07.2f}")#2 decimals, total width of 7 characters, padding with zeroes
print(f"{pi:.010f}")#6 decimals, total width of 10 characters
print(f"{pi:e}")#Scientific notation
serie = 'The Simpsons'
imdb_rating = 8.7
num_season = 30
print(f'{serie=}')#f-string con igual
print(f'{imdb_rating=}')
print(f'{serie[4:]=}')#f-string con igual y slice
print(f'{imdb_rating / num_season =}')
#Modo representación
name = 'Steven Spielberg'
print(f'{name}')
print(f'{name!r}')#repr con comillas simples
#Caracteres Unicode
rocket_code =  0x1f680#hex
rocket = chr(rocket_code)#chr() permite representar un carácter a partir de su código
print(rocket)
rocket_code = hex(ord(rocket))#ord() permite obtener el código (decimal) de un carácter a partir de su representación
print(rocket_code)
print('\N{rocket}')#El modificador \N permite representar un carácter a partir de su nombre
#ASCII
print('arca'<'arpa')#arac va antes que arpa
print(ord('c'), ord('p'), sep='\t<\t')
#casos de uso
#Python proporciona una función «built-in» llamada dir() para inspeccionar un determinado tipo de objeto
text = 'This is it!'
print(dir(text))#dir() devuelve una lista de nombres de atributos y métodos de un objeto

#Expresiones regulares
#import re
#re.sub(pattern, replacement, string)
#r'[^a-zA-Z0-9]' → Significa "cualquier cosa que NO sea una letra o un número"
#r'\s' → Representa cualquier espacio en blanco.
#r'\d' → Representa cualquier número (0-9).