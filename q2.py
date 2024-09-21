# start
world_record = 6.23
good_score: int = 0
sum_score: int = 0
record_breaker = None
for _ in range(7):
    while True:
        score: float = float(input("Enter your score: "))
        if score < 5.8:
            continue
        if 5.8 <= score < 6.23:
            good_score += 1
            sum_score += score
        if score > 6.23:
            name: str = str(input("The name of the jumper is: "))
            score: float = float(input("Enter your score: "))
            good_score += 1
            sum_score = score
else:
    score: float = float(input("Enter your score: "))

avg: float =  sum_score / good_score
print(f"The good scores are: {good_score} , {avg}")
print(f"The best scores is: {sum_score} ")
print(f"The winner with the best score is: {} ")





