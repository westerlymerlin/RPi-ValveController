# Contents for: app

* [app](#app)
  * [subprocess](#app.subprocess)
  * [enumerate\_threads](#app.enumerate_threads)
  * [Flask](#app.Flask)
  * [render\_template](#app.render_template)
  * [jsonify](#app.jsonify)
  * [request](#app.request)
  * [logger](#app.logger)
  * [httpstatus](#app.httpstatus)
  * [valvestatus](#app.valvestatus)
  * [parsecontrol](#app.parsecontrol)
  * [settings](#app.settings)
  * [VERSION](#app.VERSION)
  * [app](#app.app)
  * [read\_log\_from\_file](#app.read_log_from_file)
  * [read\_cpu\_temperature](#app.read_cpu_temperature)
  * [threadlister](#app.threadlister)
  * [index](#app.index)
  * [api](#app.api)
  * [showplogs](#app.showplogs)
  * [showgalogs](#app.showgalogs)
  * [showgelogs](#app.showgelogs)
  * [showslogs](#app.showslogs)

<a id="app"></a>

# app

This is the main flask application - called by Gunicorn

<a id="app.subprocess"></a>

## subprocess

<a id="app.enumerate_threads"></a>

## enumerate\_threads

<a id="app.Flask"></a>

## Flask

<a id="app.render_template"></a>

## render\_template

<a id="app.jsonify"></a>

## jsonify

<a id="app.request"></a>

## request

<a id="app.logger"></a>

## logger

<a id="app.httpstatus"></a>

## httpstatus

<a id="app.valvestatus"></a>

## valvestatus

<a id="app.parsecontrol"></a>

## parsecontrol

<a id="app.settings"></a>

## settings

<a id="app.VERSION"></a>

## VERSION

<a id="app.app"></a>

#### app

<a id="app.read_log_from_file"></a>

#### read\_log\_from\_file

```python
def read_log_from_file(file_path)
```

Read a log from a file and reverse the order of the lines so newest is at the top

<a id="app.read_cpu_temperature"></a>

#### read\_cpu\_temperature

```python
def read_cpu_temperature()
```

Read the CPU temperature

<a id="app.threadlister"></a>

#### threadlister

```python
def threadlister()
```

Get a list of all threads running

<a id="app.index"></a>

#### index

```python
@app.route('/')
def index()
```

Main web status page

<a id="app.api"></a>

#### api

```python
@app.route('/api', methods=['POST'])
def api()
```

API Endpoint for programatic access - needs request data to be posted in a json file

<a id="app.showplogs"></a>

#### showplogs

```python
@app.route('/pylog')
def showplogs()
```

Show the Application log

<a id="app.showgalogs"></a>

#### showgalogs

```python
@app.route('/guaccesslog')
def showgalogs()
```

"Show the Gunicorn Access Log

<a id="app.showgelogs"></a>

#### showgelogs

```python
@app.route('/guerrorlog')
def showgelogs()
```

"Show the Gunicorn Errors Log

<a id="app.showslogs"></a>

#### showslogs

```python
@app.route('/syslog')
def showslogs()
```

Show the system log

