"""
Read knight data into dictionary and provide utility functions.
"""
from pprint import pprint

def main():
    info = read_data()
    print_titles_and_names(info)
    print(get_field(info, 'Robin', 'color'))
    pretty_print(info)

def read_data():
    """
    Read data from knights.txt into a dictionary for further processing

    :return: Dict of knight info
    """
    data = {}

    with open("DATA/knights.txt") as knights_in:
        for line in knights_in:
            (name, title, color, quest, comment) = line.rstrip('\n\r').split(":")
            data[name] = {
                'title': title,
                'color': color,
                'quest': quest,
                'comment': comment,
            }
    return data

def print_titles_and_names(knight_info):
    """
    Print just the titles and names of all the knights.

    :param knight_info: Dict of knight info
    :return: None
    """
    for name, info in knight_info.items():
        print("{} {}".format(info['title'], name))

def get_field(knight_info, knight, field):
    return knight_info[knight][field]

def pretty_print(knight_info):
    pprint(knight_info)
    print()

print("MY NAME IS:", __name__)

if __name__ == '__main__':  # if I am a script, not a module
    # some testing code here...
    main()
