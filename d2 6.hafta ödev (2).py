students = []

while True:
    name = input("İsim (çıkış: q): ").strip()
    if name.lower() == "q":
        break

    if not name:
        continue

    raw = input("Not (0-100): ").strip()
    if not raw.isdigit():
        continue

    grade = int(raw)
    if not (0 <= grade <= 100):
        continue

    students.append((name, grade))



if not students:
    print("Hiç öğrenci girilmedi.")
else:
    
    students_sorted = sorted(students, key=lambda x: x[0].lower())

    print("\nİsme göre sıralı liste:")
    for s in students_sorted:
        print(s[0], "-", s[1])

    
    highest = max(students, key=lambda x: x[1])
    lowest = min(students, key=lambda x: x[1])

    print("\nEn yüksek not:", highest[0], "-", highest[1])
    print("En düşük not:", lowest[0], "-", lowest[1])

    
    toplam = sum(s[1] for s in students)
    ortalama = toplam / len(students)

    print("Ortalama:", round(ortalama, 2))
