import json
from datetime import datetime
from WebCalendar import db
from WebCalendar.models import Events
from WebCalendar.parsers import parser_post, parser_get
from WebCalendar.helpers import serialize_objects
from flask import abort
from flask_restful import Resource 



class MainResource(Resource):
    def get(self):
    	with open('WebCalendar/welcome.json', 'rt') as file_:
    		return json.load(file_)
   
    
class EventsResource(Resource):
	def get(self):
		args = parser_get.parse_args()
		start_time = args['start_time'].date() if args['start_time'] else None
		end_time = args['end_time'].date() if args['end_time'] else None

		if start_time and end_time:
			event_objs = Events.query.filter(start_time <= Events.date,
											 Events.date <= end_time)
		elif start_time:
			event_objs = Events.query.filter(start_time <= Events.date)
		elif end_time:
			event_objs = Events.query.filter(Events.date <= end_time)
		else:
			event_objs = Events.query.all()
			
		if event_objs:
			return serialize_objects(event_objs)
		return {"data": "No events to show"}
                
	def post(self):
		args = parser_post.parse_args()
		date = args['date'].strftime('%Y-%m-%d')
		evnt = Events(event=args['event'], date=args['date'],
					  location=args['location'])
		db.session.add(evnt)
		db.session.commit()
		return {
			"message": "The event has been added!",
			"event": f"{args['event']}",
			"date" : f"{date}",
			"location": f"{args['location']}",
		}


class TodaysEventsResource(Resource):
    def get(self):
        todays_events = Events.query.filter_by(date=datetime.now().date()).all()
        events = serialize_objects(todays_events)
        return events if todays_events else {"data":
        									 "There are no events for today!"}


class EventByIdResource(Resource):
    def get(self, event_id):
        resp = Events.query.filter_by(id=event_id).all()
        if resp:
            return serialize_objects(resp)[0]
        else:
            abort(404, "The event doesn't exist!")
            
    def delete(self, event_id):
        event = Events.query.filter_by(id=event_id).first()
        if event:
            db.session.delete(event)
            db.session.commit()
            return {"message": "The event has been deleted!"}
        else:
            abort(404, "The event doesn't exist!") 
            
            
