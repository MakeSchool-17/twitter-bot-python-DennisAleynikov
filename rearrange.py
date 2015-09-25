import sys
import random

# get command line arguments
stuff = sys.argv[1:]
# shuffle it with random
random.shuffle(stuff)
# splice it all together
output = ' '.join(stuff)

print(output)
