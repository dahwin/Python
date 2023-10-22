import random , string
total = string.ascii_letters + string.digits + string.punctuation
length = 35
password= "".join(random.sample(total,length))
print(password)
