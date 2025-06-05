# Kanjigrid Timelapse

Generates timelapse videos using data exported from the [Kanjigrid](https://github.com/Kuuuube/kanjigrid) Anki addon ([AnkiWeb](https://ankiweb.net/shared/info/1610304449)).

## Usage

1. Install [dependencies](#dependencies).

2. Get some [Kanjigrid Timelapse Data](#getting-kanjigrid-timelapse-data).

3. (Optional) Edit settings in `config.ini`, `dark.css`, or `light.css`.

4. Download [kanjigrid-timelapse-master.zip](https://github.com/Kuuuube/kanjigrid-timelapse/archive/refs/heads/master.zip) and extract the zip.

5. Run `generate.py` and input your json file path.

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

For advanced users: Linux venv scripts are provided `setup_venv.sh` `run_venv.sh`.

1. Python 3: [Download link](https://www.python.org/downloads/)

    Windows: Make sure to check `Add Python 3.x to PATH` on the first page of the installer.

2. Python `playwright`, `pillow`, and `opencv` modules: To install it, enter the following command in cmd or a terminal:

    ```
    pip install playwright pillow opencv-python
    ```

3. Setup playwright dependency:

    Note: On some Linux distros, this may fail to install some features but still install the required features for `Kanjigrid Timelapse`. Check whether it works before troubleshooting.

    ```
    playwright install
    ```

    If the above command doesn't work, you may be missing some python path variables. Try this:

    ```
    python -m playwright install
    ```

## Example

Note: This is highly compressed.

https://github.com/user-attachments/assets/c6338085-5f2d-436c-a594-fde2db94850e
