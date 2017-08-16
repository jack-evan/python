import random

gen = "abcdefghijklmnopqrstuvwxyz0123456789"
pw_length = input("Whats the length of your password? ")
mypw = ""

for i in range(pw_length):
  next_index = random.randrange(len(gen))
  mypw = mypw + gen[next_index]
print mypw

