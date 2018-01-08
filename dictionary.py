def ninja_intro(dictionary):
    for key, val in dictionary.items():
        print(f"I am {key} and I am a {val} belt")

ninja_belts = {
    "crystal": "red",
    "ryu": "black"
}

"yoshi" in ninja_belts

keys = list(ninja_belts.keys())
vals = list(ninja_belts.values())

print(vals.count("black"))

ninja_belts["yoshi"] = "red"

# Alternate Method to construct dict
person = dict(name="shaun", age=27, height="6ft")

# True is capitalized
while True:
    ninja_name = input("Enter a ninja name: ")
    ninja_belt = input("Enter a belt color: ")
    ninja_belts[ninja_name] = ninja_belt

    another = input("Add another? (y/n)")

    if another != "y":
        break

ninja_intro(ninja_belts)