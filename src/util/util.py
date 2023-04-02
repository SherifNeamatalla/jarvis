import os


data_path = os.path.join(os.path.dirname(__file__), "..", "..", "data")
save_path = os.path.join(os.path.dirname(__file__), "..", "..", "saved")


def get_data_path(path):
    return os.path.join(data_path, path)


def get_save_path(path):
    return os.path.join(save_path, path)
