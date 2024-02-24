from Base import Database

class Customer:
    def __init__(self,first_name,last_name,age,gmail,phone_number):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gmail = gmail
        self.phone_number = phone_number


    def insert(self, table="customer"):
        query = f"""INSERT INTO {table}(first_name,last_name,age,gmail,phone_number) VALUES('{self.first_name}','{self.last_name}','{self.age}','{self.gmail}','{self.phone_number}')"""
        return Database.connect(query, "insert")

    @staticmethod
    def select(table="customer"):
        query = f"""SELECT * FROM {table};"""
        return Database.connect(query, "select")

    @staticmethod
    def update(query):
        return Database.connect(query, "update")

    @staticmethod
    def delete(column, search_data, table):
        query = f"""DELETE FROM {table} WHERE {column} = '{search_data}'"""

        return Database.connect(query, "delete")

    @staticmethod
    def delete_id(column, search_data, table):
        query = f"""DELETE FROM {table} WHERE {column} = {search_data}"""

        return Database.connect(query, "delete")

class Course:
    def __init__(self,course_name,course_about,description,price,customer_id):
        self.course_name = course_name
        self.course_about = course_about
        self.description = description
        self.price = price
        self.customer_id = customer_id


    def insert(self, table="course"):
        query = f"""INSERT INTO {table}(course_name,course_about,description,price,customer_id) VALUES('{self.course_name}','{self.course_about}','{self.description}','{self.price}','{self.customer_id}')"""
        return Database.connect(query, "insert")

    @staticmethod
    def select(table="course"):
        query = f"""SELECT * FROM {table};"""
        return Database.connect(query, "select")

    @staticmethod
    def update(query):
        return Database.connect(query, "update")

    @staticmethod
    def delete(column, search_data, table):
        query = f"""DELETE FROM {table} WHERE {column} = '{search_data}'"""

        return Database.connect(query, "delete")

    @staticmethod
    def delete_id(column, search_data, table):
        query = f"""DELETE FROM {table} WHERE {column} = {search_data}"""

        return Database.connect(query, "delete")

class Mentor:
    def __init__(self,course_id,name,experience):
        self.course_id = course_id
        self.name = name
        self.experience = experience


    def insert(self, table="mentor"):
        query = f"""INSERT INTO {table}(course_id,name,experience) VALUES('{self.course_id}','{self.name}','{self.experience}')"""
        return Database.connect(query, "insert")

    @staticmethod
    def select(table="mentor"):
        query = f"""SELECT * FROM {table};"""
        return Database.connect(query, "select")

    @staticmethod
    def update(query):
        return Database.connect(query, "update")

    @staticmethod
    def delete(column, search_data, table):
        query = f"""DELETE FROM {table} WHERE {column} = '{search_data}'"""

        return Database.connect(query, "delete")

    @staticmethod
    def delete_id(column, search_data, table):
        query = f"""DELETE FROM {table} WHERE {column} = {search_data}"""

        return Database.connect(query, "delete")

class CoursesComment:
    def __init__(self,customer_id,course_id,mentor_id):
        self.customer_id = customer_id
        self.course_id = course_id
        self.mentor_id = mentor_id


    def insert(self, table="courses_comment"):
        query = f"""INSERT INTO {table}(customer_id,course_id,mentor_id) VALUES('{self.customer_id}','{self.course_id}','{self.mentor_id}')"""
        return Database.connect(query, "insert")

    @staticmethod
    def select(table="courses_comment"):
        query = f"""SELECT * FROM {table};"""
        return Database.connect(query, "select")

    @staticmethod
    def update(query):
        return Database.connect(query, "update")

    @staticmethod
    def delete(column, search_data, table):
        query = f"""DELETE FROM {table} WHERE {column} = '{search_data}'"""

        return Database.connect(query, "delete")

    @staticmethod
    def delete_id(column, search_data, table):
        query = f"""DELETE FROM {table} WHERE {column} = {search_data}"""

        return Database.connect(query, "delete")

class Lesson:
    def __init__(self,course_id,name):
        self.course_id = course_id
        self.name = name

    def insert(self, table="lesson"):
        query = f"""INSERT INTO {table}(course_id,name) VALUES('{self.course_id}','{self.name}')"""
        return Database.connect(query, "insert")

    def select(table="lesson"):
        query = f"""SELECT * FROM {table};"""
        return Database.connect(query, "select")

    def update(query):
        return Database.connect(query, "update")

    def delete(column, search_data, table):
        query = f"""DELETE FROM {table} WHERE {column} = '{search_data}'"""
        return Database.connect(query, "delete")

    def delete_id(column, search_data, table):
        query = f"""DELETE FROM {table} WHERE {column} = {search_data}"""

        return Database.connect(query, "delete")

class LessonEvalution:
    def __init__(self,lesson_id,lesson_evaluation):
        self.lesson_id = lesson_id
        self.lesson_evaluation = lesson_evaluation

    def insert(self, table="lesson_evaluatian"):
        query = f"""INSERT INTO {table}(lesson_id,leeson_evaluation) VALUES('{self.lesson_id}','{self.lesson_evaluation}')"""
        return Database.connect(query, "insert")

    def select(table="lesson_evaluatian"):
        query = f"""SELECT * FROM {table};"""
        return Database.connect(query, "select")

    def update(query):
        return Database.connect(query, "update")

    def delete(column, search_data, table):
        query = f"""DELETE FROM {table} WHERE {column} = '{search_data}'"""
        return Database.connect(query, "delete")

    def delete_id(column, search_data, table):
        query = f"""DELETE FROM {table} WHERE {column} = {search_data}"""

        return Database.connect(query, "delete")

