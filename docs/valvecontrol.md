# Contents for: valvecontrol

* [valvecontrol](#valvecontrol)
  * [Timer](#valvecontrol.Timer)
  * [os](#valvecontrol.os)
  * [GPIO](#valvecontrol.GPIO)
  * [logger](#valvecontrol.logger)
  * [channellist](#valvecontrol.channellist)
  * [valves](#valvecontrol.valves)
  * [parsecontrol](#valvecontrol.parsecontrol)
  * [valveopen](#valvecontrol.valveopen)
  * [valveclose](#valvecontrol.valveclose)
  * [allclose](#valvecontrol.allclose)
  * [status](#valvecontrol.status)
  * [valvestatus](#valvecontrol.valvestatus)
  * [httpstatus](#valvecontrol.httpstatus)
  * [reboot](#valvecontrol.reboot)

<a id="valvecontrol"></a>

# valvecontrol

Main valve controller module, operates the valves via the Raspberry Pi GPIO

<a id="valvecontrol.Timer"></a>

## Timer

<a id="valvecontrol.os"></a>

## os

<a id="valvecontrol.GPIO"></a>

## GPIO

<a id="valvecontrol.logger"></a>

## logger

<a id="valvecontrol.channellist"></a>

#### channellist

<a id="valvecontrol.valves"></a>

#### valves

<a id="valvecontrol.parsecontrol"></a>

#### parsecontrol

```python
def parsecontrol(item, command)
```

Parser that recieves messages from the API or web page posts and directs
messages to the correct function

<a id="valvecontrol.valveopen"></a>

#### valveopen

```python
def valveopen(valveid)
```

Open the valve specified

<a id="valvecontrol.valveclose"></a>

#### valveclose

```python
def valveclose(valveid)
```

Close the valve specified

<a id="valvecontrol.allclose"></a>

#### allclose

```python
def allclose()
```

Close all valves

<a id="valvecontrol.status"></a>

#### status

```python
def status(value)
```

Meaningful value name for the specified valve

<a id="valvecontrol.valvestatus"></a>

#### valvestatus

```python
def valvestatus()
```

Return the status of all valves as a jason message

<a id="valvecontrol.httpstatus"></a>

#### httpstatus

```python
def httpstatus()
```

Statud message formetted for the web status page

<a id="valvecontrol.reboot"></a>

#### reboot

```python
def reboot()
```

API call to reboot the Raspberry Pi

