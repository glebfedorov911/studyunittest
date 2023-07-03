def split_string(string: str) -> list:
    if type(string) not in (str,):
        raise TypeError("Not string")
    return string.split(' ')


splt = ['1 2 3', 1, 2, 3, 's', 'asdasdasd', True, False, [['12, 3, 4']], 12341224]

for s in splt:
    try:
        print(f"{s}, {split_string(s)}")
    except:
        continue