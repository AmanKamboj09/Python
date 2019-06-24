#Finding a Value in a List with the index() Method

spam = ['hello', 'hi', 'howdy', 'heyas']
print(spam.index('hello'))

print(spam.index('heyas'))

print(spam.index('howdy howdy howdy'))

#Adding Values to Lists with the append() and insert() Methods
spam = ['cat', 'dog', 'bat']
spam.append('moose')
print(spam)

spam = ['cat', 'dog', 'bat']
spam.insert(1, 'chicken')
print(spam)

#Removing Values from Lists with remove()
spam = ['cat', 'bat', 'rat', 'elephant']
spam.remove('bat')
print(spam)

spam = ['cat', 'bat', 'rat', 'cat', 'hat', 'cat']
spam.remove('cat')
print(spam)