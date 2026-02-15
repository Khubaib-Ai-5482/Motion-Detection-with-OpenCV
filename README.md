# Motion Detection with OpenCV

This project detects motion from a live webcam, image, or video file using OpenCV. It highlights areas of motion, shows the timestamp on frames, and can save motion-detected frames to a video file.

## Features
- **Live Webcam Monitoring**: Detect motion in real-time from your webcam.
- **Image Input**: Compare a single image with a reference to detect changes.
- **Video Input**: Detect motion in pre-recorded video files.
- Highlights motion areas with green rectangles.
- Displays the current timestamp on each frame.
- Saves frames with detected motion to `motion_capture.avi`.

## Requirements
- Python 3.x
- OpenCV library

```bash
pip install opencv-python
