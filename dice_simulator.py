import random
#to write name
name=input('Write all the participant\'s name with space between them.\n').split()
if name==[]:
    name=['Your']
l=len(name)
print('Welcome to this game.\n')
cl=0

#type of dice
modi=['Normal','Custommize']
six=[]
sixx=0
while True:
#to select mode
    try:
        mod = int(input('WHat type of dice do you want?\n1. Normal\n2. Customize\ninput = '))
        if mod not in range(1,3):
            print('Alert : Number is out of range.\n')
            continue
        print('You chose {} type of dice.'.format(modi[mod-1]))
    except:
        print('Alert : Give proper input in digit as given in option.\n')
        continue

    index=0
    temp=name[0]
    score=[]
    while True:
        if index==len(score):
            score.append([])
        print('\n'+'==>'+name[index]+" turn <==")
        print('\nWrite number according to given option.')
        try:
            selection = int(input('1. To throw the dice.\n2. To close the game.\nYour selection = '))
        except:
            print('Alert : Give proper input in digit as given in option.')
            continue

#to start game
        if selection==1:
#mode normal
            if mod==1:
                num=random.randint(1,6)
                print('\n')
                print('====================================')
                print('Result = ',num)
                print('====================================')

#mode Customize
            else:
                while True:
                    try:
                        dom_num = int(input('\nNear which number you want result : '))
                        if dom_num not in range(1,8):
                            print('Alert : Please provide number between 1 to 7.')
                            continue
                        else:
                            break
                    except:
                        print('Alert : Please give input in number ranging from 1 to 7.')
                        continue

                while True:
                    print('\nChoose number from below options.')
                    try:
                        inp=int(input('1.Throw  2. Terminate\nYour selection = '))
                        break
                    except:
                        print('Alert : Choose properly as given option\n')
                        continue
                if inp==1:
                    num=random.triangular(1,7,dom_num)
                    if num>6:
                        num=6
                    print('\n')
                    print('====================================')
                    print('Result = ',int(num))
                    print('====================================')
                elif inp==2:
                    cl=1
                    break
                else:
                    print('Alert : Choose properly as given option\n')
                    continue
                if cl==1:
                    break

#for repetition after 6
            if num==6:
                print('* Congratulations *\nYou are getting second chance.')
                sixx=1
                six.append(num)
                continue
            else:
                if sixx==1:
                    six.append(num)
                    score[index].append(six)
                    six=[]
                    sixx=0
                else:
                    score[index].append(int(num))

            if index<len(name)-1:
                index += 1
            else:
                index=0
            continue

#to close game
        elif selection==2:
            score[index].append('You terminated this game')
            break

        else:
            print('Alert : Give proper input in digit as given in option.')
            continue

#to print score card
    print('\n')
    print('*SCORE CARD*')
    if len(score)>0:
        for k in range(len(name)):
            if k<len(score):
                print('{}\'s score is {}'.format(name[k],score[k]))
            else:
                print('{}\'s score is "NILL"'.format(name[k]))

    print('\n\nGame is done.')
    print('Thank you.\n')
    print('Do you want to reset game with same player?\n1. Yes\n2. No ')

    sel=input('selection = ')
    if sel=='1' or str(sel).lower()=='yes':
        print('\n')
        continue
    else:
        break
