valid=False
h = int(input("Enter Height in meters: "))
d = int(input("Enter Depth in meters: "))
w = int(input("Enter Width in meters: "))

### SRC - What happens here is units is invalid?
### SRC - is x needed? Could you not just use units for the same job?
while valid==False:
    units=int(input("(1: Imperial, 2: Metric): "))
    if units == 1:
        print("Paint Needed:",round((2*w*d+2*w*h+2*h*d)/1550,4),"inch^2")
        valid=True
    elif units == 2:
        print("Paint Needed:",2*w*d+2*w*h+2*h*d,"meter^2")
        valid=True
    else:
        print("Please choose between 1 and 2")
#endwhile
    
