#
r = 4 > 6
o = 2 < 9 > 7 > 5
g = 4 < 6

print(f'{o.__bool__()} , {g} , {r.__bool__()}')
print(f'{r} , {bool(o)}')
