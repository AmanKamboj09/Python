# List comprehension

# Syntax
# list = [expresion for val in collection]
# list = [expresion for val in collection if <Condition>]
# list = [expresion for val1 in list1 and val2 in list2]

lst = []
for i in range(1,11):
    lst.append(i**2)

sq = [i**2 for i in range (1,11)]
print(sq)

neg = [-i for i in range (1,11)]
print(neg)

# program to convert the values of list in fahrenheit
list1 = [32,33,38]
F = [(9/5)*x+32 for x in list1]
print(F)

# Divisible by 5
L1 =[i for i in range(1,50) if i%5 ==0]
print(L1)

Names = ['Rohit', 'Sumit', 'Amit']
new = [name[0] for name in Names]
print(new)

# Cartesian Product
A = [1,3,5]
B = [2,4,6]
Car_Prod = [(a,b) for a in A for b in B]
print(Car_Prod, '\n')

Movies =['Bharat', 'Gully Boy', 'Total Dhamaal', 'Kesari']
L2 = [title for title in Movies if title.startswith('Gully')]
print(L2)