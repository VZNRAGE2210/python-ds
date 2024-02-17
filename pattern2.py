from turtle import*
speed(0)
bgcolor('red')
def polygon(side, size):
    for i in range(side):
        fd(100)
        lt(360/side)

#calling
polygon(3,150)
polygon(4,100)
polygon(5,75)
polygon(10,120)
mainloop()