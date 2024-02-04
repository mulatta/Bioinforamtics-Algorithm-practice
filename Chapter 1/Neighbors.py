from HammingDistance import HammingDistance

# 주어진 pattern에서 하나의 변이만 허용할 경우 가능한 모든 조합을 반환
def immediateNeighbors(pattern):
    
    # 가능한 염기 목록 선언
    baseList = ['A', 'T', 'G', 'C']

    # 가능한 조합을 저장할 set 초기화
    neighborhoods = set()

    # pattern의 각 위치를 순회하며 가능한 variant 형성
    for idx in range(len(pattern)):

        # 첫 글자를 symbol로 지정
        symbol = pattern[idx]

        # symbol의 여집합 - symbol이 아닌 나머지 3 종류의 염기를 고름
        complementSet = [base for base in baseList if base != symbol]
        
        # 여집합들로 symbol을 substitution 후 저장
        for x in complementSet:
            neighborhoods.add(pattern[:idx] + x + pattern[idx+1:])
    
    return neighborhoods

# 주어진 pattern에서 d개 이하의 변이를 허용하는 모든 variants set을 반환하는 함수
def Neighbors(pattern, d):

    # implicit order
    # Whole variants set = (prefix + suffix variants set | H.Dist < d) + (prefix variants set + suffix | H.Dist = d)

    baseSet = {'A', 'T', 'G', 'C'}
    
    # d = 0일 때, 기존 pattern에 변이가 없어야 함 --> 그대로 반환
    if d == 0: return pattern
    
    # len(pattern) == 1일 때의 가능한 모든 variant(A, T, G, C) 반환
    if len(pattern) == 1: return baseSet
    
    # 결과로 반환할 variant set 변수 초기화
    neighborhoods = set()

    # pattern을 첫 글자(prefix)와 나머지 부분(suffix)으로 쪼갬
    prefix = pattern[0]
    suffix = pattern[1:len(pattern)]

    # suffix neighborhoods를 재귀호출을 통해 선언
    # 모든 과정에서 suffix neighborhoods는 늘 correct solution이라 가정 - 재귀 호출: len(pattern) == 1에서 처리됨
    suffixNeighborhoods = Neighbors(suffix, d)
    
    # suffix variants 각각의 가장 앞에 prefix를 추가하여 저장
    for suffixNeighbor in suffixNeighborhoods:
        
        # HammingDistance가 d 미만이면, 하나까지는 임의의 base를 추가할 수 있음
        if HammingDistance(suffixNeighbor, suffix) < d:
            for base in baseSet:
                neighborhoods.add(base + suffixNeighbor)
        
        # HammingDistance가 d라면, 맨 앞자리에 prefix만 추가할 수 있음 (그래야 d를 초과하지 않음)
        else:
            neighborhoods.add(prefix + suffixNeighbor)
        
        # HammingDistance가 d보다 큰 경우는 재귀호출을 통해 subproblem에 대한 subsolution의 correctness가 보장되므로 고려할 필요가 없음

    return neighborhoods

def iterativeNeighbors(pattern, d):
    # 초기에 pattern만을 포함하는 set 초기화
    neighborhoods = {pattern}

    # d 이하의 모든 경우에 대하여 set을 늘려나감
    for i in range(d):
        
        # neighborhoods set 내의 pattern'의 immediateNeighbors를 구하여 set에 포함
        for ppattern in neighborhoods:
            neighborhoods = neighborhoods | immediateNeighbors(ppattern)
        
        # 이 경우, immediateNeighbors로 얻어진 ppattern은 d가 이전보다 1증가된 상태
        # set 자료구조의 특징으로 중복은 없음
    
    return neighborhoods

if __name__ == '__main__':
    path = "Bioinforamtics-Algorithm-practice/Chapter 1/rosalind_ba1n.txt"
    # 1N solution
    with open(path, 'r') as f:
        
        Pattern = f.readline().strip()
        d = int(f.readline().strip())

        print(*Neighbors(Pattern, d), sep='\n')
        print(*iterativeNeighbors(Pattern, d), sep='\n')