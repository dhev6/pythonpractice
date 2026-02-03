def main():
    students = []
    num_students = 10
    subjects = ["Maths", "Physics", "Computer", "Chemistry", "English"]

    print(f"-----Enter details for {num_students} students------")

    for i in range(num_students):
        name = input(f"\n[{i+1}]Enter student name: ")
        total_mark = 0

        print(f"enter marks for {name} (0-100 per subject)")
        for subject in subjects:
            while True:
                try:
                    score = float(input(f" > {subject}: "))
                    if 0 <= score <= 100:
                        total_mark += score 
                        break
                    print("Please enter a score between 0 and 100.")
                except ValueError:
                    print("Invalid input. Please enter a numerical score.")

        students.append({
            "name": name,
            "total": total_mark
        })

    ranked_students = sorted(students, key=lambda x: x['total'], reverse=True)

    print("\n" + "="*45)
    print(f"{'Rank':<6} {'Name':<20} {'Total Mark':<10} {'Average':<8}")
    print("-" * 45)

    for rank, student in enumerate(ranked_students, start=1):
        average = student['total'] / len(subjects)
        print(f"{rank:<6} {student['name']:<20} {student['total']:<10.2f} {average:<8.2f}")

main()