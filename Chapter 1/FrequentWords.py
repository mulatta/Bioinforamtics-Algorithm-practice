from PatternInText import PatternCount, ApproximatePatternCount
from PatternConversion import PattenToNumber, NumberToPattern
from HammingDistance import HammingDistance
from ReverseComplement import Complement
from ComputeFreq import ComputeFreq, makePattern
from Neighbors import Neighbors

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

    return FrequentPattern, maxCount

# 가장 빈번한 단어를 더 빨리 찾는 방법
def FasterFrequentWords(text, k):
    # 가장 빈도가 높은 pattern(words)을 저장할 리스트 선언
    FreqWords = set()

    # 주어진 text에서 등장하는 k-mer의 빈도수를 저장할 리스트 초기화
    FreqArr = ComputeFreq(text, k)

    # 계산된 빈도수 중 최대값을 저장
    maxCount = max(FreqArr)

    # FreqArr에 저장된 등장 빈도수 중 최대값인 경우의 인덱스를 찾고, 이에 해당하는 pattern만 FreqWords에 저장
    for idx in range(len(FreqArr)):
        if FreqArr[idx] == maxCount:
            FreqWords.add(NumberToPattern(idx, k))

    # 최대 등장 횟수를 확인하기 위해 maxCount도 반환하도록 수정
    return FreqWords, maxCount

# ## Mismatch가 있는 빈번한 단어 문제
# 
# ### 개요
# - 앞선 연습문제에서는 유사한 모티프가 등장하는 횟수(count)를 반환하는 함수를 구성하였다.
# - 이번 문제에서는 등장 횟수들로부터 최대값을 찾은 뒤, 그 최대값에 해당하는 모티프를 반환한다.
# - 즉, 문자열에서 d개 이하의 mismatch까지만 허용하는 *k-mer*를 찾는다.
# - 한편, 이러한 *k-mer*는 주어진 전체 문자열에 존재하지 않을 수 있다.(문자열에는 유사한 모티프만 존재할 경우)
# - 따라서, Näive 한 방법으로, 가능한 모든 k-mer를 형성한 뒤, 각각의 *k-mer*가 가지는 유사한 모티프가 등장하는 횟수를 구하는 방식으로 접근할 수 있다.
# 
# ---
# 
# 현 문제 입출력 및 함수 구현
# 
# ### Case 1: 가능한 모든 k-mer의 경우의 수를 생성한 뒤, 모든 경우에 대해 탐색
    # ## Mismatch가 있고 Reverse complement를 고려하는 빈번한 단어 문제
    # 
    # ### 개요
    # - 앞선 연습문제에서는 문자열에서 d개 이하의 mismatch까지만 허용하는 *k-mer*를 찾는다.
    # - 이번 문제에서는 reverse complement를 고려하여 *k-mer*와 *k-mer*의 complement *k-mer'*의 등장 빈도수 합이 최대인 서열을 찾는다.
    # 
    # ---

# 입력 문자열 text에서 threshold 이하의 변이를 허용하는 모든 가능한 pattern의 시작 위치를 리스트로 반환하는 함수
def findPatternWithMismatches(text, pattern, threshold):
    # 결과 변수를 저장할 리스트 선언
    pseudoMotifIdx = []
    
    for i in range(len(text) - len(pattern)):
        if HammingDistance(pattern, text[i:i+len(pattern)]) <= threshold:
            pseudoMotifIdx.append(i)

    return pseudoMotifIdx

# d개 이하의 mismatches를 허용하는 가장 빈번한 pattern을 반환하는 함수, reverse = True이면 역상보 서열까지 frequency에 포함한 가장 빈번한 pattern을 반환
def findMostFrequentPatternWithMismatches(text, k, variations, reverse = False):
    # 등장 횟수를 저장하는 count list, ppattern의 서열정보를 입력할 pList 초기화
    count, pList = [], []
    
    # 후보가 될 k-mer를 생성
    candidateKmer = makePattern(['A', 'T', 'G', 'C'], k)
    
    # reverse complement를 고려하지 않는 경우, 등장한 pattern에 대해서만 결과로 반환
    if reverse == False:

        # 생성된 후보 k-mer를 하나씩 고려(Brute-force)
        for kmer in candidateKmer:
            count.append(ApproximatePatternCount(text, kmer, variations))

    # reverse complement를 고려하는 경우, 해당 서열과 그 서열의 역상보 서열의 빈도수 합을 결과로 반환
    else:
        # 생성된 후보 k-mer를 하나씩 고려(Brute-force)
        for kmer in candidateKmer:
            count.append(ApproximatePatternCount(text, kmer, variations) + ApproximatePatternCount(text, Complement(kmer, True), variations))

    # count에서 최대값을 가질 때 pattern을 pList에 저장
    maxCount = max(count)
    pList.extend(candidateKmer[i] for i in range(len(count)) if count[i] == maxCount)
    
    # 중복값 제거
    pList = set(pList)

    # 저장된 인덱스가 나타내는 pattern을 리스트로 반환, maxCount를 반환하도록 수정
    return pList, maxCount

# ### Case 2: 주어진 text에서 k-mer 길이만큼 후보군을 가져온 뒤, d개 이하의 mismatch가 형성된 경우를 만들어 비교

