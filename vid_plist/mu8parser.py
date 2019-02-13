import os
import sys
import shutil

def parse_copy(m3u8_file_path, copy_path):

    vid_path = os.path.dirname(m3u8_file_path)

    # Parse playlist for filenames with ending .ts and put them into the list ts_filenames
    with open(m3u8_file_path, 'r') as playlist:
        ts_filenames = [line.lstrip() for line in playlist
                        if line.rstrip().endswith('.mp4') and not line.lstrip().startswith("#") ]

    vid_dir = ts_filenames[0].split('/')[-2]
    copy_dir = os.path.join(copy_path, vid_dir)

    if not os.path.isdir(copy_dir):
        os.mkdir(copy_dir, 0o755)

    for video_file in ts_filenames:
        video_file = os.path.join(vid_path,video_file)
        vid_fname = video_file.split('/')[-1]

        vid_copy = os.path.join(copy_dir, vid_fname)
        shutil.copyfile(video_file, vid_copy)


if __name__=='__main__':
    m3u8path = None
    copied_path = None

    if len(sys.argv) <= 2:
        m3u8path = '/home/deer_meat/Downloads/unloading.m3u8'
        copied_path = '/home/deer_meat/Dropbox/moments-subselection/'
    else:
        m3u8path = sys.argv[1]
        copied_path = sys.argv[2] # '/home/deer_meat/Dropbox/moments-subselection/'

    parse_copy(m3u8path, copied_path)