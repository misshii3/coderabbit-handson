import json


def read_users(file_path):
    # ファイルからユーザーデータを読み込む
    # f = open(file_path, "r")
    # data = json.load(f)
    """
    Read and parse JSON user data from the given file path.
    
    Parameters:
        file_path (str): Path to the JSON file containing user data.
    
    Returns:
        users: Parsed JSON data (typically a list or dict) representing the users.
    """
    with open(file_path, "r") as f:
        data = json.load(f)
    return data


def calculate_average_age(users):
    # ユーザーの平均年齢を計算する
    """
    Compute the average of the "age" field for a list of user objects.
    
    Parameters:
        users (list[dict]): Iterable of user objects where each object contains a numeric "age" key.
    
    Returns:
        float: The average age.
    
    Notes:
        Assumes `users` is non-empty and each user provides a numeric "age".
    """
    total = 0
    for user in users:
        total += user["age"]
    average = total / len(users)
    return average


def save_users(file_path, users):
    # ユーザーデータをファイルに保存する
    """
    Write the provided users data as JSON to the file at file_path, overwriting any existing contents.
    
    Parameters:
        file_path (str): Path to the target file.
        users (Any): JSON-serializable object representing the users to save.
    """
    f = open(file_path, "w")
    json.dump(users, f)