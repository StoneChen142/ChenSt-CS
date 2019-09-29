#Import Libraries
from random import randint

round = 1
round = int(round) # SRC - What is the purpose of this line?
y = 0 ### SRC - Please use meaningful variable name such as: computer_score
x = 0

while round < 7:
    pc = int(input("Round ("+str(round)+"/6) Rock(1),Paper(2),Scissors(3): "))
    cc = int(randint(1,3))
    x= int(x)  ### SRC - Againg what is the point of this? I think there may be a misunderstanding here.
    y = int(y)
    round+=1

    if pc==1 and cc==2:
        y+=1
        print("Computer obtained a point! Computer used Paper  "+"Player: "+str(x)+"  Computer: "+str(y))
    elif pc==2 and cc==3:
        y+=1
        print("Computer obtained a point! Computer used Scissors  "+"Player: "+str(x)+"  Computer: "+str(y))
    elif pc==3 and cc==1:
        y+=1
        print("Computer obtained a point! Computer used Rock  "+"Player: "+str(x)+"  Computer: "+str(y))
    elif pc==1 and cc==3:
        x+=1
        print("You obtained a point! Computer used Scissors  "+"Player: "+str(x)+"  Computer: "+str(y))
    elif pc==2 and cc==1:
        x+=1
        print("You obtained a point! Computer used Rock  "+"Player: "+str(x)+"  Computer: "+str(y))
    elif pc==3 and cc==2:
        x+=1
        print("You obtained a point! Computer used Paper  "+"Player: "+str(x)+"  Computer: "+str(y))
    elif pc==1 and cc==1:
        print("Draw!  "+"Player: "+str(x)+"  Computer: "+str(y))   ### SRC - Could you make these last three if statements just one?
    elif pc==2 and cc==2:
        print("Draw!  "+"Player: "+str(x)+"  Computer: "+str(y))
    elif pc==3 and cc==3:
        print("Draw!  "+"Player: "+str(x)+"  Computer: "+str(y))

### SRC - Please use end while comment.

if x>y:
    print("You Win!")
if y>x:
    print("You Lose!")
if y==x:
    print("Draw! Good Game!")
        




