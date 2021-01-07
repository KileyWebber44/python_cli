class Item:
    def __init__(self, item_id, name, condition):
        self.item_id = item_id
        self.name = name
        self.condition = condition

    def __str__(self):
        return f"Id:{self.item_id}\tName:{self.name}\tCondition:{self.condition}"



if __name__ == "__main__":
    item_one = Item(0, "book", "used")
    item_two = Item(1, "water bottle", "new")

    print(item_one)
    print(item_two)

    