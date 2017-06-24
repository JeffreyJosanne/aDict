from datetime import timedelta
import codecs, sys, subprocess, csv, os
from imp import reload
reload(sys)
start_times=[]
end_times=[]
actual_start_time=[]
actual_end_time=[]
for file in os.listdir('subs/'):
    with codecs.open('subs/'+file, 'r', 'utf8') as file:
        sceneCount=0
        csvWriter = csv.writer(open('sceneCuts/'+file.name.split('/')[1].split('.')[0]+'.csv', 'w'))
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
            secondsTrimmer = one_start_time_list[2].split(',')[0]
            seconds =int(secondsTrimmer.replace(',', ''))
            if(int(one_start_time_list[0])!=0):
                minutes = minutes + int(one_start_time_list[0])*60
            start_at =seconds +minutes * 60
            actual_start_time.append(start_at)
            one_end_time_list = one_temp_end_time.split(':')
            minutes = int(one_end_time_list[1])
            secondsTrimmer = one_end_time_list[2].split(',')[0]
            seconds = int(secondsTrimmer.replace(',', ''))
            if (int(one_end_time_list[0]) != 0):
                minutes = minutes + int(one_end_time_list[0]) * 60
            end_at = seconds + minutes *60
            actual_end_time.append(end_at)
    if(len(actual_start_time)>0):
        actual_start_time.pop(0)

    for one_actual_start_time, one_actual_end_time in zip(actual_start_time, actual_end_time):
        diff = (one_actual_start_time) - (one_actual_end_time)
        if((diff)>5):
            csvWriter.writerow([one_actual_start_time, one_actual_end_time, sceneCount])
            sceneCount += 1
            print(diff)
            print(str(timedelta(seconds=one_actual_start_time))+'-->'+str(timedelta(seconds=one_actual_end_time)))

        # subprocess.call('ffmpeg -i test_video.mp4 -ss 00:00:07 -to 00:00:13 -async 1 cut.mp4', shell=True)