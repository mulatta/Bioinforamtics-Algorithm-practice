# skewness를 계산한 뒤 최소가 되는 모든 인덱스를 리스트로 반환하는 함수
def MinSkew(genome):
    # 변수 선언
    skew = [0 for _ in range(len(genome))]
    minSkew = []

    # 가중치 값을 저장하는 dictionary
    weight = {'G':1, 'C':-1, 'A':0, 'T':0}
    
    # 가장 첫번째 genome 위치는 이전 값을 참조할 수 없으므로 자기 자신을 입력
    skew[0] = weight[genome[0]]

    # 전체 genome에 대하여 모든 문자열을 순회하고 skew를 기록
    for i in range(1, len(genome)):
        skew[i] = skew[i-1] + weight[genome[i-1]]

    # 기록된 skew 중 최소값을 찾고, 최소값을 갖는 모든 인덱스를 리스트에 저장
    minVal = min(skew)
    for i in range(len(genome)):
        if skew[i] == minVal: minSkew.append(i)
    
    return minSkew, skew

# 구현 함수 실행
if __name__ == '__main__':
    path = "Bioinforamtics-Algorithm-practice/Chapter 1/rosalind_ba1f.txt"

    with open(path, 'r') as f:
        genome = f.readline().strip()
        print(*MinSkew(genome))