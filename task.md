# Task List - Customer Dialogue Simulation (Almanac)

- [x] [Design] Define Query Patterns <!-- id: 70 -->
    - [x] Pattern 1: 今天農曆幾號 (Today's Lunar) <!-- id: 71 -->
    - [x] Pattern 2: 下星期X農曆幾號 (Next Weekday Lunar) <!-- id: 72 -->
    - [x] Pattern 3: 初一/初二是國曆幾號 (Lunar to Solar) <!-- id: 73 -->
    - [x] Pattern 4: X月X日農曆是幾號 (Solar to Lunar) <!-- id: 74 -->
- [x] [Service] Enhance AlmanacService <!-- id: 75 -->
    - [x] Add `solar_to_lunar(date)` <!-- id: 76 -->
    - [x] Add `lunar_to_solar(lunar_month, lunar_day)` <!-- id: 77 -->
    - [x] Add `get_next_lunar_day(day)` (e.g. next 初一) <!-- id: 78 -->
- [x] [NLP] Create Query Parser <!-- id: 79 -->
    - [x] Create `services/query_parser.py` <!-- id: 80 -->
    - [x] Regex for date extraction <!-- id: 81 -->
    - [x] Regex for lunar terms (初一, 十五, etc.) <!-- id: 82 -->
- [x] [Bot] Integrate Parser into app.py <!-- id: 83 -->
- [x] [Test] Create Simulation Test Suite <!-- id: 84 -->
