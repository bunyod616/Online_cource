from classes import Customer, Course, Mentor, CoursesComment,Lesson,LessonEvalution,LessonComments,Modul,CompletedCourse,PaymentStatus,PaymentType,Payment

def f_name():
    first_name = input("New First Name: ")
    id = int(input("Old Customer ID: "))
    query = f"""UPDATE customer SET first_name = '{first_name}' WHERE customer_id = {id};"""
    print(Customer.update(query))
    return _customer()
def l_name():
    last_name = input("New Last Name: ")
    id = int(input("Old Customer ID: "))
    query = f"""UPDATE customer SET last_name = '{last_name}' WHERE customer_id = {id};"""
    print(Customer.update(query))
    return _customer()



def _customer():
    services = input("""
                    1. Select
                    2. Insert
                    3. Delete
                    4. Update
                    0. Back
                        >>> """)

    if services == "1":
        for i in Customer.select("customer"):
            print(i)
        return _customer()

    elif services == "2":
        first_name = input("First Name: ")
        last_name = input("Last Name: ")
        age = input("Age: ")
        gmail = input("Gmail: ")
        phone_number = input("Phone number: ")
        customer = Customer(first_name,last_name,age,gmail,phone_number)
        print(customer.insert("customer"))

        return _customer()

    elif services == "3":
        column = input("column: ")
        data = input("data: ")
        if column != "customer_id":
            print(Customer.delete(column, data, 'customer'))

        else:
            print(Customer.delete_id(column, data, 'customer'))

        return _customer()

    elif services == "4":
            enter = input("""
                       1. First name
                       2. Last name
                       0. Back
                   """)
            if enter == "1":
                return f_name()
            elif enter == "2":
                return l_name()
            elif enter == "0":
                return _customer()
            else:
                print("Invalid")
                return _customer()

    elif services == "0":
        return main()

    else:
        print("Invalid")
        return _customer()

def _course():
    services = input("""
                    1. Select
                    2. Insert
                    3. Delete
                    4. Update
                    0. Back
                        >>> """)

    if services == "1":
        for i in Course.select("course"):
            print(i)
        return _course()

    elif services == "2":
        course_name = input("course name: ")
        course_about = input("course about: ")
        description = input("description: ")
        price = input("price: ")
        customer_id = input("customer id: ")
        course = Course(course_name,course_about,description,price,customer_id)
        print(course.insert("course"))

        return _course()

    elif services == "3":
        column = input("column: ")
        data = input("data: ")
        if column != "courses_id":
            print(Course.delete(column, data, 'course'))

        else:
            print(Course.delete_id(column, data, 'course'))

        return _course()

    elif services == "4":
        courses_name = input("New Courses Name: ")
        id = int(input("Old Courses ID: "))
        query = f"""UPDATE course SET course_name = '{courses_name}' WHERE course_id = {id};"""
        print(Course.update(query))
        return _course()

    elif services == "0":
        return main()

    else:
        print("Invalid")
        return _course()

def _mentor():
    services = input("""
                    1. Select
                    2. Insert
                    3. Delete
                    4. Update
                    0. Back
                        >>> """)

    if services == "1":
        for i in Mentor.select("mentor"):
            print(i)
        return _mentor()

    elif services == "2":
        course_id = input("course id: ")
        name = input("name: ")
        experience = input("exprience: ")
        mentore = Mentor(course_id,name,experience)
        print(mentore.insert("mentor"))

        return _mentor()

    elif services == "3":
        column = input("column: ")
        data = input("data: ")
        if column != "mentor_id":
            print(Mentor.delete(column, data, 'mentor'))

        else:
            print(Mentor.delete_id(column, data, 'mentor'))

        return _mentor()

    elif services == "4":
        courses_name = input("New Courses Name: ")
        id = int(input("Old Mentor ID: "))
        query = f"""UPDATE mentor SET name = '{courses_name}' WHERE mentor_id = {id};"""
        print(Mentor.update(query))
        return _mentor()

    elif services == "0":
        return main()

    else:
        print("Invalid")
        return _mentor()

