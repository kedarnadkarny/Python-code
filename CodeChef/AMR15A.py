no_of_soldiers = 0

no_of_weapons = list()
even = 0
odd = 0
no_of_soldiers = int(input())
no_of_weapons = list(map(int, input().split()))
pos = 0

while no_of_soldiers > 0:
    no_of_soldiers -= 1

    if no_of_weapons[pos]%2==0:
        even += 1
    else:
        odd += 1
    pos +=1

if odd>even:
    print('NOT READY')
elif even>odd:
    print('READY FOR BATTLE')
elif even==odd:
    print('NOT READY')