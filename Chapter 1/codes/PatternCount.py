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

# 구현 함수 실행
if __name__ == '__main__':
    path = "Bioinforamtics-Algorithm-practice/Chapter 1/rosalind_ba1a.txt"

    with open(path, 'r') as f:
        Text = f.readline().strip()
        Pattern = f.readline().strip()

        print(PatternCount(Text, Pattern))
