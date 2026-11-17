def export(path, item_count):
    print("Exporting...")
    file = open(path, "a")
    for i in range(item_count):
        item_id = input("Enter Item Id: ")
        item_name = input("Enter Item Name: ")
        item_colour = input("Enter Item Colour: ")
        file.write(f"\n{item_id},{item_name},{item_colour}")
    print("Done")


export("exported_items.csv",int(input("Enter the amount of items to export: ")))

