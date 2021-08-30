from api.common.reverse_vowels import reverse_vowels
from flask_restful import Resource, reqparse

parser = reqparse.RequestParser()
parser.add_argument('message', required=True, help="Message is a required field!")


class ReverseVowel(Resource):
    def post(self):
        args = parser.parse_args()
        message = args['message']

        return reverse_vowels(message)
