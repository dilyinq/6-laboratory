students = { "Дима": ["English", "German"], "Лена": ["French", "English"],
    "Саша": ["Japan", "Chinese"], "Кристина": ["Chinese", "German"]}

all_languages = set() #множество
for student, languages in students.items():
    all_languages.update(languages)
sorted_languages = sorted(all_languages)

chinese_speakers = []
for student, languages in students.items():
    if "Chinese" in languages:
        chinese_speakers.append(student)

print("Языки, которые знают студенты:", sorted_languages)
print("Студенты, знающие китайский язык:", chinese_speakers)
