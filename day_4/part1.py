import re
from datetime import datetime
import numpy as np

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
            guards[line_arr[5]] = 0
        on_duty = line_arr[5]
        continue

    if not asleep:
        asleep = True
        fell_asleep_at = datetime.strptime(line[12:17],'%H:%M')
        continue

    else:
        asleep = False
        woke_up_at = datetime.strptime(line[12:17],'%H:%M')
        slept_for = woke_up_at - fell_asleep_at
        slept_for = slept_for.seconds / 60
        guards[on_duty] += slept_for

longest = 0
longest_id = None
for guard in guards:
    if guards[guard] > longest:
        longest = guards[guard]
        longest_id = guard

minutes = np.zeros(60)
sleep_minute = None
wakeup_minute = None
our_guard = False

def add_minutes(minutes, sleep, wake):
    for i in range(sleep, wake):
        minutes[i] += 1
    return minutes



sleeping = False
for line in content:
    line_arr = re.findall('\d+', line)
    if len(line_arr) == 6 and line_arr[5] == longest_id:
        our_guard = True
        continue
    elif len(line_arr) == 6:
        our_guard = False
        continue
    
    if our_guard and not sleeping:
        sleep_minute = int(line[15:17])
        sleeping = True
        continue

    if our_guard and sleeping:
        wakeup_minute = int(line[15:17])
        minutes = add_minutes(minutes, sleep_minute, wakeup_minute)
        sleeping = False

print(minutes)
max_sleep = 0
max_min = None
for i, minute in enumerate(minutes):
    if minute > max_sleep:
        max_sleep = minute
        max_min = i

print(int(max_min) * int(longest_id))

    
    

    