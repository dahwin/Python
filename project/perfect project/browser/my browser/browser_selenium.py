from selenium import webdriver
y = webdriver.Chrome()
x = dir(y)
print('\n'.join(x))
print(len(x))