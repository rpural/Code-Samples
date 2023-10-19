import random

def check_password(test):
    if not hasattr(check_password, 'uppers'):
        check_password.uppers = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        check_password.lowers = "abcdefghijklmnopqrstuvwxyz"
        check_password.digits = "0123456789"
        check_password.symbols = "!=+-?#%@&^$_"

    types = dict()

    if len(test) < 8:
        return "Failed"

    for c in test:
        if c in check_password.uppers:
            types["uppers"] = types.get("uppers", 0) + 1
        elif c in check_password.lowers:
            types["lowers"] = types.get("uppers", 0) + 1
        elif c in check_password.digits:
            types["digits"] = types.get("digits", 0) + 1
        elif c in check_password.symbols:
            types["symbols"] = types.get("symbols", 0) + 1
        else:
            return "Invalid"
    if len(types) >= 3 and (8 <= len(test) <= 10):
        return "Average"
    if len(types) == 4 and len(test) > 10:
        return "Passed"
    return "Failed"

def check_passwords():
    counts = {"checked": 0,
              "Passed": 0,
              "Average": 0,
              "Failed": 0,
              "Invalid": 0, }

    filename = input("Filename to check (Users-Pswds.txt): ").strip()
    if not filename:
        filename = "Users-Pswds.txt"
    with open(filename, "r") as pswds, open("Users-Pswds-Checked.txt", "w") as out:
        for record in pswds:
            record = record.strip()
            if record:
                user, *pswd = record.split(",")
                pswd = ",".join(pswd)
                print(f"{user} - {pswd}")
                strength = check_password(pswd)
                print(f"{user},{pswd},{strength}", file=out)
                counts["checked"] += 1
                counts[strength] += 1
    print(f'Processed {counts["checked"]}, {counts["Passed"]} passed, {counts["Average"]} average, {counts["Failed"]} failed')
    if counts["Invalid"] > 0:
        print(f'{counts["Invalid"]} invalid passwords found')
        print("\nOutput can be found in Users-Pswds-Checked.txt")
    return True

def generate_password():
    if not hasattr(generate_password, 'selection'):
        generate_password.selection = [ "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
                                        "abcdefghijklmnopqrstuvwxyz"
                                        "0123456789"
                                        "!=+-?#%@&^$_" ]

    length = random.randrange(11, 21)
    pswd = [random.choice(s) for s in generate_password.selection]
    for _ in range(2, length):
        pswd.append(random.choice(random.choice(generate_password.selection)))
    random.shuffle(pswd)
    return "".join(pswd)

def gen_pswds():
    created = 0
    while True:
        user = input("Username: ")
        record = f"{user},{generate_password()}"
        print(record)
        answer = input("Save record? (Y or N): ")
        if answer.lower() == "y":
            with open("Users-Pswds.txt", "a") as out:
                print(record, file=out)
            created += 1
        answer = input("Create another? (Y or N): ")
        if answer.lower() == "n":
            break
    print(f"Created {created} new users")
    return True

def quit_program():
    return False
    

if __name__ == "__main__":
    print("""PwdChk.py v1.0

Menu:
  1 - Check passwords in Users-Pswds.txt
  2 - Generate a compliant password
  3 - exit

""")

running = True

options = { "1": check_passwords,
            "2": gen_pswds,
            "3": quit_program, }

while running:
    option = input("--> ")
    if option in options:
        running = options[option]()
    else:
        print(f"Invalid option '{option}; Valid options are 1, 2, or 3.")

print("\nThis program is courtesy of Bob Nix")
