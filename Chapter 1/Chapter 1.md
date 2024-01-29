# Chapter 1. DNA 복제는 유전체의 어디서부터 시작되는가?
## 개요
이 장에서는 유전체의 복제 과정이 시작되는 *ori* (Origin of Replication)을 찾는 방법을 통해 간단한(단순화된) 경우에서의 DNA motif를 찾는 연습울 수행한다.

이러한 단순한 경우로서 *ori* 를 찾기 위한 다음의 몇가지 단서들을 이용해 유전체에서 해당 조건을 만족하는 motif 서열(책에서는 pattern, k-mer)을 탐색하였다.

1. 유전체에서 얼마나 **자주** 등장하는가?
2. 자주 등장한다면, 그 pattern의 **reverse complement 등장 횟수**도 높은 빈도로 등장하는가?
3. 유전체의 **일정 영역에서 빈도수**가 높은가?(즉, 밀도있게 등장하는가?; localization)
4. G-C ratio(%)의 비율이 **비대칭적**인 부분인가?
5. **유사한 문자열**의 등장 빈도는 어떠한가?

## 목차
 #### 본문
 - [1A. 단어 세기](./1A.%20PatternCount.ipynb)
 - [1B. 빈번한 단어 문제](./1B.%20FrequentWords.ipynb)
 - [1C. 역상보 문제](./1C.%20ReverseComplement.ipynb)
 - [1D. 패턴 일치 문제](./1D.%20PatternOccurrence.ipynb)
 - [1E. 군집 찾기 문제](./1E.%20FindClumps.ipynb)
 - [1F. 최소 비대칭 문제](./1F.%20MinimizeSkew.ipynb)
 - [1G. 해밍 거리 문제](./1G.%20HammingDistance.ipynb)
 - [1I. 대략적인 패턴 일치 문제](./1H.%20NäivePatternMatiching.ipynb)
     - [연습문제: Count_d(Text, Pattern)의 구현 및 실행](./1I-Ex.%20ApproximatePatternCount.ipynb)
 - [1J. 미스매치와 역상보의 빈번한 단어 문제](./1J.%20MostFrequentPseudoPatternwithComplements.ipynb)

#### 충전소

## Introduction to find *ori* 
 ### 복제기점이란?
 - 세포는 그 수를 늘리기 위해 유전물질과 일부 세포 소기관을 복제하여 하나의 세포에서 2개의 딸세포로 분열하는 [[세포 분열]] 과정을 거침
 - 유전체의 [[Replication|복제]]는 세포 분열 과정에서 2개의 딸세포로 나뉘기 전에 유전체를 복제하는 과정을 의미함
 - 이러한 복제는 단순히 Copy-Paste의 과정이 아니라, 일련의 mechanism과 과정을 거침
 - 유전체 복제의 시작은 복제 기점, Origin of Replication(*ori*)으로부터 시작됨
 - 복제는 DNA polymerase라는 효소에 의해 진행됨

 ### 복제 기점 찾기 문제
 - Input: DNA 문자열 유전체
 - Output: 유전체의 *ori* 위치
 
    → 위 문제는 생물학자, 컴퓨터 과학자에 따라 다른 답을 내놓음

 - **생물학자**
    - 주어진 DNA sequence 중 *ori*를 찾기 위해 일부 서열을 삭제해가면서 복제 여부를 확인
	- 복제가 멈추게 되는 지점을 확인하여 찾을 수 있다.
 - **컴퓨터 과학자**
	- 주어진 문제의 조건만으로는 "해결할 수 없다"는 답을 내어 놓음
	- 즉, 더 많은 조건들을 추가하여야 함

 #### Computational approach의 중요성
 1. 실험적 접근보다 훨씬 빠르다.
 2. 실험 결과는 계산적 분석을 통해 해석되어야 한다.
 - 특히, *ori* 예측과 같은 경우, 실험적 접근으로만 수행될 경우 많은 시간이 소요됨

 ## The Hidden Message Of *ori*
 ### The Hidden Message Of Dna A box
 - Dna A box: *ori* 내에 존재하는 짧은 유전자(DNA) 서열로, Dna A 라는 단백질이 결합하는 부위
 - Dna A: 유전체 복제가 시작될 때, Dna A box에 결합하는 단백질

 ---
 - 이러한 특징을 가지는 서열을 찾기 위한 다음과 같은 규칙들을 생각해 볼 수 있음(즉, 패턴 찾기)
 1. 서열 내에서 등장하는 빈도
 2. 비대칭성(일종의 anomaly)
 ### 단어 세기
 - 다양한 생물학적 과정을 수행하기 위해, 특정 서열이 반복적으로 나타남
 - 특정 단백질의 경우, 이와 특이적으로 결합하는 DNA 서열을 가짐
    - 이러한 DNA 서열이 많이 등장할수록 결합 확률이 높아짐
	- 또한 변이가 일어나도 결합을 방해하는데에 미치는 영향을 줄일 수 있음
 - **k-mer**: 길이가 k인 문자열
 ---
 ```c
 Text(i, k) := i-th k-mer in the Text
 PatternCount(Text, Pattern):
	input: Text, Pattern
	output: the number of occurence of k-mer in the Text

	count <- 0;
	for i <- 0 to |Text|-|Pattern|
	if Text(i, |Pattern|) == Pattern 
		count <- count + 1
	return count
 ```
 ---
 1. 주어진 문자열 Text의 모든 문자열을 각각 시작점으로 삼는다
 2. 각 시작 문자열로부터 Pattern의 길이만큼의 k-mer가 Pattern과 동일한지 확인한다
 3. 즉, 각 시작 문자열이 pattern을 형성한다면 pattern의 수를 세는 변수 count를 1 증가시킨다.

### 빈번한 단어 문제