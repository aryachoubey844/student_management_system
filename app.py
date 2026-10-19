from flask import Flask, request, jsonify

app = Flask(__name__)

students = [
    {"id": 1, "name": "Aman Kumar", "course": "MCA", "fees": 50000},
    {"id": 2, "name": "Priya S", "course": "Python", "fees": 30000}
]

@app.route('/')
def home():
    return jsonify({"project": "Student Management API", "status": "Running"})

@app.route('/students', methods=['GET'])
def get_students():
    return jsonify(students)

@app.route('/students', methods=['POST'])
def add_student():
    data = request.json
    new_student = {
        "id": len(students) + 1,
        "name": data['name'],
        "course": data['course'],
        "fees": data.get('fees', 0)
    }
    students.append(new_student)
    return jsonify(new_student), 201

@app.route('/students/<int:id>', methods=['DELETE'])
def delete_student(id):
    global students
    students = [s for s in students if s['id'] != id]
    return jsonify({"message": "Deleted"})

if __name__ == '__main__':
    app.run(debug=True, port=5000)