from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class AttendanceLog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('student.id'))
    course_id = db.Column(db.Integer, db.ForeignKey('course.id'))
    date = db.Column(db.Date)

    def __repr__(self):
        return f"<AttendanceLog(student_id={self.student_id}, course_id={self.course_id}, date={self.date})>"


class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))

    def __repr__(self):
        return f"<Course(name={self.name})>"


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100))
    password = db.Column(db.String(100))
    department_id = db.Column(db.Integer, db.ForeignKey('department.id'))

    def __repr__(self):
        return f"<User(username={self.username}, department_id={self.department_id})>"


class Department(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))

    def __repr__(self):
        return f"<Department(name={self.name})>"


class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    department_id = db.Column(db.Integer, db.ForeignKey('department.id'))

    def __repr__(self):
        return f"<Student(name={self.name}, department_id={self.department_id})>"
