#PF-Assgn-15

def find_product(num1,num2,num3):
    product = 1
    if(num3 != 7):
        product *= num3
        if(num2 != 7):
            product *= num2
            if(num1 != 7):
                product *= num1
    else:
        product = -1
    return product


product=find_product(7,4,3)
print(product)
