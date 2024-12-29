import streamlit as st
import todofunctions as func
import os

if not os.path.exists("../todo_list.txt"):
    with open("../todo_list.txt","w"):
        pass



st.title("My To-do App")
st.subheader("Your to do tasks:\n Click on the checkbox button once you complete.")
todo_list = func.show_items()

def add_todo():
    new_todo = st.session_state["new_todo"]
    print(new_todo)
    if new_todo:
        func.add_item(new_todo)
        todo_list.append(new_todo)
        st.session_state["new_todo"] = ""

def remove(task_local):
    del st.session_state[task_local]


for item_number, task in enumerate(todo_list):
    task_key = task+str(item_number)
    checkbox = st.checkbox(task, key=task_key)
    # print(item_number+1, task)
    if checkbox:
        print("deletion---",st.session_state[task_key],task_key)
        del st.session_state[task_key]
        todo_list.pop(item_number)
        func.remove_item(item_number+1)
        st.rerun()

st.text_input(label="Enter your new task:", placeholder="Add your new task here",
              key="new_todo", on_change=add_todo)
print(list(st.session_state.items()))