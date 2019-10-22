def scoreboard(score,name):
    f = open("Score_Board.txt","w+")
    score = str(score)
    name = str(name)
    s_length=len(score)
    data = f.read()
    data = ""
    #Formatting the score
    if s_length < 5:
        while s_length != 5:
            score = "0"+score
            s_length +=1
    newLine = " "+score+"   "+name
    lines = f.readlines()
    #Evaluating the score
    big=False
    while i < 4:
        line=str(lines[i])
        for j in range(2,5):
            if score[i-2]>line[i]:
                big = True
            #endif
        #endfor
        if big == False:
            data = data + line+"\n"
        else:
            data = data + str(i+1) + " " + str(score)+"   "+str(name)+"\n"
    #endwhile
    f.write(data)  
    f.close()
#endfunction


scoreboard(1000,Arthur)
