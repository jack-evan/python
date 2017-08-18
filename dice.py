import random
total = 0
for i in range(2):
  a = random.randint(1,6)
  total = total + a
  print 'Dice: ' + str(a)
print 'Total Score: ' + str(total)
