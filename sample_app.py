def calculate_average(numbers):
    total = sum(numbers)
    return total / len(numbers)


def get_user_role(user):
    return user["role"]


numbers = [10, 20, 30, 40]

print("Average:", calculate_average(numbers))
print("User role:", get_user_role({"name": "Alex"}))