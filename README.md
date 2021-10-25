## Camera Calibration Utilities

### Acquiring Calibration Frames

Run **`grab_calibration_frames.py`** and press "s" to save the frame containing the chessboard.
The frames will be saved in the calibration_data/calibration_frames folder.

Run **`camera_calibration.py`** to get the camera matrix and distortion coefficients.
The parameters will be saved in the file calibration_data/calibration.npz.

To load the parameters in your scripts do the following:

```

with np.load("calibration_data/calibration.npz") as X:
    mtx, dist, rvecs, tvecs, w, h, pattern_size, rms = [X[i] for i in ("camera_matrix", "dist_coefs", "rvecs", "tvecs", "w", "h", "pattern_size", "rms")]

```