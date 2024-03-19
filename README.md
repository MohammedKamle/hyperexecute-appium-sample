# Hyperexecute-Appium-Sample


## Setup
* Clone the repo
* Add your username and accesskey in `and.py`
* Upload QATestApp.apk present in the main directory and add the corresponding app_url in "app" capability



## Running the appium test on hyperececute 
* Do `chmod +x hyperexecute` on your terminal for permissions if using mac
* If you are running on linux/Gitod, then first delete the existing binary in the project and install linux binary using `wget https://downloads.lambdatest.com/hyperexecute/linux/hyperexecute` and then do `chmod +x hyperexecute`
* execute `./hyperexecute --user <YOUR_USERNAME --key <YOUR_ACCESS_KEY> --config android.yaml --no-track`

