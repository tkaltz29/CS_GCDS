import random  # needed to make random passwords
import string  # gives us letters, numbers, and symbols to use
import csv  # allows us to export to excel
import os  # needed to find desktop path


def set_master_password():
    '''Sets a new master password with confirmation.
    Args:     None
    Print:    Status messages during setup.
    Return:   pw (str): The confirmed master password.
    Raises:   None'''
    print("No master password found. Create one to get started.")  # shown on first run
    while True:  # keep asking until the user gives a valid password
        pw, pw2 = input("  New password    : ").strip(), input("  Confirm password: ").strip()  # ask twice to confirm
        if not pw: print("  Can't be empty.")  # don't allow a blank password
        elif pw != pw2: print("  Passwords don't match.")  # both entries must be the same
        else: print("  Password saved!\n"); return pw  # all good, save it and move on


def login(master):
    '''Authenticates the user against the master password (3 attempts).
    Args:     master (str): The master password to validate against.
    Return:   (bool): True if login succeeded, False after 3 failed attempts.
    Raises:   None'''
    for i in range(1, 4):  # give the user 3 tries
        if input(f"Master password ({i}/3): ").strip() == master: return True  # correct, let them in
        print("  Wrong password.")  # wrong, try again
    return False  # used all 3 tries, lock them out


def gen_password(length=16):
    '''Generates a random secure password with guaranteed character variety.
    Args:     length (int): Total length of the password. Defaults to 16.
    Return:   (str): A randomly generated password string.
    Raises:   None'''
    chars = string.ascii_letters + string.digits + string.punctuation  # everything we can use
    pwd = [random.choice(string.ascii_uppercase), random.choice(string.ascii_lowercase),
           random.choice(string.digits), random.choice(string.punctuation)]  # make sure at least one of each type is included
    pwd += [random.choice(chars) for _ in range(length - 4)]  # fill the rest of the password randomly
    random.shuffle(pwd)  # mix it all up so the guaranteed ones aren't always first
    return "".join(pwd)  # turn the list into one string


def check_strength(pw):
    '''Scores a password on length and character variety then prints a rating.
    Args:     pw (str): The password string to evaluate.
    Print:    Score out of 5 and label: Weak / Fair / Strong / Very Strong.
    Raises:   None'''
    score = sum([len(pw) >= 8, len(pw) >= 12, any(c.isupper() for c in pw),
                 any(c.isdigit() for c in pw), any(c in string.punctuation for c in pw)])  # count how many checks it passes
    label = ["Weak", "Weak", "Fair", "Strong", "Very Strong", "Very Strong"][score]  # pick the right word for the score
    tips = [t for cond, t in [(len(pw) < 8, "8+ chars"), (len(pw) < 12, "12+ chars"),
            (not any(c.isupper() for c in pw), "Add uppercase"),
            (not any(c.isdigit() for c in pw), "Add numbers"),
            (not any(c in string.punctuation for c in pw), "Add symbols")] if cond]  # list what the password is missing
    print(f"  Strength: {label} ({score}/5)" + (f"  — tips: {', '.join(tips)}" if tips else ""))  # show the rating and any tips


def add_entry(apps, usernames, passwords):
    '''Prompts for app/username/password and saves the entry.
    Args:     apps (list): List of app/site names.
              usernames (list): List of usernames.
              passwords (list): List of passwords.
    Print:    Confirmation message with app name after saving.
    Raises:   None'''
    print("\n── Add Entry ──")  # section title
    app, user = input("  App / site : ").strip(), input("  Username   : ").strip()  # ask for the app and username
    if input("  Generate password? (y/n): ").strip().lower() == "y":  # let the user choose
        pw = gen_password(); print(f"  Generated: {pw}")  # make a password and show it
    else:
        pw = input("  Password   : ").strip()  # let them type their own
    check_strength(pw)  # show how strong the password is
    apps.append(app); usernames.append(user); passwords.append(pw)  # add everything to the lists
    print(f"  Saved '{app}'.")  # let them know it worked


