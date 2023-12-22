import os

"""get name of all folders (albums) in current directory
search list of names for matching artists
create new directory with artist folder as parent directory for respective albums.

construct a dictionary of {key} artists and {val} albums, then iterate through that dictionary with os.mkdir()"""

#files_to_list = os.listdir('.')
files_to_list = [os.listdir('.')]

print(folders_to_list)

"""lastfm API Key: 1f11ff1e36a68e99d3316cc583d98d48
#lastfm Shared Secret: 436ffae88df4e8a165683f2aba2510e5
album.search link:https://ws.audioscrobbler.com/2.0/?method=album.search&album=_____&api_key=1f11ff1e36a68e99d3316cc583d98d48&limit=1"""

"""with open('filenames.txt', 'w') as f:
    f.writelines('\n'.join(folders_to_list))"""


#artists = ['/n'.join[os.listdir('.')]]

#def album_match():
#    for artist in artists:




#albums = ['/n'.join(album_match)]

#dictionary {artist} {album} 

#matched = {}