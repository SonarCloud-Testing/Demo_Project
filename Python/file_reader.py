def read_file(file_path):
    with open(file_path, "r") as f:
        return f.read()

def write_file(file_path, data):
    with open(file_path, "w") as f:
        f.write(data)

def append_file(file_path, data):
    open(file_path, "a").write(data)  
