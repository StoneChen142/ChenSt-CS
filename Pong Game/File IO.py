#Score
def scoreboard(score,name):
    f = open("Score_Board.txt","r+")
    #Reading data
    name = str(name)
    score = str(score)
    score_length=len(score)
    lines = f.readlines()
    print(lines)
    maximum = 4
    data = ""
    f.close()
    #Formatting the score
    if score_length < 5:
        while score_length != 5:
            score = "0"+score
            score_length += 1
    addLine = ") "+score+"   "+name+"\n"
    #Evaluating the score
    rank = 0
    num = 0
    added = False
    while rank < maximum or added == False:
        big = False
        same = False
        TF = ""
        line=str(lines[rank])
        print(line)
        for j in range(3,7):
            if int(score[j-3]) > int(line[j]):
                TF = TF + "T"
            elif int(score[j-3]) == int(line[j]):
                TF = TF + "S"
            else:
                TF = TF + "F"
            #endif
        #endfor
        #Evaluating
        if added == False:
            if TF[1] == "T" or TF[:2] == "ST" or TF[:3] == "SST" or TF[:4] == "SSST":
                big = True
            elif TF == "SSSSS":
                same = True
            else:
                big = False
                same = False
            #endif
        #endif
            
        if same == True:
            data = data + str(num+1) + line[1:]
            rank += 1
            num += 1
        elif big == True and added == False:
            data = data + str(num+1) + addLine
            big = False
            rank += 1
            num += 1
            added = True
            same=False
            if rank < 4:
                data = data + str(num+1) + line[1:]
                num += 1
            #endif
        else:
            data = data + str(num+1) + line[1:]
            rank += 1
            num += 1
        #endif
    #endwhile
    f = open("Score_Board.txt","w+")
    f.write(data)  
    f.close()
#endfunction

n = "Levi"
scoreboard(500,n)
