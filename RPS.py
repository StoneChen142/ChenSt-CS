#Import Libraries
from random import randint

round = 1
c_s = 0 ### SRC - Please use meaningful variable name such as: computer_score(Fixed)
p_s = 0

while round < 7:
    pc = int(input("Round ("+str(round)+"/6) Rock(1),Paper(2),Scissors(3): "))
    cc = int(randint(1,3))      ### SRC - Againg what is the point of this? I think there may be a misunderstanding here.(Fixed)
    round+=1

    if pc==1 and cc==2:
        c_s+=1
        print("Computer obtained a point! Computer used Paper  "+"Player: "+str(p_s)+"  Computer: "+str(c_s))
    elif pc==2 and cc==3:
        c_s+=1
        print("Computer obtained a point! Computer used Scissors  "+"Player: "+str(p_s)+"  Computer: "+str(c_s))
    elif pc==3 and cc==1:
        c_s+=1
        print("Computer obtained a point! Computer used Rock  "+"Player: "+str(p_s)+"  Computer: "+str(c_s))
    elif pc==1 and cc==3:
        p_s+=1
        print("You obtained a point! Computer used Scissors  "+"Player: "+str(p_s)+"  Computer: "+str(c_s))
    elif pc==2 and cc==1:
        p_s+=1
        print("You obtained a point! Computer used Rock  "+"Player: "+str(p_s)+"  Computer: "+str(c_s))
    elif pc==3 and cc==2:
        p_s+=1
        print("You obtained a point! Computer used Paper  "+"Player: "+str(p_s)+"  Computer: "+str(c_s))
    else:
        print("Draw!  "+"Player: "+str(p_s)+"  Computer: "+str(c_s))   ### SRC - Could you make these last three if statements just one?(Fixed)
#endwhile
### SRC - Please use end while comment.(Fixed)
if p_s>c_s:
    print("You Win!")
if c_s>p_s:
    print("You Lose!")
if p_s==c_s:
    print("Draw! Good Game!")
        




