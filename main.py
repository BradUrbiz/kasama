# ─────────────────────────────────────────────────────────────
# SDE Store Inventory
#
# This file grows across SDE lessons 11–13 and is polished in L14.
#   L11  OOP Intro + Product class  — define Product (name, price,
#                                     quantity) with __init__ + __str__
#   L12  Store CRUD basics          — add / list / update / remove
#                                     products in an inventory dict
#   L13  Error handling + features  — try/except, validation,
#                                     low-stock alerts, etc.
#   L14  Polish & Stretch           — new fields, sorting, search,
#                                     total value, file save/load
#
# Save often — your work persists between lessons.
# ─────────────────────────────────────────────────────────────

import random
import json
import os

class Product:
    # TODO (L11): define __init__ with name, price, quantity
    def __init__(self, product_type, price, total):
      self.product_type = product_type
      self.price = price
      self.total = total
      self.prod_Id = random.randint(1000, 5000)

    def features(self):
      return {
        "id": self.prod_Id,
        "product_type": self.product_type,
        "price": self.price,
        "total": self.total
      }

def display_inventory(inventory):
  for prod_id, product in inventory.items():
    for key, value in product.features().items():
      if key == "total" and value < 3:
        print(f"{key}: {value} ### LOW STOCK")
      else:
        print(f"{key}: {value}")


def display_menu():
  print("""
1. View Inventory
2. Add Product
3. Remove Product
4. Exit
  """)

def add_new_product(inventory):
  product_type = (input("Classification: "))
  try:
    price = float(input("Price: "))
  except ValueError:
    print("Please only numerical inputs.")
    price = 0.0
  try:
    total = int(input("Quantity: "))
  except ValueError:
    print("Defaulting to 1")
    total = 1
    
  new_product = Product(product_type, price, total)
  inventory[new_product.prod_Id] = new_product
  print(f"Added {product_type} with id {new_product.prod_Id}.")



def remove_product(inventory):
  display_inventory(inventory)
  try:
    target = int(input("Which ID to remove?: "))
  except ValueError:
    print("Invalid ID.")
    return
  if target in inventory:
    del inventory[target]
    print(f"Removed {target}.")
  else:
    print("ID not found.")

def save_inventory(inventory):
  snapshot = []
  for prod_Id, product in inventory.items():
    snapshot.append(product.features())
  with open("store.json", "w") as file:
    json.dump(snapshot, file, indent=2)

def load_inventory():
  try:
    with open("store.json") as file:
      loaded = json.load(file)
  except FileNotFoundError:
    return {}

  inventory = {}
  for item in loaded:
    product = Product(item["product_type"], item["price"], item["total"])
    product.prod_Id = item["id"]
    inventory[product.prod_Id] = product
  return inventory



def user_selection():
  display_menu()
  user = int(input("Selection #?: "))
  if user == 1:
    print("Now viewing inventory")
    display_inventory(inventory)
  elif user == 2:
    print("Add a product")
    add_new_product(inventory)
  elif user == 3:
    print("Remove a product")
    remove_product(inventory)
  elif user == 4:
    print("Program terminating")
    save_inventory(inventory)
    return False
  else:
    print("Only values 1-4 are accepted")
  return True






inventory = load_inventory()
if not inventory:
  raspberry_pi = Product("Raspberry Pi", 15.00, 2)
  web_cam = Product("USB Webcam w/ Microphone", 10, 7)

  inventory = {
    raspberry_pi.prod_Id: raspberry_pi,
    web_cam.prod_Id: web_cam
  }

user_selection()

 


# TODO (L12): add functions to add, list, update, and remove products.
print("Store inventory ready.")


    


# game loop
program_loop = True
while program_loop:
  program_loop = user_selection()

