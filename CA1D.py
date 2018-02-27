import math
import matplotlib.pyplot as plt
import matplotlib.patches as patches

from operator import ne


def rules(a, b, c):
    if a == 1 and b == 1 and c == 1:
        return ruleset[0]
    elif a == 1 and b == 1 and c == 0:
        return ruleset[1]
    elif a == 1 and b == 0 and c == 1:
        return ruleset[2]
    elif a == 1 and b == 0 and c == 0:
        return ruleset[3]
    elif a == 0 and b == 1 and c == 1:
        return ruleset[4]
    elif a == 0 and b == 1 and c == 0:
        return ruleset[5]
    elif a == 0 and b == 0 and c == 1:
        return ruleset[6]
    elif a == 0 and b == 0 and c == 0:
        return ruleset[7]
    else:
        return 0


WIDTH = 100
ruleset = [0,1,0,1,1,0,1,0]
cells = [0 for x in range(0, WIDTH)]
white = (255,255,255)
generations = 50

cells[math.floor(len(cells)/2)-1] = 1

#print (cells)

fig1 = plt.figure()
ax1 = fig1.add_subplot(111, aspect='equal')
ax1.set_ylim([0,generations])
ax1.set_xlim([0,WIDTH])

for gen in range(0,generations):

    nextgen = [0 for x in range(0, WIDTH)]
    for cel in range(0, WIDTH):
        if cel-1 < 0:
            left = cells[WIDTH-1]
        else:
            left = cells[cel - 1]
        me = cells[cel]
        if cel+1 > WIDTH-1:
            right = cells[0]
        else:
            right = cells[cel + 1]
        nextgen[cel] = rules(left, me, right)

        if cells[cel] == 1 :
            ax1.add_patch(
                patches.Rectangle(
                    (cel, gen),  # (x,y)
                    1,  # width
                    1,  # height
                    color = 'black'
                )
            )
        else:
            ax1.add_patch(
                patches.Rectangle(
                    (cel, gen),  # (x,y)
                    1,  # width
                    1,  # height
                    color = 'white'
                )
            )


    cells = nextgen

    #print (nextgen)


#plt.axis('off')
plt.show()
#fig1.savefig('rect1.png', dpi=90, bbox_inches='tight')