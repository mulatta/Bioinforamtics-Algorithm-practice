# 이전에 구현한 PatternCount 함수
from PatternCount import PatternCount

# 주어진 text에서 특정 words의 빈도수를 계산하여 빈도수가 가장 높은 k-mer를 기록하고 반환하는 함수
def FrequentWords(text, k):

    # 입력된 text와 같은 크기로 등장 빈도수를 동일한 인덱스에 저장하는 리스트 선언
    count = [0 for i in range(len(text))]

    # 출력할 최대 빈도수의 pattern 서열을 저장할 리스트 선언
    FrequentPattern = []
    
    # i-th value가 가지는 k-mer의 빈도 수를 count라는 배열에 저장
    for i in range(len(text) - k + 1):
        pattern = text[i:i+k]
        count[i] = PatternCount(text, pattern)

    # count의 원소가 maxCount인 pattern을 FrequentPattern으로 저장
    maxCount = max(count)
    for i in range(len(text) - k):
        if count[i] == maxCount:
            FrequentPattern.append(text[i:i+k])
    
    # 1줄로 쓸 수도 있음
    # FrequentPattern.extend([text[i:i+k] for i in range(len(text) - k) if count[i] == max(count)])

    # 중복을 제거하기 위해 set 자료구조의 특성 이용
    FrequentPattern = set(FrequentPattern)

    return FrequentPattern

# 구현 함수 실행
if __name__ == '__main__':
    path = "Bioinforamtics-Algorithm-practice/Chapter 1/rosalind_ba1b.txt"

    with open(path, 'r') as f:
        Text = f.readline().strip()
        k = int(f.readline().strip())

        for element in FrequentWords(Text, k):
            print(element , end = ' ')