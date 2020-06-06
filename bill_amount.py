#PF-Assgn-19

def calculate_bill_amount(food_type,quantity_ordered,distance_in_kms):
    if((quantity_ordered<=0) or (distance_in_kms<=0)):
        return -1
    
    bill_amount=0
    
    if(distance_in_kms > 6):
        bill_amount += 9 + ((distance_in_kms-6) * 6)
    elif(distance_in_kms > 3):
        bill_amount += (distance_in_kms-3)*3
    
    if(food_type == "V"):
        bill_amount += 120*quantity_ordered
    elif(food_type == "N"):
        bill_amount += 150*quantity_ordered
    else:
        return -1
    
    return bill_amount

bill_amount=calculate_bill_amount("N",2,4)
print(bill_amount)
