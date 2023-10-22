
for Fruit in ['Mango','Berry','Banana','Jackfruit' ]:
    for fish in ['Tuna','Hilsha','whale']:
        print(f"{Fruit} , {fish}")


for fish in ['Tuna','Hilsha','whale']:
    for Fruit in ['Mango', 'Berry', 'Banana', 'Jackfruit']:
        print(f"{fish} ,{Fruit}")

for j in range(4):
  for u in range(4):
     print(f" {j}, {u} ")

#perfect nested loop
Twice_song = 'oh ahh ','tt','fancy','feel spacile '
for twice in Twice_song:
    twice+= " : Wow , I like is song . i'm going to lisent this song again"
    for xj in ('sex'):
        print(f"{twice},{xj}")

num = 3 , 4, 654 , 3, 55, 3
for n in num:
    print(n * "x")

num = 3 , 4, 654 , 3, 55, 3
for number in num:
    output = ''
    for count in range(number):
        output+='x'
    print(output)