def mergeSort(alist):
    if len(alist) > 1:
        mid = int(len(alist)/2)  	# performs integer division
        lefthalf = alist[:mid]    	# left half of alist put into lefthalf
        righthalf = alist[mid:]   	# right half of alist put into righthalf
        mergeSort(lefthalf)
        mergeSort(righthalf)

        i = 0
        j = 0
        k = 0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k] = lefthalf[i]
                i = i + 1
            else:
                alist[k] = righthalf[j]
                j = j + 1
            #endif
            k = k + 1
        #endwhile
#check if the left half still has elements not merged 
#if so, add them to alist 
        while i < len(lefthalf):
            alist[k] = lefthalf[i]
            i = i + 1
            k = k + 1
        #endwhile
#check if the right half still has elements not merged 
#if so, add them to alist 
        while j < len(righthalf):
            alist[k] = righthalf[j]
            j = j + 1
            k = k + 1
        #endwhile
        print("Merged sublist ",alist)
    #endif        
#endprocedure

alist = [1, 7, 9, 2, 10, 6]
mergeSort(alist)
