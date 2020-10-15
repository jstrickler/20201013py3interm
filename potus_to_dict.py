from pprint import pprint

# 1:Washington:George:1732-02-22:1799-12-14:Westmoreland County:Virginia:1789-04-30:1797-03-04:no party


fields = "lastname firstname dob dod bplace state tookoffice leftoffice party".split()

data = { int(line.split(':')[0]):dict(zip(fields,line.rstrip().split(':')[1:])) for line in open("DATA/presidents.txt")}

pprint(data)

print(data[26]["party"])  # Teddy
print(data[10]["party"])  # John Tyler
print('-' * 60)
data = {}
with open("DATA/presidents.txt") as pres_in:
    for line in pres_in:
        values = line.rstrip().split(':')
        term = int(values[0])
        pres_info = dict(zip(fields, values[1:]))
        data[term] = pres_info

pprint(data)

