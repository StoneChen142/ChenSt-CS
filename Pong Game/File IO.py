def scoreboard(score,name):
    f = open("Score_Board.txt","w+")
    #Reading data
    name = str(name)
    score = str(score)
    score_length=len(score)
    lines = f.readlines()
    maximum = int(len(lines)) - 1
    data = ""
    #Formatting the score
    if score_length < 5:
        while score_length != 5:
            score = "0"+score
            score_length += 1
    addLine = " "+score+"   "+name
    #Evaluating the score
    big = False
    rank = 0
    while rank < maximum:
        line=str(lines[rank])
        for j in range(2,5):
            if int(score[j-1]) > int(line[j]):
                big = True
            #endif
        #endfor
        if big == False:
            data = data + line
        else:
            data = data + str(rank+1) + " " + str(score)+"   "+str(name)+"\n"
            big = False
        rank += 1
    #endwhile
    f.write(data)  
    f.close()
#endfunction

n = "Arthur"
scoreboard(1000,n)
