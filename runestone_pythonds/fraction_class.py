# -*- coding: utf-8 -*-

def gcd(m,n):
    while m%n != 0:
        oldm = m
        oldn = n
        m = oldn
        n = oldm%oldn
    return n


class Fraction:

    def __init__(self,top,bottom):
        if (isinstance(top, int) and isinstance(bottom, int)):
            common = gcd(top,bottom)
            self.num = top//common
            self.den = bottom//common
        else:
            raise RuntimeError("Both numbers must be integers!")

    def __repr__(self):
        return "Fraction(%r,%r)" % (self.num,self.den)

    def __str__(self):
        return str(self.num)+"/"+str(self.den)

    def __add__(self,other):
        if not isinstance(other, Fraction):
            other = Fraction(other, 1)
        newnum = self.num*other.den + self.den*other.num
        newden = self.den * other.den
        return Fraction(newnum,newden)

    def __radd__(self, other):
        return self.__add__(other)

    def __iadd__(self,other):
        if not isinstance(other, Fraction):
            other = Fraction(other, 1)
        self.num = self.num*other.den + self.den*other.num
        self.den = self.den * other.den
        return self

    def __sub__(self,other):
        newnum = self.num*other.den - self.den*other.num
        newden = self.den * other.den
        return Fraction(newnum,newden)

    def __mul__(self,other):
        newnum = self.num * other.num
        newden = self.den * other.den
        common = gcd(newnum,newden)
        return Fraction(newnum//common,newden//common)

    def __truediv__(self,other):
        newnum = self.num * other.den
        newden = self.den * other.num
        common = gcd(newnum,newden)
        return Fraction(newnum//common,newden//common)

    def __eq__(self, other):
        firstnum = self.num * other.den
        secondnum = other.num * self.den
        return firstnum == secondnum

    def __ne__(self, other):
        firstnum = self.num * other.den
        secondnum = other.num * self.den
        return firstnum != secondnum

    def __lt__(self, other):
        firstnum = self.num * other.den
        secondnum = other.num * self.den
        return firstnum < secondnum

    def __le__(self, other):
        firstnum = self.num * other.den
        secondnum = other.num * self.den
        return firstnum <= secondnum

    def __gt__(self, other):
        firstnum = self.num * other.den
        secondnum = other.num * self.den
        return firstnum > secondnum

    def __ge__(self, other):
        firstnum = self.num * other.den
        secondnum = other.num * self.den
        return firstnum >= secondnum

f1 = Fraction(1,3)
f2 = Fraction(1,2)
f3 = Fraction(2,-4)
print(f1)
print(f3, f3.num, f3.den)
#print(f1 + 3)
#print(3 + f1)

#print(f1,"+",f2,"=",f1+f2)
print(f1,"-",f2,"=",f1-f2)
print(f1,"*",f2,"=",f1*f2)
print(f1,"/",f2,"=",f1/f2)

print(f1,"equals",f2,"=",f1==f2)
print(f1,"not equal",f2,"=",f1!=f2)
print(f2,"less or equal than",f3,"=",f2<=f3)
print(f2,"greater or equal than",f3,"=",f2>=f3)

f1+=f2
print(f1)

print(f3.__repr__())
print(eval(f3.__repr__()))
