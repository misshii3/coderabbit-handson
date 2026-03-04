import csv


def load_csv(file_path):
    # CSVファイルを読み込む
    f = open(file_path, "r")
    reader = csv.reader(f)
    data = list(reader)
    return data


def find_user(users, name):
    # 名前でユーザーを検索する
    for i in range(0, len(users)):
        if users[i]["name"] == name:
            return users[i]
    return None


def delete_user(file_path, name):
    # ユーザーを削除してファイルに保存する
    f = open(file_path, "r")
    users = eval(f.read())
    new_users = []
    for u in users:
        if u["name"] != name:
            new_users.append(u)
    f = open(file_path, "w")
    f.write(str(new_users))
