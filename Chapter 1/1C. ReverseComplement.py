# 텍스트 파일을 읽어서 각 line을 lines 변수에 리스트로 저장
path = "rosalind_ba1c.txt"
fileBuffer = open(path, 'r')

# 읽어온 파일의 한 line을 변수로 할당
pattern = fileBuffer.readline()
pattern = pattern.strip()

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

print(RevComp(pattern))
