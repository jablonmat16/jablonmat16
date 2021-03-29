import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="root",
  database="universityLibrary"
)

mycursor = mydb.cursor()

mycursor.execute("DROP TABLE IF EXISTS renting")
mycursor.execute("DROP TABLE IF EXISTS book")
mycursor.execute("DROP TABLE IF EXISTS author_phone")
mycursor.execute("DROP TABLE IF EXISTS author")
mycursor.execute("DROP TABLE IF EXISTS publisher_phone")
mycursor.execute("DROP TABLE IF EXISTS publisher")
mycursor.execute("DROP TABLE IF EXISTS payment")
mycursor.execute("DROP TABLE IF EXISTS student_acc")
mycursor.execute("DROP TABLE IF EXISTS student")


mycursor.execute("CREATE TABLE author (author_id INT PRIMARY KEY, author_name VARCHAR(30), Bdate VARCHAR(10))")
mycursor.execute("CREATE TABLE author_phone (author_id INT, phone_number VARCHAR(12), FOREIGN KEY(author_id) REFERENCES author(author_id))")
mycursor.execute("CREATE TABLE publisher (publisher_name VARCHAR(30) PRIMARY KEY, street VARCHAR(20), city VARCHAR(20), state VARCHAR(2), zip NUMERIC(5,0))")
mycursor.execute("CREATE TABLE publisher_phone (publisher_name VARCHAR(30), publisher_phone VARCHAR(12), FOREIGN KEY(publisher_name) REFERENCES publisher(publisher_name))")
mycursor.execute("CREATE TABLE book (title VARCHAR(50), author_id INT, type VARCHAR(20), book_no NUMERIC(10,0) PRIMARY KEY, publisher_name VARCHAR(30), availability VARCHAR(20), FOREIGN KEY(author_id) REFERENCES author(author_id) on delete set null, FOREIGN KEY(publisher_name) REFERENCES publisher(publisher_name) on delete set null)")
mycursor.execute("CREATE TABLE student (id INT PRIMARY KEY, name VARCHAR(30), department VARCHAR(20))")
mycursor.execute("CREATE TABLE student_acc(id INT, account_id INT UNIQUE, amount_due INT, PRIMARY KEY(id, account_id), FOREIGN KEY(id) REFERENCES student(id))")
mycursor.execute("CREATE TABLE payment (account_id INT, payment_no VARCHAR(10), payment_date VARCHAR(10), payment_amount INT, PRIMARY KEY(account_id, payment_no), FOREIGN KEY(account_id) REFERENCES student_acc(account_id))")
mycursor.execute("CREATE TABLE renting (id INT, book_no NUMERIC(10,0), PRIMARY KEY(id,book_no),FOREIGN KEY(id) REFERENCES student(id), FOREIGN KEY(book_no) REFERENCES book(book_no))")

mycursor.execute("INSERT INTO author VALUES (37952543, 'Marty Jablon', '11-02-2000')")
mycursor.execute("INSERT INTO author VALUES (75487876, 'John Smith', '04-20-1978')")
mycursor.execute("INSERT INTO author VALUES (12358087, 'Mary Jane', '08-13-1956')")
mycursor.execute("INSERT INTO author VALUES (65896345, 'Maxwell Davis', '06-04-1996')")
mycursor.execute("INSERT INTO author VALUES (18653975, 'Jacob Davis', '03-28-1986')")
mycursor.execute("INSERT INTO author VALUES (75489998, 'Griffin Thorpe', '05-26-1999')")
mycursor.execute("INSERT INTO author VALUES (08796456, 'Christopher Lagzdins', '09-30-1975')")
mycursor.execute("INSERT INTO author VALUES (46938230, 'Thomas Hermance', '04-26-1990')")
mycursor.execute("INSERT INTO author VALUES (11112222, 'Luke Tancredi', '10-12-1989')")
mycursor.execute("INSERT INTO author VALUES (22224444, 'Alice Gorden', '02-25-1996')")
mycursor.execute("INSERT INTO author VALUES (65478765, 'Jennifer Hewit', '06-08-1970')")

