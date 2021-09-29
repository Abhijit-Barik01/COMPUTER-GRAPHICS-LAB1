'''x=10
def lol():
    print("local")
    global x
    x+=5
    print(x)
lol()'''
li=[1,"ji",4,5,6]
def num(*a):
    print(a)
num(*li)