# ## Mismatch가 있고 Reverse complement를 고려하는 빈번한 단어 문제
# 
# ### 개요
# - 앞선 연습문제에서는 문자열에서 d개 이하의 mismatch까지만 허용하는 *k-mer*를 찾는다.
# - 이번 문제에서는 reverse complement를 고려하여 *k-mer*와 *k-mer*의 complement *k-mer'*의 등장 빈도수 합이 최대인 서열을 찾는다.
# 
# ---
# 이전 문제들에서 다룬 함수들

def Complement(pattern):
    basepair = {'A' : 'T', 'T': 'A', 'G' : 'C', 'C' : 'G'}
    CompSeq = ''
    for base in pattern:
        CompSeq += basepair.get(base, 'error')

    return CompSeq

def Reverse(pattern):
    RevSeq = ''.join(base for base in reversed(pattern))
    return RevSeq

def RevComp(pattern):
    return Reverse(Complement(pattern))

# 길이가 동일한 두 문자열이 얼마나 다른지 계산함
def HammingDistance(str1, str2):
    
    # 비교하고자 하는 두 문자열의 길이와 결과로 반환할 Mismatch 수를 변수로 선언
    strlen = len(str1)
    mismatch = 0
    
    # i를 포인터로 하여 두 문자열 각각에서 다른지 비교
    for i in range(strlen):
        if str1[i] != str2[i]: mismatch += 1

    return mismatch

# 주어진 전체 문자열 Text에서 d개 이하의 mismatch만 허용하는 유사 motif(pattern)를 찾아 그 motif의 "수"를 반환
def ApproximatePatternCount(text, pattern, d):
    # 결과로 반환할 변수 선언
    count = 0

    # 주어진 text에서 pattern을 찾을 수 있는 범위를 모두 순회
    for i in range(len(text) - len(pattern) + 1):

        # 유사 pattern의 후보로 ppattern을 text로부터 slicing 해옴
        ppattern = text[i:i+len(pattern)]

        # ppattern과 원래 pattern의 HammingDistance를 계산하고, d보다 작다면 count
        if HammingDistance(pattern, ppattern) <= d:
            count += 1
    
    return count


# ---
# 
# 현 문제 입출력 및 함수 구현

# 입력 k에 대해 가능한 모든 k-mer 조합을 리스트로 반환하는 함수
def makePattern(curPatterns, k):
    # 결과를 반환할 리스트 초기화
    result = []

    # 추가할 염기의 순서를 지정하는 리스트 초기화
    baseOrder = ['A', 'T', 'G', 'C']

    if k == 1: return curPatterns
    
    elif k > 1:
    
        # 현재 시점의 curPatterns에서 하나를 꺼내 각각 A, T, G, C를 붙인 뒤 result에 저장
        for subPattern in curPatterns:
            for i in range(len(baseOrder)):
                result.append(subPattern+baseOrder[i])

        # 한번의 step이 끝나면 감소된 k로 재귀 호출
        result = makePattern(result, k-1)

        return result

def MostFrequentPseudoPatternwithComp(text, k, d):
    # 등장 횟수를 저장하는 count list, ppattern의 서열정보를 입력할 pList 초기화
    count, pList = [], []
    
    # 후보가 될 k-mer를 생성
    candidateKmer = makePattern(['A', 'T', 'G', 'C'], k)
    
    # 후보 k-mer 중 하나씩 꺼내 전체 text에서 검사
    for kmer in candidateKmer:
        
        # 선정된 k-mer와 (k-mer)'을 pattern으로 할 때 ppattern의 각 횟수 합을 count 리스트에 저장
        count.append(ApproximatePatternCount(text, kmer, d) + ApproximatePatternCount(text, RevComp(kmer), d))
    
    # count에서 최대값을 가질 때 pattern을 pList에 저장
    pList.extend(candidateKmer[i] for i in range(len(count)) if count[i] == max(count))
    
    # 중복값 제거
    pList = set(pList)

    # 저장된 인덱스가 나타내는 pattern을 리스트로 반환
    return pList

# 구현 함수 실행

path = "rosalind_ba1j.txt"

with open(path, 'r') as f:
    Text = f.readline().strip()
    k, d = map(int,f.readline().strip().split())

    for result in MostFrequentPseudoPatternwithComp(Text, k, d):
        print(result, end=' ')