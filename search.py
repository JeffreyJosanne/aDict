from datetime import timedelta
import codecs, sys, subprocess, csv
from imp import reload
reload(sys)
start_times=[]
end_times=[]
actual_start_time=[]
actual_end_time=[]
with codecs.open('test.srt', 'r', 'utf8') as file:
    csvWriter = csv.writer(open('test.csv', 'w'))
    lines = file.readlines()
    for line in lines:
        if '-->' in line:
            list = line.split(' ')
            start_times.append(list[0])
            end_times.append(list[2].strip('\r\n'))
    for one_temp_start_time, one_temp_end_time in zip(start_times, end_times):
        start_at = 0
        end_at = 0
        one_start_time_list=one_temp_start_time.split(':')
        minutes = int(one_start_time_list[1])
        seconds =int(one_start_time_list[2].replace(',', ''))
        if(int(one_start_time_list[0])!=0):
            minutes = minutes + int(one_start_time_list[0])*60
        start_at =seconds +minutes * 60
        actual_start_time.append(start_at)
        one_end_time_list = one_temp_end_time.split(':')
        minutes = int(one_end_time_list[1])
        seconds = int(one_end_time_list[2].replace(',', ''))
        if (int(one_end_time_list[0]) != 0):
            minutes = minutes + int(one_end_time_list[0]) * 60
        end_at = seconds + minutes *60
        actual_end_time.append(end_at)
if(len(actual_start_time)>0):
    actual_start_time.pop(0)

for one_actual_start_time, one_actual_end_time in zip(actual_start_time, actual_end_time):
    diff = (one_actual_start_time) - (one_actual_end_time)
    if((diff)>0):
        csvWriter.writerow([one_actual_start_time, one_actual_end_time])
        print(diff/1000)
        print(str(one_actual_start_time/1000)+'-->'+str(one_actual_end_time/1000))

    # subprocess.call('ffmpeg -i test_video.mp4 -ss 00:00:07 -to 00:00:13 -async 1 cut.mp4', shell=True)