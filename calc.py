import time

def add(a, b):
    return str(int(a) + int(b))

def subtract(a, b):
    return str(int(a) - int(b))

def multiply(a, b):
    return str(int(a) * int(b))

def divide(a, b):
    if int(b) != 0:
        return str((int(a)/int(b)))
    else:
        return "ERROR, YOUR STUPID BRAIN WANTED TO DIVIDE BY 0, THATS YOUR ANSWER"

def exponentiaion(a,b):
    return str(int(a)**int(b))

while True:
    if input("Oh, another one? Are you really sure you want to do this?(The correct answer is no)(yes/no)\n").lower() == "yes":
        print("Uhgg, I guess we're doing this, then. You better not fall behind because I just really don't care")
    else:
        break
    
    what_to_do = input("Well I guess if you're forcing me to, would you PLEASE put in the operation you would like to do\nYou better do it correctly and im only gonna say it once\ninput a (+,-,*,/,^) b, with spaces, so some examples would be 1 + 2, or 3 * 4 or 9 / 10 or 5 ^ 2. If you don't know what one of these does just give us all an easier time and just don't use it.\nNow get on it, what do you want to do\n")
    
    if what_to_do.count(" ") == 2:
        what_to_do_list = what_to_do.split()
    else:
        print("You did that wrong, I don't want to deal with you any more")
        break
    
    if what_to_do_list[1] == "+":
        print("Your answer is: " + add(what_to_do_list[0],what_to_do_list[2]) + ", now scram")
    elif what_to_do_list[1] == "-":
        print("Your answer is: " + subtract(what_to_do_list[0],what_to_do_list[2]) + ", now scram")
    elif what_to_do_list[1] == "*":
        print("Your answer is: " + multiply(what_to_do_list[0],what_to_do_list[2]) + ", now scram")
    elif what_to_do_list[1] == "/":
        print("Your answer is: " + divide(what_to_do_list[0],what_to_do_list[2]) + ", now scram")
    elif what_to_do_list[1] == "^":
        print("Your answer is: " + exponentiaion(what_to_do_list[0],what_to_do_list[2]) + ", now scram")
    
    time.sleep(1)

    if input("Well, apparently I'm supposed to ask if you want to do this again, so do you(yes/no)\n").lower() == "no":
        print("Okay, im gonna go to bed now")
        break
    elif input("Are you SURE?? Because I know I really don't want to(yes/no)\n").lower() == "no":
        print("yay")
        break


time.sleep(1)
print("If you're reading this you either quit or annoyed me enough to make you quite, either way I hope to never see you again, BYE")