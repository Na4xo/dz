while True:
    name = input("Введите имя человека: ")
    age = int(input("Введите возраст человека: "))
    people[name] = age
    
    max_age = max(people.values())
    samii_starii = [name for name, age in people.items() if age == max_age]
    print(f"Человек с самым большим возрастом: {samii_starii}")
