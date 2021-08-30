from api.common.reverse_vowels import reverse_vowels
from flask import request
from flask_restful import Resource, reqparse

parser = reqparse.RequestParser()
parser.add_argument('message', required=True, help="Message cannot be blank!")


class ReverseVowel(Resource):
    def post(self):
        if request.method != 'POST':
            return "The method is not allowed for the requested URL.", 405

        args = parser.parse_args()
        message = args['message']

        return reverse_vowels(message)
