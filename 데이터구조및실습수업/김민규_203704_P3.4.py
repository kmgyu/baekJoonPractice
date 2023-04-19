class Polynomial :
    def __init__( self ):
        self.coef= dict() #dict 써서 10000~~ 일때 계산을 더 빠르게? 한다? 시간복잡도도 빠를수있다?

    def degree(self) :
        return max(self.coef.keys())

    def display(self, msg="f(x) = "):
        print("  ", msg, end='')
        deg = self.degree()

        for n in range(self.degree()+1, 0, -1) : #n : key, v : value
            if n in self.coef :
                print("%5.1f x^%d + " % (self.coef[n], n), end='')
        if self.coef[0]: #0나오면 스킵
            print("%4.1f"%self.coef[0]) #마지막은 상수출력
        
        #전부 출력. 일정한 자리 차지를 하게 5.1f로 포맷팅해준듯.
        #dict를 써서 for~ in coef쓰면 될 듯 하다. -> 해보려고 했는데 +출력이 성가시다... 이방법이 제일 편한듯?

    def add(self, b):
        #temp 식 생성
        p = Polynomial()
        #둘중 더 큰걸 기준으로 제어변수 범위를 설정한다.
        #if문 길게 쓸 필요 없어졌다. 굳굳~
        p.coef = dict(self.coef)
        for i in range(max(self.degree(), b.degree())+1):
            if i in p.coef and i in b.coef:
                p.coef[i] += b.coef[i]
            elif i in b.coef: #b에만 있을 때, temp에만 있을 경우에는 생략한다.
                p.coef[i] = b.coef[i]
        return p

    #x 대입시 식을 계산해서 반환.
    def eval(self, x):
        result = 0.0
        for i in range(self.degree()+1) :
            if i in self.coef:
                result += self.coef[i] * (x**i)
        return result

    ########### 뺄셈, 곱셈 함수##############
    def substract(self, b): #빼기
        p = Polynomial()
        p.coef = dict(self.coef)
        for i in range(max(self.degree(), b.degree())+1): 
            if i in p.coef and i in b.coef:
                p.coef[i] -= b.coef[i]
            elif i in b.coef: #b에만 있을 때, temp에만 있을 경우에는 생략함.
                p.coef[i] = -b.coef[i] #더하기와 다르게 -를 대입.
        #temp에 b지정, 본인을 뺌.
        return p
    
    def multiply(self, b): #곱셈
        #temp식 생성, temp에 다 짬때린다.
        p = Polynomial()
        for i in self.coef.keys():
            for j in b.coef.keys():
                if i+j in p.coef.keys():
                    p.coef[i+j] += self.coef[i] * b.coef[j]
                else:
                    p.coef[i+j] = self.coef[i] * b.coef[j]
        return p

def read_poly():
    p = Polynomial()
    deg = int(input("다항식의 최고 차수를 입력하시오: "))
    for n in range(deg, -1, -1) : #-1같은건 예제코드에서도 안될것같아서 그냥 이렇게만듬.
        coef = float(input(  "\tx^%d의 계수 : " % (n)))
        if coef: # 0이면 생략. 공간복잡도를 아낀다.
            p.coef[n] = coef
    return p


# 테스트 객체
a = read_poly()
b = read_poly()
c = a.add(b)
a.display("A(x) = ")
b.display("B(x) = ")
c.display("C(x) = ")
print(" C(2) = ", c.eval(2))

# 테스트 객체+
d = a.multiply(b)
d.display()
print(d.eval(2))
e = a.substract(b)
e.display()