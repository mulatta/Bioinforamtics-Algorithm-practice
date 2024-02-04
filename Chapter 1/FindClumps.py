from PatternInText import PatternCount
from ComputeFreq import ComputeFreq
from PatternConversion import NumberToPattern, PattenToNumber

# 주어진 유전체 문자열에서 크기가 L인 윈도우만큼을 순회하여 각 윈도우에서 t만큼의 빈도로 등장하는 k-mer를 배열로 출력
def myFindClumps(genome, k, L, t):
    
    # Clumps에 해당하는 k-mer를 저장할 리스트 선언
    ClumpPattern = set()

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
            
            # 만약 기록된 pattern의 빈도가 t와 같다면 ClumpPattern 에 저장
            if count == t: 
                ClumpPattern.add(pattern)
            
    return ClumpPattern

# 빈도 count를 빈도 배열을 생성하여 clumps 찾음
def findClumps(genome, k, L, t):
    # clump를 형성하는 pattern을 저장하는 리스트 선언
    clumpPattern = set()
    
    # 각 인덱스에 해당하는 pattern이 clump인지 여부를 저장하는 리스트 선언
    isClump = [0 for _ in range(4 ** k)]

    # 주어진 L 영역 내의 substring을 window로 초기화
    for i in range(len(genome) - L + 1):
        window = genome[i:i+L]

        # 현재 window에서 빈도 배열 생성
        freqArr = ComputeFreq(window, k)

        # 등장 횟수가 t 이상이면 clump로 저장
        for idx in range(len(freqArr)):
            if freqArr[idx] >= t:
                isClump[idx] = 1
    
    # clump로 저장된 인덱스를 pattern으로 바꾸어 clumpPattern에 저장
    for idx in range(len(isClump)):
        if isClump[idx] == 1:
            clumpPattern.add(NumberToPattern(idx, k))
    
    return clumpPattern

def betterClumps(genome, k, L, t):
    # clump를 형성하는 pattern을 저장할 list 초기화
    clumpPattern = set()

    # clump 여부를 기록하는 list 초기화
    isClump = [0 for _ in range(4 ** k)]

    # 초기에 빈도 배열을 구함
    window = genome[:L]
    freqArr = ComputeFreq(window, k)

    for idx in range(len(freqArr)):
        if freqArr[idx] >= t:
            isClump[idx] = 1

    # genome에서 window를 옮겨가면서 첫 pattern과 마지막 pattern을 고려
    for i in range(1, len(genome) - L + 1):
        firstPattern = genome[i-1:i-1+k]
        idx = PattenToNumber(firstPattern)
        freqArr[idx] -= 1
        
        lastPattern = genome[i+L-k:i+L]
        idx = PattenToNumber(lastPattern)
        freqArr[idx] += 1

        # 매 고려마다 빈도가 t 이상이면 clump 형성 여부 기록
        if freqArr[idx] >= t:
            isClump[idx] = 1
        
    # clump로 기록된 인덱스를 pattern으로 바꿈
    for j in range(len(freqArr)):
        if isClump[j] == 1:
            clumpPattern.add(NumberToPattern(j, k))

    return clumpPattern


# 구현 함수 실행
if __name__ == '__main__':
    path = "Bioinforamtics-Algorithm-practice/Chapter 1/rosalind_ba1e.txt"
    # path = "Bioinforamtics-Algorithm-practice/Chapter 1/ex.txt"
    with open(path, 'r') as f:
        import time

        genome = f.readline().strip()
        k, L, t = map(int, f.readline().strip().split())
        
        # 스스로 구현한 Clumps를 찾는 함수
        start = time.time()
        print(*myFindClumps(genome, k, L, t))
        end = time.time()
        print(f"{end - start:.5f}sec")

        # Textbook에 있는 pseudo-code로 구현한 함수
        start = time.time()
        print(*findClumps(genome, k, L, t))
        end = time.time()
        print(f"{end - start:.5f}sec")
        
        # 더 빠른 Clumps를 찾는 함수
        start = time.time()
        print(*betterClumps(genome, k, L, t))
        end = time.time()
        print(f"{end - start:.5f}sec")