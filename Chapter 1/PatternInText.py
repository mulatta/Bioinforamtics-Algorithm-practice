from HammingDistance import HammingDistance

# 전체 Text에서 주어진 Pattern의 등장 횟수를 반환하는 함수
def PatternCount(text, pattern):
    
    # 결과로 반환할 변수 선언
    count = 0

    # pattern의 시작점이 될 수 있는 영역을 모두 순회
    for idx in range(len(text) - len(pattern) + 1):
        
        # 현재 인덱스를 시작으로 하는 pattern이 입력 pattern과 같다면 count
        if(text[idx:idx + len(pattern)] == pattern):
            count += 1
            
    return count

# 주어진 text 문자열에서 pattern이 발생한 문자열의 인덱스를 리스트로 반환하는 함수
def findPatternIndices(text, pattern):
    
    # 발생 빈도를 저장할 배열 선언
    OccList = []
    
    # pattern을 셀 수 있는 모든 문자열을 시작점으로 순회
    for idx in range(len(text) - len(pattern) + 1):
        
        # 시작 문자열부터 pattern 길이만큼의 부분문자열(substring)이 pattern을 형성하면 그 인덱스를 배열에 저장
        if(text[idx:idx + len(pattern)] == pattern):
            OccList.append(idx)

    return OccList


# ## 유사한 pattern(k-mer motif) 찾기
# 
# ### 개요
# - 임의의 threshold *d*에 대하여, 이보다 적은 횟수로 mismatch가 일어나는 pattern을 찾고자 함
# - 즉, d개의 Mismatch까지 허용하는 유사 motif를 찾는 것이 목표
# - 이전까지의 실습에서는 *정확히 동일한* pattern만을 찾았으나, 실제로는 Muatation 등의 이유로 유사한 서열의 Motif(pattern)를 가지기도 함. 
# - 따라서, 어느정도 유사한 서열을 찾는 것은 중요함

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

# 구현 함수 실행
if __name__ == '__main__':
    path1 = "Bioinforamtics-Algorithm-practice/Chapter 1/rosalind_ba1a.txt"
    path2 = "Bioinforamtics-Algorithm-practice/Chapter 1/rosalind_ba1d.txt"

    with open(path1, 'r') as f:
        Text = f.readline().strip()
        Pattern = f.readline().strip()
        print(PatternCount(Text, Pattern))
    
    with open(path2, 'r') as f:
        Pattern = f.readline().strip()
        Text = f.readline().strip()
        print(*findPatternIndices(Text, Pattern))
    
    ############### Textbook 60p. 예제 ###############
    Text = "AACAAGCATAAACATTAAAGAG"
    Pattern = "AAAAA"

    # Count_1(AACAAGCATAAACATTAAAGAG, AAAAA)
    print(ApproximatePatternCount(Text, Pattern, 1))
    
    # Count_2(AACAAGCATAAACATTAAAGAG, AAAAA)
    print(ApproximatePatternCount(Text, Pattern, 2))