mycursor.execute("INSERT INTO author_phone VALUES (37952543, '364-296-3956')")
mycursor.execute("INSERT INTO author_phone VALUES (37952543, '364-135-8456')")
mycursor.execute("INSERT INTO author_phone VALUES (75487876, '865-437-3575')")
mycursor.execute("INSERT INTO author_phone VALUES (75487876, '124-536-1238')")
mycursor.execute("INSERT INTO author_phone VALUES (12358087, '879-478-2647')")
mycursor.execute("INSERT INTO author_phone VALUES (65896345, '737-276-1595')")
mycursor.execute("INSERT INTO author_phone VALUES (65896345, '737-964-1368')")
mycursor.execute("INSERT INTO author_phone VALUES (65896345, '737-437-8687')")
mycursor.execute("INSERT INTO author_phone VALUES (75489998, '848-346-8658')")
mycursor.execute("INSERT INTO author_phone VALUES (08796456, '745-876-2841')")
mycursor.execute("INSERT INTO author_phone VALUES (08796456, '965-856-3523')")
mycursor.execute("INSERT INTO author_phone VALUES (11112222, '976-246-2349')")
mycursor.execute("INSERT INTO author_phone VALUES (11112222, '976-906-4842')")
mycursor.execute("INSERT INTO author_phone VALUES (22224444, '652-842-2528')")

mycursor.execute("INSERT INTO publisher VALUES ('McGraw', 'Green st.', 'Hunter', 'NY', 52647)")
mycursor.execute("INSERT INTO publisher VALUES ('Webster', 'Hilltop ave.', 'Browning', 'CA', 12463)")
mycursor.execute("INSERT INTO publisher VALUES ('Columbia', 'Spring st.', 'Buffalo', 'NY', 62364)")
mycursor.execute("INSERT INTO publisher VALUES ('Neural', 'Grand ave.', 'San Francisco', 'CA', 13425)")
mycursor.execute("INSERT INTO publisher VALUES ('Exportal', 'Latent rd.', 'Syracuse', 'NY', 12536)")
mycursor.execute("INSERT INTO publisher VALUES ('Radiate', 'First rd.', 'Kingston', 'NY', 23263)")
mycursor.execute("INSERT INTO publisher VALUES ('Zyrtex', '68th ave.', 'New York', 'NY', 73342)")
mycursor.execute("INSERT INTO publisher VALUES ('Burnal', 'Main st.', 'Ridgewood', 'NJ', 77432)")
mycursor.execute("INSERT INTO publisher VALUES ('Python', 'Resting rd.', 'Potsdam', 'NY', 21535)")
mycursor.execute("INSERT INTO publisher VALUES ('Capstone', '18th st.', 'New York', 'NY', 18486)")

mycursor.execute("INSERT INTO publisher_phone VALUES ('McGraw', '485-626-3785')")
mycursor.execute("INSERT INTO publisher_phone VALUES ('McGraw', '485-347-2935')")
mycursor.execute("INSERT INTO publisher_phone VALUES ('Webster', '059-268-5238')")
mycursor.execute("INSERT INTO publisher_phone VALUES ('Webster', '059-532-6979')")
mycursor.execute("INSERT INTO publisher_phone VALUES ('Columbia', '123-747-2356')")
mycursor.execute("INSERT INTO publisher_phone VALUES ('Neural', '979-397-2853')")
mycursor.execute("INSERT INTO publisher_phone VALUES ('Exportal', '236-7457-356')")
mycursor.execute("INSERT INTO publisher_phone VALUES ('Exportal', '236-2399-660')")
mycursor.execute("INSERT INTO publisher_phone VALUES ('Exportal', '236-6074-296')")
mycursor.execute("INSERT INTO publisher_phone VALUES ('Radiate', '518-369-0069')")
mycursor.execute("INSERT INTO publisher_phone VALUES ('Zyrtex', '347-352-9795')")
mycursor.execute("INSERT INTO publisher_phone VALUES ('Zyrtex', '347-109-9693')")
mycursor.execute("INSERT INTO publisher_phone VALUES ('Burnal', '251-563-7391')")
mycursor.execute("INSERT INTO publisher_phone VALUES ('Burnal', '251-969-1231')")
mycursor.execute("INSERT INTO publisher_phone VALUES ('Python', '197-019-0592')")
mycursor.execute("INSERT INTO publisher_phone VALUES ('Python', '197-775-2234')")
mycursor.execute("INSERT INTO publisher_phone VALUES ('Capstone', '718-504-1928')")

