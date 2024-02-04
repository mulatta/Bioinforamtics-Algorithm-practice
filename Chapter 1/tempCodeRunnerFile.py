# clump로 기록된 인덱스를 pattern으로 바꿈
    for j in range(len(freqArr)):
        if isClump[j] == 1:
            clumpPattern.add(NumberToPattern(j, k))