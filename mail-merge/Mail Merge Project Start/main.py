with open("./Input/Names/invited_names.txt", "r") as name_file:
    for name in name_file.readlines():
        with open("./Input/Letters/starting_letter.txt", "r") as letter:
            letter_content = letter.read().replace("[name]", name.strip())
            letter_title = f"invitation_for_{name.strip()}"
            save_path = f"./Output/ReadyToSend/{letter_title}.txt"
            with open(save_path, "w") as output:
                output.write(letter_content)