def _cources_comment():
    services = input("""
                    1. Select
                    2. Insert
                    3. Delete
                    4. Update
                    0. Back
                        >>> """)

    if services == "1":
        for i in CoursesComment.select("courses_comment"):
            print(i)
        return _cources_comment()

    elif services == "2":
        customer_id = input("customer id: ")
        course_id = input("course_id: ")
        mentor_id = input("mentor_id: ")
        mentore = CoursesComment(customer_id,course_id,mentor_id)
        print(mentore.insert("courses_comment"))

        return _cources_comment()

    elif services == "3":
        column = input("column: ")
        data = input("data: ")
        if column != "courses_comment_id":
            print(CoursesComment.delete(column, data, 'courses_comment'))

        else:
            print(Customer.delete_id(column, data, 'courses_comment'))

        return _cources_comment()

    elif services == "4":
        courses_name = input("New Courses Name: ")
        id = int(input("Old Mentor ID: "))
        query = f"""UPDATE mentor SET name = '{courses_name}' WHERE mentor_id = {id};"""
        print(Mentor.update(query))
        return _mentor()

    elif services == "0":
        return main()

    else:
        print("Invalid")
        return _mentor()

def _lesson():
    services = input("""
                    1. Select
                    2. Insert
                    3. Delete
                    4. Update
                    0. Back
                        >>> """)

    if services == "1":
        for i in Lesson.select("lesson"):
            print(i)
        return _lesson()

    elif services == "2":
        course_id = input("course_id: ")
        name = input("name: ")
        lesson = Lesson(course_id,name)
        print(lesson.insert("lesson"))

        return _lesson()

    elif services == "3":
        column = input("column: ")
        data = input("data: ")
        if column != "lesson_id":
            print(Lesson.delete(column, data, 'lesson'))

        else:
            print(Lesson.delete_id(column, data, 'lesson'))

        return _lesson()

    elif services == "4":
        name = input("New Courses Name: ")
        course_id = input("New Course_id: ")
        id = int(input("Old Lesson ID: "))
        query = f"""UPDATE lesson SET name = '{name}',course_id = '{course_id}' WHERE lesson_id = {id};"""
        print(Lesson.update(query))
        return _lesson()

    elif services == "0":
        return main()

    else:
        print("Invalid")
        return _lesson()

def _lesson_evalution():
    services = input("""
                    1. Select
                    2. Insert
                    3. Delete
                    4. Update
                    0. Back
                        >>> """)

    if services == "1":
        for i in LessonEvalution.select("lesson_evaluatian"):
            print(i)
        return _lesson_evalution()

    elif services == "2":
        lesson_id = input("lesson id: ")
        leeson_evaluation = input("lesson evaluation: ")
        lesson_1 = LessonEvalution(lesson_id,leeson_evaluation)
        print(lesson_1.insert("lesson_evaluatian"))

        return _lesson_evalution()

    elif services == "3":
        column = input("column: ")
        data = input("data: ")
        if column != "lesson_evaluation_id":
            print(LessonEvalution.delete(column, data, 'lesson_evaluatian'))

        else:
            print(LessonEvalution.delete_id(column, data, 'lesson_evaluatian'))

        return _lesson_evalution()

    elif services == "4":
        leeson_evaluation = input("New lesson evaluation: ")
        id = int(input("Old Lesson Evaluation ID: "))
        query = f"""UPDATE lesson_evaluatian SET leeson_evaluation = '{leeson_evaluation}' WHERE leeson_evaluation_id = {id};"""
        print(LessonEvalution.update(query))
        return _lesson_evalution()

    elif services == "0":
        return main()

    else:
        print("Invalid")
        return _lesson_evalution()

