import math


def vecMultiply(vec1, vec2):
    result = []
    result.append(vec1[1] * vec2[2] - vec1[2] * vec2[1])
    result.append(vec1[2] * vec2[0] - vec1[0] * vec2[2])
    result.append(vec1[0] * vec2[1] - vec1[1] * vec2[0])

    return result


def angle(a, b):
    scalar = 0

    for i in range(len(a)):
        scalar += a[i] * b[i]

    distanceA = 0
    distanceB = 0

    for i in range(len(a)):
        distanceA = distanceA + (a[i] * a[i])
    distanceA = math.sqrt(distanceA)

    for i in range(len(b)):
        distanceB = distanceB + (b[i] * b[i])
    distanceB = math.sqrt(distanceB)

    result = scalar / (distanceA * distanceB)
    result = (math.acos(result) * 180) / math.pi

    return result


with open("input.txt") as f:
    v = list(map(float, f.readline().split()))
    v.append(float(0))
    a = list(map(float, f.readline().split()))
    a.append(float(0))
    m = list(map(float, f.readline().split()))
    m.append(float(1))
    w = list(map(float, f.readline().split()))
    w.append(float(0))

globalResult = open("output.txt", "w")

enemyPos = []
standartPos = [0, 0, 1]
for i in range(len(w)):
    enemyPos.append(w[i] - v[i])

rGunPosition = vecMultiply(a, standartPos)
lGunPosition = vecMultiply(standartPos, a)

Angle = angle(standartPos, m)
rightAngle = angle(rGunPosition, enemyPos)
leftAngle = angle(lGunPosition, enemyPos)

if leftAngle > 60 and rightAngle > 60 or Angle > 60:
    print("0\nBye", file=globalResult)
    exit()

temp = vecMultiply(a, standartPos)

if leftAngle > 60:
    print("-1", file=globalResult)

    if angle(m, temp) < 90:
        Angle *= -1

    if angle(a, enemyPos) > 90:
        rightAngle *= -1

    rightAngle = float("{:.2f}".format(rightAngle))
    print(float(rightAngle), file=globalResult)
else:
    print("1", file=globalResult)

    if angle(m, temp) > 90:
        Angle *= -1

    if angle(a, enemyPos) > 90:
        leftAngle *= -1

    leftAngle = float("{:.2f}".format(leftAngle))
    print(float(leftAngle), file=globalResult)
print(float(Angle), file=globalResult)
print("Bye", file=globalResult)
