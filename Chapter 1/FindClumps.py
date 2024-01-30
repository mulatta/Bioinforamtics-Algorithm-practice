from PatternCount import PatternCount

# 주어진 유전체 문자열에서 크기가 L인 윈도우만큼을 순회하여 각 윈도우에서 t만큼의 빈도로 등장하는 k-mer를 배열로 출력
def findClumps(genome, k, L, t):
    
    # Clumps에 해당하는 k-mer를 저장할 리스트 선언
    ClumpsList = []

    # genome에서 길이가 L인 substr을 가져오는 반복문
    for window in range(len(genome)-L+1):
        
        # 주어진 windoe 범위 내에 있는 substr(length: L)을 slicing
        substr = genome[window:window+L]

        # L-substr에서 모든 문자열에 대한 순회 시작
        for i in range(L-k+1):
        
            # 각 시작점에서 형성되는 k-mer를 pattern으로 설정
            pattern = substr[i:i+k]
            
            # 현재 window의 substr에서 pattern의 등장 횟수를 저장
            count = PatternCount(substr, pattern)
            
            # 만약 기록된 pattern의 빈도가 t와 같다면 ClumpsList 에 저장
            if count == t: 
                ClumpsList.append(pattern)

    # 중복 제거
    ClumpsList = set(ClumpsList)
            
    return ClumpsList

# 구현 함수 실행
if __name__ == '__main__':
    path = "Bioinforamtics-Algorithm-practice/Chapter 1/rosalind_ba1e.txt"

    with open(path, 'r') as f:
        genome = f.readline().strip()
        k, L, t = map(int, f.readline().strip().split())

        print(' '.join(findClumps(genome, k, L, t)))