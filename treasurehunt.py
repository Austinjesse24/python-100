print('''
       ,__                                                  _, \n
    \~\|  ~~---___              ,                          | \n
     | Wash.| |   ~~~~~~~|~~~~~| ~~---,   _            VT_/,ME> \n
    /~-_--__| |  Montana |N Dak\ Minn/ ~\~_/Mich.     /~| ||,' \n
    |Oregon |  \         |------|   { WI / /~)     __-NY',|_\,NH \n
   /       |Ida.|~~~~~~~~|S Dak.\    \   | | '~\  |_____,|~,-'Mass. \n
   |~~--__ |    | Wyoming|____  |~~~~~|--| |__ /_-'Penn.{,~Conn (RI) \n
   |   |  ~~~|~~|        |    ~~\ Iowa/  `-' |`~ |~_____{/NJ \n
   |   | Nev |  '---------, Nebr.\----|   |IN|OH,' ~/~\,|`MD (DE) \n
   ',  \     |Utah| Colo. |~~~~~~~|    \IL| ,'~~\WV/ VA | \n
    |Cal\    |    |       | Kansas| MO  \_-~ KY /`~___--\ \n
    ',   \  ,-----|-------+-------'_____/__----~~/N Car./
     '_   '\|     |      |~~~|Okla.|    | Tenn._/-,~~-,/ \n
       \    |Ariz.| New  |   |_    |Ark./~~|~~\    \,/S Car. \n
        ~~~-'     | Mex. |     `~~~\___|MS |AL | GA / \n
            '-,_  | _____|          |  /   | ,-'---~\ \n
                `~'~  \    Texas    |LA`--,~~~~-~~,FL\ \n
                       \/~\      /~~~`---`         |  \ \n
                           \    /                   \  |  -jorn \n
                            \  |                     '\' \n
                             `~")''')

print("Welcome to Treasure Country.")
print("Your mission is to find the treasure.")

choice1 = input("You're in the States. Where do you want to go? Type 'south' or 'north': ").lower()

if choice1 == "south":
    choice2 = input("You have reached the south side. Which direction do you want to go? Type 'right' or 'left': ").lower()

    if choice2 == "left":
        choice3 = input(
            "There are four possible states where the treasure could be:\n"
            "- Texas\n- Utah\n- California\n- Arizona\n"
            "Which state do you choose? "
        ).lower()

        if choice3 == "arizona":
            print("You died of thirst before you found the treasure. Game Over.")
        elif choice3 == "california":
            print("You were arrested for trespassing. Game Over.")
        elif choice3 == "utah":
            print("You fell into a chemical plant. Game Over.")
        elif choice3 == "texas":
            print("You found the treasure in the city of Dallas at a McDonald's restaurant. Congratulations!")
        else:
            print("You chose a state that doesn't exist. Game Over.")
    else:
        print("You went the wrong direction. Game Over.") 
else:
    print("You got lost. Game Over.")
