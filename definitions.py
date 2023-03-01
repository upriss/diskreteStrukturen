def istPythonAussage (x):
    return type(x) is bool

def hasNeutrElem (setOrList,op,n_elem):
    return all (op(x,n_elem) == x and op(n_elem,x) == x for x in setOrList)

def isKompl (setOrList,op,n_elem,neg):
    return all (op(x,neg(x)) == n_elem and op(neg(x),x) == n_elem
           for x in setOrList)

def hasAbsorbElem (setOrList,op,n_elem):
    return all (op(x,n_elem) == n_elem and op(n_elem,x) == n_elem for x in setOrList)

def isKommut (setOrList,op):
    return all (op(x,y) == op(y,x) for x in setOrList for y in setOrList)

def isAssoc (setOrList,op):
    return all (op(x,op(y,z)) == op(op(y,x),z) 
           for x in setOrList for y in setOrList for z in setOrList)

def isDistrib (setOrList,op1,op2):
    return all (op1(x,op2(y,z)) == op2(op1(x,y),op1(x,z)) 
           for x in setOrList for y in setOrList for z in setOrList)

def isAbsorp (setOrList,op1,op2,neg):
    return all (op1(x,op2(x,y) == x) and op1(x,op2(neg(x),y) == op1(x,y)) 
           for x in setOrList for y in setOrList)

def isIdemp (setOrList,op):
    return all (op(x,x) == x for x in setOrList)

def hasDoubleNeg (setOrList,neg):
    return all (neg(neg(x)) == x for x in setOrList)

def isTransitiv (setOrList,op):
    return all ((op(a,b) and op(b,c)) -s>> op(a,c)
    for a in setOrList for b in setOrList for c in setOrList)
