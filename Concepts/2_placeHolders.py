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
print(sentence.split())
sentence = 'Red,Blue,Green,Black'
print(sentence.split(","))
#rawdata
text= r'abc\ndef'
print(text)
