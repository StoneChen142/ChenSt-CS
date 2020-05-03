def bubbleSort(alist):
    unsorted = True
    i=0
    swap=0
    length=len(alist)
    while i < len(alist)-1 and unsorted:
        unsorted = False
        for j in range(len(alist)-i-1):
            if alist[j] > alist[j+1]:
                temp = alist[j]
                alist[j] = alist[j+1]
                alist[j+1] = temp
                unsorted = True
                swap+=1
            #endif
        #endfor
        i+=1
    #endwhile
    print("Bubbled sublist ",alist)
#endprocedure

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

alist = [4, 12, 18, 5, 3, 1, 10, 11, 2, 14]
bubbleSort(alist)
mergeSort(alist)
