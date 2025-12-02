import csv

CSV_FILE = "/home/glalu/python_step/project/users.csv"



def init_csv():
    #CSV ფაილის შემოწმება თუ არსეობს თუ არა შექიმნება
    try:
        with open(CSV_FILE, "r", encoding="utf-8") as f:
            pass
    except FileNotFoundError:
        with open(CSV_FILE, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["name", "password", "id", "balance"])



def get_next_id():
    #CSV ფაილში ბოლო ID ის ამოღება, თუ ცარიელია მაშინ აიდი იქნება 1
    try:
        with open(CSV_FILE, "r", encoding="utf-8") as f:
            reader = csv.reader(f)
            next(reader)
            ids = [int(row[2]) for row in reader if row]
            return max(ids) + 1 if ids else 1
    except:
        return 1


def read_all_users():
    #CSV ფაილიდან მომხმარებლების დაბეჭდვა
    users = []
    with open(CSV_FILE, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        next(reader)
        for row in reader:
            if row:
                users.append(row)
    return users



def add_user():
    #მომხმარებლის დამატება CSV ფაილში
    name = input("შეიყვანე სახელი: ")
    password = input("შეიყვანე პაროლი: ")
    user_id = get_next_id()
    balance = input("შეიყვანე ბალანსი: ")

    with open(CSV_FILE, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([name, password, user_id, balance])

    print(f"მომხმარებელი დაემატა! მინიჭებული ID: {user_id}\n")


def delete_user():
    #მომხმარებლის წაშლა CSV ფაილიდან
    delete_name = input("რომელი მომხმარებელი წაიშალოს? შეიყვანე სახელი: ")

    rows = []
    found = False

    with open(CSV_FILE, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        for row in reader:
            if row and row[0] == delete_name:
                found = True
                continue
            rows.append(row)

    if found:
        with open(CSV_FILE, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerows(rows)
        print("მომხმარებელი წაიშალა!\n")
    else:
        print("ასეთი მომხმარებელი ვერ მოიძებნა.\n")


def list_users():

    print("\n--- იუზერების სია ---")
    for row in read_all_users():
        print(f"სახელი: {row[0]}, პაროლი: {row[1]}, ID: {row[2]}, ბალანსი: {row[3]}₾")
    print()


def add_balance_admin():
    username = input("ვის დაემატოს ბალანსი? შეიყვანე სახელი: ")
    amount = float(input("რამდენის დამატება გინდა? "))

    rows = []
    found = False

    with open(CSV_FILE, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        for row in reader:
            if row and row[0] == username:
                row[3] = str(float(row[3]) + amount)
                found = True
            rows.append(row)

    if found:
        with open(CSV_FILE, "w", newline="", encoding="utf-8") as f:
            csv.writer(f).writerows(rows)
        print("ბალანსი დაემატა წარმატებით!\n")
    else:
        print("ასეთი მომხმარებელი არ არსებობს.\n")


def admin_panel():
    admin_password = input("ჩაწერე ადმინის პაროლი: ")
    if admin_password == "12345":
        while True:
            print("\n--- ADMIN PANEL ---")
            print("1. მომხმარებლის დამატება")
            print("2. მომხმარებლის წაშლა")
            print("3. იუზერების ნახვა")
            print("4. ბალანსის დამატება მომხმარებელზე")
            print("5. გამოსვლა")

            choice = input("აირჩიე: ")

            if choice == "1":
                add_user()
            elif choice == "2":
                delete_user()
            elif choice == "3":
                list_users()
            elif choice == "4":
                add_balance_admin()
            elif choice == "5":
                break
            else:
                print("არასწორი არჩევანი!")
    else:
        print("არასწორი ადმინის პაროლი")


def find_user(name, password):
    with open(CSV_FILE, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        next(reader)
        for row in reader:
            if row[0] == name and row[1] == password:
                return row
    return None


def update_balance(name, new_balance):
    rows = []
    with open(CSV_FILE, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        for row in reader:
            if row and row[0] == name:
                row[3] = str(new_balance)
            rows.append(row)

    with open(CSV_FILE, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerows(rows)


def user_panel():
    name = input("შეიყვანე სახელი: ")
    password = input("შეიყვანე პაროლი: ")

    user = find_user(name, password)

    #print("---------------------------",user[3])


    if not user:
        print("მონაცემები არასწორია!\n")
        return

    print(f"\nმოგესალმები, {name}!")
    balance = float(user[3])
    print(f"შენი ბალანსი: {balance} ₾")

    choice = input("გინდა ბალანსის გამოტანა? (y/n): ")

    if choice.lower() == "y":
        amount = float(input("რამდენის გამოტანა გსურს? (გამოტანის საკომისიოა 10%) "))
        perc = amount/10
        sakomisio = 2


        if (amount+perc+sakomisio) > balance:
            if(amount == balance):
                print("ოპერაცია გაუქმებულია. გაითვალისწინეთ გატანის(10%) და მომსახურების(2₾) ხარჯები!")
            else :
                print("არასაკმარისი ბალანსი")
        else:
            print("გასატანი თანხა: ",amount)
            print("პროცენტი: ",perc)
            #balance -= (amount - perc)
            balance = balance - amount - perc - sakomisio
            print("მომსახურების საკომისიო : ",sakomisio)
            update_balance(name, balance)
            print(f"ოპერაცია წარმატებულია. ახალი ბალანსი: {balance} ₾")
            
    else:
        print("ოპერაცია გაუქმებულია.")



def main():
    init_csv()
    
    mode = input("მოგესალმებათ მევახშე ბანკი!\nადმინი თუ მომხმარებელი? (admin/user): ")

    if mode.lower() == "admin":
        admin_panel()
    elif mode.lower() == "user":
        user_panel()
    else:
        print("არასწორი არჩევანი.")


if __name__ == "__main__":
    main()
