import cv2
import numpy as np

ascii_characters = ' .:-=+*#%@'
ascii_array = np.linspace(1, 256, len(ascii_characters))
video_name = 'bad apple.mp4'

def main():
    ascii_frames = []
    cap = cv2.VideoCapture(video_name)
    print(f'Is video opened: {cap.isOpened()}')
        
    while True:
        success, frame = cap.read()
        
        if success:
            ascii_frame = convert_from_frame_to_ascii(frame)
            ascii_frames.append(ascii_frame)
        else:
            break
    
    cap.release()
    print('cap finished')
    
    with open("data.txt", "w") as f:
        f.write('\nSPLIT'.join(str(item) for item in ascii_frames))
    
def convert_from_frame_to_ascii(frame):
    # 使用 NumPy 的 mean() 函數計算每個像素的平均灰度值
    gray = np.mean(frame, axis=2).astype(np.uint8)
    small_frame = cv2.resize(gray, (80, 45))
    ascii = ""
    
    # 使用二元搜尋來尋找最接近的 ASCII 字元
    for i, pixel in enumerate(small_frame.flat):
        ascii += ascii_characters[np.searchsorted(ascii_array, pixel, side='right')]
        if (i + 1) % 80 == 0:
            ascii += "\n"
            
    return ascii

if __name__ == '__main__':
    main()