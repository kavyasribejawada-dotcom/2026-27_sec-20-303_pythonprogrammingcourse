students = {"student1": {"name": "Kavya","marks": 90},
            "student2": {"name": "Ravi","marks": 85 },
            "student3": {"name": "Sita", "marks": 95 } }

for key, value in students.items():
    print("Name:", value["name"])
    print("Marks:", value["marks"])