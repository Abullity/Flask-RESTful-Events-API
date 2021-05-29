from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///events.db'
db = SQLAlchemy(app)
api = Api(app)


from WebCalendar import models, resources


db.create_all()


api.add_resource(resources.MainResource, '/')
api.add_resource(resources.EventsResource, '/event')
api.add_resource(resources.EventByIdResource, '/event/<int:event_id>')
api.add_resource(resources.TodaysEventsResource, '/event/today')
