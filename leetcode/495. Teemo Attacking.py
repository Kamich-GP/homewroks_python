# Our hero Teemo is attacking an enemy Ashe with poison attacks! When Teemo attacks Ashe,
# Ashe gets poisoned for a exactly duration seconds. More formally, an attack at second t will mean
# Ashe is poisoned during the inclusive time interval [t, t + duration - 1]. If Teemo attacks again before
# the poison effect ends, the timer for it is reset, and the poison effect will end duration seconds after the new attack.
# You are given a non-decreasing integer array timeSeries, where timeSeries[i] denotes that Teemo attacks
# Ashe at second timeSeries[i], and an integer duration.
# Return the total number of seconds that Ashe is poisoned.
def findPoisonedDuration(timeSeries, duration):
    potential = (len(timeSeries)) * duration
    for a in timeSeries:
        for b in timeSeries:
            if timeSeries.index(a) != timeSeries.index(b):
                c = timeSeries.index(b) - 1
                if timeSeries.index(a) == c and timeSeries.index(b) != -1:
                    if b - a < duration:
                        potential -= duration - (b - a)
    return potential
print(findPoisonedDuration([1,4], 2))
print(findPoisonedDuration([1,2], 2))
# тут такая же беда со временем, не знаю как ускорять код, но проверку проходит