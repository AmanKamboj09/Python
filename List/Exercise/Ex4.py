#Changing Values in a List with Indexes
spam = ['cat', 'bat', 'rat', 'elephant']
spam[1] = 'aardvark'
print(spam)

spam[2] = spam[1]
print(spam)

spam[-1] = 12345
print(spam)

#List Concatenation and List Replication
print([1, 2, 3] + ['A', 'B', 'C'])

print(['X', 'Y', 'Z'] * 3)

spam = [1, 2, 3]
spam = spam + ['A', 'B', 'C']
print(spam)

#Removing Values from Lists with del Statements
spam = ['cat', 'bat', 'rat', 'elephant']
del spam[2]
print(spam)

del spam[2]
print(spam)