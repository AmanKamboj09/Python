#Using for Loops with Lists
for i in range(4):
    print(i)

for i in [0, 1, 2, 3]:
    print(i)

supplies = ['pens', 'staplers', 'flame-throwers', 'binders']
for i in range(len(supplies)):
    print('Index ' + str(i) + ' in supplies is: ' + supplies[i])

#The in and not in Operators

'howdy' in ['hello', 'hi', 'howdy', 'heyas']

spam = ['hello', 'hi', 'howdy', 'heyas']
print('cat' in spam)

print('howdy' not in spam)

print('cat' not in spam)