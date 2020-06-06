#goal of this tryout is to create a function from scratch and invoke it for the given problem
def convert(t, t_type):
    if(t_type == 'Celcius'):
        print('Celcius: ', t)
        print('Fahrenheit: ',(t*(9/5))+32)
    elif(t_type == 'Fahrenheit'):
        print('Fahrenheit: ', t)
        print('Celcius: ',(t-32)*(5/9))
    else:
        return -1

convert(-40, 'Fahrenheit')
