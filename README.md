# Camera Calibration Utilities

## Quick start

Setup the python pyenv working environment as described in [this guide](https://github.com/csermac/environment)

Install the dependencies:

```pip install -r requirements.txt```

Run ```grab_calibration_frames.py``` and press "s" to save the frame containing the chessboard.
The frames will be saved in the calibration_data/calibration_frames folder.

Run ```camera_calibration.py``` to get the camera matrix and distortion coefficients.
The parameters will be saved in the file calibration_data/calibration.npz.

To load the parameters in your scripts do the following:

```
import numpy as np

with np.load("calibration_data/calibration.npz") as X:
    mtx, dist, rvecs, tvecs, w, h, pattern_size, rms = [X[i] for i in ("camera_matrix", "dist_coefs", "rvecs", "tvecs", "w", "h", "pattern_size", "rms")]

```

## Bugs and feature requests

Have a bug or a feature request? Please first read the [issue guidelines](https://github.com/csermac/camera_calibration/blob/main/CONTRIBUTING.md) and search for existing and closed issues. If your problem or idea is not addressed yet, [please open a new issue](https://github.com/csermac/face/issues/new).

## Contributing

Please read through our [contributing guidelines](https://github.com/csermac/camera_calibration/blob/main/CONTRIBUTING.md). Included are directions for opening issues, coding standards, and notes on development.

For informations on code styling and conventions consult the [lab style and conventions guide](https://github.com/csermac/conventions)

## Creators

**Federico Zappone**

- <https://github.com/federicozappone>

## Copyright and license

Code and documentation copyright 2011-2018 the authors. Code released under the [MIT License](https://github.com/csermac/camera_calibration/blob/master/LICENSE.md).