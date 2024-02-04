from PatternConversion import PattenToNumber
from Neighbors import Neighbors

# 입력 문자열 text에 대해 임의의 (가능한 모든 경우의) k-mer가 등장하는 빈도 수를 리스트로 반환하는 함수
def ComputeFreq(text, k, d=0):
    
    # 각 인덱스에 해당하는 k-mer가 text에 등장하는 빈도수를 기록할 리스트 초기화
    freqArr = [0 for _ in range(4 ** k)]

    # k-mer를 형성할 수 있는 text 시작점을 모두 순회
    for i in range(len(text)-k+1):
        
        # 현재 순번에서 형성 가능한 k-mer를 pattern으로 선언
        pattern = text[i:i+k]
        
        # mismatch를 포함할 경우
        if d:
            # pattern으로부터 d 이하의 mismatch를 허락하는 variants set 형성
            variants = Neighbors(pattern, d)
            
            # 각 variants가 등장할 때마다 count
            for var in variants:
                idx = PattenToNumber(var)
                freqArr[idx] += 1
            
            return freqArr
        
        # 선정된 현재 순번의 pattern이 등장하면 이에 상응하는 인덱스의 리스트에 기록
        freqArr[PattenToNumber(pattern)] += 1

    return freqArr

if __name__ == '__main__':
    path = "Bioinforamtics-Algorithm-practice/Chapter 1/rosalind_ba1k.txt"
    with open(path, 'r') as f:
        Text = f.readline().strip()
        k = int(f.readline().strip())

        print(*ComputeFreq(Text, k))