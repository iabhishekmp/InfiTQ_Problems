#PF-Assgn-24
def form_triangle(num1,num2,num3):
    success="Triangle can be formed"
    failure="Triangle can't be formed"
    
    for i in range(0, 3):
        if(num1 < num2+num3):
            if(num2 < num1 + num3):
                if(num3 < num1 + num2):
                    return success
                else:
                    return failure
            else:
                return failure
        else:
            return failure

num1=1
num2=2
num3=3
print(form_triangle(num1, num2, num3))
