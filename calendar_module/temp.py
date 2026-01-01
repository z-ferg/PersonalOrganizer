from calendar_funcs import get_all_calendars, get_next_events

all_cals = get_all_calendars(name_only=True)
all_events = []

for cal in all_cals:
    all_events += get_next_events(cal, num_events=15)

sorted_events = sorted(all_events, key=lambda i: i['start']['date'] if 'date' in i['start'].keys() else i['start']['dateTime'])

for i in range(10):
    sorted_events[i]['Calendar'] = sorted_events[i]['organizer']['displayName']
    del sorted_events[i]['organizer']
    print(sorted_events[i])
