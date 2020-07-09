def f(x):
    return x**2+2               #return f
def deriv(x):
    h =.1
    DerComplex1H = 0                        #get deriv by making h smaller and smaller
    H1DOD = 0
    while h >= 0.000001:
        h = h / 10
        DerComplex1H = (x+h)**2+2
        H1DOD = (DerComplex1H -f(x) ) / h
    return(H1DOD)
def newton_step(x):
    return (x-(f(x)/deriv(x)))                   #plug into newton step eqaution
def newton(x):
    guesses = []
    h = newton_step(x)
    guesses.append(h)
    h = newton_step(h)                                          #prellimnary newton guesses to get a diffrence possible
    guesses.append(h)
    while (abs(guesses[len(guesses)-1]-guesses[len(guesses)-2])>.000006) :                      #loop till diffrence small enough
      h = newton_step(h)
      guesses.append(h)
    return (guesses)
ans = newton(float(input("Enter a guess for the root")))
print('the set of root approximations is ', ans, sep = '')                          #print and run
#no real roots x^2+1 results in infinite loop
#newton step quicker