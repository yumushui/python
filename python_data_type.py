#!/usr/bin/env python
#_*_ coding:utf-8 _*_

''' python data type : number  '''
print ("## 1 python numbe ")
2 + 2
50 - 5 * 6
(50 - 5*6) /4
8 / 5

19 / 3
19 // 3
17 % 3
5 * 3 + 2.0
5 ** 2
2 ** 7

print ("int(x)  can make x to a int.")
print ("float(x) can make x to a float.")
print ("complex(x) can make x to a complex")
print ("many number functions")

''' python data type : string '''
print ("")
print ("## python string")
print ("01 define string")
print (" \'abc\' ")
print (" \"abc\" ")
print ('''  abc
       efg
       hil ''' )

a =  'a\'b\'c'
print (a)
b = "a'b'c"
print (b)


S = 'First line. \n Second line.'
print(S)
s = ''' Fist line.
Second line. '''
print(s)

s = r"This is a rather log string containing\n\
        serval lines of text muchk as you would do in C."
print(s)

word = 'Help' + '  ' + 'ME'
print(word)
word = "word " * 5
print (word)

print("")
print ("02  the index of string")
s = "abcdefg"
print(s[0])
print(s[1])
s[:]
s[2:3]
s[2:]
s[-1]
s[-2:]
#s[0] = 'f'

print("")
print("03  travesal string")
print(s)

for i,a in enumerate(s):
    print(i, a)

for a in s:
    print(a)

for i in range(len(s)):
    print(s, s[i])

print ("")
print ("04  strings format")
print ("My name is %s , I am %d years old . " % ('feixiang.zhao', 30)) 
print ("My name is {} , I am {} years old .  ".format('feixiang.zhao', 30))
print ("My name is {0}, I am {1} years old. ".format('feixiang.zhao', 30))

print ("")
print ("05 string internel functions")
print ("print (dir(s))")
print (dir(s))


print("")
print("")
print("## python data type : list and tuple")
print("")
print("01 define list")
list1 = ['Google', 'Huawei', 1997, 2000]
list2 = [1, 2, 3, 4, 5]
list3 = ["a", "b", "c", "d"]
list4 = ["all of them", list1, list2, list3 ]
print ("list1[0]: ", list1[0])
print ("list2[1:5]:  ", list2[1:5])
print (list4)
print (list4[1][1])

print("")
print("02 update list")
list = ['Google', 'Huawei', 1997, 2000]
print ('the third word :', list[2])
list.append('aliyun')
print('the apped last word is :', list[-1] )
list.insert(2, 'baidu')
print('the 3 location insert word is : ', list[2])
print(list)

print("")
print("03 delete list")
list = ['Google', 'Huawei', 1997, 2000]
print(list)
print("del list[0]")
del list[0]
print(list)

print("the list usually functions :")
len([1, 2, 3])
[1, 2, 3] + [4, 5, 6]
['Hi!'] * 10
3 in [1, 2, 3]
for x in [1, 2, 3]: print(x)
max([1, 2, 3])
min([1, 2, 3])



print("")
print ("04  the usage of tuple")
t = ("Google", "Huawei", 1997, 2000)
print(t)
print(t[0])
print(t[-1])
#t[0] = "Baidu"
t = ()
print(type(t))
t = (1,)
print((1) == 1)

print("")
print ("05  one of tuple is list")
a = ['a', 'b']
b = ['c', 'd']
t = ('e', 'f', a)
print(t)
t[2][0]  = 'x'
t[2][1]  = 'y'
print(a)
print(t)
#t[2] = b

print("")
print("## python data type : dict") 
print ("")
print ("01 define dict")
dict = { 'hello':'你好', 'world':'世界',  }
print(dict)
dict['hello']
len(dict)
str(dict)
dict = { 'hello':'你好', 'world':'世界', 'hello':'world'  }
print(dict)
print("the dict key can not change.")

print("")
print("02 遍历dict")
d = { 'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6  }
print(d)
for key, value in d.items():
    print(key, value)

for key in d:
    print(key, d[key])


print("")
print("03 update dict")
d = { 'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6  }
d['b'] = 'back'
print(d)

print("")
print("04 delete dict")
del d['b'] 
print(d)
d.clear()
print(d)
del d
#print(d)


print("")
print("")
print("## python data type : set")
print("")
print("01 define set")
x = set('abcd')
y = set(['a', 'bc', 'd', 10])
print (x, y)
print (x & y)
print (x | y)
print (x - y)
print (x ^ y)

print("")
print("02 distinct set")
a = [ 11, 22, 33, 44, 11, 22 ]
b = set(a)
print (a, b)









