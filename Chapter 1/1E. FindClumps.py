# 텍스트 파일을 읽어서 각 line을 lines 변수에 리스트로 저장
path = "rosalind_ba1e.txt"
fileBuffer = open(path, 'r')
lines = fileBuffer.readlines()

# 각 line을 해당하는 변수들로 할당
genome = lines[0].strip()
param = lines[1].strip().split()
k = int(param[0])
L = int(param[1])
t = int(param[2])

# 주어진 유전체 문자열에서 크기가 L인 윈도우만큼을 순회하여 각 윈도우에서 t만큼의 빈도로 등장하는 k-mer를 배열로 출력
def findClumps(genome, k, L, t):
    # 출력 변수 선언
    ClumpsList = []

    # genome에서 길이가 L인 substr을 가져오는 반복문
    for window in range(len(genome)):
        substr = genome[window:window+L]

        # L-substr에서 모든 문자열에 대한 순회 시작
        for i in range(L):
        
            # 각 시작점에서 형성되는 k-mer를 pattern으로 설정
            pattern = substr[i:i+k]
            
            # 등장 횟수를 세기 위한 count 변수 선언
            count = 0

            # k-mer가 형성될 수 있는 substr을 순회
            for j in range(len(substr)-k):
                
                # 현재 시작점으로 설정된(순회중인) 문자열이 형성하는 k-mer가 찾고자 하는 k-mer(pattern)과 같다면 count
                if(substr[j:j+k] == pattern):
                    count += 1
            
            # 만약 기록된 pattern의 빈도가 t와 같다면 ClumpsList 에 저장
            if count == t: 
                ClumpsList.append(pattern)

    # 중복 제거
    ClumpsList = set(ClumpsList)
            
    return ClumpsList

print(' '.join(findClumps(genome, k, L, t)))

# 열었던 파일 닫기
fileBuffer.close()

