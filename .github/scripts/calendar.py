import datetime
from collections import defaultdict

# 색상 정의
COLOR_COMMIT = "#ffc0cb"  # 라이트 핑크
COLOR_EMPTY = "#ebedf0"   # 회색

# 날짜별 커밋 수 저장
commit_days = set()
try:
    with open('commits.txt') as f:
        for line in f:
            date = line.strip()
            if date:
                commit_days.add(date)
    print(f"Found {len(commit_days)} commit days: {commit_days}")
except Exception as e:
    print(f"Error reading commits.txt: {e}")
    commit_days = set()

# 오늘 날짜 확인
today = datetime.date.today()
print(f"Today is {today.isoformat()}")

# SVG 만들기
start_date = today - datetime.timedelta(days=364)
weeks = [[]]
current_week = 0

for i in range(365):
    day = start_date + datetime.timedelta(days=i)
    date_str = day.isoformat()
    
    # 디버깅: 오늘 날짜가 커밋 날짜 목록에 있는지 확인
    if date_str == today.isoformat():
        print(f"Today ({date_str}) is in commit_days: {date_str in commit_days}")
    
    color = COLOR_COMMIT if date_str in commit_days else COLOR_EMPTY
    
    # 주의 첫 번째 날짜인 경우 새로운 주 시작
    if day.weekday() == 0 and i > 0:
        weeks.append([])
        current_week += 1
    
    rect = f'<rect x="{current_week*13}" y="{day.weekday()*13}" width="10" height="10" fill="{color}" rx="2" ry="2"/>'
    weeks[-1].append(rect)

rects = "\n".join(["\n".join(week) for week in weeks])

# SVG 조립
svg_width = (len(weeks))*13 + 2  # 약간의 마진 추가
svg = f'''<svg width="{svg_width}" height="100" xmlns="http://www.w3.org/2000/svg">
{rects}
</svg>'''

with open('commit-calendar.svg', 'w') as f:
    f.write(svg)

print("SVG calendar created successfully")
