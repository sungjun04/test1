import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
# import random as r

c1 = st.radio('선의 색을 선택하시오', ['red', 'green', 'blue', 'orange'])
s1 = st.radio('선의 형태를 선택하시오', ['-', ':', '-.', '--'])

fig, ax = plt.subplots()

x = []
y = []
for i in range(-20, 21, 2):   
    x.append(i)
    y.append(3*i*i - 5*1 + 2)

# plt.plot(x,y, 'rs-', linewidth = 2)

plt.plot(x, y, color=c1, linestyle=s1, marker='h')


st.pyplot(fig)


import sys
# sys.exit()

fig, ax = plt.subplots()

x = []
for i in range(-00, 21, 15): 
# for i in range(-100, 100):
    i
    x.append(i/10.0)

col = st.columns(3)
with col[0]:
    a = st.number_input('Insert a', step = 1)
with col[1]:
    b = st.number_input('Insert b', step = 1)
with col[2]:
    c = st.number_input('Insert c', step = 1)

y = []
for i in x:
    y.append(a*i**2 + b*i + c)

plt.plot(x, y)
st.pyplot(fig)




# s1 = 1
# s2 = 2
# s3 = 3
# s4 = 4
# s5 = 5
# s1, s2, 3, s4, s5

# s = ['a', 'b', 'c', 'd', 'e']


# s.append ('사과')


# a1 = random.randint(1, 45)
# a1



# import turtle

# t = turtle.Turtle()

# t.shape('turtle')
# t.speed(0)
# t.pensize(5)
# # t.goto(-50,0)

# def tree(lenght):
#     if lenght > 5:
#         t.forward(lenght)
#         t.right(20)
#         tree(lenght-15)
#         t.left(40)
#         tree(lenght-15)
#         t.right(20)
#         t.backward(lenght)

# t = turtle.Turtle()
# t. left(90)

# t.color("green")
# t.speed(0)
# tree(90)


#     # for j in range(sh):
#     #         t.forward(1 + 5*1)
#     #         t.left(360/sh)




# sh = 3
# while True:
#     for i in range(30):
#         # shape(5)
#         t.forward(1 + 5*i)
#         # t.left(120/sh)
#         t.forward(1 + 5*i)
#         t.left(90)
#         t.forward(1 + 5*i)
#         t.left(90)
#         t.forward(1 + 5*i)
#         t.left(90)
#         # t.circle(1 + 5*i)
#         t.color((r.random(), r.random(), r.random()))
#         t.goto(i*20, 0)
#     # t.clear()



# # t.color((r.random(), 77/255(), 239/255(), 93/255()))

# # t.forward(100)

# #  77/255(), 239/255(), 93/255()
# turtle.done()



# screen = turtle.Screen()
# image = '카피바라.gif'


# t1 = turtle.Turtle()
# t2 = turtle.Turtle()

# t1.shape('turtle')
# t2.shape('turtle')

# t1.penup()
# t1.shapesize(3)
# t1.pensize(5)
# t1.goto(-300,100)

# t2.penup()
# t2.shapesize(3)
# t2.pensize(5)
# t2.goto(-300,-100)

# t1.pendown()
# t2.pendown()
# t1.speed(1)
# t2.speed(1)

# for i in range(50):
#     d1 = r.randint(1, 30)
#     t1.forward(d1)
#     d2=r.randint(1, 30)
#     t2.forward(d2)

# turtle.done()

# t.speed(1)

# def rec(x, y, lx, ly):
#     turtle.bgcolor('yellow')
#     t.width(3)
#     t.color('blue')
#     t.up()
#     t.goto(x, y)
#     t.down()
#     for l in range(2):
#         t.forward(lx)
#         t.left(90)
#         t.forward(ly)
#         t.left(90)
    

# rec(-200, 0, 100, 50)
# rec(0, 0, 100, 150)
# rec(200, 0, 100, 100)







# def user_sum(n):   
#     s = 0
#     for i in range(1, n+1):
#         s = s + i
#     s

# user_sum(100)
# user_sum(200)


# s = 0
# for i in range(10, 21):
#     s = s +i
#     s






# range(1,100,5)




# for i in range(1, 100):
#     if i%5 == 2:
#         i

# p = int(input("100"))
# q = int(input("10"))
# print("10=", p // q)
# print("10=", p // q)





# age = 20
# if age < 20:
#     print('aa')
# else:
#     print('bb')




# 'apple' + 'grape'
# 'apple' * 3





'나는' + '12' + '개의 사과를 먹었다.'












# import turtle

# t = turtle.Turtle()
# t.shape('turtle')
# t.speed(0)


# colors = {'red', 'purple', 'blue', 'yellow', 'orange', 'green' }


# t.width(2)
# t.pencolor('black')



# lenght = 5
# for i in range(100):
#     t.forward(lenght)
#     # t.pencolor(colors[lenght%6])
#     t.right(89)
#     lenght += 5




# turtle.done()



# for i in range(20):
#     t.circle(80)
#     t.left(90)





# t.circle(100) # 80 : 픽섹(원의 반지름)
# t.left(60) # 60 : 각도
# t.circle(100)
# t.left(60)
# t.circle(100)
# t.left(60)
# t.circle(100)
# t.left(60)
# t.circle(100)
# t.left(60)
# t.circle(100)





# for i in range(1, 10):
#     if i%3 == 1:
#         i



# s = 70
# if s >= 90:
#     st.wrrite('귀하의 점수는 '+ str(s)+ '점으로 :blue[A등급]입니다')
# elif s >= 80:
#     '# 귀하의 점수는 '+ str(s) +'점으로 :green[B등급]입니다.'
# elif s >= 70:
#     '# 귀하의 점수는 '+ str(s) +'점으로 :orange[C등급]입니다.'
# elif s >= 60:
#     '# 귀하의 점수는 '+ str(s) +'점으로 :blue[D등급]입니다.'
# else:
#     '# 귀하의 점수는 '+ str(s) +'점으로 :red[F등급]입니다.'











# st.latex(r'''
#     a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
#     \sum_{k=0}^{n-1} ar^k =
#     a \left(\frac{1-r^{n}}{1-r}\right)
#     ''')



# a = 1
# b = '1 '
# c = '1'

# b+c

# print('a=',a)
# 'a=', a
# b
# c

# x = 100

# x += 5
# x -=10
# x


# s = 0 # 초기값
# for i in range(12 , 1001, 2):
#     's = ', s, 'i = ', i
#     s = s + 1
    # s += i
#     's + 1 = ', s 



# s





























# '7과 4의 산술 연산'

# '덧셈', 7 + 4
# '뺄셈', 7 - 4
# '곱셈', 7 * 4
# '나눗셈', 7 // 4
# '몫', 7 / 4
# '나머지', 7 % 4
# '거듭제곱', 2 ** 4





# import turtle


# t = turtle.Turtle()
# t.shape('turtle')


# turtle.done()

# r = 15
# pi = 3.14
# area = pi*r**2

# area



# distance = 50
# angle = 90
# for i in range(4):
#     t.forward(distance)
#     t.left(anfle)

# x = 100
# x
# y = x + 100
# y
# x + y = 100
# x

# a = 3.141592*10*10.0
# b = (1/100)*1234

# print(a, b)
# a, b

# print('Hello')
# st.write('Hello')
# # st.write('강아지'+'고양이')
# # st.write('1'+'1')

# st.write('스트리밋 .......')
# st.title('streamlit Image')
# st.image('im,jpg')

