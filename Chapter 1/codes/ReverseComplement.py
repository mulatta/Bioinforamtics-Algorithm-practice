# 주어진 서열을 상보적인 서열로 바꿔 반환하는 함수
def Complement(seq):

    # 상보적인 서열이 어떤 것인지 저장하는 dictioinary 선언
    basepair = {'A' : 'T', 'T': 'A', 'G' : 'C', 'C' : 'G'}
    
    # 반환할 상보적 서열 문자열 변수 선언
    CompSeq = ''
    
    # 입력 서열에서 문자를 하나씩 상보적인 염기 문자를 추가함
    for base in seq:
        CompSeq += basepair.get(base, '?')

    return CompSeq

# 입력 문자열을 뒤집은 뒤 문자열로 반환하는 함수
def Reverse(seq):
    RevSeq = ''.join(base for base in reversed(seq))
    return RevSeq

def RevComp(seq):
    return Reverse(Complement(seq))

# 구현 함수 실행
if __name__ == '__main__':
    path = "Bioinforamtics-Algorithm-practice/Chapter 1/rosalind_ba1c.txt"

    with open(path, 'r') as f:
        Pattern = f.readline().strip()
        print(RevComp(Pattern))
