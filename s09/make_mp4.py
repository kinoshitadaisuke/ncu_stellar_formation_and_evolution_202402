#!/usr/pkg/bin/python3.12

#
# Time-stamp: <2024/04/12 12:23:40 (UT+8) daisuke>
#

# importing argparse module
import argparse

# importing sys module
import sys

# importing subprocess module
import subprocess

# initialising a parser
desc   = 'making a MP4 movie file from a set of image files'
parser = argparse.ArgumentParser (description=desc)

# adding arguments
parser.add_argument ('-d', '--dir', default='', \
                     help='directory storing images')
parser.add_argument ('-o', '--output', default='', \
                     help='output file name')
parser.add_argument ('-f', '--ffmpeg', default='ffmpeg', \
                     help='ffmpeg command name')
parser.add_argument ('-t', '--thread', type=int, default=8, \
                     help='number of thread (default: 8)')
parser.add_argument ('-r', '--framerate', type=int, default=30, \
                     help='frame rate in frame per sec (default: 30)')

# parsing arguments
args = parser.parse_args ()

# parameters
dir_images     = args.dir
file_output    = args.output
command_ffmpeg = args.ffmpeg
n_thread       = args.thread
framerate      = args.framerate

# check of directory name
if (dir_images == ''):
    print (f'ERROR: directory name has to be given!')
    sys.exit (0)

# check of output file name
if (file_output == ''):
    print (f'ERROR: output file name has to be given!')
    sys.exit (0)
    
# ffmpeg options
options_ffmpeg = f'-f image2 -i {dir_images}/{dir_images}_%08d.png' \
    + f' -start_number 0 -framerate {framerate}' \
    + f' -an -vcodec libx264 -pix_fmt yuv420p' \
    + f' -threads {n_thread}'

# command to be executed
command_ffmpeg = f'{command_ffmpeg} {options_ffmpeg} {file_output}'

# execution of command
subprocess.run (command_ffmpeg, shell=True)
