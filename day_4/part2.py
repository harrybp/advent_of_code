import re
from datetime import datetime
import numpy as np

def add_minutes(minutes, sleep, wake):
    for i in range(sleep, wake):
        minutes[i] += 1
    return minutes

with open('input.txt') as f:
    content = f.readlines()
content = sorted(content)

guards = {}
asleep = False
on_duty = None
fell_asleep_at = None
for line in content:
    line_arr = re.findall('\d+', line)

    if len(line_arr) == 6:
        if line_arr[5] not in guards:
            guards[line_arr[5]] = np.zeros(60)
        on_duty = line_arr[5]
        continue

    if not asleep:
        asleep = True
        fell_asleep_at = int(line[15:17])
        continue

    else:
        asleep = False
        woke_up_at = int(line[15:17])
        guards[on_duty] = add_minutes(guards[on_duty], fell_asleep_at, woke_up_at)

max_time = 0
max_time_min = None
max_guard_id = None

for guard in guards:
    max_sleep = 0
    max_min = None
    for i, minute in enumerate(guards[guard]):
        if minute > max_sleep:
            max_sleep = minute
            max_min = i
    if max_sleep > max_time:
        max_guard_id = guard
        max_time_min = max_min
        max_time = max_sleep

print(max_guard_id)
print(max_time_min)
print(max_time)
print(int(max_guard_id) * int(max_time_min))