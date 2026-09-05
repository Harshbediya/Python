# while True:
    
#     opertion=input("Select the operation\n +\t-\t*\t/\t\n Option : ")
#     val1=int(input("val1 : "))
#     val2=int(input("val2 : "))

#     match opertion:
#         case '+':
#             res=val1+val2
#             print(res)
#         case '-':
#                 res=val1-val2
#                 print(res)
#         case '*':
#                 res=val1*val2
#                 print(res)
#         case '/':
#             if val2==0:
#                 print("Error")
#             else:
#                 res=val1//val2
#                 print(res)
                
        
#         case 'stop':
#             exit()
            
#         case _:
#             print("Invaild")
            
            
while True:

    operation = input("Select the operation\n+\t-\t*\t/\t\nOption : ")

    if operation == "stop":
        exit()

    val1 = int(input("val1 : "))
    val2 = int(input("val2 : "))

    match operation:
        case '+':
            res = val1 + val2
            print(res)

        case '-':
            res = val1 - val2
            print(res)

        case '*':
            res = val1 * val2
            print(res)

        case '/':
            if val2 == 0:
                print("Error: Cannot divide by zero")
            else:
                res = val1 / val2
                print(res)

        case _:
            print("Invalid operation")