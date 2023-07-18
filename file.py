def StringChallenge(str):
    for i in range(len(str)):
        digit = int(str[i])
        remaining_length = len(str) - i
        if remaining_length < digit:
            continue
        substring = str[i:i+digit]
        if substring == str[i] * digit:
            return "true"
    return "false"

input_str ="564244342544443"
result = StringChallenge(input_str)
print(result)
print("Aditya")
