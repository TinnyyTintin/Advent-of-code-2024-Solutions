with open("Day 3 inputs.txt") as file:
        text = " ".join(line.strip() for line in file)

to_find:str = "mul("
def find_index(fromm:str,what:str):

        disable = []
        dis = fromm.find("don't()")
        activate = []
        act = fromm.find("do()")
        while dis !=-1:
                disable.append(dis)
                dis = fromm.find("don't()",dis+7)
        while act !=-1:
                activate.append(act)
                act = fromm.find("do()",act+4)

        newerstring = fromm[:disable[0]]
        k = 0
        i = 0
        yep = 0

        while True:
                if i >= len(disable):
                        newerstring += fromm[activate[-1]:]
                        break
                elif activate[k]>disable[i]:
                        i +=1
                elif disable[i]>activate[k]:
                        newerstring += fromm[activate[k]:disable[i]]
                        while activate[k] <= disable[i]:
                                k+=1

        print("don't()" in newerstring)
        indexes:list = []
        mhm = newerstring.find(what)
        while mhm !=-1:
                indexes.append(mhm)
                mhm = newerstring.find(what,mhm+4)
        values = []
        sum = 0

        for i in range(0,len(indexes)):

                yah = ""
                for j in range(indexes[i]+4,len(newerstring)):
                        if j == len(newerstring) and newerstring[-1]==")":
                                yah.strip(",")
                                values.append(yah)
                                break
                        if newerstring[j]==")":
                                yah.strip(",")
                                values.append(yah)
                                break
                        else:
                                yah += newerstring[j]
        for i in values:
                try:
                        to_sum = i.split(",")
                        sum +=int(to_sum[0])*int(to_sum[1])
                except ValueError:
                        pass
        return sum

print("total sum",find_index(text,to_find))
