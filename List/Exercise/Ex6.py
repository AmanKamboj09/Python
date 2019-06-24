petNames = []
while True:
    print('Enter the name of cat ' + str(len(petNames) + 1) +
        ' (Or enter nothing to stop.):')
    name = input()
    if name == '':
        break
    petNames = petNames + [name] # list concatenation
print('The cat names are:')
for name in petNames:
    print(' ' + name)