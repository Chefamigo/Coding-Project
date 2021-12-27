smallest = None
x = [3, 41, 12, 9, 74, 15]

for low in x:
    if smallest is None or low < smallest:
        smallest = low
    print(smallest)
print("Done and smallest is:", smallest) 
