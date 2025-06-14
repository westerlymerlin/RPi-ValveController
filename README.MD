# Valve Controller

### Valve controller is a python app that can operate 24v valves and is controlled via an HTTP API


`app.py`			    Flask application that manages the API 

----------------------------------------------------

`README.pdf`		software description and details how to setup on a Raspberry Pi

Python module documentation can be found in the folder: [docs](./docs/readme.md)

Change log can be found in the file [changelog.txt](./changelog.txt)

`Valve Control Circuit.fzz`     contains the schematics and PCB layout for use in the Fritzing application https://fritzing.org/

### JSON Commands
 
`{'status', '1'}` Return the ststus of all valves

`{'valveN', 'open'}` Open valve N

`{'valveN', 'close'}` Close valve N

`{'closeallvalves', 1}` close all valves and pipettes   


&nbsp;   
&nbsp;    
&nbsp;  
&nbsp;   
&nbsp;   
&nbsp;   
--------------

#### Copyright (C) 2025 Gary Twinn

This program is free software: you can redistribute it and/or modify  
it under the terms of the GNU General Public License as published by  
the Free Software Foundation, either version 3 of the License, or  
(at your option) any later version.  

This program is distributed in the hope that it will be useful,  
but WITHOUT ANY WARRANTY; without even the implied warranty of  
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the  
GNU General Public License for more details.  

You should have received a copy of the GNU General Public License  
along with this program. If not, see <https://www.gnu.org/licenses/>.


Author:  Gary Twinn  
Repository:  [github.com/westerlymerlin](https://github)

-------------





