s1 = "hello"
s2 = "Hello"
print( s1 == s2 ) #False
print( s1.lower() == s2.lower() ) #True
ustring = u'A unicode \u018e string \xf1'
print( ustring )
result = ustring.encode('utf-8')
print( result )
s3 = result.decode('utf-8')
print( s3 )