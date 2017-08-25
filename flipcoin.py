# flip coin 

import random

#generate random value (can only be 1 or 2)
for i in range(1):
  coin = random.randint(1,2)

#prompt user for heads or tails
prompt = raw_input('Heads or Tails? ').lower()

#compare user value with coin flip
if prompt == 'heads' and coin == 1:
  print 'You win!'
elif prompt == 'tails' and coin == 2:
  print 'You win!'
else:
  print 'Better luck next time'