# 가장 빈번한 pattern을 sorting을 통해 반환하는 함수
def FrequentWordsbySorting(text, k):
    # 가장 빈번하게 나타나는 pattern을 저장하는 리스트 초기화
    FreqPattern = []
    patIdx, count = [], []

    # 문자열의 각 인덱스를 시작점으로 하는 k-mer를 번호로 저장
    for idx in range(len(text) - k + 1):
        patIdx.append(PattenToNumber(text[idx:idx+k]))
        count.append(1)
    
    # 각 위치에 해당하는 pattern의 번호가 담긴 리스트를 정렬
    # 이때, count 리스트 내에는 모두 1로 초기화 되었으므로 별도의 정렬 필요 없음
    patIdx.sort()

    # 이전 pattern과 현재 pattern이 같다면(연속적이라면), count를 이전보다 1 증가
    for idx in range(1, len(text) - k + 1):
        if patIdx[idx] == patIdx[idx-1]:
            count[idx] = count[idx-1] + 1
    
    # 최대값을 저장
    maxCount = max(count)

    # 최대값만큼 등장한 pattern을 저장
    FreqPattern.extend(NumberToPattern(patIdx[idx], k) for idx in range(len(text) - k + 1) if count[idx] == maxCount)

    return FreqPattern, maxCount


# d개의 mismatch를 허용할 때의 pattern 중 가장 빈번하게 등장하는 것들을 정렬을 통해 구한 뒤 반환하는 함수
def findFrequentWordsWithMismatchesBySorting(text, k, variations):
    # 입력된 text에서 가능한 모든 pattern(mismatches 허용)을 for-loop을 따라 중복을 허용하여 순차적으로 저장하는 리스트 초기화
    neighbors = []
    
    # 결과로 반환할 mismatch를 포함하는 가장 빈번한 pattern을 저장할 set 변수 초기화
    freqPattern = set()

    # 입력 text에서 가능한 모든 k-mer를 순회
    for idx in range(len(text) - k + 1):
    
        # k-mer를 순회하면서 해당 k-mer에서 허용 가능한 모든 pattern을 저장
        neighbors.extend(Neighbors(text[idx:idx+k], variations))

    # 저장된 k-mer들을 하나씩 순회하며 각각을 index와 count 배열에 저장
    index = [0 for _ in range(len(neighbors))]
    count = [0 for _ in range(len(neighbors))]
    
    # 저장한 pattern들을 인덱스로 변환하여 index list에 저장하고 count = 1로 초기화
    for idx in range(len(neighbors)):
        index[idx] = PattenToNumber(neighbors[idx])
        count[idx] = 1
    
    # index를 정렬
    index.sort()

    # 정렬된 리스트를 순회하면서 count
    for idx in range(1, len(index)):
        if index[idx] == index[idx - 1]:
            count[idx] = count[idx - 1] + 1

    # maxCount를 구한 뒤, 최대값인 pattern만 모아서 반환
    maxCount = max(count)
    for idx in range(len(count)):
        if count[idx] == maxCount:
            freqPattern.add(NumberToPattern(index[idx], k))
    
    return freqPattern, maxCount

# 상위 top개의 가장 빈번한 pattern을 dictionary로 반환하는 함수
def FrequentDict(text, k, variations=0, top=10):
    # 반환 딕셔너리 변수 초기화
    FreqDict = dict()
    
    # 상위 top 개의 빈도를 가져옴
    FreqArr = ComputeFreq(text, k, variations)
    TopFreq = FreqArr.sort()[:top]
    
    # 상위 top개의 빈도 수를 key로, 해당 pattern을 value로 dictionary 생성
    for freq in TopFreq:
        FreqDict[freq] = NumberToPattern()
    
    return FreqDict



# 구현 함수 실행
if __name__ == '__main__':
    path1 = "Bioinforamtics-Algorithm-practice/Chapter 1/rosalind_ba1b.txt"
    path2 = "Bioinforamtics-Algorithm-practice/Chapter 1/rosalind_ba1h.txt"
    path3 = "Bioinforamtics-Algorithm-practice/Chapter 1/rosalind_ba1i.txt"
    path4 = "Bioinforamtics-Algorithm-practice/Chapter 1/rosalind_ba1j.txt"
    
    # 1B solution
    with open(path1, 'r') as f:
        Text = f.readline().strip()
        k = int(f.readline().strip())
        print(*FrequentWords(Text, k))

    # 1H solution
    with open(path2, 'r') as f:
        Pattern = f.readline().strip()
        Text = f.readline().strip()
        variations = int(f.readline().strip())
        print(*findPatternWithMismatches(Text, Pattern, variations))

    # 1I solution
    with open(path3, 'r') as f:
        Text = f.readline().strip()
        k, variations = map(int,f.readline().strip().split())
        print(*findMostFrequentPatternWithMismatches(Text, k, variations))
    
    # 1J solution
    with open(path4, 'r') as f:
        Text = f.readline().strip()
        k, variations = map(int,f.readline().strip().split())
        print(*findMostFrequentPatternWithMismatches(Text, k, variations, True))
    
    # Textbook 71p. pseudo-code implementation
    with open(path1, 'r') as f:
        Text = f.readline().strip()
        k = int(f.readline().strip())
        print(*FasterFrequentWords(Text, k))

    # Textbook 75p. pseudo-code implementation 
    with open(path1, 'r') as f:
        Text = f.readline().strip()
        k = int(f.readline().strip())
        print(*FrequentWordsbySorting(Text, k))

    # Textbook 82-83p. pseudo-code implementation
    with open(path3, 'r') as f:
        Text = f.readline().strip()
        k, variations = map(int,f.readline().strip().split())
        print(*findFrequentWordsWithMismatchesBySorting(Text, k, variations))