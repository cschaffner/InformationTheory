import random

randstring = ''
for i in range(10000):
  if random.uniform(0,1) <= 0.01:
    randstring += '1' 
  else:
    randstring += '0'

with open('random.txt', 'w') as fout:
    fout.write(randstring) 