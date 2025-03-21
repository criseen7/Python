#DICCIONARIES
students = {'Bob' : 12, 'Rachel' : 14, 'Emily' : 13}# if you have equal elements, it goes last
print(students)
print(students['Rachel'])

#update
students['Emily'] = 15
print(students)

#delete
del students['Emily']
print(students)

print(len(students))
