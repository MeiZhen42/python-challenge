import webbrowser as wb
x = 'e'.join('nvr')
y = 'annog'[::-1]
z = 'forgive'[-4:]
a = ('me', 'you')[1]
b = 'soup'.split('o')[1]
list1 = [x, y, z, a, b]
print(" ".join(list1))
c = 'naetviegr'[::2]
d = 'aegonnar'[2:-1]
e = 'wet eal'[::-2].rstrip('w')
f = 'your table is ready'[:3]
g = 'up down all around'.split(' ')[1]
list2 = [c, d, e, f, g]
print(" ".join(list2))
random_nums = [104, 116, 116, 112, 115, 58, \
    47, 47, 119, 119, 119, 46, 121, 111, 117, \
        116, 117, 98, 101, 46, 99, 111, 109, 47, \
            119, 97, 116, 99, 104, 63, 118, 61, 100, \
                81, 119, 52, 119, 57, 87, 103, 88, 99, 81]
messy_string = ""
for i in random_nums:
    messy_string += chr(i)
wb.open(messy_string)