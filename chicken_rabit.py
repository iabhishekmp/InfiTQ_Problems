#PF-Assgn-26

def solve(heads,legs):
    error_msg="No solution"
    chicken_count=0
    rabbit_count=0

    x = ((4*heads) - legs)
    if(x % 2 != 0):
        print(error_msg)
        return -1
    x //= 2
    if(x > heads):
        print(error_msg)
        return -1
    y = heads - x 
    print(x, y)

#Provide different values for heads and legs and test your program
solve(150,400)
