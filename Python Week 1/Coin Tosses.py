def coinToss(times):
    import random

    attempt_count = 1
    tails = 0
    heads = 0
    result = ""

    for i in range(1, times + 1):
        x = random.randint(0,1)
        if x == 1:
            heads +=1
            result = "head"
            print "Attempt #", attempt_count, ": Throwing a coin... It's a ", result, "! Got ", heads, "head(s) so far and", tails, "tail(s) so far"
        else:
            tails +=1
            result = "tail"
            print "Attempt #", attempt_count, ": Throwing a coin... It's a ", result, "! Got ", heads, "head(s) so far and", tails, "tail(s) so far"
        attempt_count += 1

print coinToss(5000)