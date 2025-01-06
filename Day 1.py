with open("Day 1 inputs.txt") as file:
    list: list = file.readlines()
    left_parsedlist:list = []
    right_parsedlist:list = []
    iterable:int = 1
    for line in list:
        parsing: list = line.strip().split()
        for words in parsing:
            iterable +=1
            if iterable % 2 == 0:
                left_parsedlist.append(words)
            else:
                right_parsedlist.append(words)

        #left_parsedlist.sort()
        #right_parsedlist.sort()

leftoverlist: list = []
for i in range(len(left_parsedlist)):
    if left_parsedlist[i] in right_parsedlist:
        value:int = int(left_parsedlist[i])
        count:int = 0
        for j in right_parsedlist:
            if int(j) == value:
                #print("j", j)
                #print("value", value)
                count +=1
                #print("count,value",count,value)
        leftoverlist.append(value*count)

total_sum:int = 0
for i in leftoverlist:
   total_sum +=i
#print(leftoverlist)
#print(total_sum)
#print("left list: ",left_parsedlist,"right list: ",right_parsedlist)
data = [*map(int, open('test inputs.txt').read().split())]
print(data)