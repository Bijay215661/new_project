name = ["Bijay", "Sagai", "Sandesh", "Anil"]

def print_lol(fname):
    for each_item in fname:
        if isinstance(each_item, list):
            print_lol(each_item)

        else:
            print(each_item)    
print_lol(name)