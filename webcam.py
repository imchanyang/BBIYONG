import cv2


def webcam():
    cap = cv2.VideoCapture(0)  # load WebCamera
    print('width:', cap.get(3), ' height:', cap.get(4))

    videoFileName = 'output.mp4'
    w = round(cap.get(cv2.CAP_PROP_FRAME_WIDTH)) # width
    h = round(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)) #height
    fps = cap.get(cv2.CAP_PROP_FPS) #frame per second
    fourcc = cv2.VideoWriter_fourcc(*'mp4v') #fourcc
    delay_ = round(1000/fps) #set interval between frame

    out = cv2.VideoWriter(videoFileName, fourcc, fps, (w,h))
    if not (out.isOpened()):
        print("File isn't opend!!")
        cap.release()
        sys.exit()

    while(True): #Check Video is Available
        ret, frame = cap.read() #read by frame (ret=TRUE/FALSE)s

        if ret:
            cv2.imshow('viedo', frame)
            if cv2.waitKey(delay_) == 27: #wait 10ms until user input
                break

        else:
            print("ret is false")
            break

    cap.release() #release memory
    out.release() #release memory
    cv2.destroyAllWindows() #destroy All Window


def save_video_from_webcam():
    cap = cv2.VideoCapture(0)  # load WebCamera
    print('width:', cap.get(3), ' height:', cap.get(4))

    videoFileName = 'output.mp4'
    w = round(cap.get(cv2.CAP_PROP_FRAME_WIDTH)) # width
    h = round(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)) #height
    fps = cap.get(cv2.CAP_PROP_FPS) #frame per second
    fourcc = cv2.VideoWriter_fourcc(*'mp4v') #fourcc
    delay_ = round(1000/fps) #set interval between frame

    out = cv2.VideoWriter(videoFileName, fourcc, fps, (w,h))
    if not (out.isOpened()):
        print("File isn't opend!!")
        cap.release()
        sys.exit()

    while(True): #Check Video is Available
        ret, frame = cap.read() #read by frame (ret=TRUE/FALSE)s

        if ret:
            out.write(frame) #save video frame
            cv2.imshow('viedo', frame)
            if cv2.waitKey(delay_) == 27: #wait 10ms until user input
                break

        else:
            print("ret is false")
            break

    cap.release() #release memory
    out.release() #release memory
    cv2.destroyAllWindows() #destroy All Window



def load_video():
    videoFile = '/home/ubuntu/BBIYONG/output.mp4' #read video file
    cap = cv2.VideoCapture(videoFile) #load as a VideoCapture class
    fps = cap.get(cv2.CAP_PROP_FPS)
    delay_ = round(1000/fps)
    print(cap.get(cv2.CAP_PROP_FPS))
    while(cap.isOpened()): #Check Video is Available
        ret, frame = cap.read() #read by frame (ret=TRUE/FALSE)

        if ret:
            cv2.imshow('VIDEO', frame)
            if cv2.waitKey(delay_) == 27: #wait 10ms until user input
                break
        else:
            print("ret is false")
            break

    cap.release() #release memory
    cv2.destroyAllWindows() #destroy All Window
