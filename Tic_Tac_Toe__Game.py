instructions="""This will be our tic tac toe board 

    1 |  2  | 3
   ---|-----|---
    4 |  5  | 6  
   ---|-----|---
    7 |  8  | 9


 *instructions::
    1)Insert the spot number(0-9) to put your sign
    2)You must fill all the sport to obtain the result
    3)Player 1 will go first


"""

def print_board():
    board=f"""

    {syb_dict[0]} |  {syb_dict[1]}  | {syb_dict[2]}
   ---|-----|---
    {syb_dict[3]} |  {syb_dict[4]}  | {syb_dict[5]}  
   ---|-----|---
    {syb_dict[6]} |  {syb_dict[7]}  | {syb_dict[8]}



"""
    print(board)

syb_dict=[]
for i in range(9):
    syb_dict.append(' ')

index_list=[]
def take_input(player_name):
    while True:
        x=int(input(f'{player_name} (Enter position number ): '))
        x-=1
        if 0<=x<10:
            if x in index_list:
                print('This sport in blocked ')
                continue
            index_list.append(x)  
            return x
        print("Please enter number between 1-9 ")


def calcu_res(player1,player2):
    if syb_dict[0]==syb_dict[1]== syb_dict[2]=='X' or syb_dict[3]==syb_dict[4]== syb_dict[5]=='X' or syb_dict[6]==syb_dict[7]== syb_dict[8]=='X' or syb_dict[0]==syb_dict[3]== syb_dict[6]=='X' or syb_dict[1]==syb_dict[4]== syb_dict[7]=='X' or syb_dict[2]==syb_dict[5]== syb_dict[8]=='X' or syb_dict[0]==syb_dict[4]== syb_dict[8]=='X' or syb_dict[2]==syb_dict[4]== syb_dict[6]=='X':
        print(f'Congratulations {player1} !! You Won.')
        quit("Thankyou both for joining ")
    elif syb_dict[0]==syb_dict[1]== syb_dict[2]=='O' or syb_dict[3]==syb_dict[4]== syb_dict[5]=='O' or syb_dict[6]==syb_dict[7]== syb_dict[8]=='O' or syb_dict[0]==syb_dict[3]== syb_dict[6]=='O' or syb_dict[1]==syb_dict[4]== syb_dict[7]=='O' or syb_dict[2]==syb_dict[5]== syb_dict[8]=='O' or syb_dict[0]==syb_dict[4]== syb_dict[8]=='O' or syb_dict[2]==syb_dict[4]== syb_dict[6]=='O':  
        print(f'Congratulations {player2} !! You Won.')
        quit("Thankyou both for joining ")  


def main():
    print("Welcome to tic tac toe game..🔥")
    print()
    player1=input("Enter player one name  ")
    player2=input('Enter player two name  ')
    print()
    print(f'Thankyou for joining {player1} and {player2} ')
    print()

    print(instructions)
    print()
    print(f"{player1} sign is will be -X")
    print(f"{player2} sign is will be -0")
    print("Enter any key to start the game ")

    print_board()

    for i in range(9):
        if i%2==0:
            index=take_input(player1)
            syb_dict[index]='X'
        else:
            index=take_input(player2)  
            syb_dict[index]='O' 
        print_board() 
        calcu_res(player1,player2)   
    print("This is a tie,Play again")      



main()