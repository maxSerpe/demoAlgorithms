# TODO make optional whether argurments are positional or keyword
def threeSumClosest(nums, target) -> int:
    # brute force would be n^3, make every combo of 3 and take the best
    # we can copy previous problem...
    # pos1 starts right and moves left
    # pos2 starts 1 to the right of pos1
    # pos3 starts left
    # if total is too high, pos3 moves left
    # if too low, pos2 moves right
    # optimizations present...break out if you hit the target
    # learned we don't need to bounds check p1 if p2 is checked against p3
    # watch out for pos2/pos3 pointer move comparison, we messed that up by
    #   comparing difference between target and temp to 0 instead of just the
    #   difference between target and temp
    nums.sort()
    numsLen = len(nums)
    diff = float('inf')
    for x in range(numsLen):
        pos1 = x
        pos2 = pos1 + 1
        pos3 = numsLen - 1
        while(pos2 < pos3):
            # print([pos1, pos2, pos3])
            tempAns = nums[pos1] + nums[pos2] + nums[pos3]
            if (tempAns == target):
                return tempAns
            if (abs(target - tempAns) < abs(diff)):
                diff = target - tempAns
            if (target > tempAns):
                pos2 += 1
            else:
                pos3 -= 1
    return target - diff
