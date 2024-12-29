todo_items = []
FILEPATH = "../todo_list.txt"

def open_file_func(filepath=FILEPATH):
    with open(filepath, "r+") as file:
        return file.readlines()
# def write_todo(todo_list):
#     with open(FILEPATH, "w") as file:
#         for item in todo_items:
#             file.write(f"{item}\n")
def user_inputs():
    user_input = int(input("Select the options: \n1. Add item \n2. Show items \n3. Complete \n4. Edit \n5. Exit: \n"))
    return user_input


def add_item(user_input):
    with open('../todo_list.txt', '+a') as file:
        file.write(f"{user_input}\n")



def show_items():
    todo_items_local = open_file_func()
    # for i in range(len(todo_items_local)):
        # print(f"{i+1} -> {todo_items_local[i].replace('\n','')}")
    return todo_items_local

def remove_item(item_number):
            todo_list = open_file_func()
            for i in range(len(todo_list)):
                if i + 1 == item_number:
                    todo_list.pop(i)
                    with open(FILEPATH,"w") as file:
                        file.writelines(todo_list)
                    print("Kudos for completion your task!!!")
                    break
                elif i+1 == len(todo_list):
                    print("Please provide the correct number.")

def edit_item(edit_value_number,edit_value):
    content = open_file_func()
    for i in range(len(content)):
        if i + 1 == edit_value_number:

            content[i] = edit_value +"\n"

            with open("../todo_list.txt","w") as file:
                file.writelines(content)
            print(f"item Value Updated successfully!")
        elif i+1 == len(content):
            print("Please, provide correct number for the item you want to update!")
