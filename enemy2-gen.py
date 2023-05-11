import random

# set a variable for a file that holds the current and, up until running the script again, previous generated name
file_name = "undead2-generated_name.txt"

# open the files that contain the parts of the undead2 monster names names required to generate Too Human style names along with the previously generated name file
with (
    open("undead2-enemy-part1.txt", "r", encoding="utf-8") as file1,
    open("undead2-enemy-part2.txt", "r", encoding="utf-8") as file2,
    open("undead2-enemy-part3.txt", "r", encoding="utf-8") as file3,
    open(file_name, "r+", encoding="utf-8") as generated_names_file,
):
    # read em up and split em up
    list1 = file1.read().splitlines()
    list2 = file2.read().splitlines()
    list3 = file3.read().splitlines()
    generated_names = generated_names_file.read().splitlines()

    # generate a name from each part at random
    name = (
        random.choice(list1)
        + " "
        + random.choice(list2)
        + " "
        + random.choice(list3)
    )

    # check if the name has been generated before and if so generate a new one
    while name in generated_names:
        name = (
            random.choice(list1)
            + " "
            + random.choice(list2)
            + " "
            + random.choice(list3)
        )
    # clear the contents of the generated name file and write the new name to it
    generated_names_file.seek(0)  # Move the file pointer to the beginning
    generated_names_file.truncate()  # Clear the contents of the file
    generated_names_file.write(name + "\n")
# clear the screen and print the name
print("\033[H\033[J")
print(name)
