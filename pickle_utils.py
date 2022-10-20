import pickle
import os

def write_pickle(path, obj):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "wb") as f:
        pickle.dump(obj, f)
        
def read_pickle(path):
    if not os.path.isfile(path):
        print(f"path did not exist: {path}")
        return None
    with open(path, "rb") as f:
        obj = pickle.load(f)
    return obj