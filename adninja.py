import cv2
import os

def playvideo():
    where_to_look = '/root/Documents/Python/Videos'
    total_videos = (len([f for f in os.listdir(where_to_look) if os.path.isfile(os.path.join(where_to_look, f))]))	
    while True:
        for y in range(total_videos):
            y+=1
            z=str(y)
            Videospath="Videos/"
            currentpath=Videospath+z
            print(currentpath)
            filepath=currentpath+'.mp4'
            video = cv2.VideoCapture(filepath)
            cv2.namedWindow('Capturing',cv2.WINDOW_NORMAL)
            cv2.setWindowProperty('Capturing', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
            frames_counter = 1

            while True:
                frames_counter = frames_counter + 1
                check, frame = video.read()
                # print(frame)
                # print(check)
                if check:
                    cv2.imshow("Capturing", frame)
                    key = cv2.waitKey(1)
                else:
                    break

            print("Number of frames in the video: ", frames_counter)
            video.release()

    cv2.destroyAllWindows()

def main():
        playvideo()

if __name__ == '__main__':
    main()
