print('WELCOME')
amt = 0
sr = {1: 20, 2: 50, 3: 15, 4: 30}
dr = {1: 50, 2: 30, 3: 50, 4: 55}
cr = {1: 20, 2: 10, 3: 30, 4:25}
pr = {1:10,2:50,3:150,4:3}
nr = {1:60,2:50,3:65,4:20}

a = input('Hi,sir what\'s your name ')
print('Hi Mr.', a)

while True:
    print('These are the products available')
    print('1-Soap\n2-Detergent\n3-Chocolate\n4-Pen\n5-Notebook')
    
    b = int(input('Enter your choice in (1/2/3/4/5) '))

    if b ==1:
        while True:
            print('You have selected soap')
            print('These are brands available-')
            print('1-Lux   Rs.2o/-\n2-Dettol   Rs.15/-\n3-Dove   Rs.50/-\n4-Lifebuoy   Rs.30/-')
            c = int(input('Enter brand code in 1/2/3/4 '))
            if c in (1, 2, 3, 4):
                qty = int(input('Enter quantity '))
            else:
                print('Invalid choice')
            amt = amt + sr[c] * qty
        ch=input("do you want to buy soap of any other brand y/n ")
        if ch=='n':
            break


    if b == 2:
        while True:
            print('You have selected detergent')
            print('These are brands available-')
            print('1-Surf Excel   Rs.50/-\n2-Ghadi   Rs.30/-\n3-Wheel   Rs.50/-\n4-Vanish   Rs.55/-')
            c = int(input('Enter brand code in 1/2/3/4 '))
            if c in (1, 2, 3, 4):
                qty = int(input('Enter quantity '))
                amt = amt + dr[c] * qty
            else:
                print('Invalid choice')
        ch=input('Do you want to buy dteregent of any other brand y/n ')
        if ch=='n':
            break
    if b == 3:
        while True:
            print('You have selected Chocolate')
            print('These are brands available-')
            print('1-Dairy Milk  Rs.20/-\n2-5 Star   Rs.10/-\n3-Fuse   Rs.30/-\n4-Kit Kat   Rs.25/-')
            c = int(input('Enter brand code in 1/2/3/4 '))
            if c in (1, 2, 3, 4):
                qty = int(input('Enter quantity '))
                amt = amt + dr[c] * qty
            else:
                print('Invalid choice')
        ch=input('Do you want to buy chocolate of any other brand y/n ')
        if ch=='n':
            break

    if b == 4:
        while True:
            print('You have selected Pen')
            print('These are brands available-')
            print('1-Octane  Rs.10/-\n2-Trimax   Rs.50/-\n3-Parker   Rs.150/-\n4-Flair   Rs.3/-')
            c = int(input('Enter brand code in 1/2/3/4 '))
            if c in (1, 2, 3, 4):
                qty = int(input('Enter quantity '))
                amt = amt + dr[c] * qty
            else:
                print('Invalid choice')
        ch=input('Do you want to buy pen of any other brand y/n ')
        if ch=='n':
            break

    if b == 5:
        while True:
            print('You have selected Notebook')
            print('These are brands available-')
            print('1-Classmate  Rs.60/-\n2-Extramarks   Rs.50/-\n3-Rajdhani   Rs.65/-\n4-Vijeta   Rs.20/-')
            c = int(input('Enter brand code in 1/2/3/4 '))
            if c in (1, 2, 3, 4):
                qty = int(input('Enter quantity '))
                amt = amt + dr[c] * qty
            else:
                print('Invalid choice')
        ch=input('Do you want to buy notebook of any other brand y/n ')
        if ch=='n':
            break
    if b not in (1, 2, 3, 4, 5):
        print('Invalid choice')
    ch=input('Do you want to continue shopping y/n ')
    if ch=='n':
        break

print('Total amount=', amt)
print('Thank You for shopping with us ...Have a nice day!')