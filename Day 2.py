import time
start_time = time.time()

with open("Day 2 inputs.txt") as file:
    new_list = []
    for line in file:
        ello = line.strip().split()
        newer_list = []
        for i in ello:
            newer_list.append(int(i))
        new_list.append(newer_list)

clear:int = 0
unsafe_ones:list = []
for value in new_list:
    up = False
    down = False
    for numbah in range(1,len(value)):
            difference = value[numbah]-value[numbah-1]
            if 0 > difference >=-3 and not up :
                down = True
            elif 0 < difference <=3 and not down:
                up = True
            else:
                unsafe_ones.append(value)
                break
    else:
        clear +=1

for value in unsafe_ones:
    up = False
    down = False
    list_versions = []
    for numbah in range(len(value)):
        new_value = value.copy()
        new_value.pop(numbah)
        print(new_value)
        for aaa in range(1,len(new_value)):
                difference = new_value[aaa]-new_value[aaa-1]
                if 0 > difference >=-3 and not up :
                    down = True
                elif 0 < difference <=3 and not down:
                    up = True
                else:
                    break
        else:
            clear +=1
            break
print("clears",clear)
end_time = time.time()

execution_time = end_time - start_time
print(f"Execution Time: {execution_time} seconds")