# num =int(input("Enter a number: "))

# if num>=0:
#     print("Positive")
# elif num<=-1:
#     print("negative ")
# else:
#     print("Zero")


# question 2
# num2=int(input("Enter a num :"))
# if num2%2==0:
#     print("Even")
# else:
#     print("Odd")
    
# # question 3.
# age=int(input("Enter a age :"))

# if age>=18:
#     print("You can vote")
# else:
#     print("You can't vote")
  
  # question 3.
    
# n1=int(input("Enter 1st n1 "))
# n2=int(input("Enter 1st n2 "))

# if n1>n2:
#     print("1st num greater")
# elif n2>n1:
#     print("2nd greater")
# else:
#     print("equal")
    
meun=input("Enter a choise: ")

match meun:
    case "tea":
        print("this your tea: ")
    case "coffee":
        print("this your coffee: ")
    case "juice":
        print("this your juice: ")
    case "water":
        print("this your water: ")
    case _:
        print("This is not avivable")
        