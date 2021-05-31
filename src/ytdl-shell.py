#!/usr/bin/env python3

from __future__ import unicode_literals
import argparse
import youtube_dl


def getopts():
    '''
    returns a filename
    '''
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--filename", help="source filename")
    return parser.parse_args().filename


def shell():
    url = input("enter url: ")
    name = input("enter new file name: ")
    download_song(url, name)
    while again := input("download another? y/n: "):
        if again == "y":
            shell()
        elif again != "n":
            print("invalid, plese enter y or n")
            continue
        exit()


def clean_line(line):
    u, t, n = line.split("|")
    return [u.strip(), t.strip(), n.strip()]


def read_file(f):
    '''
    read a file and return valid lines
    valid lines are in format
    url | {m,v} | string with space
    '''
    return_data = []
    with open(f, "r") as fil:
        for line in fil.read().split("\n"):
            if len(line.split("|")) == 3:
                return_data.append(clean_line(line))
    return return_data


def my_hook(d):
    if d['status'] == 'finished':
        print('Done downloading, now converting ...')


def download_song(url, name):
    opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
        }],
        'progress_hooks': [my_hook],
        'outtmpl': f'{name}.%(ext)s',
    }
    with youtube_dl.YoutubeDL(opts) as ydl:
        ydl.download([url])


def main():
    filename = getopts()
    if filename == None:
        print("starting shell...")
        shell()
    data = read_file(filename)
    for item in data:
        if item[1] == "m":
            download_song(item[0], item[2])


if __name__ == "__main__":
    main()
