try:
    from pytube import YouTube
    from pytube import Playlist
except:
    print("cannot import Youtube or Playlist")
# download music from youtube
# import re
# playlist = Playlist('https://www.youtube.com/playlist?list=PLtDwx4fu48jIHZ2f7RTI4Aoxxs3WGn0Oh')
# playlist._video_regex = re.compile(r"\"url\":\"(/watch\?v=[\w-]*)")
# # without re.compile it cannot find any thing due to the pattern search, so we have to change the format of the regular expression
#
# # print(len(playlist))
#
# for url in playlist:
#
#
#     youtube = YouTube(url).streams.filter(progressive=True).order_by('resolution').desc()
#     # progress mean have both audio and video
#     output = "C:/Users/Owner/Downloads/Music"
#     youtube = youtube.first().download(output)



# convert mp4 to mp3
# import moviepy.editor
# import os
#
# path = "C:/Users/Owner/Downloads/Music"
# source_path = os.listdir(path)
# dest_path=""
# vid=moviepy.editor
# dest_path="C:/Users/Owner/Downloads/song"
# for title in source_path:
#     name= title.replace(".mp4", ".mp3")
#     # title= title.replace(" MV.mp4", " MV")
#     # video = VideoFileClip(title) you have to close the audio and video every time
#     # audio= VideoClip.audio
#     video = vid.VideoFileClip(path+"/"+title)
#     audio = video.audio
#     audio.write_audiofile(dest_path+"/"+name)

# playlist.download_all()
#  Call to deprecated function _path_num_prefix_generator (This function will be removed in the future.).
#   prefix_gen = self._path_num_prefix_generator(reverse_numbering)



# url = "https://www.youtube.com/watch?v=Uqi34thogl4&list=PLTn4feGbf_VqxPUZKKY_Ah140wi05b8Wi&index=2&t=0s"
# url="https://www.youtube.com/watch?v=CbFh06IpSwA"
# # youtube = YouTube(url).streams.filter(progressive=True).order_by('resolution').desc()
# youtube = YouTube(url).streams.filter(only_audio=True)
# output="C:/Users/Owner/Downloads/Music"
# youtube=youtube.first().download(output)
# # stream is the quality of the video
# print(youtube)


# from pytube import YouTube
# YouTube('https://youtu.be/9bZkp7q19f0').streams.get_highest_resolution().download()
# yt = YouTube('http://youtube.com/watch?v=9bZkp7q19f0')
# yt.streams
