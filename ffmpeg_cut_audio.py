import sys
import os

def ffmpeg_cut_audio(input_filename, output_filename, start_time, end_time, ffmpeg_location='C:\\"Program Files (x86)"\\"FFmpeg for Audacity"\\'):
    '''

        ffmpeg -i input.mp4 -ss 00:00:00 -to 00:10:00 -c copy output1.mp4
        ffmpeg -i input.mp4 -ss 00:10:00 -to 00:20:00 -c copy output2.mp4

        /**
        * -i  input file
        * -ss start time in seconds or in hh:mm:ss
        * -to end time in seconds or in hh:mm:ss
        * -c codec to use
        */
    '''
    # print(input_filename)
    # print(output_filename)
    # print(start_time)
    # print(end_time)
    # print(ffmpeg_location)
    cmd_str = ffmpeg_location + 'ffmpeg -i ' + input_filename + ' -ss ' + start_time + ' -to ' + end_time + ' ' + output_filename
    print(cmd_str)
    os.system(cmd_str)


if __name__ == '__main__':
    input_filename = '"C:\\Users\\pwara\\OneDrive - infomobius.com\\02-Customer Projects\\NBTC_Voice\\input\\test1.mp4"'
    output_filename = '"C:\\Users\\pwara\\OneDrive - infomobius.com\\02-Customer Projects\\NBTC_Voice\\input\\test1_output.mp4"'
    start_time = '00:00:05'
    end_time = '00:00:10'
    ffmpeg_cut_audio(input_filename, output_filename, start_time, end_time)