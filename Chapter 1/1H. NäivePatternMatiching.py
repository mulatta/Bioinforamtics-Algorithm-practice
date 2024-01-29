# 텍스트 파일을 읽어서 각 line을 lines 변수에 리스트로 저장
path = "rosalind_ba1h.txt"
fileBuffer = open(path, 'r')
lines = fileBuffer.readlines()

# 각 line을 해당하는 변수들로 할당
Pattern = lines[0].strip()
Text = lines[1].strip()
d = lines[2].strip()

# 파일 입력으로부터 문자열 자료형을 정수형으로 변형
d = int(d)

def HammingDistance(str1, str2):
    # 비교하고자 하는 두 문자열의 길이와 결과로 반환할 Mismatch 수를 변수로 선언
    strlen = len(str1)
    mismatch = 0
    
    for i in range(strlen):
        if str1[i] != str2[i]: mismatch += 1

    return mismatch

def NaivePatternMismatch(text, pattern, threshold):
    # 결과 변수를 저장할 리스트 선언
    pseudoMotifIdx = []
    
    for i in range(len(text) - len(pattern)):
        if HammingDistance(pattern, text[i:i+len(pattern)]) <= threshold:
            pseudoMotifIdx.append(i)

    return pseudoMotifIdx

# 결과 출력
for result in NaivePatternMismatch(Text, Pattern, d):
    print(result, end=' ')

# 열었던 파일 닫기
fileBuffer.close()

