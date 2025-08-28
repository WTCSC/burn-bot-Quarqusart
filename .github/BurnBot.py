import sys
import time

NoCounter = 0

def printCool(WhatYouWantToPrint):
    string = WhatYouWantToPrint + '\n'
    for char in string:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(.03)

def addNo(Var):
    if Var.lower() == "no":
        NoCounter+=1

printCool("Hello There User, You think you are so cool coming here don't you?\nWell lets see about that")
time.sleep(1)
printCool("To Begin, could you give me some information about yourself. Super safe I know but I pinky swear that I wont try to steal your identity.\nFor a little bit of collateral, ill give you some of my information, my name is Burn Bot, so you better not steal that")

printCool("First Question, what is your name?")
Name = input("")

printCool("Next we'll go with age, what's yours?")
Age = input("")

printCool("Could you tell me how tall you are please?")
Height = input("")

printCool("Could you please give me the hospital you were born in next?")
PlaceOfOrigin = input("")
addNo(PlaceOfOrigin)

printCool("How about your first pet? What was their name?")
Pet = input("")
addNo(Pet)

printCool("Now lets go with your Fathers middle name. Just common small talk going on here.")
FathersMiddleName = input("")
addNo(FathersMiddleName)

printCool("While we're on the topic of family, whats your mothers Maiden Name?")
MothersMaidenName = input("")
addNo(MothersMaidenName)

printCool("Ok so now if you were to chose a random security question that isn't one of the ones above, what would it be?")
SecurityQuestion = input("")
addNo(SecurityQuestion)

printCool(SecurityQuestion+"?")
SecurityAnswer = input("")
addNo(SecurityAnswer)

printCool("OK, now if you had to make a password, could you input just a random one?")
Password = input("")
addNo(Password)

printCool("And finally, can you give me a good email?")
Email = input("")
addNo(Email)

printCool("Just one more, what's your social security number?")
SocialCode = input("")
addNo(SocialCode)

printCool(f"Alright, lets see what we got here {Name}, Age {Age}, and is {Height}")
time.sleep(0.5)

printCool(f"Dang, your parents really messed you up didn't they? Not only giving you the name {Name}, \nbut aslo giving you that name when you were born, DANG that sucks")
if int(Age) < 20:
    printCool(f"Speaking of your age, you're really that young huh. Can't image what it must be like to be living as a baby during todays day and age. Like wow, do you even know what a CD is??")
else:
    printCool(f"Speaking of age, it seems we've got a grandpa here. Are you still using VHS tapes to watch movies? It must be cool to have been alive during the roaring 20's")
printCool("I'm just gonna skip over your height, becuase that doesn't really matter does it? Or at least you can't control it, unlike your name or age.")
time.sleep(0.5)

printCool("Okay, now lets see if you were dim enough to believe me earlier and you gave me all your accounts, or if you at least have something knocking around in the noggin of yours")
if NoCounter > 5:
    printCool("Dannggg, we really got a braniac here, you said no to my inquires {NoCounter} times. I really don't know what to do with you, I guess that I have to leave you here.\nWell then, good bye Mr. Cybersecurity, I guess I won't be taking over all your accounts, which knowing you probably all have different passwords, you're so special.")
else:
    printCool("Well, lookie here, you really gave me everything didn't you. If I were'nt just a a python script, you'd be done, identity taken, I could probably become you if I tried hard enough.")