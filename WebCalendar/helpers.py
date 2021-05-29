def serialize_objects(event_objs):
    events = []
    for event in event_objs:
        date = event.date.strftime('%Y-%m-%d')
        events.append(
        {
                "id" : event.id,
                "event": event.event,
                "date" : date,
                "location": event.location
        })
    return events
