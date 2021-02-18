def hi_name(name="shubham"):
    return "Hi " + name


print(hi_name("Shubham"))  # Hi Shubham
print(hi_name())  # Hi shubham


def pig_latin(word):
    if word[0] in "aeiouAEIOU":
        word = word + "ay"
    else:
        word = word[1:] + word[0] + "ay"
    return word


print(pig_latin("apple"))  # appleay
print(pig_latin("word"))  # ordway
print(pig_latin("Apple"))  # Appleay
print(pig_latin("Word"))  # ordWay


def max_quantity(fruits_quantity):
    fruit = ""
    quantity = 0;

    for f, q in fruits_quantity:
        if q > quantity:
            fruit = f;
            quantity = q;

    return (fruit, quantity)


print(max_quantity([("apple", 4), ("mango", 5), ("orange", 2)]))  # ('mango', 5)
fruit, quantity = max_quantity([("apple", 4), ("mango", 5), ("orange", 2)])
print(f"{fruit} - {quantity}")  # mango - 5
