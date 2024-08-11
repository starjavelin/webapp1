import streamlit as st
import functions

todos = functions.get_todos()


def add_todo():
    to_do = st.session_state["new_todo"] + '\n'
    todos.append(to_do)
    functions.write_todos(todos)


st.title("New Todo App")
st.subheader("Increase Productivity")
st.write("Use this to track your daily items to do:")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.rerun()

st.text_input(label='', placeholder="Add a new todo",
              on_change=add_todo, key="new_todo")
