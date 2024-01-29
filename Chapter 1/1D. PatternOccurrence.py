# 텍스트 파일을 읽어서 각 line을 lines 변수에 리스트로 저장
path = "rosalind_ba1d.txt"
fileBuffer = open(path, 'r')
lines = fileBuffer.readlines()

# 각 line을 해당하는 변수들로 할당
pattern = lines[0].strip()
text = lines[1].strip()

# 주어진 text 문자열에서 pattern이 발생한 문자열의 인덱스를 리스트로 반환하는 함수
def PatternOccurrence(text, pattern):
    # 발생 빈도를 저장할 배열 선언
    OccList = []
    # pattern을 셀 수 있는 모든 문자열을 시작점으로 순회
    for idx in range(len(text) - len(pattern) + 1):
        
        # 시작 문자열부터 pattern 길이만큼의 부분문자열(substring)이 pattern을 형성하면 그 인덱스를 배열에 저장
        if(text[idx:idx + len(pattern)] == pattern):
            OccList.append(idx)

    return OccList

# 결과 출력
for idx in PatternOccurrence(text, pattern):
    print(idx, end=' ')

# 열었던 파일 닫기
fileBuffer.close()

