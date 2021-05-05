n = int(input("Enter the number of students:"))
data = {} 
languages = ('Physics', 'Maths', 'History') 
for i in range(0, n): 
    name = input('Enter the name of the student %d: ' % (i + 1)) 
    marks = []
    for x in languages:
        marks.append(int(input('Enter marks of %s: ' % x))) 
    data[name] = marks
for x, y in data.items():
    total =  sum(y)
    print("%s 's  total marks %d" % (x, total))
    if total < 120:
        print("%s failed :(" % x)
    else:
        print("%s passed :)" % x)
