count = 0
uscore = 0
cscore = 0

while count < 3:
  count += 1
  prompt = raw_input('Rock Paper Scissors?: ').lower()

  import random
  for i in range(1):
    gen = random.randint(1,3)
  
  if prompt == 'rock' and gen == 1:
    print 'Draw' 
  elif prompt == 'rock' and gen == 2:
    cscore += 1
    print 'You lose!  Paper beats Rock'
  elif prompt == 'rock' and gen == 3:
    uscore += 1
    print 'You win! Rock beats Scissors'

  if prompt == 'paper' and gen == 1:
    uscore += 1
    print 'You win! Paper beats Rock' 
  elif prompt == 'paper' and gen == 2:
    print 'Draw'
  elif prompt == 'paper' and gen == 3:
    cscore += 1
    print 'You lose! Scissors beats Paper'
 
  if prompt == 'scissors' and gen == 1:
    cscore += 1
    print 'You lose! Rock beats Scissors' 
  elif prompt == 'scissors' and gen == 2:
    uscore += 1
    print 'You win! Scissors beats Paper'
  elif prompt == 'scissors' and gen == 3:
    print 'Draw'


print 'You: ' + str(uscore) + ' Computer: ' + str(cscore)

if uscore > cscore:
  print 'You win!'
elif uscore == cscore:
  print 'Draw!'
else:
  print 'Game over! Try again'

