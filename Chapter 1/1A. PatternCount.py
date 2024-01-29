# 텍스트 파일을 읽어서 각 line을 lines 변수에 리스트로 저장
path = "rosalind_ba1a.txt"
fileBuffer = open(path, 'r')
lines = fileBuffer.readlines()

# 각 line을 해당하는 변수들로 할당
text = lines[0].strip()
pattern = lines[1].strip()

# 알고리즘에 필요한 함수 정의
def PatternCount(text, pattern):
    count = 0
    for idx in range(len(text) - len(pattern) + 1):
        if(text[idx:idx + len(pattern)] == pattern):
            count += 1
    return count

# 결과 출력
print(PatternCount(text, pattern))

# 열었던 파일 닫기
fileBuffer.close()

