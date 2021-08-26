import json

from flask_restful import Resource, reqparse

TODOS = {
        "e94ajkdfc-42cd-436e-b63e-bcb485ad1407": {
            'task': "build an API",
            'completed': False,
        },
        "e94ks8fc-42cd-436e-b63e-bcb485ad1407": {
            'task': "D0 not go to grandma",
            'completed': False,
        },
        "e94aa8fc-42cd-436e-b63e-bjb485ad1407": {
            'task': "Do not make profit!",
            'completed': True,
        },
        "e94aa8fc-42cd-436e-b63e-bcb485ad1407": {
            'task': "Go to market",
            'completed': False,
        },
        "e94aa8fc-42cd-486e-b63e-bcb485ad1407": {
            'task': "Do not deploy",
            'completed': False,
        },
    }

parser = reqparse.RequestParser()
parser.add_argument('completed')
parser.add_argument('todo')


class CompleteTodo(Resource):
    def put(self, todo_id):
        if todo_id not in TODOS:
            return {"Error": "Todo not found"}, 400

        TODOS[todo_id]['completed'] = not TODOS[todo_id]['completed']

        return TODOS[todo_id], 201


class TodoList(Resource):
    def get(self):
        return TODOS

    def post(self):
        args = parser.parse_args()
        try:
            todo_data = args['todo'].replace("\'", "\"")
            todo_data = json.loads(todo_data)
            todo = list(todo_data.items())
            todo_id = todo[0][0]
        except Exception:
            return {"Error": "Bad data format"}, 400
        if todo_id in TODOS:
            return {"Error": "Todo already found"}, 400
        task = todo[0][1].get('task')
        if task is None or not task.strip():
            return {"Error": "Kindly enter a task"}, 400
        todo[0][1]['completed'] = False
        TODOS.update(todo_data)

        return todo_data, 201
