from datetime import datetime, timezone

from flask import request
from flask_restful import Resource
from google.cloud import datastore

# Instantiates a client
datastore_client = datastore.Client()


class CompleteTodo(Resource):
    def put(self, todo_id):
        with datastore_client.transaction():
            try:
                id = int(todo_id)
            except Exception:
                return f"Invalid todo id {todo_id}", 400
            complete_key = datastore_client.key("todos", id)
            task = datastore_client.get(key=complete_key)

            if not task:
                return f"Task {todo_id} does not exist.", 400
            task["completed"] = not task["completed"]
            datastore_client.put(task)

            return task, 201


class TodoList(Resource):
    def get(self):
        query = datastore_client.query(kind='todos')
        query.order = ["-created"]
        results = list(query.fetch())
        for res in results:
            res['id'] = res.id

        return results

    def post(self):
        todo_data = request.get_json()
        task = todo_data.get('task')

        if task is None or not task.strip():
            return {"Error": "Kindly enter a task"}, 400
        now = datetime.now(timezone.utc).astimezone()
        todo_data['completed'] = False
        todo_data['created'] = str(now)

        entity = datastore.Entity(
            key=datastore_client.key('todos'),
            exclude_from_indexes=['task', 'completed'])
        entity.update(todo_data)
        datastore_client.put(entity)
        todo_data['id'] = entity.id

        return todo_data, 201
