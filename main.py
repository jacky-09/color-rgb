import turtle
# rgb输入框
r = turtle.textinput("red：","红色比例（0-255）：")
g = turtle.textinput("green：","绿色比例（0-255）：")
b = turtle.textinput("blue：","蓝色比例（0-255）：")
t = turtle.Pen()
# 打印文字
t.penup()
t.goto(-200,-200)
t.pendown()
text = "R=" + r + "；" + "G=" + g + "；" + "B=" + b + "."
t.write(text,font=("Aria",20,"normal"))
# 度数
num = int(r)+int(g)+int(b)
rd = 360*int(r)/num
gd = 360*int(g)/num
bd = 360*int(b)/num
#绘制饼图
'''
t.penup()
t.goto(200,200)
t.pendown()
t.circle("red",int(rd))
t.circle("green",int(rd))
t.circle("blue",int(rd))
'''
# 绘制混合图形
turtle.colormode(255) # 重点
t.penup()
t.goto(0,0)
t.pendown()
t.fillcolor((int(r),int(g),int(b)))
t.begin_fill()
t.circle(100)
t.end_fill()


