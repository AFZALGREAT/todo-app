from flask import Flask, request, jsonify
import mysql.connector
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

def get_db_connection():
    return mysql.connector.connect(
        host="todo-mysql", user="root", password="root", database="todo_db"
    )

@app.route('/tasks', methods=['GET', 'POST'])
def tasks():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    if request.method == 'POST':
        data = request.get_json()
        cursor.execute("INSERT INTO tasks (task) VALUES (%s)", (data['task'],))
        conn.commit()
    cursor.execute("SELECT * FROM tasks")
    tasks = cursor.fetchall()
    conn.close()
    return jsonify(tasks)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
