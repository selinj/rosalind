a = 42
if a < 10:
    print 'the number is less than 10'
else:
        print 'the number is greater or equal to 10'


b = -38
if a + b ==4:
    print 'printed when a + b equals four'
print 'always printed'

print a
print b


#while loop

counter = 1
while counter <=3:
    print 'Hello!' * counter #increment counter by 1
    counter = counter + 1

names = ['Alice', 'Bob', 'Charlie']
for name in names:
    print 'Hello, ' + name

n = 10
for i in range(n):
    print i

#range is a function that creates a list of integers between
    #0 and n

    print range(5, 12)
