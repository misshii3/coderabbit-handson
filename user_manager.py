import json


def read_users(file_path):
    # ファイルからユーザーデータを読み込む
    # f = open(file_path, "r")
    # data = json.load(f)
    with open(file_path, "r") as f:
        data = json.load(f)
    return data


def calculate_average_age(users):
    # ユーザーの平均年齢を計算する
    total = 0
    for user in users:
        total += user["age"]
    average = total / len(users)
    return average


def save_users(file_path, users):
    # ユーザーデータをファイルに保存する
    f = open(file_path, "w")
    json.dump(users, f)