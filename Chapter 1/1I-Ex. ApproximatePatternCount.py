# ## 유사한 pattern(k-mer motif) 찾기
# 
# ### 개요
# - 임의의 threshold *d*에 대하여, 이보다 적은 횟수로 mismatch가 일어나는 pattern을 찾고자 함
# - 즉, d개의 Mismatch까지 허용하는 유사 motif를 찾는 것이 목표
# - 이전까지의 실습에서는 *정확히 동일한* pattern만을 찾았으나, 실제로는 Muatation 등의 이유로 유사한 서열의 Motif(pattern)를 가지기도 함. 
# - 따라서, 어느정도 유사한 서열을 찾는 것은 중요함
# 

# 길이가 동일한 두 문자열이 얼마나 다른지 계산함
def HammingDistance(str1, str2):
    
    # 비교하고자 하는 두 문자열의 길이와 결과로 반환할 Mismatch 수를 변수로 선언
    strlen = len(str1)
    mismatch = 0
    
    # i를 포인터로 하여 두 문자열 각각에서 다른지 비교
    for i in range(strlen):
        if str1[i] != str2[i]: mismatch += 1

    return mismatch

# 주어진 전체 문자열 Text에서 d개 이하의 mismatch만 허용하는 유사 motif(pattern)를 찾아 그 motif의 "수"를 반환
def ApproximatePatternCount(text, pattern, d):
    # 결과로 반환할 변수 선언
    count = 0

    # 주어진 text에서 pattern을 찾을 수 있는 범위를 모두 순회
    for i in range(len(text) - len(pattern) + 1):

        # 유사 pattern의 후보로 ppattern을 text로부터 slicing 해옴
        ppattern = text[i:i+len(pattern)]

        # ppattern과 원래 pattern의 HammingDistance를 계산하고, d보다 작다면 count
        if HammingDistance(pattern, ppattern) <= d:
            count += 1
    
    return count

# Textbook의 예제 상황 변수 선언
Text = "AACAAGCATAAACATTAAAGAG"
Pattern = "AAAAA"

# 책에서 주어진대로, 1개의 mismatch를 허용하는 유사 motif는 다음과 같이 찾을 수 있다.
print(ApproximatePatternCount(Text, Pattern, 1))

# 연습 문제의 구현 및 풀이
print(ApproximatePatternCount(Text, Pattern, 2))

