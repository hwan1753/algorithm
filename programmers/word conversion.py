from _collections import deque


def solution(begin, target, words):

    answer = 0      # 결과값
    length = len(begin)     # 단어 길이
    word_node = {}          # 변환 가능한 단어를 노드로 변환
    words.insert(0, begin)  # begin값 words에 추가

    # words 값들을 노드변환
    for idx in range(len(words)):
        word_node[idx] = []

    # 변환가능한 단어를 간선으로 변환
    for idx in range(len(words)):
        for idx2 in range(idx + 1, len(words)):
            chk_word = 0
            for c in range(length):
                if words[idx][c] == words[idx2][c]:
                    chk_word += 1
            # 만약 다른 글자가 1개인 경우 변환가능한 단어
            if chk_word == length - 1:
                word_node[idx].append(idx2)
                word_node[idx2].append(idx)

    wait_visit = []     # 다음 거리의 노드
    visit = deque([0])  # 큐에 넣어서 순차적으로 노드 방문
    visited = [0] * len(words)      # 노드 방문 여부 체크
    visited[0] = 1      # begin값부터 시작
    

    while True:
        # 큐에 값이 있을때까지
        while visit:
            # 방문 노드
            now_word = visit.pop()
            
            # word_node에서 간선으로 방문가능한지 확인
            for idx in word_node[now_word]:

                # 이미 방문한 노드인지 확인
                if visited[idx] == 1:
                    continue
                # 만약 해당 노드가 target값이면 종료
                if words[idx] == target:
                    return answer + 1
                # 다음 큐 리스트에 추가
                wait_visit.append(idx)
                # 방문체크
                visited[idx] = 1
        # 노드간의 거리 
        answer += 1
        
        # 만약 다음 방문할 노드가 없으면 종료
        if wait_visit:
            visit = deque(wait_visit)
            wait_visit = []
        else:
            return 0
