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
 #### [서론](#서론)
 #### 본문
 - [1A. 단어 세기](#1a-단어-세기) | [code](./1A.%20PatternCount.py)
 - [1B. 빈번한 단어 문제](#1b-빈번한-단어-문제) | [code](./1B.%20FrequentWords.py)
 - [1C. 역상보 문제](#1c-역상보-문제) | [code](./1C.%20ReverseComplement.py)
 - [1D. 패턴 일치 문제](#1d-패턴-일치-문제) | [code](./1D.%20PatternOccurrence.py)
 - [1E. 군집 찾기 문제](#1e-군집-찾기-문제) | [code](./1E.%20FindClumps.py)
 - [1F. 최소 비대칭 문제](#1f-최소-비대칭-문제) | [code](./1F.%20MinimizeSkew.py)
 - [1G. 해밍 거리 문제](#1g-해밍-거리-문제) | [code](./1G.%20HammingDistance.py)
 - [1H. 대략적인 패턴 일치 문제](#1h-대략적인-패턴-일치-문제) | [code](./1H.%20NäivePatternMatiching.py)
 - [1I. 미스매치가 있는 빈번한 단어 문제](#1i-미스매치가-있는-빈번한-단어-문제) | [code](./1I.%20MostFrequentPseudoPattern.py)
     - [연습문제: Count_d(Text, Pattern)의 구현 및 실행](#연습문제-count_dtext-pattern의-구현-및-실행) | [code](./1I-Ex.%20ApproximatePatternCount.py)
 - [1J. 미스매치와 역상보의 빈번한 단어 문제](#1j-미스매치와-역상보의-빈번한-단어-문제) | [code](./1J.%20MostFrequentPseudoPatternwithComplements.py)

#### 충전소


## 서론
세포에서는 다양한 생물학적 과정을 수행하기 위해, 특정 서열이 반복적으로 나타난다.

### 생물학에서 단백질과 특이성(Specificity)
우리 몸에서 중요한 구성요소이며 다양한 역할을 수행하는 분자로, **단백질**이 있다. 단백질은 정확한 표적에 정확히 작용하기 위해 **특이성(specificity)** 이라는 특징을 가지는데, DNA의 예를 들면 특정 단백질에 대해 이와 특이적으로 결합하는 특정 DNA 서열을 가진다. 

### DNA의 이중 나선 구조와 복제
한편, DNA의 복제(replication)는 생물의 가장 기본적인 구성 단위인 세포가 그 수를 늘리기 위해 필요한 과정인데, 이중 나선으로 이루어진 DNA를 복제하기 위해서는 이를 풀어내는 과정이 필수불가결하다. 

특히, 이번 장에서는 원형의 유전체를 가지는 bacterial genome에 대한 복제를 기준으로 전체적인 흐름이 진행되는데, 원형의 유전체는 이중 나선의 끝과 끝이 닫힌 형태(closed form)이기 때문에 복제가 시작되는 영역이 어디에 위치해 있는지를 아는 것은 중요하며, 이 영역을 **origin of replication**(***ori***)이라 한다.

### DnaA box
앞서 설명한 바와 같이, 유전체는 복제가 시작되기 위해 이중 나선을 풀어주는 과정이 필요하다. 따라서, *ori*라는 영역에는 이중 나선을 풀어주는 단백질이 결합하는 DNA 영역이 존재한다. 이 과정에 관여하는 단백질과 DNA 서열 쌍을 DnaA protein - DnaA box(sequence)라 한다.

<p align="center">
    <img src="https://github.com/mulatta/Bioinforamtics-Algorithm-practice/blob/main/images/Chapter%201/DnaA%20box.png" width="298" height="541">
</p>

정리하자면, 유전체 복제가 시작되는 영역을 찾기 위해서 DnaA box를 찾는 것은 중요하다.

하지만, 유전체에서 이러한 DnaA box를 생물학자들이 직접 실험을 통해 찾는 것은 경제적/시간적으로 큰 비용이 부담되기 때문에 몇가지 조건들을 통해 컴퓨터 과학자들이 이를 찾아내는 것이 효율적이다.

그러므로, 우리는 이번 장에서 DnaA box라는 암호를 찾는 방법에 대해서 논의해본다.

## 1A. 단어 세기
앞서 단백질의 특이성(specificity)에 대해 이야기하였다. 세포 내에서 일어나는 이러한 단백질의 특이성은 마치 단백질에 눈이 달린 것 처럼 작동한다고 생각하기 쉽지만, 단백질의 특이성 또한 결국 물리화학적 법칙을 따르는 분자의 운동에 불과하다.

즉, 단백질 분자가 외부 계의 물리적 힘 - 특히 열 - 에 의해 진동하거나 부유하는 brownian motion을 통해 돌아다니다가, 적절한 DNA 서열과 유효충돌이 일어나야 상호작용이 일어나는 것이다. 

따라서, 우리는 다음과 같은 가설을 세울 수 있다. 
> **1. DnaA box가 많을수록 DnaA protein과의 유효충돌 횟수가 커진다.**

> **2. DnaA box가 많이 존재한다면, 이 서열들 중 일부에 변이가 일어나도 결합을 방해하는 데에 미치는 영향을 줄일 수 있다.**

그러므로, 위 가설에 따르면 문제는 반복되는 특정 서열을 찾는 것으로 귀결된다.
하지만 여전히 우리는 이 *특정 서열* 의 길이가 어느정도인지 알지 못하기 때문에, 임의의 길이를 가지는 특정 서열을 k-mer로 정의한다.

 ***k-mer***: 길이가 k인 문자열

### Problem
- Input: 전체 문자열 Text, Text에서 찾으려는 문자열 Pattern
- Output: Text에서 등장하는 Pattern의 횟수

### Pseudo-code
```
PatternCount(Text, Pattern)
count <- 0
for i <- 0 to |Text| - |Pattern|
    if Text(i, |Pattern|) == Pattern
        count <-- count + 1
return count
```

### [Implementation](./1A.%20PatternCount.py)

## 1B. 빈번한 단어 문제

## 1C. 역상보 문제

## 1D. 패턴 일치 문제

## 1E. 군집 찾기 문제

## 1F. 최소 비대칭 문제

## 1G. 해밍 거리 문제

## 1H. 대략적인 패턴 일치 문제

## 1I. 미스매치가 있는 빈번한 단어 문제

### 연습문제: Count_d(Text, Pattern)의 구현 및 실행

## 1J. 미스매치와 역상보의 빈번한 단어 문제

