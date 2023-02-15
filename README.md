# librarymanager
A Python script designed to automatically rename and edit the metadata of large media libraries, allowing for easier management of your movies and tv shows

# Dependancies
* ffmpeg

##pip packages:
* python-decouple
* tmdbv3api

# Setup
* Create a .env file in the same directory as the python file
* Add the line ```API_KEY='Your TMDb API Key'```
* Run the python script

## Current limitations
* only does tv shows
* Expects media files to be in folders named the correct TV show's name
* Doesn't remove the old media after renaming and changing the metadata
* expects all media folders to be in the directory above the librarymanager directory 
* Doesn't support nested directories
* Doesn't support any seasons other than the first of any TV show
