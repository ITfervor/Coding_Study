def solution(k, score):
    answer = []
    rank = []
    for i in range(0,k):
        rank.append(score[i])
        rank.sort()
        print("rank 값",rank)
        answer.append(min(rank))
    for i in range(k, len(score)):
        if rank[0] < score[i]:
            rank.remove(rank[0])
            rank.append(score[i])
            rank.sort()
            answer.append(min(rank))
        else:
            answer.append(min(rank))

    return answer

print(solution(3, [10, 100, 20, 150, 1, 100, 200]))

# k일 까지 모든 출연 가수의 점수가 명예의 전당에 오른다
# k일 이후에는 k번째 순위의 가수보다 점수가 더 높으면 명예의 전당에 오른다. 
# score가 주어진다. 
# 각 차례별 최하위 점수를 출력한다. /정렬되어잇는것중 최솟값을 answer 리스트에 저장