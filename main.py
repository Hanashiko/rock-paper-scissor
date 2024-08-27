from random import choice

global short_options, full_options, scissor, paper, rock, wins, tried

short_options: list[str] = ['r', 'p', 's']
full_options: list[str] = ['rock', 'paper', 'scissor']

scissor: str = "scissor"
paper: str = "paper"
rock: str = "rock"

tried: int = 0
wins: int = 0

def validation_user(choice: str) -> bool:
    if choice in short_options:
        return True
    else: 
        return False

def isUserWin(user: str, computer: str) -> None:
    global wins
    if ((user == "r" and computer == scissor) or
        (user == "p" and computer == rock) or
        (user == "s" and computer == paper)):
        print("You are winner!!!")    
        wins += 1
    elif ((user == "r" and computer == rock) or
          (user == "p" and computer == paper) or
          (user == "s" and computer == scissor)):
        print("It's a draw")
    else:
        print("I am win")

def main() -> None:
    print(""""For playing, write:
\'r\' - rock,
\'p\' - paper,
\'s\' - scissors
\'st\' for checking stats of games
\'q\' for quit the game""")
    while 1:
        global tried, wins
        
        user_choice: str = input("Write your option: ")
        if user_choice == "st":
            print(f"We played - {tried} times\nYou won {wins} times")
            continue
        elif user_choice == "q":
            print(f"We played - {tried} times\nYou won - {wins} times")
            break
        elif not user_choice in short_options:
            print("You write wrong option")
            continue
        
        computer_choice: str = choice(full_options)
        print("My choice -", computer_choice)
        
        tried += 1
        isUserWin(user_choice, computer_choice)
        
if __name__ == "__main__":
    main()