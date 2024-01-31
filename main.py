with open("./Input/Letters/starting_letter.txt") as letter:
    lines = letter.readlines()

with open("./Input/Names/invited.txt") as inv:
    names = inv.readlines()

for n in names:
    new = lines[0].replace('[name]', n.strip())
    msg = [f"{new}"]
    with open(f"./Output/ReadyToSend/letter_for_{n.lower().strip().replace(' ', '')}.txt", 'w') as nw:
        for li in lines[1:]:
            msg.append(li)
        nw.writelines(msg)
