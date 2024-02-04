# 다음의 Test case를 통해 A, C, G, T의 이진 표현 패턴을 확인할 수 있음

# 하나의 base로 이루어진 경우, 4가지 base는 이진법 2^2, 즉, 두자릿수로 표현 가능
# A C G T --> 00 01 10 11

# 2가지 base로 이루어진 경우, base의 각 자릿수마다 하나의 base로 이루어진 binary value를 붙이면 됨
# AA AC AG AT --> 0000 0001 0010 0011
# CA CC CG CT --> 0100 0101 0110 0111
# GA GC GG GT --> 1000 1001 1010 1011
# TA TC TG TT --> 1100 1101 1110 1111

# 주어진 pattern을 baseOrder를 기준으로 할 때 decimal index로 반환하는 함수
def MyPattenToNumber(pattern):
    # 임의의 base 우선순위를 dictionary로 선언
    baseOrder = {'A': '00', 'C': '01', 'G': '10', 'T': '11'}

    # 결과로 반환할 변수를 문자열로 선언 - string type의 문자열 연결 특성을 활용하기 위함
    pat2idx = ''

    # pattern의 각 자릿수를 이진으로 표현하는 문자열 생성
    for digit in pattern:
        if digit in baseOrder:
            pat2idx += baseOrder.get(digit)
        else:
            raise ValueError(f"Invalide Character {digit} in pattern")
    
    # 생성된 이진 문자열을 decimal로 변형
    pat2idx = int(pat2idx, 2)

    return pat2idx

# 주어진 decimal index를 orderBase를 기준으로 할 때 k-mer로 반환하는 함수
def MyNumberToPattern(idx, k):
    # 주어진 이진 우선순위에 해당하는 문자열을 mapping하기 위해 dictionary 선언
    orderBase = {'00': 'A', '01': 'C', '10': 'G', '11': 'T'}
    
    # 주어진 decimal idx를 이진으로 변환한 뒤, k 자릿수만큼 0으로 채워 전체 자릿수를 이진으로 표현
    binidx = bin(idx)[2:].zfill(k*2)
    
    # 결과로 반환할 문자열 변수 선언
    pattern = ''

    # 이진 표기의 두 자릿수마다 그에 상응하는 문자열로 변환
    for i in range(0, len(binidx), 2):
        pattern += orderBase.get(binidx[i:i+2])
    
    return pattern

# 주어진 symbol(문자열 하나)에 부여된 번호를 반환하는 함수
def SymbolToNumber(symbol):
    
    # 주어진 symbol에 해당하는 번호를 반환
    return {'A': 0, 'C': 1, 'G': 2, 'T': 3}[symbol]

def NumberToSymbol(idx):
    num2sym = {0: 'A', 1: 'C', 2:'G', 3:'T'}

    if idx not in num2sym:
        raise ValueError(f"Invalid index {idx}.")
    else: return num2sym.get(idx)

# 주어진 pattern을 prefix와 symbol로 나누어 할당될 번호를 계산하여 반환하는 함수
def PattenToNumber(pattern):
    
    # 만약 symbol이 없다면(즉, 주어진 문자열의 길이가 1이라면) 0을 반환
    if len(pattern) == 0: return 0
    
    # symbol이 존재한다면 주어진 pattern을 symbol과 prefix로 각각 초기화
    symbol = pattern[-1]
    prefix = pattern[:-1]
    
    # 주어진 symbol이 유효하다면, prefix를 다음 자릿수로 올리고 symbol의 번호를 추가
    return 4 * PattenToNumber(prefix) + SymbolToNumber(symbol)


# 주어진 idx % 4를 symbol로 하여 문자열을 끝에서부터 하나씩 붙여 최종 pattern을 생성한 뒤 반환하는 함수
def NumberToPattern(idx, k):
    
    # k-mer가 1개의 문자열로 이루어진 경우, idx 자체의 symbol 반환
    # NumberToSymbol 함수에 idx는 0~3에 대한 mapping만 허용하므로 idx와 k의 예외가 모두 cover
    if k == 1: return NumberToSymbol(idx)
    
    # 주어진 idx를 symbol과 prefix에 해당하는 idx로 각각 나누어 선언
    prefixIdx = idx // 4
    symbolIdx = idx % 4

    # prefix idx가 나타내는 pattern을 재귀 호출로 구하고, 그 뒤에 symbol idx가 나타내는 symbol을 붙여 완성한 뒤 반환
    return NumberToPattern(prefixIdx, k-1) + NumberToPattern(symbolIdx, 1)


if __name__ == '__main__':
    # print("My code>\n",
    #         MyPattenToNumber('ATGCAA'),
    #         MyNumberToPattern(5437, 7),
    #         MyNumberToPattern(5437, 8),
    #         "\n", sep=' ')
    
    # print("Codes implementation refers to the text book>\n", 
    #         PattenToNumber('ATGCAA'),
    #         NumberToPattern(5437, 7),
    #         NumberToPattern(5437, 8),
    #         "\n", sep=' ')

    # print("연습문제>\n", 
    #         "MyNumberToPattern(11, 3)",
    #         MyNumberToPattern(11, 3),
    #         "NumberToPattern(11, 3)",
    #         NumberToPattern(11, 3),
    #         "\n", sep=' ')

    path1 = "Bioinforamtics-Algorithm-practice/Chapter 1/rosalind_ba1m.txt"
    with open(path1, 'r') as f:
        idx = int(f.readline().strip())
        k = int(f.readline().strip())
        print(NumberToPattern(idx, k))
    
    path2 = "Bioinforamtics-Algorithm-practice/Chapter 1/rosalind_ba1l.txt"
    with open(path2, 'r') as f:
        Pattern = f.readline().strip()
        print(PattenToNumber(Pattern))