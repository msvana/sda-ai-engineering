employee = {
    "id": 145,
    "name": "Anna Nováková",
    "age": 31,
    "workplace": "Ostrava",
    # "position": "Accountant",
}

# position = employee.get("position", "unknown")
# position = employee["position"]
# print(position)

# print("position" in employee)

# del employee["workplace"]
# print(employee)

# for k in employee.keys():
#    print(k)

# for v in employee.values():
#    print(v)

for k, v in employee.items():
    print(k, v)