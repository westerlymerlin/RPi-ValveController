# Valve Controller

### Valve controller is a python app that can operate 24v valves and is controlled via an HTTP API


`app.py`			    Flask application that manages the API 

----------------------------------------------------

`valvecontrol.py`		pyton GPIO routine for setting up and managng valves

`README.pdf`		software description and details how to setup on a Raspberry Pi

`Valve Control Circuit.fzz`     contains the schematics and PCB layout for use in the Fritzing application https://fritzing.org/

### JSON Commands
 
`{'status', '1'}` Return the ststus of all valves

`{'valveN', 'open'}` Open valve N

`{'valveN', 'close'}` Close valve N

`{'closeallvalves', 1}` close all valves and pipettes   

`{'restart', 'pi'}` Restart the raspberry pi after a 15 second delay   




