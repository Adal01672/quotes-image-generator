import random
import string
t=False

def unique_key():   
    result = ''.join((random.choice(string.ascii_lowercase) for x in range(10)))
    with open('key.txt', 'a') as f:
        f.write(result+'\n')
        return result
