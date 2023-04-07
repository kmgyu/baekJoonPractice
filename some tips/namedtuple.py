from collections import namedtuple

class Book:
    def __init__(self, title, price):
        self.title = title
        self.price = price
#클래스는 label을 만들수 있다! 튜플은 그런거 없음 힝헹힝홍 아힝헹

mybook1 = Book("모비딕", 27000)
print(mybook1.title) #label로 접근하기.

mybook2 = ("태양의 탑 11권", 17000) #일반적인 튜플은 label이 없어서 index로 접근해야 한다.
print(mybook2[0]) #index로 접근하기

book = namedtuple('book', ['title', 'price']) #book은 class type이다. 참고할 것. Book은 위의 클래스고 이건 namedtuple book임 대소문자 주의.
mybook3 = book("만멘미", 1500) #이렇게 생성된 튜플은 immutable한 book 객체다. index를 통한 접근도 가능하니 참고.
print(mybook3.title)
print(mybook3[1])
