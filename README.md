# Untis Next Lesson Tray

System tray app that shows your next Untis lesson.
Written in python 🐢

## Dependencies 

Webuntis, PIL and pystray:
```bash
pip install -r requirements.txt
```

## Usage

```bash
python3 widget.py [path to config file]
```

You can also use untis.py as a polybar module:
```
[module/untis]
type = custom/script
exec = python -u /home/USER/untis-next-lesson-tray/untis.py  /home/USER/untis-next-lesson-tray/config.json
tail = true
```
You will probably want to tweak the formatting in config.json though.