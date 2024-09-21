# start
positive_count: int = 0
negative_count: int = 0
zero_count: int = 0
divided_by_7 : int = 0
last_positive: int = None
last_negative: int = None

for _ in range(10):

    num: int = int(input("Enter number: "))
    if num == -999:
        break
    if num > 1000 or num < -1000:
        continue

    if num == 0:
        zero_count += 1
    elif num > 0:
        positive_count += 1
        last_positive = num
    elif num < 0:
        negative_count += 1
        last_negative = num
    if num % 7 == 0:
        divided_by_7 += 1

if last_positive is None and last_negative is None:
    print("Statistics not available")
else:
    print("Statistics: ")
    print(f"positive numbers : {positive_count}")
    print(f"negative numbers : {negative_count}")
    print(f"zero numbers : {zero_count}")
    print(f"divided by 7 numbers : {divided_by_7}")
    print(f"Last positive number: {last_positive}")
    print(f"Last negative number: {last_negative}")
