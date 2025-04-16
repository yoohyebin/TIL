import datetime
from collections import defaultdict

# 색상 정의
COLOR_COMMIT = "#ffc0cb"  # 라이트 핑크
COLOR_EMPTY = "#ebedf0"   # 회색

# 날짜별 커밋 수 저장
commit_days = set()

with open('commits.txt') as f:
    for line in f:
        date = line.strip()
        if date:
            commit_days.add(date)

# SVG 만들기
start_date = datetime.date.today() - datetime.timedelta(days=364)
weeks = [[]]

for i in range(365):
    day = start_date + datetime.timedelta(days=i)
    date_str = day.isoformat()
    color = COLOR_COMMIT if date_str in commit_days else COLOR_EMPTY

    rect = f'<rect x="{len(weeks)*13}" y="{(day.weekday())*13}" width="10" height="10" fill="{color}" rx="2" ry="2"/>'
    weeks[-1].append(rect)

    # 일요일마다 주 단위로 분리
    if day.weekday() == 6:
        weeks.append([])

rects = "\n".join(["\n".join(week) for week in weeks])

# SVG 조립
svg = f'''<svg width="{len(weeks)*13}" height="100" xmlns="http://www.w3.org/2000/svg">
{rects}
</svg>'''

with open('commit-calendar.svg', 'w') as f:
    f.write(svg)
