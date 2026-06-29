marks=[85, 92, 78, 96, 88,55]
print(marks)
print(type(marks))
print(len(marks))
a=[3,]
print(a)
print(marks[2])
print(marks[-2:])
marks.append(52)#add new element in last
print(marks)
marks.insert(1,34)#add new element on particular place
print(marks)
marks[0]=78
print(marks)
marks.sort()#arrange list in ascending order
print(marks)
marks.sort(reverse=True)#arrange list in descending order
print(marks)
marks.reverse()#reverse the order of elements
print(marks)
marks.remove(88)#remove specific element
print(marks)
marks.pop(1)#remove element at specific index
print(marks)
#merge two lists
x=[2,3,4,5,6]
y=[10,20,30,40,50]
z=x+y
print(z)
#duplicate any element in list
d=2*x
print(d)
