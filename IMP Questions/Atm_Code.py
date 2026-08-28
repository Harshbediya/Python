balance=10000
while True:
  
    op=input("Select Any one:  \n Depsoit\t wirthdraw\tbalance enquiry\tcancel\n option: ")
    match op:
        case 'Depsoit':
            amt=int(input(" amount: "))
            balance+=amt
            print(f"{amt} deposited\navailable balance : {balance}")
        case 'wirthdraw':
                    amt=int(input(" amount: "))
                    if amt<balance:
                        balance-=amt
                        print(f"{amt} wirthdraw\navailable balance : {balance}")
                    else:
                        print("Insufficient balance : ")
                        
        case 'balance enquiry':
                print(f"Your balance is : {balance}")
    
        case 'cancel':
            exit()
        case _:
            print("Plese select vaild option..!!")
     