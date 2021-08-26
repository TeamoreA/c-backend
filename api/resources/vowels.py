from flask_restful import reqparse, Resource
from api.common.reverse_vowels import reverse_vowels

parser = reqparse.RequestParser()
parser.add_argument('message', required=True, help="Message cannot be blank!")


class ReverseVowel(Resource):
    def post(self):
        args = parser.parse_args()
        message = args['message']

        return reverse_vowels(message)
