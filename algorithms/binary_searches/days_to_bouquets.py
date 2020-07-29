def daysToBouquets(bloomDay: [int], m: int, k: int) -> int:
    if (len(bloomDay) < m*k):
        return -1
    if(not m or not k):
        return 1
    if(not bloomDay):
        return -1
    bloomDaySorted = sorted(bloomDay)
    possibleDays = bloomDaySorted[m*k-1:]
    midPoint = 0
    while(len(possibleDays) > 1):
        posDaysLen = len(possibleDays)
        if(posDaysLen == 2):
            edgeCase = willBloom(possibleDays[0], bloomDay, m, k)
            return possibleDays[0] if edgeCase else possibleDays[1]
        midPoint = posDaysLen//2
        if (willBloom(possibleDays[midPoint], bloomDay, m, k)):
            possibleDays = possibleDays[:midPoint+1]
        else:
            possibleDays = possibleDays[midPoint:]
    return possibleDays[midPoint]


def willBloom(day, bloomDay, m, k):
    flowerRun = 0
    bouquets = 0
    for flower in bloomDay:
        if flower <= day:
            flowerRun += 1
            if flowerRun == k:
                flowerRun = 0
                bouquets += 1
                if bouquets == m:
                    return True
        else:
            flowerRun = 0
    return False