mycursor.execute("INSERT INTO book VALUES ('Intro to Econ', 37952543, 'Textbook', 2359235998, 'McGraw', 'Not Available')")
mycursor.execute("INSERT INTO book VALUES ('Econ 101', 37952543, 'Textbook', 2359235913, 'McGraw', 'Not Available')")
mycursor.execute("INSERT INTO book VALUES ('Of Mice and Men', 75487876, 'Fiction', 4395729538, 'Webster', 'Not Available')")
mycursor.execute("INSERT INTO book VALUES ('Poland Spring', 12358087, 'Non-Fiction', 1234698753, 'Radiate', 'Not Available')")
mycursor.execute("INSERT INTO book VALUES ('Delicje', 65896345, 'Fantasy', 7458235864, 'Zyrtex', 'Not Available')")
mycursor.execute("INSERT INTO book VALUES ('BenQ Alert', 18653975, 'Mystery', 9764278456, 'Zyrtex', 'Not Available')")
mycursor.execute("INSERT INTO book VALUES ('Chapped Lips', 12358087, 'Drama', 2357077890, 'Radiate', 'Not Available')")
mycursor.execute("INSERT INTO book VALUES ('Intro to Biology', 65478765, 'Textbook', 0896567845, 'Capstone', 'Not Available')")
mycursor.execute("INSERT INTO book VALUES ('Chemistry for College', 65478765, 'Textbook', 1269553865, 'Capstone', 'Not Available')")
mycursor.execute("INSERT INTO book VALUES ('Paper Fake', 75489998, 'Fiction', 8888444653, 'Columbia', 'Not Available')")
mycursor.execute("INSERT INTO book VALUES ('Neurosurgery for Students', 08796456, 'Textbook', 9994567345, 'Neural', 'Not Available')")
mycursor.execute("INSERT INTO book VALUES ('Medical 101', 08796456, 'Textbook', 4446854365, 'Exportal', 'Available')")
mycursor.execute("INSERT INTO book VALUES ('Nature Bounty', 46938230, 'Fiction', 9967434567, 'Burnal', 'Available')")
mycursor.execute("INSERT INTO book VALUES ('The Shack', 11112222, 'Religion', 6666352346, 'Burnal', 'Available')")
mycursor.execute("INSERT INTO book VALUES ('File Explorer', 22224444, 'Non-Fiction', 7432576666, 'Python', 'Available')")
mycursor.execute("INSERT INTO book VALUES ('Dolphin Dive', 22224444, 'Romance', 5346455322, 'Python', 'Available')")

mycursor.execute("INSERT INTO student VALUES (12345, 'Mateusz Jablonowksi', 'Computer Science')")
mycursor.execute("INSERT INTO student VALUES (62347, 'Katy Rays', 'Computer Science')")
mycursor.execute("INSERT INTO student VALUES (37854, 'Ellie Golden', 'Computer Science')")
mycursor.execute("INSERT INTO student VALUES (23678, 'Chris Brow', 'Computer Science')")
mycursor.execute("INSERT INTO student VALUES (23578, 'Matthew Makit', 'Computer Science')")
mycursor.execute("INSERT INTO student VALUES (23388, 'Lester Guy', 'Computer Science')")
mycursor.execute("INSERT INTO student VALUES (86586, 'Chester Fry', 'Business')")
mycursor.execute("INSERT INTO student VALUES (85345, 'Jade Dire', 'Business')")
mycursor.execute("INSERT INTO student VALUES (11112, 'Wolf Blitz', 'Business')")
mycursor.execute("INSERT INTO student VALUES (23566, 'Nicole Grant', 'Business')")
mycursor.execute("INSERT INTO student VALUES (96785, 'Kylie Bruno', 'Business')")
mycursor.execute("INSERT INTO student VALUES (14356, 'Kim Krash', 'Art')")
mycursor.execute("INSERT INTO student VALUES (44453, 'Amber Toro', 'Art')")
mycursor.execute("INSERT INTO student VALUES (22577, 'Robert Cash', 'Art')")
mycursor.execute("INSERT INTO student VALUES (86589, 'George Loper', 'Engineering')")
mycursor.execute("INSERT INTO student VALUES (45744, 'Erica Hart', 'Engineering')")
mycursor.execute("INSERT INTO student VALUES (66466, 'Eric Kappel', 'Engineering')")
mycursor.execute("INSERT INTO student VALUES (77342, 'Chase Plattner', 'Engineering')")

