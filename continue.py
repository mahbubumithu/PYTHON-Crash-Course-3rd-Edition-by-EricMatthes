# continue - example

print("\nThe continue instruction:")
for i in range(1, 6):
    print(i)
    if i == 3:
        
        continue
    print("Inside the loop.", i)
print("Outside the loop.")