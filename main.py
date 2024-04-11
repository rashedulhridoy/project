import random
import pyfiglet 


print(pyfiglet.figlet_format("Yes or No"))

c = """
> Made By Rashedul Hridoy
"""

print(c)



say = ("Yes", "No")
m = "Robot: "

fuck = ("Don't Ask Again, I Hate This", "lol")

while True:
    xd = input("Me: ")
    x = random.choice(say)
    y = random.choice(fuck)
    if xd == "exit":
        print(m + "Goodbye :D")
        exit()
    elif xd == "Fuck You" or xd == "fuck you":
        print(m + "Fuck You Too!", "🖕")
        #exit()

    elif xd == "You Love Me" or xd == "you love me" or xd == "You Love Me ?" or xd == "you love me ?" or xd == "you love me ??" or xd == "you love me ???":
        
        print(m + y)
    elif xd == "i love you" or xd == "I Love You":
        print(m + y)
    elif xd == "okay i am sorry" or xd == "sorry" or xd == "Sorry":
        print(m + "🙂")
    else:
        print(m + x)