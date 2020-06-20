checklist_name = input('Введите список')
checklist = checklist_name.split(',')
i =0
while i < len(checklist [:-1]):
    checklist [i], checklist[i+1] = checklist[i+1],checklist [i]
    i+=2
print(checklist)