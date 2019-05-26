import os
import threading


with open("url_list.txt", 'r') as f:
    video_list = f.readlines()


def get_url_list():
    global video_list
    if len(video_list) != 0:
        video = video_list[:20]
        video_list = video_list[20:]
        for item in video:
            os.system("you-get {}".format(item))




# def download_item(url_list):
#     for url in url_list:
#         os.system("you-get {}".format(url))


if __name__ == '__main__':
    for i in range(1,11):
        t = threading.Thread(target=get_url_list, args=())
        t.start()
