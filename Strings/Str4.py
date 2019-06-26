#Formats used in strings
n1 = 43
n2 = 54
ans = n1 + n2
print( ' [ ' + str(n1) + ' + ' + str(n2) + ' = ' + str(ans) + ' ] ')
print(' [ {} + {} = {} ] '.format( n1 , n2 , ans ))
print(' [ %d + %d = %d ] ' % (n1,n2,ans))
