import random

random_string = ''

list = ['i', '¡', ':', '!', '|', '¦', ';', '—', '\'']

for _ in range(30):
    random_string += (random.choice(list))

print(random_string)


