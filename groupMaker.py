import random
splitSize = 4
i = open('Section03.txt','r')
o = open('Section03_Output.txt','w')

names = i.readlines()
random.shuffle(names)
count = 0
groupNumber = 1
o.write("---------------------------\n")
o.write("Group#"+str(groupNumber)+"\n")
o.write("---------------------------\n")
for name in names:
    if count == splitSize:
        groupNumber += 1
        count = 1
        o.write("---------------------------\n")
        o.write("Group#"+str(groupNumber)+"\n")
        o.write("---------------------------\n")
        o.write(name)
    else:
        count += 1
        o.write(name)
print (len(names))
i.close()
o.close()
    