mycursor.execute("INSERT INTO student_acc VALUES (12345, 888666, 50)")
mycursor.execute("INSERT INTO student_acc VALUES (12345, 473788, 0)")
mycursor.execute("INSERT INTO student_acc VALUES (62347, 444466, 432)")
mycursor.execute("INSERT INTO student_acc VALUES (37854, 374747, 34)")
mycursor.execute("INSERT INTO student_acc VALUES (23678, 232456, 0)")
mycursor.execute("INSERT INTO student_acc VALUES (23578, 953458, 0)")
mycursor.execute("INSERT INTO student_acc VALUES (23388, 234864,34)")
mycursor.execute("INSERT INTO student_acc VALUES (86586, 268975, 4)")
mycursor.execute("INSERT INTO student_acc VALUES (86586, 364587, 86)")
mycursor.execute("INSERT INTO student_acc VALUES (85345, 732741, 124)")
mycursor.execute("INSERT INTO student_acc VALUES (11112, 867831, 75)")
mycursor.execute("INSERT INTO student_acc VALUES (23566, 434865, 346)")
mycursor.execute("INSERT INTO student_acc VALUES (96785, 227876, 0)")
mycursor.execute("INSERT INTO student_acc VALUES (96785, 787768, 0)")
mycursor.execute("INSERT INTO student_acc VALUES (14356, 595432, 54)")
mycursor.execute("INSERT INTO student_acc VALUES (44453, 888888, 79)")
mycursor.execute("INSERT INTO student_acc VALUES (22577, 363632, 32)")
mycursor.execute("INSERT INTO student_acc VALUES (86586, 747734, 0)")
mycursor.execute("INSERT INTO student_acc VALUES (86586, 114244, 324)")
mycursor.execute("INSERT INTO student_acc VALUES (45744, 326677, 546)")
mycursor.execute("INSERT INTO student_acc VALUES (66466, 998079, 0)")
mycursor.execute("INSERT INTO student_acc VALUES (77342, 598900, 19)")

mycursor.execute("INSERT INTO payment VALUES (888666, '9677940867', '12-06-2018', 50)")
mycursor.execute("INSERT INTO payment VALUES (473788, '0678457896', '11-06-2018', 80)")
mycursor.execute("INSERT INTO payment VALUES (598900, '2467848532', '12-09-2018', 50)")
mycursor.execute("INSERT INTO payment VALUES (998079, '8546256842', '10-12-2018', 45)")
mycursor.execute("INSERT INTO payment VALUES (326677, '5764832578', '07-25-2018', 62)")
mycursor.execute("INSERT INTO payment VALUES (326677, '3862378674', '09-21-2018', 57)")
mycursor.execute("INSERT INTO payment VALUES (114244, '7856856756', '11-07-2018', 158)")
mycursor.execute("INSERT INTO payment VALUES (747734, '2523523465', '06-30-2018', 462)")
mycursor.execute("INSERT INTO payment VALUES (363632, '1231243233', '04-17-2018', 98)")
mycursor.execute("INSERT INTO payment VALUES (888888, '5555544321', '12-15-2018', 70)")

mycursor.execute("INSERT INTO renting VALUES (12345, 0896567845)")
mycursor.execute("INSERT INTO renting VALUES (37854, 2359235998)")
mycursor.execute("INSERT INTO renting VALUES (23678, 4395729538)")
mycursor.execute("INSERT INTO renting VALUES (23678, 2359235913)")
mycursor.execute("INSERT INTO renting VALUES (86586, 1234698753)")
mycursor.execute("INSERT INTO renting VALUES (11112, 7458235864)")
mycursor.execute("INSERT INTO renting VALUES (23566, 9764278456)")
mycursor.execute("INSERT INTO renting VALUES (14356, 2357077890)")
mycursor.execute("INSERT INTO renting VALUES (44453, 1269553865)")
mycursor.execute("INSERT INTO renting VALUES (22577, 8888444653)")
mycursor.execute("INSERT INTO renting VALUES (77342, 9994567345)")

