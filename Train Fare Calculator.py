age = int(input())
distance = int(input())

fare = distance * 5

if age < 12:
    fare = fare * 0.5
elif age <= 59:
    fare = fare
else:
    fare = fare * 0.75

if fare == int(fare):
    print(int(fare))
else:
    print(fare)
