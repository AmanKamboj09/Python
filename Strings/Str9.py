s1 = " "
seq = ("Ram","Sham","Ajay")
s2 = s1.join(seq)
print(s2)
print( s2.ljust( 50 , '*'))
print( s2.rjust( 50 , '*'))
s1 = "     Hello "
s2 = " World           "
s3 = " Magic "
s4 = s1 + s2 + s3
print( s4 )
s4 = s1.lstrip() + s2 + s3
print( s4 )
s4 = s1.lstrip() + s2.rstrip() + s3
print( s4 )
s4 = s1.strip() + s2.strip() + s3.strip()
print( s4 )