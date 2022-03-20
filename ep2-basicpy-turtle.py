import turtle
tao = turtle.Pen()    #ดึงความสามารถการใช้ปากกา
tao.shape('turtle')   #แปลงร่างเป็นเต่า
tao.speed(20)         #กำหนดความเร็วเต่า

def Rectangle():
    '''ฟังก์ชั่นนี้เอาใว้วาดรูปสี่เหลี่ยม'''
    for i in range(74):
        tao.color('blue')
        tao.left(25)
        tao.forward(100)
        tao.left(90)

def Circle():
    '''ฟังก์ชั่นนี้เอาใว้วาดรูปวงกลม'''
    for i in range(1):
        tao.color('yellow')
        tao.circle(100)
            
def Triangle():
    '''ฟังก์ชั่นนี้เอาใว้วาดรูปสามเหลี่ยม'''
    for i in range(12):
        tao.color('red')
        tao.right(90)
        tao.forward(100)
        tao.right(120)
        tao.forward(100)
        tao.right(120)
        tao.forward(100)

def Go(x,y):
    tao.penup()
    tao.goto(x,y)
    tao.pendown()


Triangle()
Go(0,-100)
Circle()
Go(-30,-50)
Rectangle()
tao.color('black')
Go(0,0)






    

