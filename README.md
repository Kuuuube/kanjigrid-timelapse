# Kanjigrid Timelapse

Generates timelapse videos using data exported from the [Kanjigrid](https://github.com/Kuuuube/kanjigrid) Anki addon ([AnkiWeb](https://ankiweb.net/shared/info/1610304449)).

## Usage

1. Install [dependencies](#dependencies).

2. Get some [Kanjigrid Timelapse Data](#getting-kanjigrid-timelapse-data).

3. (Optional) Edit settings in `config.ini`, `dark.css`, or `light.css`.

4. Run `generate.py` and input your json file path.

    If the video didn't turn out how you wanted but the image data is good, answer `y` to the `Skip image generation` prompt when running `generate.py`.

## Getting Kanjigrid Timelapse Data

1. Install the [Kanjigrid Anki addon](https://github.com/Kuuuube/kanjigrid/blob/master/README.md#installation)

2. In Anki, on the top menu, go to Tools > Generate Kanji Grid.

3. Set any settings you want for the timelapse.

4. Select the `Data` tab.

5. Set the timelapse range and step size under `Timelapse`.

6. Click `Generate Timelapse Data` and select somewhere to save the file.

    It can take a VERY long time to generate this data for large grids, long timespans, or small step sizes.

## Dependencies

Python 3: [Download link](https://www.python.org/downloads/)

Python `playwright`, `pillow`, and `opencv` modules: To install it, enter the following command in cmd or a terminal:

```
pip install playwright pillow opencv-python
```

Setup playwright dependency:

Note: On some Linux distros, this may fail to install some features but still install the required features for `Kanjigrid Timelapse`. Check whether it works before troubleshooting.

```
playwright install
```
