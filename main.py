import mysql.connector

#database connection
conn=mysql.connector.connect(
       host="localhost",
       user="root",
       password="Avk26",
       database="student_db"
    )
    
cursor=conn.cursor()

def add_student():
    try:
        sid= int(input("Enter Student ID: "))
        name= input("Enter Name: ")
        age= int(input("Enter Age: "))
        course= input("Enter Course: ")
        city= input("Enter City: ")

        query= "INSERT INTO students VALUES (%s, %s, %s, %s, %s)"
        values =(sid, name, age, course, city)

        cursor.execute(query,values)
        conn.commit()

        print("✅ Student added successfully!")

    except Exception as e:
        print("❌ Error:", e)


def view_students():
    cursor.execute("select * from students")
    records=cursor.fetchall()

    if len(records)==0:
        print("No students found")
    else:
        print("\n----- Student List -----")
        for row in records:
            print(row)


def search_student():
    sid=int(input("Enter Student ID to search: "))
    cursor.execute("select * from students where id =%s",(sid,))
    record=cursor.fetchone()
    
    if record:
        print("\nStudent Found:")
        print(f"ID: {record[0]}, Name: {record[1]}, Age: {record[2]}, Course: {record[3]}, City: {record[4]}")
    else:
        print("❌ Student not found")


def update_student():
    sid=int(input("Enter Student ID to update: "))
    cursor.execute("select * from students where id =%s",(sid,))
    record=cursor.fetchone()

    if record is None:
        print("❌ Student not found")
        return
    
    name = input("Enter new Name: ")
    age = int(input("Enter new Age: "))
    course = input("Enter new Course: ")
    city = input("Enter new City: ")

    query = """
    UPDATE students
    SET name=%s, age=%s, course=%s, city=%s
    WHERE id=%s
    """
    values = (name, age, course, city, sid)

    cursor.execute(query, values)
    conn.commit()

    print("✅ Student updated successfully")


def delete_student():
    sid=int(input("Enter Student ID to delete: "))
    cursor.execute("select * from students where id =%s",(sid,))
    record=cursor.fetchone()

    if record is None:
        print("❌ Student not found")
        return

    cursor.execute("DELETE FROM students WHERE id = %s", (sid,))
    conn.commit()

    print("🗑️ Student deleted successfully")  

 
while True:
    print("\n----- Student Management System -----")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice=="1":
        add_student()
    elif choice =="2":
        view_students()
    elif choice =="3":
        search_student() 
    elif choice == "4":
        update_student()
    elif choice == "5":
        delete_student()   
    elif choice=="6":
        print("👋 Exiting program")
        break
    else:
        print("❌ Invalid choice")


         