calendar = {
    'зима': [12,1,2],
    'весна': [3,4,5],
    'лето': [6,7,8],
    'осень': [9,10,11],
}
mec = int (input())
b = list(calendar.values())
for i in calendar.get('зима'):
    #print(i)
    i=1
if mec in calendar.get('зима'):
    print('зима')
elif mec in calendar.get('весна'):
    print('весна')
elif mec in calendar.get('лето'):
    print('лето')
elif mec in calendar.get('осень'):
    print('осень')