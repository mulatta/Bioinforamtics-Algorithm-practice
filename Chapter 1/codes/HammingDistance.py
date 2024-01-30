# 길이가 동일한 두 문자열이 얼마나 다른지 계산함
def HammingDistance(str1, str2):
    
    # 비교하고자 하는 두 문자열의 길이와 결과로 반환할 Mismatch 수를 변수로 선언
    strlen = len(str1)
    mismatch = 0
    
    # i를 포인터로 하여 두 문자열 각각에서 다른지 비교
    for i in range(strlen):
        if str1[i] != str2[i]: 
            mismatch += 1

    return mismatch

# 구현 함수 실행
if __name__ == '__main__':
    path = "Bioinforamtics-Algorithm-practice/Chapter 1/rosalind_ba1g.txt"

    with open(path, 'r') as f:
        str1 = f.readline().strip()
        str2 = f.readline().strip()

        print(HammingDistance(str1, str2))