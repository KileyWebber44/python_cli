from models.items import Item
import csv

next_id = 0
items = []
# Make a menu print out showing options
def menu():
    print("""
1. List All Items
2. Add New Item
3. Update Existing Item
4. Delete Item (By item id)
5. Exit
""")

# List all Items
def list_items():
    with open("inventory.csv", "r") as file:
        csv_reader = csv.DictReader(file, ["id", "name", "condition"])
        for row in csv_reader:
            message = f"ID: { row['id'] }\tName: { row['name'] }\tCondition: { row['condition'] }"
            print(message)

# Add New Item
def new_item():
    with open("inventory.csv", "r+") as file:
        current_items= list(csv.DictReader(file))
        try:
            last_id = int(current_items[-1]["id"])
        except IndexError:
            last_id = -1

    with open("inventory.csv", "a+") as file:
        name = input("Name: >")
        condition = input("Condition: >")
        item = {
            "id" : last_id + 1,
            "name": name,
            "condition": condition
        }
        writer = csv.DictWriter(file, ["id", "name", "condition"])
        if last_id == -1:
            writer.writeheader()
        writer.writerow(item)

    # global next_id
    # name = input("Name: ")
    # cond = input("Condition: ")
    # item_id = next_id
    # next_id += 1

# Update Existing Item
def update_existing():
    if not items:
        print("You have no items to update")
        return
    list_items()
    try:
        item_id_to_update = int(input("What is the item id?\n>"))
    except Exception:
        print("This is not a valid number")
        return
    found_item = False
    for item in items:
        if item.item_id == item_id_to_update:
            name = input("Name: ")
            cond = input("Condition: ")
            item.name = name
            item.condition = cond
            break
        else:
            print("We didn't find a match")

# Delete Item (By item id)
def delete_item(itemId):
    if not items:
        print("You have no items to delete")
        return
    list_items()
    try:
        item_id_to_delete = int(input("What is the item you wish to delete?\n>"))
    except Exception:
        print("This is not a valid number")
        return

    for index, item in enumerate(items):
        if item.item_id == item_id_to_delete:
            index_to_reomve = index
            break
        else:
            print("We didn't find a match")
            return
    print(f"Found:\n{items.pop(index_to_remove)} it has been removed")

# Make the menu questions that grab the data 
def main():
    open("inventory.csv", "a+").close
    while True:
        menu()
        choice = input("> ")

        if choice == "1":
            list_items()
        elif choice == "2":
            new_item()
        elif choice == "3":
            update_existing()
        elif choice == "4":
            delete_item()
        elif choice == "5": # Exit
            exit()
        else:
            input("Invalid Input!\n(Press Enter to try again)")


# TODO Make the File Saving stuff

main()

