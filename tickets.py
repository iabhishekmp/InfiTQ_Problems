#PF-Exer-22

def generate_ticket(airline,source,destination,no_of_passengers):
    ticket_number_list=[]
    for i in range(no_of_passengers):
        #ticket_number_list.append(f'{airline}:{source[:3]}:{destination[:3]}:{i+101}')
        ticket_number_list.append('{0}:{1}:{2}:{3}'.format(airline, source[:3], destination[:3], i+101))

    if(len(ticket_number_list)<5):
        return ticket_number_list
    return ticket_number_list[-5:]
#Provide different values for airline,source,destination,no_of_passengers and test your program
print(generate_ticket("AI","Bangalore","London",7))
