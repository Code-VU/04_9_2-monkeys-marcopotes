def calculateTime():
    
    # This first line is provided for you
    monkey_one = input("Is the first monkey smiling?y/n:  ")
    monkey_two = input("Is the second monkey smiling?y/n: ")

    if monkey_one == "y" and monkey_two == "y":
        print("Uh Oh! We're in trouble!")
    elif monkey_one == "n" and monkey_two == "n":
        print("Uh Oh! We're in trouble!")
    elif monkey_one == 'y' and monkey_two =='n':
        print("Yay! We're going to have a good day!")
    elif monkey_one == 'n' and monkey_two =='y':
        print("Yay! We're going to have a good day!")



    # end assignment


## If you want to test locally run > python monkeyCalculator.py

if __name__ == "__main__":
    calculateTime()
    
