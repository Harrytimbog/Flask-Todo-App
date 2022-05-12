from app import db, Todo

# first_todo = Todo(todo_text = "Learn Flask")
# db.session.add(first_todo)
# db.session.commit()

all_todos = Todo.query.all()
print(all_todos)
# print(all_todos[0].todo_text)

### Other Methods to seed database Model

# second_to = Todo(todo_text = "Setup venev")  
#  db.session.add(second_to) 

# db.session.add(Todo(todo_text="Build Cool app"))  
# db.session.commit()
# Todo.query.all()  