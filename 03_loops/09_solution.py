fruits = [
    "Apple",
    "Banana",
    "Mango",
    "Orange",
    
    "Grapes",
    "Banana",
    "Pineapple",
    "Mango",
    "Papaya",
    
    "Watermelon",
    "Strawberry",
    "Guava",
    "Mango",
]

unique_item = set()

for fruit in fruits:
    if fruit in unique_item:
        print("Duplicate item found" , fruit)
        break
    unique_item.add(fruit)
print(unique_item)