def _lesson_comments():
    services = input("""
                    1. Select
                    2. Insert
                    3. Delete
                    4. Update
                    0. Back
                        >>> """)

    if services == "1":
        for i in LessonComments.select("lesson_comments"):
            print(i)
        return _lesson_comments()

    elif services == "2":
        lesson_id = input("lesson_id: ")
        comment = input("comment: ")
        lesson_C = LessonComments(lesson_id,comment)
        print(lesson_C.insert("lesson_comments"))

        return _lesson_comments()

    elif services == "3":
        column = input("column: ")
        data = input("data: ")
        if column != "lesson_comments":
            print(LessonComments.delete(column, data, 'lesson_comments'))

        else:
            print(LessonComments.delete_id(column, data, 'lesson_comments'))

        return _lesson_comments()

    elif services == "4":
        name = input("New lesson id Name: ")
        comment = input("New comment: ")
        id = int(input("Old Lesson ID: "))
        query = f"""UPDATE lesson_comments SET lesson_id = '{name}',comment = '{comment}' WHERE lesson_comments = {id};"""
        print(LessonComments.update(query))
        return _lesson_comments()

    elif services == "0":
        return main()

    else:
        print("Invalid")
        return _lesson_comments()

def _modul():
    services = input("""
                    1. Select
                    2. Insert
                    3. Delete
                    4. Update
                    0. Back
                        >>> """)

    if services == "1":
        for i in Modul.select("modul"):
            print(i)
        return _modul()

    elif services == "2":
        course_id = input("course_id: ")
        number_vd_lessons = input("number_vd_lesson: ")
        duration = input("duration: ")
        modul = Modul(course_id,number_vd_lessons,duration)
        print(modul.insert("modul"))

        return _modul()

    elif services == "3":
        column = input("column: ")
        data = input("data: ")
        if column != "modul_id":
            print(Modul.delete(column, data, 'modul'))

        else:
            print(Modul.delete_id(column, data, 'modul'))

        return _modul()

    elif services == "4":
        course_id = input("New course id Name: ")
        number_vd_lesson = input("New vd_lesson: ")
        duration = input("duration: ")
        id = int(input("Old modul ID: "))
        query = f"""UPDATE modul SET course_id = '{course_id}',number_vd_lessons = '{number_vd_lesson}',duration = '{duration}' WHERE modul_id = {id};"""
        print(Modul.update(query))
        return _modul()

    elif services == "0":
        return main()

    else:
        print("Invalid")
        return _modul()

def _completed_course():
    services = input("""
                    1. Select
                    2. Insert
                    3. Delete
                    4. Update
                    0. Back
                        >>> """)

    if services == "1":
        for i in CompletedCourse.select("completed_course"):
            print(i)
        return _completed_course()

    elif services == "2":
        customer_id = input("customer_id: ")
        course_id = input("course_id: ")
        persantage = input("persentage: ")
        completed = CompletedCourse(customer_id,course_id,persantage)
        print(completed.insert("completed_course"))

        return _completed_course()

    elif services == "3":
        column = input("column: ")
        data = input("data: ")
        if column != "completed_course_id":
            print(CompletedCourse.delete(column, data, 'completed_course'))

        else:
            print(CompletedCourse.delete_id(column, data, 'completed_course'))

        return _completed_course()

    elif services == "4":
        customer_id = input("New customer id: ")
        course_id = input("New course id Name: ")
        persentage = input("persentage: ")
        id = int(input("Old completed course ID: "))
        query = f"""UPDATE completed_course SET customer_id = '{customer_id}',course_id = '{course_id}',persentage = '{persentage}' WHERE completed_course_id = {id};"""
        print(CompletedCourse.update(query))
        return _completed_course()

    elif services == "0":
        return main()

    else:
        print("Invalid")
        return _completed_course()

