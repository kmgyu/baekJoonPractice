#zip은 두개의 리스트를 하나로 묶을 때 사용한다.
#zip으로 묶으면 하나의 "zip" 객체가 생성되며 리스트에 튜플이 있는 형태로 출력된다.
name = ["kim", "seo", "yang", "choi"]
age = [38, 27, 59, 31]
z = zip(name, age)
print(z)

for n, a in zip(name,age):
    print(f"{n} : {a}")
#이런식으로 사용 가능하다.
#단, zip 객체는 callable하지 않으니 z(name, age)를 사용한다면 syntax error가 뜬다. 주의할 것! 중요!!!!!

#딕셔너리 생성 방법 3가지
dic1 = {"만멘미":500, "움냠냠":1000} #일반적인 방법
dic2 = dict(만멘미=500, 움냠냠=1000) #문자열이 키일시 이렇게 쓸수있다
dic3 = dict([("만멘미", 500),("움냠냠",1000)]) #키와 값 튜플로 저장하고 리스트에 입력해 딕셔너리 만들기

#zip으로 딕셔너리에 추가하기
name = ["고봉밥", "백숙", "백반"]
price = [1000, 35000, 17000]
dic = dict(zip(name, price)) #주의 하자. {} 쓰면 주소가 입력됨. 객체니까!!!!!!!! 주소가 입력된다!!! 알간???
print(dic)

data = {}

#setdefault를 이용해 key 추가하면서 초깃값 설정하기.
ret = data.setdefault('a', 0)    # key로 'a'를 추가하고 value 0을 설정함, setdefault는 현재 value 값을 리턴
print(ret, data)

ret = data.setdefault('a', 1)   # 이미 key가 있는 경우 setdefault시 현재 value 값을 리턴
print(ret, data) #'a' 있어? 없으면 1, 아님 말고~

#딕셔너리 원소갯수 세기
data = ["BTC", "ETH", "ETH", "ETH", "XRP"]
dit = {}

for i in set(data):
    count = data.count(i) #집합형태로 변환하고 count()함수 사용해서 원소 반복횟수 세면 됨.
    print(i, count) # 딕셔너리로 값 추가 가능하다.
    dit.setdefault(i, count) #귀찮아서 이거씀.. ㅎ... 그냥 추가도 가능함.
    print(dit)

