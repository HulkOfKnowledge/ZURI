#!/usr/bin/env python 3

from random import choice
import sys

def play():
    
    user_score=0
    cpu_score=0
    count=0

    choice_list=["R","P","S"]
    while count < rounds:
        print()
        print(f"{user_name}:{user_score}")
        print(f"CPU:{cpu_score}")
        print()
        user_choice=input("(R)ock, (P)aper, (S)cissors? ").capitalize()
        cpu_choice=choice(choice_list)
        
        if user_choice.startswith("R"):
            user_choice="Rock"
        elif user_choice.startswith("P"):
            user_choice="Paper"
        elif user_choice.startswith("S"):
            user_choice="Scissors"
        else:
            pass
        if cpu_choice.startswith("R"):
            cpu_choice="Rock"
        elif cpu_choice.startswith("P"):
            cpu_choice="Paper"
        elif cpu_choice.startswith("S"):
            cpu_choice="Scissors"
        else:
            pass
        print(f"{user_name} ({user_choice}) : CPU ({cpu_choice})")
        print()
        count+=1
        if user_choice==cpu_choice:
            user_score+=1
            cpu_score+=1
            print("draw")
            
        elif user_choice=="R":
            if cpu_choice=="P":
                cpu_score+=1
                print("Cpu wins")
            else:
                user_score+=1
                print(f"{user_name} wins")
                    
        elif user_choice=="P":
            if cpu_choice=="R":
                user_score+=1
                print(f"{user_name} wins")
            else:
                cpu_score+1
                print("CPU wins")
                    
        elif user_choice=="S":
            if cpu_choice=="P":
                user_score+=1
                print(f"{user_name} wins")
            else:
                cpu_score+=1
                print("CPU wins")
        else:
            print("Invalid Input! Try again ")
            print("To play, simply type R for Rock,\nP for Paper\nS for Scisssors")
            sys.exit()
            
    if user_score > cpu_score:
        print()
        print(f"{user_name}:{user_score}")
        print(f"CPU:{cpu_score}")
        print(f"Winner: {user_name}")
        
    elif user_score==cpu_score:
        print("Tie !")
        print("No winner")
        
    else:
        print()
        print(f"{user_name}:{user_score}")
        print(f"CPU:{cpu_score}")
        print("Winner: CPU")

    
def main():
    global user_name
    global rounds
    print("Welcome to Hulk's RoCk PapEr ScisSoRs v1.0.2\nTo play, simply type R for Rock,\nP for Paper\nS for Scisssors")
    print()
    user_name=input("Enter your username: ").capitalize()
    rounds=int(input("How many rounds do you wish to play? "))
    play()
    
        
if __name__ == "__main__":
    main()
