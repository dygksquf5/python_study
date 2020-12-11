import collections

# 내풀이 .. 다 절반만 맞음
def solution(scoville, k):
    sco = collections.deque(sorted(scoville))
    answer = 0

    while True:
        tem = sco.popleft()

        if k > min(sorted(sco)):
            number = (sco.popleft() * 2)
            sco.appendleft(tem + number)
            answer += 1

            if k <= min(sorted(sco)):
                return answer

        if answer + 1 == len(sco):
            return -1


# 힙 써서 매번 새롭게 힙정렬이 된 상태로, 진행하는게 더 깔끔하고 빠르고 정확도가 높다.
import heapq as hq

def solution(scoville, K):

    hq.heapify(scoville) # 주어진 배열을 힙배열로 바꾸기
    answer = 0
    while True:
        first = hq.heappop(scoville) # 힙팝은 매번 받아온 값을 새롭게 힙정렬한다음 거기서 가장 작은 값을 뽑아냄
        if first >= K:
            break
        if len(scoville) == 0:
            return -1
        second = hq.heappop(scoville)
        hq.heappush(scoville, first + second*2) # 푸쉬를 할 때에도, 푸쉬 하면 자동으로 다시 해당 값을 힙정렬하여 리턴함.
        answer += 1

    return answer