This is the program for the computer assistant using python version 3.6.

Before you run the setup files your system should contain pyautogui python library and active internet connection.
Run the setup file to create environment for the assistant to work and import all the libraries.
Set up file contain libraries : speech recognition, webbrowser, wikipedia, pyttsx3

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

If any search instruction is given and the file or folder with exact name is present it will automatically go on web.

--------------------------------------Tips for using assistant------------------------------------------------------------
Different keywords have given for different kind of instructions.
The main set of keywords is given below:
['volume','brightness','type','press','close','screen','search','play','open','show','web','google','chrome']

#1. To start using keyboard say Keyboard and type the instruction.
#2. To stop the voice command speak cut
#3. To start the voice command say start
--------------------------------------------------------------------------------------------------------------------------