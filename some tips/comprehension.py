#list comprehension
def even(list):
    n = len(list)
    even_num = [] #len(list) object가 iterable하지 않다는데, 원인을 모르겠음. parameter가 포인팅한 객체에 무슨 문제가 있는건가? 그래서 이렇게 만듬.
    for i in range(0, n):
        if list[i] % 2 == 0:
            even_num.append(list[i]) #division operator(나누기 연산자) 사용시 참고, /는 float, //는 integer, %는 나머지 연산. ㅇㅋ?
    return even_num
#사용하지 않았을 때의 함수

def even_comp(ran):
    even_num = [i for i in range(2, ran) if i % 2 == 0] #int iterable 문제를 해결하지 못해서 list를 list comprehension에 써먹는건 하지 못했다...
    #앞에 있는 i는 입력될 값이고, 뒤의 for부터는 반복문이다.
    return even_num

#dictionary comprehension
def dict_comp(list1, list2):
    comp = {k: v*2 for k, v in zip(list1, list2) if v > 100} #zip으로 묶어준 후 for문에 쓰면 된다. value 출력과정에서 변경할 수도 있고, 조건문도 list처럼 붙일 수 있다.
    return comp



list1 = [1,2,3,4,5,6,7,8,9,10]
even_list1 = even(list1)
even_list2 = even_comp(len(list1))
print(even_list1)
print(even_list2)

gun = ['gungeon', 'guntor', 'voltor']
value = [10000, 500000, 4000]
print(dict_comp(gun, value))