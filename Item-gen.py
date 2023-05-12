import random

file_name = "items-generated_name.txt"
name1replace = [
    "Absolute",
    "Bright",
    "Chaotic",
    "Exquisite",
    "Feral",
    "Focused",
    "Glorious",
    "Honed",
    "Howling",
    "Immaculate",
    "Massive",
    "Mithril",
    "Platinum",
    "Prime",
    "Refined",
    "Shimmering",
    "Silver",
    "Stout",
    "Superior",
    "Supreme",
]


with (
    open("list1.txt", "r", encoding="utf-8") as file1,
    open("list2.txt", "r", encoding="utf-8") as file2,
    open("list3.txt", "r", encoding="utf-8") as file3,
    open("list4.txt", "r", encoding="utf-8") as file4,
    open("list5.txt", "r", encoding="utf-8") as file5,
    open(file_name, "r+", encoding="utf-8") as generated_names_file,
):
    list1 = file1.read().splitlines()
    list2 = file2.read().splitlines()
    list3 = file3.read().splitlines()
    list4 = file4.read().splitlines()
    list5 = file5.read().splitlines()
    generated_names = generated_names_file.read().splitlines()

    name1 = random.choice(list1)
    name2 = random.choice(list2)
    name3 = random.choice(list3)
    name4 = random.choice(list4)
    name5 = random.choice(list5)

    if "Active" in name2:
        name1 = random.choice(name1replace)
    if "Bloodeagle" in name2:
        name1replace.remove("Focused")
        name1replace.append("Partial")
        name1 = random.choice(name1replace)
    if "Bludgeoner" in name2:
        name1replace.append("Adept")
        name1replace.append("Aesir")
        name1replace.append("Ancient")
        name1replace.append("Bold")
        name1replace.append("Ceremonial")
        name1replace.append("Fine")
        name1replace.append("Grand")
        name1replace.append("Great")
        name1replace.append("Illustrious")
        name1replace.append("Legendary")
        name1replace.append("Majestic")
        name1replace.append("Master")
        name1replace.append("Neophyte")
        name1replace.append("Sanguinary")
        name1replace.append("Splendid")
        name1replace.append("Strong")
        name1replace.append("Valiant")
        name1replace.append("Willful")
        name1replace.remove("Exquisite")
        name1replace.remove("Focused")
        name1replace.remove("Glorious")
        name1replace.remove("Immaculate")
        name1replace.remove("Mithril")
        name1replace.remove("Platinum")
        name1replace.remove("Prime")
        name1replace.remove("Silver")
        name1replace.remove("Stout")
        name1 = random.choice(name1replace)

    name = name1 + " " + name2 + " " + name3 + " " + name4 + " " + name5

    while name in generated_names:
        name = (
            random.choice(list1)
            + " "
            + random.choice(list2)
            + " "
            + random.choice(list3)
            + " "
            + random.choice(list4)
            + " "
            + random.choice(list5)
        )

    generated_names_file.seek(0)
    generated_names_file.truncate()
    generated_names_file.write(name + "\n")

print("\033[H\033[J")
print(name)
