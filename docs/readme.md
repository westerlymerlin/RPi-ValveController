# Module Documentation


This document contains the documentation for all the modules in this project.

---

## Contents


[app](./app.md)  
Valve Controller Web Application

A Flask-based web application for monitoring and controlling valves through a REST API.
This module serves as the main entry point and is designed to be run by Gunicorn.

Features:
- Web interface for valve status monitoring
- REST API for programmatic valve control with API key authentication
- System monitoring (CPU temperature, thread listing)
- Log viewing (application logs, Gunicorn logs, system logs)

The application exposes endpoints for valve control, system status, and log viewing.

[app_control](./app_control.md)  
Settings module, reads the settings from a settings.json file. If it does not exist or a new setting
has appeared it will creat from the defaults in the initialise function.

[logmanager](./logmanager.md)  
logmanager, setus up application logging. use the **logger** property to
write to the log.

[valvecontrol](./valvecontrol.md)  
Raspberry Pi Valve Control System

This module provides a comprehensive interface for controlling and monitoring laboratory
valves via Raspberry Pi GPIO pins. It implements safety interlocks to prevent conflicting
valve states, handles system commands, and provides status monitoring capabilities.

Features:
- Individual valve control (open/close) with conflict prevention
- Batch operations (close all valves)
- System control commands (restart)
- Status reporting for monitoring
- Logging of all valve operations and errors

The module initializes GPIO pins, defines valve configurations with their relationships,
and provides functions for valve manipulation through a consistent interface.

Dependencies:
- RPi.GPIO: For hardware control of GPIO pins
- threading.Timer: For delayed execution of commands
- logmanager: For operational logging


---


  
-------
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
  
  ##### Author: Gary Twinn  
  
 -------------
  
