# 텍스트 파일을 읽어서 각 line을 lines 변수에 리스트로 저장
path = "rosalind_ba1f.txt"
fileBuffer = open(path, 'r')
genome = fileBuffer.readline().strip()

# skewness를 계산한 뒤 최소가 되는 모든 인덱스를 리스트로 반환하는 함수
def minimizeSkew(genome):
    # 변수 선언
    skew, minSkew = [], []
    minValue = 9999

    # 가중치 값을 저장하는 dictionary
    weight = {'G':1, 'C':-1, 'A':0, 'T':0}
    
    # 가장 첫번째 genome 위치는 이전 값을 참조할 수 없으므로 자기 자신을 입력
    skew.append(weight.get(genome[0]))

    # 전체 genome에 대하여 모든 문자열을 순회하고 skew를 기록
    for i in range(len(genome)):
        skew.append(skew[i] + weight.get(genome[i]))

    # 기록된 skew 중 최소값을 찾고, 최소값을 갖는 모든 인덱스를 리스트에 저장
    for i in range(len(genome)):
        if skew[i] == min(skew): minSkew.append(i)
    
    return minSkew

for result in minimizeSkew(genome):
    print(result, end=' ')

# 열었던 파일 닫기
fileBuffer.close()