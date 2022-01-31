import random

print('pandomaser')
print()

connect = True

while connect == True:
    a = input('Ot: ')
    print()
    b = input('Do: ')
    print()
    if b < a:
        print('ei tohi kirjuta numnrid vähem kui esimesel real! ')
        break

    finish = random.randint(int(a),int(b))

    print('vastus:', int(finish))
    print()

input()