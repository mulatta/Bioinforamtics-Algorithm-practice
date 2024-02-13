# 주어진 서열을 상보적인 서열로 바꿔 반환하는 함수
def Complement(seq, reverse=False):

    # 상보적인 서열이 어떤 것인지 저장하는 dictioinary 선언
    basepair = {'A' : 'T', 'T': 'A', 'G' : 'C', 'C' : 'G'}
    
    # 반환할 상보적 서열 문자열 변수 선언
    CompSeq = ''
    
    # 입력 서열에서 문자를 하나씩 상보적인 염기 문자를 추가함
    for base in seq:
        CompSeq += basepair.get(base, '?')

    # reverse 매개변수를 참으로 받을 때 역상보 서열을 반환 (5' -> 3')
    if reverse: return CompSeq[::-1]
    
    # 그렇지 않으면 상보 서열만 반환 (3' -> 5')
    else: return CompSeq

# 구현 함수 실행
if __name__ == '__main__':
    path = "Bioinforamtics-Algorithm-practice/Chapter 1/rosalind_ba1c.txt"

    with open(path, 'r') as f:
        Pattern = f.readline().strip()
        print(Complement(Pattern, True))