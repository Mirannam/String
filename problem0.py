a = "Strings in python are surrounded by either single quotation marks, or double quotation marks."
l = len(a) + 1
part_1 = a[0:l//2].lower()
part_2 = a[l//2:].upper()
print(part_1 + part_2)