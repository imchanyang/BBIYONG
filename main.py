from webcam import *
from server import app



if __name__ == '__main__':
    # save_video_from_webcam();
    # load_video();

    app.run(host='0.0.0.0', port = 5000, debug=True)



