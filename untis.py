from datetime import date, datetime, time
import json
import webuntis
from time import sleep
from sys import argv


def get_next_lesson_for_user(session, template):
    
    try:
        if not getattr(session, "_is_logged_in", False):
            session.login()

        today = date.today()
        now_time = datetime.now().time()

        lessons = session.my_timetable(start=today, end=today)
        
        # lessons starting next
        upcoming = [l for l in lessons if l.start and (l.start.time() > now_time)]
        if not upcoming:
            return "No upcoming lessons today."
            
        next_lesson = min(upcoming, key=lambda l: l.start.time())
        
        subject = next_lesson.subjects[0].name if next_lesson.subjects else None
        room = next_lesson.rooms[0].name if next_lesson.rooms else None
        #teacher = next_lesson.teachers[0].name if next_lesson.teachers else None
        # didnt work on my end when i had this in, some serverside error
        
        return template.format(
            start=next_lesson.start.strftime('%H:%M'),
            end=next_lesson.end.strftime('%H:%M'),
            subject=subject,
            room=room
        )
    
    except Exception:
        return "Error"
        

if __name__ == "__main__":
    import atexit
    
    cfg = {}
    with open(argv[1]) as config_file:
        cfg = json.load(config_file)

    session = webuntis.Session(
            **cfg['auth'],
            useragent="UntisWidget/1.0",
    )
    atexit.register(lambda: session.logout())

    while True:
        next_l = get_next_lesson_for_user(session, cfg['settings']['template'])    
        print(next_l)
        sleep(cfg['settings']['interval'])






















