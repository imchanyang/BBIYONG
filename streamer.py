
import cv2


def stream():  # generate frame by frame from camera

    camera = cv2.VideoCapture(0)  # use 0 for web camera

    while True:

        # Capture frame-by-frame

        success, frame = camera.read()  # read the camera frame

        if (not success):

            break

        else:

            ret, buffer = cv2.imencode('.jpg', frame)

            frame = buffer.tobytes()
            # jpgBin = bytearray(buffer.tobytes())

            yield (b'--frame\r\n'

                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

                   # concat frame one by one and show result
