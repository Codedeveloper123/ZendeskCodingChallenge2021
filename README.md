# ZendeskCodingChallenge2021
## Installation Instructions
1. Install Python on Computer
     Use this link if not on device https://realpython.com/installing-python/.
2. Install VSCODE
    Use this link to download if not on device https://code.visualstudio.com/download
3. Install VSCODE Python extension
    Hit Ctrl + shift + x. Then type python in the extensions bar and then hit install. 
4. Install PIP onto machine
    If you are using python 2.7.9 or greater it should already be installed if not follow the instructions in this link https://www.makeuseof.com/tag/install-pip-for-python/
5. Install requests on computer 
    Type this command on terminal python -m pip install requests
## Usage Instructions
1. To change the dataset change the url, useremail, and password fields in main.py
![](2021-11-27-20-44-34.png)
2.  Click onto main.py editor, Click Run and then Run withought debuggging 
![](2021-11-27-20-45-04.png)
3. Follow Instructions on Terminal as it is a  CLI application
## Testing Instructions
1. To run first test use command below in terminal
    python -m unittest UnitTest.TestTicketViewerMethods.test_wrong_authentication 
2. To run second test use command below in terminal
    python -m unittest UnitTest.TestTicketViewerMethods.test_all_tickets_are_displayed
3. To run third test use command below in terminal
    python -m unittest UnitTest.TestTicketViewerMethods.test_get_specific_ticket

