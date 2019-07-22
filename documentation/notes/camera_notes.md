#### Notes on endoscope camera
- The Pi Zero shows a very laggy video feed from the camera (using VLC Player).
Have to check if loading video capture within Python code is better. Based on its power consumption (135mA), most likely will have to disable continuous video capture and only enable it when required by user, e.g. through GUI touch button. Image will still be taken when trigger button is pressed.
- Camera cable to be modified, being too stiff right now. Camera's integrated LEDs can be disabled to save power.