class LessonComments:
    def __init__(self,lesson_id,comment):
        self.lesson_id = lesson_id
        self.comment = comment

    def insert(self, table="lesson_comments"):
        query = f"""INSERT INTO {table}(lesson_id,comment) VALUES('{self.lesson_id}','{self.comment}')"""
        return Database.connect(query, "insert")

    def select(table="lesson_comments"):
        query = f"""SELECT * FROM {table};"""
        return Database.connect(query, "select")

    def update(query):
        return Database.connect(query, "update")

    def delete(column, search_data, table):
        query = f"""DELETE FROM {table} WHERE {column} = '{search_data}'"""
        return Database.connect(query, "delete")

    def delete_id(column, search_data, table):
        query = f"""DELETE FROM {table} WHERE {column} = {search_data}"""

        return Database.connect(query, "delete")

class Modul:
    def __init__(self,course_id,number_vd_lesson,duration):
        self.course_id = course_id
        self.number_vd_lessons = number_vd_lesson
        self.duration = duration

    def insert(self, table="modul"):
        query = f"""INSERT INTO {table}(course_id,number_vd_lessons,duration) VALUES('{self.course_id}','{self.number_vd_lessons}','{self.duration}')"""
        return Database.connect(query, "insert")

    def select(table="modul"):
        query = f"""SELECT * FROM {table};"""
        return Database.connect(query, "select")

    def update(query):
        return Database.connect(query, "update")

    def delete(column, search_data, table):
        query = f"""DELETE FROM {table} WHERE {column} = '{search_data}'"""
        return Database.connect(query, "delete")

    def delete_id(column, search_data, table):
        query = f"""DELETE FROM {table} WHERE {column} = {search_data}"""

        return Database.connect(query, "delete")

class CompletedCourse:
    def __init__(self,customer_id,course_id,persentage):
        self.customer_id = customer_id
        self.course_id = course_id
        self.persentage = persentage

    def insert(self, table="completed_course"):
        query = f"""INSERT INTO {table}(customer_id,course_id,persentage) VALUES('{self.customer_id}','{self.course_id}','{self.persentage}')"""
        return Database.connect(query, "insert")

    def select(table="completed_course"):
        query = f"""SELECT * FROM {table};"""
        return Database.connect(query, "select")

    def update(query):
        return Database.connect(query, "update")

    def delete(column, search_data, table):
        query = f"""DELETE FROM {table} WHERE {column} = '{search_data}'"""
        return Database.connect(query, "delete")

    def delete_id(column, search_data, table):
        query = f"""DELETE FROM {table} WHERE {column} = {search_data}"""

        return Database.connect(query, "delete")

class PaymentStatus:
    def __init__(self,customer_id,name):
        self.customer_id = customer_id
        self.name = name

    def insert(self, table="payment_status"):
        query = f"""INSERT INTO {table}(customer_id,name) VALUES('{self.customer_id}','{self.name}')"""
        return Database.connect(query, "insert")

    def select(table="payment_status"):
        query = f"""SELECT * FROM {table};"""
        return Database.connect(query, "select")

    def update(query):
        return Database.connect(query, "update")

    def delete(column, search_data, table):
        query = f"""DELETE FROM {table} WHERE {column} = '{search_data}'"""
        return Database.connect(query, "delete")

    def delete_id(column, search_data, table):
        query = f"""DELETE FROM {table} WHERE {column} = {search_data}"""

        return Database.connect(query, "delete")

class PaymentType:
    def __init__(self,customer_id,name):
        self.customer_id = customer_id
        self.name = name

    def insert(self, table="payment_type"):
        query = f"""INSERT INTO {table}(customer_id,name) VALUES('{self.customer_id}', '{self.name}')"""
        return Database.connect(query, "insert")

    def select(table="payment_type"):
        query = f"""SELECT * FROM {table};"""
        return Database.connect(query, "select")

    def update(query):
        return Database.connect(query, "update")

    def delete(column, search_data, table):
        query = f"""DELETE FROM {table} WHERE {column} = '{search_data}'"""
        return Database.connect(query, "delete")

    def delete_id(column, search_data, table):
        query = f"""DELETE FROM {table} WHERE {column} = {search_data}"""

        return Database.connect(query, "delete")

class Payment:
    def __init__(self,customer_id,course_id,price,payment_status_id,payment_type_id):
        self.customer_id = customer_id
        self.course_id = course_id
        self.price = price
        self.payment_status_id = payment_status_id
        self.payment_type_id = payment_type_id

    def insert(self, table="payment"):
        query = f"""INSERT INTO {table}(customer_id,course_id,price,payment_status_id,payment_type_id) VALUES('{self.customer_id}','{self.course_id}','{self.price}','{self.payment_status_id}','{self.payment_type_id}')"""
        return Database.connect(query, "insert")

    def select(table="payment_type"):
        query = f"""SELECT * FROM {table};"""
        return Database.connect(query, "select")

    def update(query):
        return Database.connect(query, "update")

    def delete(column, search_data, table):
        query = f"""DELETE FROM {table} WHERE {column} = '{search_data}'"""
        return Database.connect(query, "delete")

    def delete_id(column, search_data, table):
        query = f"""DELETE FROM {table} WHERE {column} = {search_data}"""

        return Database.connect(query, "delete")