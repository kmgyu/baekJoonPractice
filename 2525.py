#2525 시간계산하기

from datetime import *
h, m = map(int, input().split())
start = datetime(100, 1, 1, h, m)
end = timedelta(minutes=int(input()))
start = start + end
print(start.hour, start.minute)

# https://www.infoking.site/144
# https://cosmosproject.tistory.com/105
# https://datascienceschool.net/01%20python/02.15%20%ED%8C%8C%EC%9D%B4%EC%8D%AC%EC%97%90%EC%84%9C%20%EB%82%A0%EC%A7%9C%EC%99%80%20%EC%8B%9C%EA%B0%84%20%EB%8B%A4%EB%A3%A8%EA%B8%B0.html