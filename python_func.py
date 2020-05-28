#/usr/bin/env python
#_*_ coding:utf-8 _*_

def fun(a, b, h):
    s = (a + b) * h / 2
    return s

fun(3, 4, 5)


for a, b, h in [(3, 4, 5), (7, 5, 9), (12, 45, 20), (12, 14, 8), (12, 5, 8) ]:
    print ("up {} , down {} , high {} the stage is {}".format(a, b, h, fun(a,b,h)))

print("")
def trapezoidal_area(upperLength, bottom, height):
    print (( upperLength + bottom ) * height / 2)
    return ( upperLength + bottom ) * height / 2

trapezoidal_area( upperLength = 3, bottom = 4, height = 5 )
trapezoidal_area( upperLength = 4, height = 5, bottom = 4 )

print("")
def trapezoidal_area ( upperLength, bottom, height = 5 ):
    print (( upperLength + bottom ) * height / 2)
    return ( upperLength + bottom ) * height / 2

trapezoidal_area(upperLength = 3, bottom = 4)
trapezoidal_area(3, 4)
trapezoidal_area(3, 4, 5)
trapezoidal_area(3, 4, 10)

print("")
def change_nothing(var):
    var = "changed"

def change_mabe(var):
    var.append("new value")

param1 = "hello"
print( change_nothing(param1)  )

param2 = ["value"]
print(change_mabe(param2))
print(param2)


print ("")
print (" if case ")
print (''' if codition 01:
       satement 01
       elif condition 02:
           statement 02
       else:
           statment 03''')

# the code can save as ls_if.py
def score(num):
    if num >= 90:
        print(num, 'excellent')
    elif num >= 80:
        print(num, 'fine')
    elif num >- 60:
        print(num, 'pass')
    else:
        print(num, 'bac')

score(99)
score(80)
score(70)
score(60)
score(59)

print ("")
a, b = 3, 4
c = a if a < b else b
print (c)
a, b = 5, 4
c = a if a < b else b
print (c)


print ("")
print ("## for and while")
print (''' while condition:
       statement 01
    else:
       satement 02''')


# the code can save as lx_while.py
flag = True
while flag:
    #input_str = input("please input something, 'q' for quit. ->")
    input_str = "q"
    type(input_str)
    #print("your input is : {}".format(input_str))
    print("your input is : %s " % input_str)
    if input_str == 'q':
        flag = False
print ("You are out of circulation.")


print ("")
print ("for")
print (''' for <variable> in <sequence>:
    <statements>
else:
    <statements>''')


sum = 0
for i in range(1000):
    sum += i

print (sum)

print ("")
print ("break and continue")
# the code can save as lx_break_continue.py
print ("break--------------------------")
count = 0
while count < 5:
    print("aaa", count)
    count += 1
    if count == 2:
        break
    print('bbb', count)

print("continue------------------------")
count = 0
while count < 5:
    print('aaa', count)
    count = count + 1
    if count == 2:
        continue
    print('bbb', count)



