time = '1h 45m,360s,25m,30m 120s,2h 60s'

time_list = time.split(',')

total_time = []

for i in time_list:
    separate_time = i.split(' ') 

    for i2 in separate_time: 
        if 'h' in i2:
            hour = i2.replace('h', '')
            total_time.append(int(hour) * 60)
        elif 'm' in i2:
            total_time.append(int(i2.replace('m', '')))
        elif 's' in i2:
            total_time.append(int(i2.replace('s', '')) // 60) 

print(sum(total_time))           