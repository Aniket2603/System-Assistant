This is a demo version of voice based system assistant in python for simplyfying the day to day task.

-------------------------------------To install required libraries------------------------------------------------------
Before you run the program (setup files) your system should contain pyautogui python library and active internet connection.
Run the setup file to create environment for the assistant to work and import all the libraries.
Set up file contain libraries : speech recognition, webbrowser, wikipedia, pyttsx3.

--------------------------------------WorkFlow of Assistant--------------------------------------------------------------
The main assistant starts when the file name Zoya runs.
It goes to controller which control the input/output and decide responsibility to be handled.
Every instruction given is first taken as an audio input. You can switch to input as keyboard.
Than controller based on keywords decide the responsibility to be used and perform the operation.
After that depending on the result the controller provide output through speaker or display as required.


Responsibities have been divided into
1. Basic function which includes all the instruction for controlling volume, screen size, typing.
2. System search which tries to find the file in the local system. 
3. Web search which tries to search query on web.

If any search instruction is given and the file or folder with exact name is not present it will automatically go on web.

--------------------------------------How to give instruction------------------------------------------------------------
The instruction to be given is in the specific format:
[assistant name] + [command] + [to be done]

[assistant name] be default is 'Zoya'. It can be anytime by just changing the keyword.
[command] is to search, play etc.
[to be done] is the file name or task.

--------------------------------------------------------------------------------------------------------------------------
