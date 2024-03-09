import re

def snake_to_camel(word):
    return ''.join(x.capitalize() or '_' for x in word.split('_'))

test = "Pochemu_by_i_net"
print(snake_to_camel(test))