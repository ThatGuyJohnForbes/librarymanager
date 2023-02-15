#!/usr/bin/env python3

import os
import asyncio
from decouple import config
from tmdbv3api import TMDb, Movie, TV, Season
import math


def check_dir(path):
    files = os.listdir(path)
    print(path)
    tmdb = TMDb()
    tmdb.api_key = config('API_KEY')
    tv = TV()
    show = tv.search(path)
    if not show:
        return
    season_number = 1
    show_season = Season().details(show[0].id, season_number)
    order_of_mag_of_episode_count = math.ceil(math.log(len(files),10)) #this allows us to pad the episode number with the correct amount of leading zeros
    for x in range(0,len(files)):
        episode = show_season.episodes[x]
        print(files[x])
        newfilename = f"({show[0].name}) [S{season_number}E{str(episode.episode_number).zfill(order_of_mag_of_episode_count)}] {episode.name}"
        print(newfilename)
        ffmpeg_command = f'ffmpeg -loglevel quiet -i "{path}/{files[x]}" -metadata title="{episode.name}" -metadata show="{show[0].name}" -metadata episode_id={episode.episode_number} -c copy -map 0 "{path}/{newfilename}.mkv"'
        print(f"Running: {ffmpeg_command}")
        os.system(ffmpeg_command)

if __name__ == "__main__":
    os.chdir('..')
    dirs = [x[0] for x in os.walk('.') if x[0] != '.' and x[0] != '..' and "librarymanager" not in x[0]]
    for dir in dirs:
        check_dir(dir)


