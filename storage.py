import build
from pathlib import Path


def write(path, data):
    with open(path, "a") as fout:
        fout.write(str(data)+"\n")

def write_data(store):
    user = build.get_user()
    date = build.build_date()
    path = build.build_path(user, date)
    header = [build.build_first_head()]
    border = "=" * len(header[0])
    space = " \n"
    Path(path).touch()
    write(path, store[0])
    write(path, store[1][0])
    write(path, store[1][1])
    write(path, store[2])
    write(path, "")
    write(path, store[3][0])
    write(path, store[3][1])
    write(path, "")
    write(path, store[4][0])
    store[4].pop(0)
    for item in store[4]:
        write(path, item)
    write(path, "")
    write(path, store[5][0])
    store[5].pop(0)
    for item in store[5]:
        write(path, item)
    write(path, "")
    write(path, store[6][0])
    write(path, store[6][1])
    write(path, store[6][2])
    write(path, store[6][3])
    write(path, store[6][4])
    print(store[7])



