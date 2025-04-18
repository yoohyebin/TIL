import datetime
import os
import re

# 색상 정의
COLOR_COMMIT = "#ffc0cb"  # 라이트 핑크
COLOR_EMPTY = "#ebedf0"   # 회색

# README.md 파일 경로
README_PATH = "README.md"

# 오늘 날짜 가져오기
today = datetime.date.today()
today_str = today.strftime("%Y-%m-%d")

print(f"Today's date: {today_str}")

# 2025년 1월 1일부터 시작하는 날짜 생성
start_date = datetime.date(2025, 1, 1)
days_to_generate = (datetime.date(2025, 12, 31) - start_date).days + 1

dates = []
for i in range(days_to_generate):
    day = start_date + datetime.timedelta(days=i)
    dates.append(day.strftime("%Y-%m-%d"))

# SVG 생성
SVG_WIDTH = 830
SVG_HEIGHT = 128
CELL_SIZE = 11
CELL_MARGIN = 2

svg_start = f"""<svg width="{SVG_WIDTH}" height="{SVG_HEIGHT}" viewBox="0 0 {SVG_WIDTH} {SVG_HEIGHT}"
     xmlns="http://www.w3.org/2000/svg">
  <style>
    .cell {{ stroke: #1b1f230a; stroke-width: 1px; }}
    .cell:hover {{ stroke: #1b1f23; stroke-width: 1px; }}
    .text {{ font: 10px sans-serif; fill: #767676; }}
  </style>
  <g transform="translate(20, 20)">
"""

# 월 이름 추가 
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
for i in range(12):
    month_date = datetime.date(2025, 1, 1) + datetime.timedelta(days=30*i)
    month_idx = month_date.month - 1
    x = i * (CELL_SIZE + CELL_MARGIN) * 4.3 + 35  # 월 위치 조정
    svg_start += f'    <text x="{x}" y="-5" class="text">{months[month_idx]}</text>\n'

# 요일 표시 제거 (요청에 따라)

svg_cells = ""
commits_data = {}

# commits.txt 파일에서 커밋 데이터 읽기
try:
    with open('commits.txt', 'r') as f:
        for line in f:
            date = line.strip()
            if date in commits_data:
                commits_data[date] += 1
            else:
                commits_data[date] = 1
    print(f"Found commits for dates: {list(commits_data.keys())}")
except Exception as e:
    print(f"Error reading commits.txt: {e}")

# 오늘 날짜가 commits.txt에 있는지 확인
print(f"Today ({today_str}) in commits_data: {today_str in commits_data}")

# 각 날짜에 대한 셀 생성
for week_idx in range(53):  # 53주 (2025년은 53주가 될 수 있음)
    for day_idx in range(7):  # 7일
        date_idx = week_idx * 7 + day_idx
        
        if date_idx >= len(dates):
            continue
            
        date = dates[date_idx]
        x = week_idx * (CELL_SIZE + CELL_MARGIN) + 30  # x 위치 계산
        y = day_idx * (CELL_SIZE + CELL_MARGIN) + 5    # y 위치 계산
        
        # 커밋이 있으면 핑크색, 없으면 회색
        color = COLOR_COMMIT if date in commits_data else COLOR_EMPTY
        
        # 오늘 날짜인 경우 특별히 표시
        if date == today_str:
            print(f"Marking today's cell ({date}) with color: {color}")
            stroke = 'stroke="#000" stroke-width="2"'
        else:
            stroke = ''
            
        svg_cells += f'    <rect x="{x}" y="{y}" width="{CELL_SIZE}" height="{CELL_SIZE}" rx="2" ry="2" fill="{color}" class="cell" data-date="{date}" {stroke}/>\n'

svg_end = """  </g>
</svg>"""

full_svg = svg_start + svg_cells + svg_end

# SVG 파일 저장
with open('commit-calendar.svg', 'w') as f:
    f.write(full_svg)
print("SVG calendar created successfully")

# README 파일 업데이트
readme_content = ""
readme_marker_start = "<!-- COMMIT-CALENDAR-START -->"
readme_marker_end = "<!-- COMMIT-CALENDAR-END -->"

calendar_content = f"{readme_marker_start}\n## Commit Calendar\n\n![Commit Calendar](./commit-calendar.svg)\n\nLast updated: {today_str}\n{readme_marker_end}"

# README.md 파일이 있는지 확인
if os.path.exists(README_PATH):
    with open(README_PATH, 'r', encoding='utf-8') as f:
        readme_content = f.read()
    
    # 마커가 있는지 확인
    if readme_marker_start in readme_content and readme_marker_end in readme_content:
        # 마커 사이의 내용 교체
        pattern = f"{readme_marker_start}.*?{readme_marker_end}"
        readme_content = re.sub(pattern, calendar_content, readme_content, flags=re.DOTALL)
    else:
        # 마커가 없으면 README 끝에 추가
        readme_content += f"\n\n{calendar_content}"
else:
    # README가 없으면 새로 생성
    readme_content = f"# TIL\n\n{calendar_content}"

# 수정된 README 저장
with open(README_PATH, 'w', encoding='utf-8') as f:
    f.write(readme_content)
print("README.md updated successfully")
