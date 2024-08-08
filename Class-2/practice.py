text = "hehehe"
print(text[::3])
first = "Abdul"
last = "Moiz"
age = 19
fulname = first + "" + last
intro = "I am "+str(age)+" Year old"
print(fulname)
print(intro)
lough = text*5 + "!"
print(lough)
lough2 = text.replace("hehehe", "Hello")


emoji = ["he", "he", "he", "he"]

concatenate_join = " ".join(emoji)
print(concatenate_join)

print(lough2)

itemlist = [1, 2, 3, 4, "HELLO", 5000]
itemlist[3] = 50
print(itemlist)

items = {
    'name': "Abdul Moiz",
    'age': 19,
    'city': "Lahore",
}
print(items["name"])
