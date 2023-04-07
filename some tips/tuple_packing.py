from random import *
from time import sleep

#튜플로 랜덤하게 리스트 배치해서 덱 짜기
magic = (["smite", 80, 40], ["ignite", 30, 20], ["orb shield", 0, 10], ["meteor rock", 150, 70], ["originium arts", 100, 45], ["subjective time dilation", 125, 67])
deck = []
mp = 500


def add_magic():
    for i in range(0, 3):
        temp_magic = []
        temp_magic += magic[i]
        temp_magic.append(True)
        deck.append(temp_magic)
        print(f"덱에 마법 추가, {temp_magic[0]}")

def magic_start():
    roof = True
    while roof:
        add_magic()
        for value in deck:
            print(f"받아라! {value[0]}")
            print(f"{value[1]}의 피해를 입혔다! {value[2]}의 마나 소모!")
            mp -= value[2]
        if mp <= 0:
            print(f"현재 마나는 {mp}, 마법을 사용할 수 없다.")
            roof = False
            pass
        else:
            print("덱에 있는 마법을 전부 소모했다. 재정렬할까?")
            switch = input("0을 입력시 종료합니다: ")
            if switch == "0":
                roof = False
            print(f"현재 마나는 {mp}")
            sleep(1)


# 최댓값과 최솟값 제외하여 출력하기
scores = (1, 2, 3, 4, 5)
high, *others, low = scores
print(scores)

#함수에 다수의 값 입력시 튜플로 패킹되어 출력됨
def foo():
    return 1, 2, 3, 4, 5
print(foo())

#함수에 다수의 값 입력시 튜플 이용가능

def pee(a, b, c, d, e):
    alisa = [a, b, c, d, e]
    for value in alisa:
        print(value)
def sum(a, b, c, d, e):
    return a+b+c+d+e #이런것도 굳이 for문이나 직접 입력하기 안해도됨.
pee(*foo()) # 언패킹은 * 쓰면 됨
sum(*foo())