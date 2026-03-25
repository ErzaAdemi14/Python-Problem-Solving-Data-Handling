users = [
    {"id": 1, "name": "John", "salary": 500},
    {"id": 2, "name": "", "salary": 300},
    {"id": 3, "name": "Anna", "salary": -100},
    {"id": None, "name": "Mike", "salary": 400}
]

invalid_records = []

for user in users:
    issues = []

    if user["id"] is None:
        issues.append("id must not be None")

    if user["name"] == "":
        issues.append("name must not be empty")

    if user["salary"] <= 0:
        issues.append("salary must be positive")

    if issues:
        invalid_records.append({
            "record": user,
            "issues": issues
        })

for record in invalid_records:
    print("Record:", record["record"])
    print("Issues:", record["issues"])
    print()