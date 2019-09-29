x=0  ### SRC - is x needed? Could you not just use units for the same job?
units=int(input("1: Imperial, 2: Metric"))

if units == 1:
    h = int(input("Enter Height in inches: "))
    d = int(input("Enter Depth in inches: "))
    w = int(input("Enter Width in inches: "))
    x=1
elif units == 2:
    h = int(input("Enter Height in meters: "))
    d = int(input("Enter Depth in meters: "))
    w = int(input("Enter Width in meters: "))
    x=2
else:
    print("invalid") 
    
#endif

### SRC - What happens here is units is invalid?
if x == 1:
    print("Paint Needed:",2*w*d+2*w*h+2*h*d,"inch^2")
else:
    print("Paint Needed:",2*w*d+2*w*h+2*h*d,"meter^2")
    
