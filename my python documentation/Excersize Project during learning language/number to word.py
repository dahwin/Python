phone_number = input('type your phone number')

number = {
    '1' : 'one',
    '2' : 'tow',
    '3' : 'three',
    '4' : 'four' ,
    '5' : 'five' ,
    '6' : 'six' ,
    '7' : 'seven',
    '8' : 'eight' ,
    '9' : 'nine' ,
    '10' : 'ten' ,
}
output = ''
for c in phone_number:
     output += number.get(c  ,  '!' )  +  " "

print(output)
