countries_capitals = { "Россия": "Москва", "Япония": "Токио", "Германия": "Берлин",
    "Великобритания": "Лондон, округ Колумбия", "Китай": "Пекин"}

print("Пары ключ-значение в словаре:")
for country, capital in countries_capitals.items():
    print(country, "-", capital)

country = "Япония"
print(f"Столица страны '{country}': {countries_capitals.get(country)}")

sorted_countries = sorted(countries_capitals.keys())
print("\nСодержимое словаря, отсортированное по названию стран:")
for country in sorted_countries:
    print(country, "-", countries_capitals[country])