#PF-Tryout

def find_new_salary(current_salary,job_level):
    if(job_level >=3 and job_level <= 5):
        if(job_level == 3):
            new_salary = (current_salary + current_salary*0.15)
        elif(job_level == 4):
            new_salary = (current_salary + current_salary*0.07)
        else:
            new_salary = (current_salary + current_salary*0.05)
    else:
        new_salary = current_salary
    return new_salary

# provide different values for current_salary and job_level and test yor program
new_salary = find_new_salary(15000,3)
print(new_salary)
