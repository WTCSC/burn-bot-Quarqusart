import sys
import time

def printCool(WhatYouWantToPrint):
    string = WhatYouWantToPrint + '\n'
    for char in string:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(.03)

printCool("Hello There User, You think you are so cool coming here don't you?\nWell lets see about that")
time.sleep(1)
printCool("To Begin, could you give me some information about yourself. Super safe I know but I pinky swear that I wont try to steal your identity.\nFor a little bit of collateral, illl give you some of my information, my name is Burn Bot, so you better not steal that")

printCool("First Question, what is your name?")
Name = input("")

printCool("Next we'll go with age, what's yours?")
Age = input("")

printCool("Could you tell me how tall you are please?")
Height = input("")

printCool("Could you please give me the hospital you were born in next?")
PlaceOfOrigin = input("")

printCool("How about your first pet?")
Pet = input("")

printCool("Now lets go with your Fathers middle name. Just common small talk going on here.")
FathersMiddleName = input("")

printCool("While we're on the topic of family, whats your mothers Maiden Name?")
MothersMaidenName = input("")

printCool("Ok so now if you were to chose a random security question that isn't one of the ones above, what would it be?")
SecurityQuestion = input("")

printCool(SecurityQuestion+"?")
SecurityAnswer = input("")

printCool("OK, now if you had to make a password, could you input just a random one?")
Password = input("")

printCool("And finally, can you give me a good email?")
Email = input("")

printCool("Just one more, what's your social security number?")
SocialCode = input("")

numNos = 0
printCool(f"Alright, lets see what we got here {Name}, Age {Age}, and is {Height}")
time.sleep(0.5)
printCool(f"Dang, your parents really messed you up didn't they? Not only giving you the")
