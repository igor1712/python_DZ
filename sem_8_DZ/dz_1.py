import os
import json
import pickle
import csv

_PATH = os.getcwd()


def serial(path_bytes: bytes):
    path_bytes.decode(encoding="utf=8")
    os.chdir(path_bytes)

    list_name = []
    list_dir = []
    list_path = []
    for dir_path, dir_name, file_name in os.walk(os.getcwd()):
        list_name.append(file_name)
        list_dir.append(dir_name)
        list_path.append(dir_path)
    os.chdir(_PATH)
    with open("test_file.json", "w", encoding="utf-8") as f:
        json.dump([list_name, list_dir], f)

    with open("test_file.pickle", "wb") as pk:
        pickle.dump([list_name, list_dir], pk)

    with open("test_file.csv", "w", newline='') as cs:
        spamwriter = csv.writer(cs)
        spamwriter.writerow([list_name, list_dir])
    return list_dir,  list_name, list_path


if __name__ == '__main__':

    all_lst_dir = serial(b"C:\Users\Admin\PycharmProjects\pythonProjectj\geeekbrains\sem_7")
    lst_name_dir = (list(i for i in all_lst_dir[0] if i))
    lst_path_dir = list(i for i in all_lst_dir[2] if "C:" in i)
    lst_file_name = list(i for i in all_lst_dir[1])
    head_path = lst_path_dir[0].split("\\")[-1]

    for i in lst_file_name:
        for j in i:
            my_dict = {
            "name": j,
            "type": j.split(".")[-1],
            "dir": head_path
            }
            with open("result.json", "a", encoding="utf-8") as r:
                json.dump(my_dict, r)



