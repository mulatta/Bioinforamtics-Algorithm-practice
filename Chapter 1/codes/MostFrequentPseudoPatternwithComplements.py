# ## Mismatch가 있고 Reverse complement를 고려하는 빈번한 단어 문제
# 
# ### 개요
# - 앞선 연습문제에서는 문자열에서 d개 이하의 mismatch까지만 허용하는 *k-mer*를 찾는다.
# - 이번 문제에서는 reverse complement를 고려하여 *k-mer*와 *k-mer*의 complement *k-mer'*의 등장 빈도수 합이 최대인 서열을 찾는다.
# 
# ---

# 이전 문제들에서 다룬 함수들
from ReverseComplement import RevComp
from MostFrequentPseudoPattern import makePattern
from ApproximatePatternCount import ApproximatePatternCount
# ---
# 
# 현 문제 입출력 및 함수 구현
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

if __name__ == '__main__':
    path = "Bioinforamtics-Algorithm-practice/Chapter 1/rosalind_ba1j.txt"
    
    with open(path, 'r') as f:
        Text = f.readline().strip()
        k, d = map(int,f.readline().strip().split())

        for result in MostFrequentPseudoPatternwithComp(Text, k, d):
            print(result, end=' ')