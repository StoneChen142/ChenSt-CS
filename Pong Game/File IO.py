def scoreboard(score,name):
<<<<<<< HEAD
    f = open("Score_Board.txt","r+")
=======
    f = open("Score_Board.txt","w+") ### SRC - This will overwrite your existing file
>>>>>>> 1b4b8cc06359edee8c0f5717312fb2da49913fb2
    #Reading data
    name = str(name)
    score = str(score)
    score_length=len(score)
<<<<<<< HEAD
    lines = f.readlines()
    maximum = 4
=======
    lines = f.readlines()  ### SRC - There will be no data!
    maximum = int(len(lines)) - 1
>>>>>>> 1b4b8cc06359edee8c0f5717312fb2da49913fb2
    data = ""
    f.close()
    #Formatting the score
    ### SRC - This works
    if score_length < 5:
        while score_length != 5:
            score = "0"+score
            score_length += 1
    addLine = " "+score+"   "+name+"\n"
    print(addLine)
    #Evaluating the score
    rank = 0
<<<<<<< HEAD
    num = 0
    added = False
    while rank < maximum or added == False:
        big = False
        same = False
        TF = ""
=======
    ### SRC - This doesn't work because maximum is always -1
    while rank < maximum:
>>>>>>> 1b4b8cc06359edee8c0f5717312fb2da49913fb2
        line=str(lines[rank])
        print(line[1:])
        for j in range(2,6):
            if int(score[j-2]) > int(line[j]):
                TF = TF + "T"
            elif int(score[j-2]) == int(line[j]):
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
            print(data)
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
            print(data)
        else:
            data = data + str(num+1) + line[1:]
            print(data)
            rank += 1
            num += 1
        #endif
    #endwhile
    #f = open("Score_Board.txt","w+")
    #f.write(data)  
    #f.close()
#endfunction

n = "Levi"
scoreboard(6000,n)
