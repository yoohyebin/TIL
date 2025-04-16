import datetime

with open('commits.txt') as f:
    days = f.read().splitlines()

today = datetime.date.today()
boxes = []
for i in range(29, -1, -1):
    day = (today - datetime.timedelta(days=i)).isoformat()
    color = "#00c853" if day in days else "#eeeeee"
    boxes.append(f'<rect x="{(29-i)*12}" y="0" width="10" height="10" fill="{color}" />')

svg = f'<svg width="360" height="20" xmlns="http://www.w3.org/2000/svg">{"".join(boxes)}</svg>'

with open('commit-calendar.svg', 'w') as f:
    f.write(svg)
