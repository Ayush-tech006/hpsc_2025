def sqrt2(x):
    s= 1.5	
    x=2.0
    kmax= 15
    tolerance= 1.0e-14;
    for k in range(kmax):	
        print(f"At iteration {k}, the value of s is: {s}")
        s1= s
        s=0.5*( s+x/s)
        delta= abs(s-s1)
        print(f"Error at iteration {k} is {delta}")
        if(abs(delta)/s < tolerance):
            break 
        print(f"The final value of s is {s}")
    from math import sqrt
    print(f"The machine epsilon is: ", sqrt(2)-s)
	
