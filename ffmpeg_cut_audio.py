import sys
import os

def ffmpeg_cut_audio(input_filename, output_filename, start_time, end_time, ffmpeg_location='C:\\"Program Files (x86)"\\"FFmpeg for Audacity"\\'):
    print(input_filename)
    print(output_filename)
    print(start_time)
    print(end_time)
    print(ffmpeg_location)
    cmd_str = ffmpeg_location + 'ffmpeg'
    print(cmd_str)
    os.system(cmd_str)


if __name__ == '__main__':
    ffmpeg_cut_audio(1,2,3,4)