import random

def rollDice():
    return random.choice(range(1,6))

def main():
    print("welcome to roll dise simulator")
    while True:
        roll=input('Press enter to roll the dice (if you want quit press q): ')
        if roll=="q":
            break
        showResult=rollDice()
        print("the roll is",showResult)
    print("thank you for pick roll dise simulator")

if __name__=="__main__":
    main()