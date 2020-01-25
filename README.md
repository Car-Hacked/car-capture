# Car Capture

HackMT 2020. Car Hacked.

This is the repo for capturing car data.

## Requirements
- `python3`

## Installation
Make sure you have `python3` installed. Once it is, run `python3 -m venv venv` to create a virtual environment. Then run `source venv/bin/activate` to activate it. *Make sure your environment is running everytime you need to develop or run the application.* When your environment is activated, run `pip install -r requirements` to install the required packages.

## Running the program
Start the IP Cam app on your phone and note the IP address provided. To run the program, enter `python capture.py rtsp://<your_ip>`. You should see a frame appear that mirrors your phone's camera.
