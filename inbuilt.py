from typing import TypedDict

class User(TypedDict):
    name: str
    age: int
    department: str
    salary: int

users: list[User] = [
    {"name": "Alice", "age": 28, "department": "Engineering", "salary": 85000},
    {"name": "Ravi", "age": 35, "department": "Marketing", "salary": 72000},
    {"name": "Mina", "age": 30, "department": "Sales", "salary": 68000},
    {"name": "Janel", "age": 42, "department": "Finance", "salary": 94000},
    {"name": "Kai", "age": 24, "department": "Design", "salary": 61000},
]


users_under_30 = [
    u["name"] for u in users if u["age"] < 30
]
print(users_under_30)

salary_by_title = {
    job["department"]: job["salary"]
    for job in users
}

print(f"salary_by_title : {salary_by_title}")

# user: User =   {"name": "Alice", "age": 28, "department": "Engineering", "salary": 85000}

# stock = user.get("stock")

# print(f"stock is {stock}");

age_sum = sum([u["age"] for u in users])

print(f"sum of age for all the users is {age_sum}")

names = (", ").join([ u["name"] for u in users])

print(f"user names are {names}")


for i, user in enumerate(users):
    print(f"{i}, {user}")