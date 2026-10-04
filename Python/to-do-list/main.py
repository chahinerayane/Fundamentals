import sqlite3
from utils.utils import (cmd_cleaner, logo, database_err, resume, todo_not_exists)

def choice() :
    choices = {
        1 : "SHOW ALL",
        2 : "ADD",
        3 : "MARK AS COMPLETED",
        4 : "DELETE",
        5 : "EXIT",
    }


    cmd_cleaner(0)
    print(logo("TO DO LIST"))

    while True :


        for choice_key, choice_value in choices.items():
            print(f"  {choice_key} => {choice_value}")

        try :
            entered_choice = int(input("\n      => : "))
            if entered_choice in choices:
                return entered_choice
            else :
                print("Choice are unvailable.")
                resume(1.1)
        except ValueError:
            print("Invalid number.")
            resume(1.1)



def connect_to_db() :
    try :
        db = sqlite3.connect("to_do_list.db")
        db.execute("CREATE TABLE if not exists users(user_id INT, user_name TEXT)")
        db.execute("CREATE TABLE if not exists todo(user_id INT, name TEXT, status BOOL)")
        return db
    except sqlite3.Error as err:
        print(f"Database error : {err}")

def disconnect(db , cr):
    commit_close_db(db, cr)

def add(db, cr, status = False) : 

    user_id = 1

    to_do_name = input("enter the to do name : ")
    
    

    if todo_not_exists(cr, to_do_name):
        try :
            cr.execute("INSERT INTO todo values(?, ? , ?)", (user_id, to_do_name, status))
            db.commit()
            print("Added successfully!")
            

        except sqlite3.Error as err:
            database_err(err)
        finally:
            resume(1.1)

    else:
        print("Name already exists")
        resume(1.2)


def show_all(db, cr):
    user_id = 1

    try :
        results = cr.execute("SELECT * FROM todo WHERE user_id = ? order by status asc", (user_id,))
        
        result = results.fetchall()
    
        print(f"you have {len(result)} results !")

        if result :
            print("#" * 80)
            print(" Showing Skills With Progress : ".center(80, "#"))
            print("#" * 80)
        
        for todo in result:
            if todo[2] :
                print("\n", f"  => {todo[1]} : Completed 🟩")
            else :
                print("\n", f"  => {todo[1]} : In progress ⌛")



    except sqlite3.Error as err:
        database_err(err)
    finally :
        resume(1.2)


def complete(db, cr):

    user_id = 1
    to_do_name = input("Enter task name : ")
    if todo_not_exists(cr, to_do_name):
        print("Name not found")
        resume(1.1)
    else :
        try :
            cr.execute("UPDATE todo set status = ? where name = ? and user_id = ?", (True, to_do_name, user_id))
            db.commit()
            print("Task completed!")
            resume(1.1)
        except sqlite3.Error as err:
            database_err(err)
            resume(1.1)


def delete(db, cr):
    user_id = 1

    to_do_name = input("Enter the todo name : ")

    
    if todo_not_exists(cr, to_do_name):
        print("Name not found")
        resume(1.1)
    else :
        try :
            cr.execute("DELETE FROM todo WHERE name = ? and user_id = ?", (to_do_name, user_id))
            db.commit()
            print("Deleted successfully")

        except sqlite3.Error as err:
            database_err(err)
        finally:
            resume(1.1)
        



def commit_close_db(db, cr) :

    db.commit()

    cr.close()

    db.close()



db = connect_to_db()
cr = db.cursor()



def program():

    while True:  
        
        actions = {
            1 : show_all,
            2 : add,
            3 : complete,
            4 : delete,
            5 : disconnect
        }


        entered_choice = choice()

        actions[entered_choice](db,cr)

        if entered_choice == 5:
            break



if __name__ == "__main__": 
    program()