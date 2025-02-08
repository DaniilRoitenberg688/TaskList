from flask import Flask, request, jsonify, send_file
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks.db'
db = SQLAlchemy(app)
Migrate(app, db)

app.config['DEBUG'] = True

# модель для хранения задачи
class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    is_done = db.Column(db.Boolean, nullable=False, default=False)

# презентер для задачи
def present_task(task):
    return {
        "id": task.id,
        "title": task.title,
        "is_done": task.is_done
    }

# получаем все задачи
@app.route('/api/tasks', methods=['GET'])
def get_tasks():
    tasks = Task.query.all()
    print([present_task(task) for task in tasks])
    return [present_task(task) for task in tasks], 200, {'Access-Control-Allow-Origin': '*'}

# добавляем новую задачу
@app.route('/api/tasks', methods=['POST'])
def add_task():
    data = request.get_json()

    # если нет названия - возвращаем ошибку
    if not data.get('title'):
        return jsonify({'error': 'no title'}), 400

    task = Task(title=data['title'])
    db.session.add(task)
    db.session.commit()

    return jsonify(present_task(task))

@app.route('/api/tasks/<id:int>', methods=['DELETE'])
def delete_task(id):
    task = db.session.get(Task, id)
    if not task:
        return jsonify({'error': 'can not find task'}), 404

    db.session.delete(task)
    db.session.commit()
    return jsonify({'status': 'OK'}), 200


@app.route('/api/tasks', methods=['PATCH'])
def edit_task():
    data: dict = request.get_json()
    if not data:
        return jsonify({'error': 'no task'}), 400

    if not data.get('title'):
        return jsonify({'error': 'no title'}), 400

    task: Task = db.session.get(Task, int(data.get('id')))
    if not task:
        return jsonify({'error': 'can not find task'}), 404

    task.title = data.get('title')
    db.session.commit()
    return jsonify({'status': 'OK'}), 200





if __name__ == '__main__':
    app.run(debug=True, port=8080)