# 클래스로 구현.
class Polynomial :
    def __init__( self ):
        self.coef= []

    def degree(self) :
        return len(self.coef) - 1

    def display(self, msg="f(x) = "):
        print("  ", msg, end='')
        deg = self.degree()

        for n in range(deg, 0, -1) :
            print("%5.1f x^%d + " % (self.coef[n], n), end='')
        print("%4.1f"%self.coef[0])

    def add(self, b):
        p = Polynomial()
        if self.degree() > b.degree() :
            p.coef = list(self.coef)
            for i in range(b.degree()+1) :
                p.coef[i] += b.coef[i]
        else :
            p.coef = list(b.coef)
            for i in range(self.degree()+1) :
                p.coef[i] += self.coef[i]
        return p

    def eval(self, x):
        result = 0.0
        for i in range(self.degree()+1) :
            result += self.coef[i] * (x**i)
        return result

    def substract(self):
        pass
    
    def multiply(self):
        pass
    
    # 뺄셈, 곱셈 관련 함수 추가할 것

def read_poly():
    p = Polynomial()
    deg = int(input("다항식의 최고 차수를 입력하시오: "))
    for n in range(deg+1) :
        coef = float(input(  "\tx^%d의 계수 : " % (deg-n)))
        p.coef.append(coef)
    p.coef.reverse()
    return p

# 테스트 코드.... 뺄셈, 곱셈 추가할 것
a = read_poly()
b = read_poly()
c = a.add(b)
a.display("A(x) = ")
b.display("B(x) = ")
c.display("C(x) = ")
print(" C(2) = ", c.eval(2))
