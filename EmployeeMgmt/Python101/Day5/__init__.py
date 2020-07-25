#
import shape as sp
import ComplexNumber as cn

def main():
    print(list(set([11,22,33,44,11,22])))
    defaultshape = sp.shape()
    if(isinstance(defaultshape, sp.shape)):
        print ('default area is {}'.format(defaultshape.area()))
    
    squareshape = sp.square(5)
    if(isinstance(squareshape,sp.shape)):
        print ('Square area is {}'.format(squareshape.area()))
    
    c1 = cn.ComplexNumber(4,2)
    c2 = cn.ComplexNumber(5,3)
    
    
    c3 = c1.add(c2)
    #print("Complex Number {}+i{}".format(c3.real, c3.complex))
    print('Sum is {}'.format(c3))
x = main()
print(x)
    
