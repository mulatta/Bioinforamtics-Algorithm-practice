# 텍스트 파일을 읽어서 각 line을 lines 변수에 리스트로 저장
path = "rosalind_ba1g.txt"
fileBuffer = open(path, 'r')
lines = fileBuffer.readlines()

# 각 line을 해당하는 변수들로 할당
str1 = lines[0].strip()
str2 = lines[1].strip()

# 길이가 동일한 두 문자열이 얼마나 다른지 계산함
def HammingDistance(str1, str2):
    
    # 비교하고자 하는 두 문자열의 길이와 결과로 반환할 Mismatch 수를 변수로 선언
    strlen = len(str1)
    mismatch = 0
    
    # i를 포인터로 하여 두 문자열 각각에서 다른지 비교
    for i in range(strlen):
        if str1[i] != str2[i]: mismatch += 1

    return mismatch

print(HammingDistance(str1, str2))

# 열었던 파일 닫기
fileBuffer.close()