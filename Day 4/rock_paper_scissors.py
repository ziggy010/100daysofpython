import random;

rock = '''
                _    
               | |   
 _ __ ___   ___| | __
| '__/ _ \ / __| |/ /
| | | (_) | (__|   < 
|_|  \___/ \___|_|\_

'''

paper = '''
                             
                             
 _ __   __ _ _ __   ___ _ __ 
| '_ \ / _` | '_ \ / _ \ '__|
| |_) | (_| | |_) |  __/ |   
| .__/ \__,_| .__/ \___|_|   
| |         | |              
|_|         |_|           


'''

scissors = ''' 
                                 
                              
                                                                              
                     88                                                       
                     ""                                                       
                                                                              
,adPPYba,  ,adPPYba, 88 ,adPPYba, ,adPPYba,  ,adPPYba,  8b,dPPYba, ,adPPYba,  
I8[    "" a8"     "" 88 I8[    "" I8[    "" a8"     "8a 88P'   "Y8 I8[    ""  
 `"Y8ba,  8b         88  `"Y8ba,   `"Y8ba,  8b       d8 88          `"Y8ba,   
aa    ]8I "8a,   ,aa 88 aa    ]8I aa    ]8I "8a,   ,a8" 88         aa    ]8I  
`"YbbdP"'  `"Ybbd8"' 88 `"YbbdP"' `"YbbdP"'  `"YbbdP"'  88         `"YbbdP"'  
                                   



'''

my_list = [rock, paper, scissors];




user_input = int(input("\nChoose 0 for rock, 1 for paper, 2 for scissors!\n- "))

computer = random.randint(0,2);

print("\nYou chose: \n")

if user_input == 0:
    print(rock)
    print("\nComputer chose: \n")
    print(my_list[computer]);
    if computer == 0:
        print("\nDraw!\n")
    elif computer == 1:
        print("\nYou lose!\n")
    else:
        print("\nYou won!\n")
elif user_input == 1:
    print(paper)
    print("\nComputer chose: \n")
    print(my_list[computer]);
    if computer == 0:
        print("\nYou won!\n")
    elif computer == 1:
        print("\nDraw!\n")
    else:
        print("\nYou Lost!\n")
elif user_input == 2:
    print(scissors)
    print("\nComputer chose: \n")
    print(my_list[computer]);
    if computer == 0:
        print("\nYou lost!\n")
    elif computer == 1:
        print("\nYou won!\n")
    else:
        print("\nDraw!\n")
else:
    print("\nPlease input right numbers!\n")