def _payment_status():
    services = input("""
                    1. Select
                    2. Insert
                    3. Delete
                    4. Update
                    0. Back
                        >>> """)

    if services == "1":
        for i in PaymentStatus.select("payment_status"):
            print(i)
        return _payment_status()

    elif services == "2":
        customer_id = input("customer_id: ")
        name = input("name: ")
        completed = PaymentStatus(customer_id,name)
        print(completed.insert("payment_status"))

        return _payment_status()

    elif services == "3":
        column = input("column: ")
        data = input("data: ")
        if column != "payment_status_id":
            print(PaymentStatus.delete(column, data, 'payment_status'))

        else:
            print(PaymentStatus.delete_id(column, data, 'payment_status'))

        return _payment_status()

    elif services == "4":
        customer_id = input("New customer id: ")
        name = input("New name: ")
        id = int(input("Old payment status ID: "))
        query = f"""UPDATE payment_status SET customer_id = '{customer_id}',name = '{name}' WHERE payment_status_id = {id};"""
        print(PaymentStatus.update(query))
        return _payment_status()

    elif services == "0":
        return main()

    else:
        print("Invalid")
        return _payment_status()

def _payment_type():
    services = input("""
                    1. Select
                    2. Insert
                    3. Delete
                    4. Update
                    0. Back
                        >>> """)

    if services == "1":
        for i in PaymentType.select("payment_type"):
            print(i)
        return _payment_type()

    elif services == "2":
        customer_id = input("customer_id: ")
        name = input("name: ")
        completed = PaymentType(customer_id,name)
        print(completed.insert("payment_type"))

        return _payment_type()

    elif services == "3":
        column = input("column: ")
        data = input("data: ")
        if column != "payment_type_id":
            print(PaymentType.delete(column, data, 'payment_type'))

        else:
            print(PaymentType.delete_id(column, data, 'payment_type'))

        return _payment_type()

    elif services == "4":
        customer_id = input("New customer id: ")
        name = input("New name: ")
        id = int(input("Old payment type ID: "))
        query = f"""UPDATE payment_type SET customer_id = '{customer_id}',name = '{name}' WHERE payment_type_id = {id};"""
        print(PaymentType.update(query))
        return _payment_type()

    elif services == "0":
        return main()

    else:
        print("Invalid")
        return _payment_type()

def _payment():
    services = input("""
                    1. Select
                    2. Insert
                    3. Delete
                    4. Update
                    0. Back
                        >>> """)

    if services == "1":
        for i in Payment.select("payment"):
            print(i)
        return _payment()

    elif services == "2":
        customer_id = input("customer_id: ")
        course_id = input("course id: ")
        price = input("price: ")
        payment_status_id = input("payment_status_id: ")
        payment_type_id = input("payment_type_id: ")
        completed = Payment(customer_id,course_id,price,payment_status_id,payment_type_id)
        print(completed.insert("payment"))

        return _payment()

    elif services == "3":
        column = input("column: ")
        data = input("data: ")
        if column != "payment_id":
            print(Payment.delete(column, data, 'payment'))

        else:
            print(Payment.delete_id(column, data, 'payment'))

        return _payment()

    elif services == "4":
        customer_id = input("New customer id: ")
        course_id = input("New course id: ")
        price =input("New price: ")
        id = int(input("Old payment type ID: "))
        query = f"""UPDATE payment SET customer_id = '{customer_id}',course_id = '{course_id}',price = '{price}' WHERE payment_id = {id};"""
        print(Payment.update(query))
        return _payment()

    elif services == "0":
        return main()

    else:
        print("Invalid")
        return _payment()

def main():
    tables = input("""
       1. Customer
       2. Course 
       3. Mentor 
       4. CoursesComment
       5. Lesson
       6. Lesson Evalution
       7. Lesson Comments
       8. Modul
       9. Completed Course
       10. Payment Status 
       11. Payment Type
       12. Payment
            >>> """)

    if tables == "1":
        return _customer()

    elif tables == "2":
        return _course()

    elif tables == "3":
        return _mentor()

    elif tables == "4":
        return _cources_comment()

    elif tables == "5":
        return _lesson()

    elif tables == "6":
        return _lesson_evalution()

    elif tables == "7":
        return _lesson_comments()

    elif tables == "8":
        return _modul()

    elif tables == "9":
        return _completed_course()

    elif tables == "10":
        return _payment_status()

    elif tables == "11":
        return _payment_type()

    elif tables == "12":
        return _payment()





    else:
        print("Invalid")
        return main()


if __name__ == "__main__":
    main()
