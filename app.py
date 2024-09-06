from flask import Flask, render_template, request, redirect, url_for
from models import Student, AbstractRegistry, StudentRegistry

app = Flask(__name__)

registry: AbstractRegistry = StudentRegistry()


@app.route('/')
def index():
    return redirect(url_for('student_list'))


@app.route('/students')
def student_list():
    students = registry.get_all()
    return render_template('student_list.html', students=students)


@app.route('/student/<int:id>')
def student_detail(id):
    student = registry.get_by_id(id)
    return render_template('student_detail.html', student=student)


@app.route('/register', methods=['GET', 'POST'])
def register_student():

    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']
        grade = request.form['grade']
        student = Student(name, age, grade)
        registry.add(student)
        return redirect(url_for('student_list'))

    return render_template('register_student.html')


@app.route('/student/<int:id>/edit', methods=['GET', 'POST'])
def edit_student(id):
    student = registry.get_by_id(id)
    if request.method == 'POST':
        name = request.form['name']
        age = int(request.form['age'])
        grade = request.form['grade']
        registry.update(id, name=name, age=age, grade=grade)
        return redirect(url_for('student_list'))

    return render_template('edit_student.html', student=student)


@app.route('/student/<int:id>/delete', methods=['POST'])
def delete_student(id):
    registry.delete(id)
    return redirect(url_for('student_list'))


if __name__ == '__main__':
    app.run(debug=True)

