ch = input()

if ch.islower() and ch.isalpha():
    print(ch.upper())
elif ch.isupper() and ch.isalpha():
    print(ch.lower())
else:
    print("abcd theriyatha?")
