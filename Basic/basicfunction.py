def hello():
    print('Hello, My name is wirot')

#hello()

def hellofriend(name):
    print(f'Hello, My name is {name}.')

#hellofriend('Ronaldo')

def checkNameAge(name, age):
    print(f'Hello, Your name is {name}')
    print(f'Your age is {age} year old')

#checkNameAge('Messi', 34)

#checkNameAge(age=45,name='Messi')

#checkNameAge('Messi')

def addNumber(x, y):
    return x + y

sum = addNumber(3,7)
#print(sum)

#Leap year
#หาร 4 ลงตัว หาร 100 ไม่ลงตัว
#หาร 400 ลงตัว
#year = int (input('ปี ค.ศ. : '))
#if year % 4 == 0 and year % 400 == 0 or year % 100 != 0 :
 #   print(f'ค.ศ. {year} เป็น Leap year')
#else:
#    print(f'ค.ศ. {year} ไม่เป็น Leap year')


color = ["red", "green", "blue"]
color.append('yellow')

for x in color:
  print(x)