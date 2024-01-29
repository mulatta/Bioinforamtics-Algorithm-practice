# 텍스트 파일을 읽어서 각 line을 lines 변수에 리스트로 저장
path = "rosalind_ba1b.txt"
fileBuffer = open(path, 'r')
lines = fileBuffer.readlines()

# 각 line을 해당하는 변수들로 할당
text = lines[0].strip()
k = int(lines[1].strip())

# 이전에 구현한 PatternCount 함수
def PatternCount(text, pattern):
    count = 0
    for idx in range(len(text) - len(pattern) + 1):
        if(text[idx:idx + len(pattern)] == pattern):
            count += 1
    return count

# 주어진 text에서 특정 words의 빈도수를 계산하여 빈도수가 가장 높은 k-mer를 기록하고 반환하는 함수
def FrequentWords(text, k):
    count = [0 for i in range(len(text))]
    FrequentPattern = []
    
    # i-th value가 가지는 k-mer의 빈도 수를 count라는 배열에 저장
    for i in range(len(text) - k + 1):
        pattern = text[i:i+k]
        count[i] = PatternCount(text, pattern)

    # count 배열을 순회하면서 maxCount값을 가지는 pattern을 FrequentPattern으로 저장
    maxCount = max(count)
    for i in range(len(text) - k):
        if count[i] == maxCount:
            FrequentPattern.append(text[i:i+k])
    
    # 위 4줄을 다음의 한 줄로 줄일 수 있음
    # FrequentPattern.extend([text[i:i+k] for i in range(len(text) - k) if count[i] == max(count)])
    
    # 중복을 제거하기 위해 set 자료구조의 특성 이용
    FrequentPattern = set(FrequentPattern)

    return FrequentPattern

for element in FrequentWords(text, k):
    print(element , end = ' ')

# 열었던 파일 닫기
fileBuffer.close()

