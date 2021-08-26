from flask import Flask
from flask_restful import Api
from api.resources.hello import Hello
from api.resources.todos import CompleteTodo, TodoList
from api.resources.vowels import ReverseVowel
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
api = Api(app)

api.add_resource(TodoList, '/todos')
api.add_resource(CompleteTodo, '/todos/<todo_id>/')
api.add_resource(Hello, '/hello')
api.add_resource(ReverseVowel, '/vowel-service')

if __name__ == '__main__':
    app.run(debug=True)