def view_all(apps, usernames, passwords):
    '''Displays all stored entries in a formatted table.
    Args:     apps (list): List of app/site names.
              usernames (list): List of usernames.
              passwords (list): List of passwords.
    Print:    Table of index, app, username, and password.
    Raises:   None'''
    print("\n── All Entries ──")  # section title
    if not apps: print("  Nothing saved yet."); return  # nothing to show
    w = max(len(a) for a in apps)  # find the longest app name to line up the columns
    print(f"  {'#':<4}{'App':<{w+3}}{'Username':<25}Password")  # column headers
    print("  " + "-" * (w + 54))  # line under the headers
    for i in range(len(apps)):  # go through every saved entry
        print(f"  {i+1:<4}{apps[i]:<{w+3}}{usernames[i]:<25}{passwords[i]}")  # print one row per entry


def lookup(apps, usernames, passwords):
    '''Searches entries by app name and prints the match.
    Args:     apps (list): List of app/site names.
              usernames (list): List of usernames.
              passwords (list): List of passwords.
    Print:    App, username, password, and strength for the match.
    Raises:   None'''
    print("\n── Look Up ──")  # section title
    search = input("  App name: ").strip().lower()  # make lowercase so capitalization doesn't matter
    for i in range(len(apps)):  # go through every saved entry
        if apps[i].lower() == search:  # found a match
            print(f"\n  App: {apps[i]}  |  User: {usernames[i]}  |  Pass: {passwords[i]}")  # show the details
            check_strength(passwords[i]); return  # show strength then stop looking
    print(f"  No entry for '{search}'.")  # nothing matched


def edit_entry(apps, usernames, passwords):
    '''Lets the user update the username or password for an existing entry.
    Args:     apps (list): List of app/site names.
              usernames (list): List of usernames.
              passwords (list): List of passwords.
    Print:    Updated field values; strength if password is changed.
    Raises:   ValueError: If the user types something that isn't a number.'''
    print("\n── Edit Entry ──")  # section title
    if not apps: print("  Nothing to edit."); return  # nothing saved yet
    view_all(apps, usernames, passwords)  # show the list so they can pick a number
    try:
        idx = int(input("\n  Entry # to edit (0 to cancel): ").strip())  # which entry do they want
        if idx == 0 or not (1 <= idx <= len(apps)): print("  Cancelled / invalid."); return  # out of range or cancelled
        i = idx - 1  # lists start at 0, menu starts at 1
        new_user = input(f"  Username [{usernames[i]}]: ").strip()  # show current username, let them change it
        if new_user: usernames[i] = new_user  # only update if they typed something
        if input("  Generate new password? (y/n): ").strip().lower() == "y":  # let them choose
            passwords[i] = gen_password(); print(f"  Generated: {passwords[i]}"); check_strength(passwords[i])  # make a new one and show it
        else:
            new_pw = input("  New password (blank to keep): ").strip()  # let them type one
            if new_pw: passwords[i] = new_pw; check_strength(passwords[i])  # save it if they typed something
        print(f"  '{apps[i]}' updated.")  # done
    except ValueError: print("  Enter a valid number.")  # they typed something that isn't a number


