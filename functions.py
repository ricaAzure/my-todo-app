# ******************* FILE PATH ***********************************

FILEPATH = r"todos.txt"

# ******************* functions ***********************************
def get_todos(filepath_local=FILEPATH):
    """Read the text file and return the lis of to-do items."""
    with open(filepath_local, 'r') as file:
        todos_local = file.readlines()
    return todos_local


def write_todos(todos_arg, filepath_local1=FILEPATH):
    """Write the to-do list of items in the text file."""
    with open(filepath_local1, "w") as file:
        file.writelines(todos_arg)



if __name__=="__main__":
    print("Hello from functions")
    print(get_todos())