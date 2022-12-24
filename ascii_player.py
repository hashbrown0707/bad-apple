import os, sys
import time
import pygame
 
FPS = 67

def main():
    raw_frames = get_raw_frames()
    frames = raw_frames.split('SPLIT')
    pygame.init()
    pygame.mixer.music.load('bad apple.mp3')
    pygame.mixer.music.play()
            
    timer = time.perf_counter()
    for frame in frames:
        elapsed_time = time.perf_counter() - timer
        delay = 1.0 / FPS - elapsed_time
        
        if delay > 0:
            time.sleep(delay)
            
        # print('\033c')
        os.system('cls')
        sys.stdout.write(frame)
        timer = time.perf_counter()
        
    # for frame in frames:
    #     time.sleep(1.0 / FPS)
    #     os.system('cls')
    #     print(frame)

def get_raw_frames():
    with open('data.txt', 'r') as f:
        return f.read()

if __name__ == "__main__":
    main()
