from HammingDistance import HammingDistance

def NaivePatternMismatch(text, pattern, threshold):
    # 결과 변수를 저장할 리스트 선언
    pseudoMotifIdx = []
    
    for i in range(len(text) - len(pattern)):
        if HammingDistance(pattern, text[i:i+len(pattern)]) <= threshold:
            pseudoMotifIdx.append(i)

    return pseudoMotifIdx

if __name__ == '__main__':
    path = "Bioinforamtics-Algorithm-practice/Chapter 1/rosalind_ba1h.txt"

    with open(path, 'r') as f:
        Pattern = f.readline().strip()
        Text = f.readline().strip()
        d = int(f.readline().strip())

        # 결과 출력
        for result in NaivePatternMismatch(Text, Pattern, d):
            print(result, end=' ')