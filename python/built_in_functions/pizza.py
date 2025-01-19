def string_repeat(number, pizza_name):
    return pizza_name * number

better_name = string_repeat(3, "Picante")
print(better_name) # PicantePicantePicante

def no_space(pizze_name):
    return "".join(pizze_name.split(" "))
    # return pizze_name.replace(" ", "")

name_no_spaces = no_space("Super Cool Pizza!")
print(name_no_spaces) # SuperCoolPizza!

def number_to_string(number):
    return str(number)

number_as_text = number_to_string(145)
print(number_as_text) # "145"
print(type(number_as_text)) # str

def boolean_to_string(bool_value):
    if bool_value:
        return "1"
    return "0"

bool_as_string = boolean_to_string(True)
print(bool_as_string)
print(type(bool_as_string))

def abbrev_name(pizza_name):
    #first, second = pizza_name.split()
    # return f"{first[0]}.{second[0]}"
    split = pizza_name.split(" ")
    first_letters = []
    for i in split:
        first_letters.append(i[0].upper())
    return '.'.join(first_letters)

pizza_abbr = abbrev_name("Cool Mega Pizza")
print(pizza_abbr) # C.P

def name_lenght(pizza_name):
    if not isinstance(pizza_name, str):
        return

    words = pizza_name.split()
    return [f"{word} {len(word)}" for word in words]

pizza_name_length = name_lenght("Cool Mega Pizza")
print(pizza_name_length) # ["Cool 4", "Mega 4", "Pizza 5"]


def remove_orders(orders):
    numbers = orders.split(",")
    numbers = numbers[1:-1]
    return ",".join(numbers)

orders_removed = remove_orders("1,2,3,4,5")
print(orders_removed) # "2,3,4"

def food_menu(menu):
    menu_numbered = []
    for num, f in enumerate(menu, 1):
        menu_numbered.append(str(num) + ". " + f)
    return menu_numbered   

menu = food_menu(["Cool Pizza", "Diablo Pizza", "Vegan Pizza"])
print(menu) # ["1. Cool Pizza", "2. Diablo Pizza", "3. Vegan Pizza"]

