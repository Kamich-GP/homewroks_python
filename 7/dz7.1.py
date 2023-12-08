import sqlite3

def database():
    conn = sqlite3.connect("mydatabase.db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE students4(id INTEGER PRIMARY KEY,name TEXT,age INTEGER,grade TEXT)")
    conn.commit()
    conn.close()

def insert_students():
    conn = sqlite3.connect("mydatabase.db")
    cursor = conn.cursor()
    students = [("Sasha", 15, "A"),("Oleg", 16, "B"),("Ahmed", 15, "C")]
    cursor.executemany("INSERT INTO students4(name, age, grade) VALUES (?, ?, ?)", students)
    conn.commit()
    conn.close()

def get_student_by_name(name):
    conn = sqlite3.connect("mydatabase.db")
    cursor = conn.cursor()
    cursor.execute("SELECT name, age, grade FROM students4 WHERE name=?", (name,))
    result = cursor.fetchone()
    conn.close()
    return result

def update_student_grade(name, new_grade):
    conn = sqlite3.connect("mydatabase.db")
    cursor = conn.cursor()
    cursor.execute("UPDATE students4 SET grade=? WHERE name=?", (new_grade, name))
    conn.commit()
    conn.close()

def delete_student(name):
    conn = sqlite3.connect("mydatabase.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM students4 WHERE name=?", (name,))
    conn.commit()
    conn.close()

database()

insert_students()

student_info = get_student_by_name("Sasha")
print(student_info)

update_student_grade("Oleg", "B+")

delete_student("Ahmed")
