import os


def walk(dirname):
    names = []
    for name in os.listdir(dirname):
        path = os.path.join(dirname, name)
        if os.path.isfile(path):
            names.append({path, name})
        else:
            names.extend(walk(path))
    return names


def check_file(list_dir):
    list_duplicate = dict()
    for key, value in list_dir:
        if value in list_duplicate:
            list_duplicate[value].append(key)
        else:
            list_duplicate[value] = [key]
    return list_duplicate


cws = os.getcwd()
list_dir = walk(cws)
list_res = check_file(list_dir)
for item in list_res:
    print(item, list_res[item])
