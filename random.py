import random

while True:
    numbers=[]
    kn = input("kaç sayı içinden : ")
    for i in range(int(kn)):
        numbers.append(i)
    print(random.choice(numbers))