go = 0
from random import seed
from random import randint
seed(1)
while go == 0:
    print("1. Make a payment.")
    print("2. View your recent payments.")
    print("3. Delete payments from payment history.")
    print("4. View all books, their book numbers, and their availability in the library.")
    print("5. See if a book is availabe, and if not, who it's taken by.")
    print("6. Enter a book number to see the author's details.")
    print("7. Rent a book.")
    print("8. Exit")

    choice = input()

    if choice == "1":
        sid = str(input("Enter your student ID: "))
        ano = str(input("Enter your account number: "))
        mycursor.execute("SELECT id, account_id FROM student_acc WHERE id = " + sid + " and account_id = " + ano)
        row = mycursor.fetchone()
        
        if not row:
            print("This combination of student ID and account number does not exist.")

        else:
            mycursor.execute("SELECT amount_due FROM student_acc WHERE id = " + sid + " and account_id = " + ano)
            myresult = mycursor.fetchall()

            for row in myresult:
                print("You currently owe: $" + str(row[0]))
                
            amnt = input("Enter payment amount: ")
            date = input("Enter today's date in form {\"xx-xx-xxxx\"}: ")

            go2 = 0
            while go2 == 0:
                rand = randint(0, 9)
                rand2 = randint(0, 9)
                rand3 = randint(0, 9)
                rand4 = randint(0, 9)
                rand5 = randint(0, 9)
                rand6 = randint(0, 9)
                rand7 = randint(0, 9)
                rand8 = randint(0, 9)
                rand9 = randint(0, 9)
                rand10 = randint(0, 9)
                pno = str(rand) + str(rand2) + str(rand3) + str(rand4) + str(rand5) + str(rand6) + str(rand7) + str(rand8) + str(rand9) + str(rand10)
                mycursor.execute("SELECT account_id, payment_no FROM payment WHERE account_id = " + ano + " AND payment_no = " + pno)
                row_ = mycursor.fetchone()
                
                if not row_:
                    go2 = 1
                else:
                    go2 = 0
                      
            mycursor.execute("INSERT INTO payment VALUES (" + ano + "," + pno + "," + date + "," + amnt + ")")
            mycursor.execute("UPDATE student_acc SET amount_due = amount_due-" + amnt + " WHERE id = " + sid + " and account_id = " + ano)
            mycursor.execute("SELECT amount_due FROM student_acc WHERE id = " + sid + " and account_id = " + ano)
            myresult = mycursor.fetchall()

            for row in myresult:
                print("You now owe: $" + str(row[0]))

    elif choice == "2":
        ano = str(input("Enter your account number: "))
        mycursor.execute("SELECT * FROM payment WHERE account_id = " + ano)
        myresult = mycursor.fetchall()

        if not myresult:
            print("No payments found for this account number.")

        for y in myresult:
            print("Payment number: " + str(y[1]) + " || Payment date: " + str(y[2]) + " || Payment amount: " + str(y[3])) 

    elif choice == "3":
        ano = str(input("Enter your account number: "))
        mycursor.execute("SELECT account_id FROM student_acc WHERE account_id = " + ano)
        row = mycursor.fetchone()
        if not row:
            print("Account number was not found")
        else:
            pno = str(input("Enter payment number you would like to be deleted: "))
            mycursor.execute("SELECT payment_no FROM payment WHERE payment_no = " + pno)
            row = mycursor.fetchone()
            if row:
                mycursor.execute("DELETE FROM payment WHERE payment_no = " + pno)
                print("Deleted.")
            else:
                print("Payment number was not found")               
        
    elif choice == "4":
        mycursor.execute("SELECT * FROM book")
        myresult = mycursor.fetchall()

        for row in myresult:
            print(row[0] + ": " + str(row[3]) + ": " + row[5])

    elif choice == "5":
        bookno = input("Enter the book number: ")
        mycursor.execute("SELECT * FROM book WHERE book_no = " + bookno)
        myresult = mycursor.fetchall()
        
        if myresult:
            for x in myresult:
                print(x[0] + ": " + x[5])

            mycursor.execute("SELECT * FROM renting NATURAL JOIN student WHERE book_no = " + bookno)
            myresult = mycursor.fetchall()

            for x in myresult:
                print("Taken by: " + x[2])
        else:
            print("Book number not found.")

    elif choice == "6":
        bookno = input("Enter book number: ")
        mycursor.execute("SELECT author_id, author_name, bdate FROM book NATURAL JOIN author WHERE book_no = " + bookno)
        myresult = mycursor.fetchall()
        if not myresult:
            print("Book number not found")
        else:
            for x in myresult:
                print("Author ID: " + str(x[0]) + " || Author Name: " + x[1] + " || Birth Date: " + x[2])

            mycursor.execute("SELECT phone_number FROM book NATURAL JOIN author, author_phone WHERE author_phone.author_id = author.author_id AND book_no = " + bookno)
            myresult = mycursor.fetchall()
            if myresult:
                print("Phone Numbers: ")
                for x in myresult:
                    print(x[0] + "   ")
            else:
                print("No phone numbers on record for author.")

    elif choice == "7":
        sid = input("Enter your student ID: ")
        mycursor.execute("SELECT id FROM student where id = " + sid)
        myresult = mycursor.fetchone()
        if myresult:
            bookno = input("Enter the number of the book you would like to rent out: ")
            mycursor.execute("SELECT * FROM book WHERE availability = 'Available' AND book_no = " + bookno)
            row = mycursor.fetchone()
            if not row:
                print("Sorry, that book is either unavailable right now, or doesn't exist")
            else:
                print("You have rented out " + row[0])
                mycursor.execute("UPDATE book SET availability = 'Not Available' WHERE book_no = " + bookno)
                mycursor.execute("INSERT INTO renting VALUES (" + sid + "," + bookno + ")")
        else:
            print("Student ID wasn't found in database.")

    elif choice == "8":
        print("Goodbye!")
        go = 1

    else:
        print("Invalid choice.")

            
