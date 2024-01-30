# 주어진 text 문자열에서 pattern이 발생한 문자열의 인덱스를 리스트로 반환하는 함수
def PatternOccurrence(text, pattern):
    
    # 발생 빈도를 저장할 배열 선언
    OccList = []
    
    # pattern을 셀 수 있는 모든 문자열을 시작점으로 순회
    for idx in range(len(text) - len(pattern) + 1):
        
        # 시작 문자열부터 pattern 길이만큼의 부분문자열(substring)이 pattern을 형성하면 그 인덱스를 배열에 저장
        if(text[idx:idx + len(pattern)] == pattern):
            OccList.append(idx)

    return OccList

# 구현 함수 실행
if __name__ == '__main__':
    path = "Bioinforamtics-Algorithm-practice/Chapter 1/rosalind_ba1d.txt"

    with open(path, 'r') as f:
        Pattern = f.readline().strip()
        Text = f.readline().strip()

        for idx in PatternOccurrence(Text, Pattern):
            print(idx, end=' ')