def remove_entry(apps, usernames, passwords):
    '''Lets the user delete a stored entry by its index number.
    Args:     apps (list): List of app/site names.
              usernames (list): List of usernames.
              passwords (list): List of passwords.
    Print:    Confirmation after deletion, or error if index is invalid.
    Raises:   ValueError: If the user types something that isn't a number.'''
    print("\n── Remove Entry ──")  # section title
    if not apps: print("  Nothing to remove."); return  # nothing saved yet
    view_all(apps, usernames, passwords)  # show the list so they can pick a number
    try:
        idx = int(input("\n  Entry # to remove (0 to cancel): ").strip())  # which one to delete
        if idx == 0 or not (1 <= idx <= len(apps)): print("  Cancelled / invalid."); return  # out of range or cancelled
        if input(f"  Delete '{apps[idx-1]}'? (y/n): ").strip().lower() == "y":  # make sure they really want to
            removed = apps.pop(idx-1); usernames.pop(idx-1); passwords.pop(idx-1)  # delete from all three lists
            print(f"  Removed '{removed}'.")  # confirm it's gone
        else: print("  Cancelled.")  # they changed their mind
    except ValueError: print("  Enter a valid number.")  # they typed something that isn't a number


def export_csv(apps, usernames, passwords):
    '''Exports all saved entries to a CSV file that can be opened in Excel.
    Args:     apps (list): List of app/site names.
              usernames (list): List of usernames.
              passwords (list): List of passwords.
    Print:    The full path of the saved file, or an error message.
    Raises:   None'''
    print("\n── Export to CSV ──")  # section title
    if not apps: print("  Nothing to export."); return  # nothing saved yet

    default_path = os.path.join(os.path.expanduser("~"), "Desktop", "passwords.csv")  # default save location
    custom = input(f"  Save path (blank = Desktop): ").strip()  # let them pick a different location
    filepath = custom if custom else default_path  # use their path or the default

    try:
        with open(filepath, "w", newline="", encoding="utf-8") as f:  # open the file for writing
            writer = csv.writer(f)  # create a csv writer
            writer.writerow(["App / Site", "Username", "Password"])  # write the header row
            for row in zip(apps, usernames, passwords):  # go through every saved entry
                writer.writerow(row)  # write one row per entry
        print(f"  Exported {len(apps)} entries to:\n  {filepath}")  # tell them where the file is
        print("  Open it in Excel  ")  # safety reminder
    except Exception as e:
        print(f"  Export failed: {e}")  # something went wrong (e.g. bad path)


def menu():
    '''Prints the main menu to the console.
    Args:     None
    Print:    Numbered menu options.
    Raises:   None'''
    print("\n══════════════════════════\n      PASSWORD KEEPER\n══════════════════════════")  # top of the menu
    for n, opt in enumerate(["Add entry", "View all", "Look up app", "Edit entry",
                              "Remove entry", "Check strength", "Export to CSV", "Exit"], 1):  # go through each option
        print(f"  {n}. {opt}")  # print the number and name
    print("══════════════════════════")  # bottom of the menu


def main():
    '''Entry point — handles setup, login, and the main menu loop.
    Args:     None
    Print:    Status messages; exits on choice 8 or failed login.
    Raises:   None'''
    apps, usernames, passwords = [], [], []  # three lists to store saved entries

    print("Password Keeper\n")  # show the app name
    master = set_master_password()  # set up the master password
    print("Locked. Log in to continue.")  # ask them to log in
    if not login(master): print("Too many attempts. Bye."); return  # too many wrong tries, close the app
    print("\nAccess granted!\n")  # they're in
    actions = {"1": lambda: add_entry(apps, usernames, passwords),
               "2": lambda: view_all(apps, usernames, passwords),
               "3": lambda: lookup(apps, usernames, passwords),
               "4": lambda: edit_entry(apps, usernames, passwords),
               "5": lambda: remove_entry(apps, usernames, passwords),
               "6": lambda: check_strength(input("  Password to check: ").strip()),
               "7": lambda: export_csv(apps, usernames, passwords)}  # connect each menu number to a function
    while True:  # keep showing the menu until they choose to exit
        menu()  # show the options
        choice = input("Option (1-8): ").strip()  # wait for their pick
        if choice == "8": print("\nBye. Stay safe."); break  # they chose exit
        elif choice in actions: actions[choice]()  # run the matching function
        else: print("  Enter 1–8.")  # not a valid option


if __name__ == "__main__":
    main()  # start the app