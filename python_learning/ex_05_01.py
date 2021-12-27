
count = 0
tot = 0.0

while True:
    user = input("input a value:")
    if user == "done":
        break
    try:
        user = float(user)
    except:
        print("invalid input")
        continue
    print(user)
    count = count + 1
    tot = tot + user



print("All done!")
print(count, tot, tot / count)