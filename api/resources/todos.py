import uuid

from flask_restful import Resource, reqparse

TODOS = {
        "e94ajkdfc-42cd-436e-b63e-bcb485ad1407":{
            'task': "build an API",
            'completed': False,
        },
        "e94ks8fc-42cd-436e-b63e-bcb485ad1407":{
            'task': "?????",
            'completed': False,
        },
        "e94aa8fc-42cd-436e-b63e-bjb485ad1407":{
            'task': "profit!",
            'completed': True,
        },
        "e94aa8fc-42cd-436e-b63e-bcb485ad1407":{
            'task': "Go to market",
            'completed': False,
        },
    }

parser = reqparse.RequestParser()
parser.add_argument('completed')
parser.add_argument('task')

class CompleteTodo(Resource):
    def put(self, todo_id):
        TODOS[todo_id]['task'] = not TODOS[todo_id]['task']

        return TODOS[todo_id], 201

class TodoList(Resource):
    def get(self):
        return TODOS

    def post(self):
        args = parser.parse_args()
        todo_id = str(uuid.uuid4())
        TODOS[todo_id] = {'task': args['task'], 'completed': False}
        return TODOS[todo_id], 201
