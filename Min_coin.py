#PF-Assgn-16
def make_amount(rupees_to_make,no_of_five,no_of_one):
    five_needed=0
    one_needed=0

    five_needed = (rupees_to_make // 5)
    if(five_needed > no_of_five):
        five_needed = no_of_five
    one_needed = (rupees_to_make - (five_needed*5))
    if(one_needed > no_of_one):
        one_needed = no_of_one
    if(rupees_to_make == ((five_needed*5) + one_needed)):
        print("No. of Five needed :", five_needed)
        print("No. of One needed  :", one_needed)
    else:
        print(-1)

make_amount(44,8,5)
