small = int(input())
medium  = int(input())
large  = int(input())

happiness_score = int(1 * small + 2 * medium + 3 * large)
if happiness_score >= 10:
    print("happy")
else:
    print("sad")