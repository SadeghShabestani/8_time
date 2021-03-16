hour = float(input("Enter Hour: "))
minute = float(input("Enter Minute: "))
second = float(input("Enter Second: "))
print(f"{hour} : {minute} : {second}")


result_hour = hour * 3600
result_minute = minute * 60

result = result_hour + result_minute + second

print(f"Seconds: {result}")

