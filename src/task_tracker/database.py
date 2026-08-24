import sqlite3


def add_task(title):

    connection = sqlite3.connect("task.db")

    connection.execute( """
        INSERT INTO tasks (title) VALUES (?)
    """,
      (title,)
      
    )
    connection.commit()
    connection.close()

def update_task(id,title):
    connection = sqlite3.connect("task.db")
    connection.execute("UPDATE tasks SET title = ? WHERE id = ?",
                       (title, id)
    )
    connection.commit()
    connection.close()

def get_task(id):
    connection = sqlite3.connect("task.db")

    cursor = connection.execute("SELECT * FROM tasks WHERE id = ?",
                       (id,)
    )
    task = cursor.fetchone()
    # connection.commit() | No DB write duh 
    connection.close()
    return task

def get_all_tasks():
    connection = sqlite3.connect("task.db")

    cursor = connection.execute("SELECT * FROM tasks")
    tasks = cursor.fetchall()
    # connection.commit() | No DB write duh 
    connection.close()
    # Wait but this shit just READS the db then fuck all
    # we need to return the tasks
    return tasks


def delete_task(id):
    connection = sqlite3.connect("task.db")

    connection.execute("DELETE FROM tasks WHERE id = ?",
                       (id,)
    )
    connection.commit()
    connection.close()