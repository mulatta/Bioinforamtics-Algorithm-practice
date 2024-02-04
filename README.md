# Bioinforamtics Algorithm practice
 이 Repository는 생물정보학 알고리듬 3/e (필립 콤포, 파벨 페블즈너 저)의 학습 기록을 담고 있습니다.  
 책의 구성에 따라, 각 Chapter를 본문과 충전소의 2개 section으로 나누어 학습하였습니다.

 이 Repository에서는 [Rosalind Bioinformatics Textbook Track](https://rosalind.info/problems/list-view/?location=bioinformatics-textbook-track)의 풀이에 대해 다루며, 상기 내용에 대한 상세한 기록은 [블로그](https://mulatta.github.io/bioinformatics-review)에서 다룹니다.

 Rosalind의 기타 문제들에 대한 풀이는 [Rosalind PS repo](https://github.com/mulatta/Rosalind_PS)에서 다뤄집니다.

## Guidelines
 ### About this Page
 - 이 페이지에서는 이용 가이드와 목차만 확인이 가능합니다.
 ### For Users
 - 각 절의 코드는 한 파일에 연관이 있는 코드 별로 묶어서 업로드 되어 있습니다.
 - **Concepts**: 목차에 링크된 블로그 *Chapter page*의 내용을 따라가면서 코드를 확인하실 것을 권장드립니다.
 - **Codes**: 목차의 코드를 확인하시면 됩니다.
 ### Another Issues
 - 본문이나 코드 내용 상의 오류에 대한 문의는 [Issues](https://github.com/mulatta./issues) 페이지를 이용 부탁드립니다.
 - 그 외 기타 contact은 [e-mail](mailto:lsw1167@gmail.com) 로 부탁드립니다.

## 목차
 ### Chapter 1. DNA 복제는 유전체의 어디서부터 시작되는가?
 ### 본문
 - [1A. PatternCount](https://rosalind.info/problems/ba1a/) | [code](./Chapter%201/PatternInText.py)
 - [1B. FrequentWords](https://rosalind.info/problems/ba1b/) | [code](./Chapter%201/FrequentWords.py)
 - [1C. ReverseComplement](https://rosalind.info/problems/ba1c/) | [code](./Chapter%201/ReverseComplement.py)
 - [1D. findPatternIndices](https://rosalind.info/problems/ba1d/) | [code](./Chapter%201/PatternInText.py)
 - [1E. FindClumps](https://rosalind.info/problems/ba1e/) | [code](./Chapter%201/FindClumps.py)
 - [1F. MinimizeSkew](https://rosalind.info/problems/ba1f/) | [code](./Chapter%201/MinSkew.py)
 - [1G. HammingDistance](https://rosalind.info/problems/ba1g/) | [code](./Chapter%201/HammingDistance.py)
 - [1H. ApproximatePatternCount](https://rosalind.info/problems/ba1h/) | [code](./Chapter%201/FrequentWords.py)
 - [1I. findMostFrequentPatternWithMismatches](https://rosalind.info/problems/ba1i/) | [code](./Chapter%201/FrequentWords.py)
     - [연습문제: Count_d(Text, Pattern)의 구현 및 실행](./Chapter%201/PatternInText.py)
 - [1J. findMostFrequentPatternWithMismatches](https://rosalind.info/problems/ba1j/) | [code](./Chapter%201/FrequentWords.py)
 
 ### 충전소
 - 빈도 배열
    - [1K. ComputingFrequencies](https://rosalind.info/problems/ba1k/) | [code](./Chapter%201/ComputeFreq.py)
    - [FasterFrequentWords](./Chapter%201/FrequentWords.py)
- 패턴과 숫자를 서로 변환하기
    - [1L. PatternToNumber](https://rosalind.info/problems/ba1l/) | [code](./Chapter%201/PatternConversion.py)
    - [1M. NumberToPattern](https://rosalind.info/problems/ba1m/) | [code](./Chapter%201/PatternConversion.py)
- 정렬을 사용해 빈번한 단어 찾기
    - [FindingFrequentWordsBySorting](./Chapter%201/FrequentWords.py)
- 군집 찾기 문제 해결
    - [ClumpFinding](./Chapter%201/FindClumps.py)
    - [BetterClumpFinding](./Chapter%201/FindClumps.py)
- 미스매치를 포함한 자주 나오는 단어 문제 해결
    - [ComputingFrequenciesWithMismatches](./Chapter%201/ComputeFreq.py)
- 문자열 이웃 생성
    - [ImmediateNeighbors](./Chapter%201/Neighbors.py)
    - [1N. Neighbors](https://rosalind.info/problems/ba1n/) | [code](./Chapter%201/Neighbors.py)
    - [IterativeNeighbors](./Chapter%201/Neighbors.py)
- 정렬로 미스매치를 포함한 빈번한 단어 찾기
    - [FindingFrequentWordsWithMismatchesBySorting](./Chapter%201/FrequentWords.py)