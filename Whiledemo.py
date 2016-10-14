
for num in range (1, 20): #range from 10 to 20
    for i in range (2, num):
       if num % i == 0:
          j = num / i
          print '%d equals %d * %d ' % (num, i, j)
          break
    else:
        print num, 'is a prime number'


#second approach to find the prime number

print "--------------------Second Approach -----------------"
i = 2
while(i < 100):
 j = 2
 while(j <= (i/j)):
   if not(i%j): break
   j = j + 1
 if (j > i/j) : print i, " is prime"
 i = i + 1
