import random

# set a variable for a file that holds the current and, up until running the script again, previous generated name
file_name = "items-generated_name.txt"

# open the files that contain the parts of the item names required to generate Too Human style names along with the previously generated name file
with (
    open("list1.txt", "r", encoding="utf-8") as file1,
    open("list2.txt", "r", encoding="utf-8") as file2,
    open("list3.txt", "r", encoding="utf-8") as file3,
    open("list4.txt", "r", encoding="utf-8") as file4,
    open("list5.txt", "r", encoding="utf-8") as file5,
    open(file_name, "r+", encoding="utf-8") as generated_names_file,
):
    # read em up and split em up
    list1 = file1.read().splitlines()
    list2 = file2.read().splitlines()
    list3 = file3.read().splitlines()
    list4 = file4.read().splitlines()
    list5 = file5.read().splitlines()
    generated_names = generated_names_file.read().splitlines()

    # generate a name from each part at random
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

    # check if the name has been generated before and if so generate a new one
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
    # clear the contents of the generated name file and write the new name to it
    generated_names_file.seek(0)
    generated_names_file.truncate()
    generated_names_file.write(name + "\n")
# clear the screen and print the name
print("\033[H\033[J")
print(name)
