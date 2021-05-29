from flask_restful import reqparse, inputs


parser_post = reqparse.RequestParser()
parser_get = reqparse.RequestParser()

parser_post.add_argument(
    'date',
    type=inputs.date,
    help="The event date with the correct format is required! The correct format is YYYY-MM-DD!",
    required=True
)

parser_post.add_argument(
    'event',
    type=str,
    help="The event name is required!",
    required=True
)

parser_post.add_argument(
    'location',
    type=str,
    help="The event location is required!",
    required=True
)



parser_get.add_argument(
    'start_time',
    type=inputs.date,
    required=False
)

parser_get.add_argument(
    'end_time',
    type=inputs.date,
    required=False
)
