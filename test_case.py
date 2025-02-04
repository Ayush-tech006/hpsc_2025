def test_1():
    from numpy import sqrt
    from mysqrt import sqrt2
    small= 1.0e-14

    xvalues= [0,2,10,100,0.0001,1e5]
    for x in xvalues:
        s= sqrt2(x)
        s_numpy= sqrt(x)
        print(f"fro x= {x}, s={s} and s_numpy= {s_numpy}")
        assert(s-s_numpy)<small,f"square root disagrees with numpy square root for x={x}"

# In terminal: python3 test_case.py
# In general we use pytest to run tests rather than using "python3 test_case.py"

def test_2():
    from numpy import sqrt
    from mysqrt import sqrt2
    small= 1.0e-14

    xvalues= [3,6,"5"]
    for x in xvalues:
        s= sqrt2(x)
        s_numpy= sqrt(x)
        print(f"fro x= {x}, s={s} and s_numpy= {s_numpy}")
        assert(s-s_numpy)<small,f"square root disagrees with numpy square root for x={x}"