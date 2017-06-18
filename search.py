from datetime import timedelta
start_times=[]
end_times=[]
actual_start_time=[]
actual_end_time=[]
with open('test.srt','r') as file:
    lines = file.readlines()
    for line in lines:
        if '-->' in line:
            list = line.split(' ')
            start_times.append(list[0])
            end_times.append(list[2].strip('\r\n'))
    for one_temp_start_time, one_temp_end_time in zip(start_times, end_times):
        one_start_time_list=one_temp_start_time.split(':')
        actual_start_time.append(timedelta(int(one_start_time_list[0]), int(one_start_time_list[1]), int(one_start_time_list[2].replace(',', ''))))
        one_end_time_list= one_temp_end_time.split(':')
        actual_end_time.append(timedelta(int(one_end_time_list[0]), int(one_end_time_list[1]), int(one_end_time_list[2].replace(',', ''))))
actual_start_time.pop(0)

for one_actual_start_time, one_actual_end_time in zip(actual_start_time, actual_end_time):
    diff = (one_actual_start_time) - (one_actual_end_time)
    print(diff.total_seconds()*1000)
    print(str(one_actual_start_time)+'-->'+str(one_actual_end_time))