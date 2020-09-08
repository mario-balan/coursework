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


    def __str__(self):
        return str(self.num)+"/"+str(self.den)

    def __add__(self,otherfraction):
        newnum = self.num*otherfraction.den + self.den*otherfraction.num
        newden = self.den * otherfraction.den
        return Fraction(newnum,newden)

    def __sub__(self,otherfraction):
        newnum = self.num*otherfraction.den - self.den*otherfraction.num
        newden = self.den * otherfraction.den
        return Fraction(newnum,newden)

    def __mul__(self,otherfraction):
        newnum = self.num * otherfraction.num
        newden = self.den * otherfraction.den
        common = gcd(newnum,newden)
        return Fraction(newnum//common,newden//common)

    def __truediv__(self,otherfraction):
        newnum = self.num * otherfraction.den
        newden = self.den * otherfraction.num
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

f1 = Fraction(1.1,3)
#f2 = Fraction(1,2)
#f3 = Fraction(2,4)
print(f1)

#print(f1,"+",f2,"=",f1+f2)
#print(f1,"-",f2,"=",f1-f2)
#print(f1,"*",f2,"=",f1*f2)
#print(f1,"/",f2,"=",f1/f2)

#print(f1,"equals",f2,"=",f1==f2)
#print(f1,"not equal",f2,"=",f1!=f2)
#print(f2,"less or equal than",f3,"=",f2<=f3)
#print(f2,"greater or equal than",f3,"=",f2>=f3)
