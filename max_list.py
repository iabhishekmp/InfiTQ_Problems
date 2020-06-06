#PF-Assgn-28

def find_max(num1, num2):
    max_num=-1
    if(num1 < num2):
        l1 = []
        for i in range(num1, num2+1):
            if(i % 5 != 0):
                continue
            if(len(str(i)) != 2):
                continue
            s = 0
            for j in str(i):
                s += int(j)
            if(s % 3 != 0):
                continue
            l1.append(i)
        print(l1)
        try:
            max_num = max(l1)
        except:
            max_num = -1
    return max_num

#Provide different values for num1 and num2 and test your program.
max_num=find_max(10,50)
print(max_num)
