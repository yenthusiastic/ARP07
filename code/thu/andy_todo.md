## main.py
### def trigger_pressed_cb
set **self.session_datetime** at start-up, after first reading from RTC
greate session folder after that (independet from trigger press)

if trigger pressed:
  - append trigger_data to data.csv
    - header: timestamp, gps, data[array]
    - format: string, string, array



## SpectrometerGUI.py
change def calibrate_ref
  - if called, append the calibration data into "calibration.csv" in the session folder
  - check if file exists, else create it
    - format: header: timestamp, ref_1, ref_2
