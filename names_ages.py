age = 0
name= 0
def doehet():
    print(zin)

while age or name != "stop":
    name = input('what is your name? ')
    if name  == "stop":
        exit()
    age = input('what is your age? ')
    if age  == "stop":
        exit()
    zin = 'Hallo '+str(name)+ ', je leeftijd is '+str(age)
    doehet()


if age  != "stop":
    exit()