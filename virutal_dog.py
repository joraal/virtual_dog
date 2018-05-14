import os
#import vlc
from pygame import mixer


def print_headers():
    print('-------------------------------------')
    print('           virtualdog app')
    print('-------------------------------------')

def play_file(filepath):
    mixer.init()
    print("playing : " + filepath )
    mixer.music.load(filepath)
    mixer.music.play()


def get_dog_file(full_file):
    pass

def play_in_folders(folder):
    # all_matches = []
    items = os.listdir(folder)

    for item in items:
        full_item = os.path.join(folder, item)
        if os.path.isdir(full_item):
            # matches = search_folders(full_item, text)
            # all_matches.extend(matches)

            # for m in matches:
            #     yield m
            # yield from matches
            # yield from search_folders(full_i)
            print("folder "+ full_item)

        else:
            #yield from search_file(full_item, text)
            # all_matches.extend(matches)
            # for m in matches:
            #     yield m
            play_file(full_item)
            print("file {} ",format(full_item))



def main():
    print_headers()
    folder = "dogfiles"
    filepath = os.path.abspath(folder)

    print(filepath)

    play_in_folders(folder)





if __name__ == '__main__':
   main()

