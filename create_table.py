from Base import Database


def create_tables():
    Customer = f"""
        CREATE TABLE customer(
            customer_id SERIAL PRIMARY KEY,
            first_name VARCHAR(50) NOT NULL,
            last_name VARCHAR(50),
            age int not null ,
            gmail text,
            phone_number int NOT NULL,
            last_update TIMESTAMP DEFAULT now());
    """

    Cource = f"""
        CREATE TABLE course(
            course_id SERIAL PRIMARY KEY,
            course_name VARCHAR(50) NOT NULL,
            course_about text,
            description text,
            price smallint not null,
            customer_id int references customer(customer_id),
            last_update TIMESTAMP DEFAULT now());
    """

    Mentor = f"""
        CREATE TABLE mentor(
            mentor_id SERIAL PRIMARY KEY,
            course_id int references course(course_id),
            name VARCHAR(50) NOT NULL,
            experience smallint,
            last_update TIMESTAMP DEFAULT now());
    """

    CoursesComment = f"""
       CREATE TABLE course_comment(
            course_comment_id SERIAL PRIMARY KEY,
            customer_id int references customer(customer_id),
            course_id int references course(course_id),
            mentor_id int references mentor(mentor_id),
            last_update TIMESTAMP DEFAULT now());"""

    Lesson = f"""
         CREATE TABLE lesson(
            lesson_id SERIAL PRIMARY KEY,
            course_id int references course(course_id),
            name VARCHAR(50) NOT NULL,
            last_update TIMESTAMP DEFAULT now());
    """

    LessonEvalution = f"""
        CREATE TABLE lesson_evaluatian(
            lesson_evaluation_id SERIAL PRIMARY KEY,
            lesson_id int references lesson(lesson_id),
            leeson_evaluation smallint,
            last_update TIMESTAMP DEFAULT now());
    """


    LessonComments = f"""
        CREATE TABLE lesson_comments(
            lesson_comments SERIAL PRIMARY KEY,
            lesson_id int references lesson(lesson_id),
            comment text not null ,
            last_update TIMESTAMP DEFAULT now());
    """

    Modul = f"""
        CREATE TABLE modul(
            modul_id serial PRIMARY KEY,
            course_id int references course(course_id),
            number_vd_lessons smallint,
            duration  smallint,
            last_update TIMESTAMP DEFAULT now());"""

    CompletedCourse = f"""
        CREATE TABLE completed_course(
            completed_course_id serial PRIMARY KEY,
            customer_id int references customer(customer_id),
            course_id int references course(course_id),
            persentage smallint,
            last_update TIMESTAMP DEFAULT now());"""

    PaymentStatus = f"""
        CREATE TABLE payment_status(
            payment_status_id serial PRIMARY KEY,
            customer_id int references customer(customer_id),
            name varchar(20),
            last_update TIMESTAMP DEFAULT now());
    """

    PaymentType = f"""
        CREATE TABLE payment_type(
            payment_type_id serial PRIMARY KEY,
            customer_id int references customer(customer_id),
            name varchar(20),
            last_update TIMESTAMP DEFAULT now());
    """

    Payment = f"""
        CREATE TABLE payment(
            payment_id serial PRIMARY KEY,
            customer_id int references customer(customer_id),
            course_id int references course(course_id),
            price smallint,
            payment_status_id int references payment_status(payment_status_id),
            payment_type_id int references payment_type(payment_type_id),
            last_update TIMESTAMP DEFAULT now());
    """
#
#     data_table = {
#         "customer": Customer,
#         "course": Cource,
#         "mentor": Mentor,
#         "course_comment": CoursesComment,
#         "lesson": Lesson,
#         "lesson_evaluation": LessonEvalution,
#         "lesson_comments": LessonComments,
#         "modul": Modul,
#         "completed_course": CompletedCourse,
#         "payment_status": PaymentStatus,
#         "payment_type": PaymentType,
#         "payment": Payment
#
#     }
#     for i in data_table:
#         print(f"{i} {Database.connect(data_table[i], 'create')}")
#
#
#
# if __name__ == "__main__":
#     create_tables()

