#PF-Assgn-20

def calculate_loan(account_number,salary,account_balance,loan_type,loan_amount_expected,customer_emi_expected):
    eligible_loan_amount=0
    bank_emi_expected=0
    if((len(str(account_number))==4 and (int(str(account_number)[0])) == 1)):
        if(account_balance >=100000):
            if(loan_type == 'Car' and salary>25000):
                eligible_loan_amount = 500000
                bank_emi_expected = 36
                print("Account number:", account_number)
                print("The customer can avail the amount of Rs.", eligible_loan_amount)
                print("Eligible EMIs :", bank_emi_expected)
                print("Requested loan amount:", loan_amount_expected)
                print("Requested EMI's:",customer_emi_expected)
            elif(loan_type == 'House' and salary>50000):
                eligible_loan_amount = 6000000
                bank_emi_expected = 60
                print("Account number:", account_number)
                print("The customer can avail the amount of Rs.", eligible_loan_amount)
                print("Eligible EMIs :", bank_emi_expected)
                print("Requested loan amount:", loan_amount_expected)
                print("Requested EMI's:",customer_emi_expected)
            elif(loan_type == 'Business' and salary>75000):
                eligible_loan_amount = 7500000
                bank_emi_expected = 84
                print("Account number:", account_number)
                print("The customer can avail the amount of Rs.", eligible_loan_amount)
                print("Eligible EMIs :", bank_emi_expected)
                print("Requested loan amount:", loan_amount_expected)
                print("Requested EMI's:",customer_emi_expected)
            else:
                return -1
        else:
            return -1
    else:
        return -1
calculate_loan(1005,44000,255000,"Car",300000,30)
