def sqrt2(x, debug=False):
    from numpy import nan
    if x==0:
        return 0
    elif x<0:
        return nan
    s= 1.5	
    kmax= 15
    tolerance= 1.0e-14;
    for k in range(kmax):	
        if debug:
            print(f"At iteration {k}, the value of s is: {s:20.15f}")
        s1= s
        s=0.5*( s+x/s)
        delta= abs(s-s1)
        if debug:
            print(f"Error at iteration {k} is {delta}")
        if(delta/abs(x) < tolerance):
            break 
    if debug:
        print(f"The final value of s is {s}")
    return s