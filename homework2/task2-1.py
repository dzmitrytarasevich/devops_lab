number_of_students=n=3
number_of_subjects=m=3
dict1={'name':'Krishna','maths':67,'physics':68,'chemistry':69}
dict2={'name':'Arjun','maths':70,'physics':98,'chemistry':63}
dict3={'name':'Malika','maths':52,'physics':56,'chemistry':60}
Krishna=(dict1['maths']+dict1['physics']+dict1['chemistry'])/m
Arjun=(dict2['maths']+dict2['physics']+dict2['chemistry'])/m
Malika=(dict3['maths']+dict3['physics']+dict3['chemistry'])/m
print "Number of students is:", n
print "Average mark of Krishna is:", format(Krishna,'.2f')
print "Average mark of Arjun is:", format(Arjun,'.2f')
print "Average mark of Malika is:", format(Malika,'.2f')
