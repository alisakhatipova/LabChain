# LabChain

In our BitLab Blockchain Course we develop our own blockchain platform.

### Objectives for the Platform are:

- Exchangeable components
- Strong documentation
- Excellent test coverage
- Well established software engineering processes
- Good maintainability and extendability  after project - conclusion


## Project Prerequisites
- Python3 (https://www.python.org/)
  - PEP 8 Style Guide for Python Code (https://www.python.org/dev/peps/pep-0008/)
- Git Repository (https://git-scm.com/)
- Agile development
  - Code reviews, iterative development, extensive testing, no requirement spec. overhead
- Test first approach (Almost every function deserves a unit test)
  - Python3 Unit Testing Framework (https://docs.python.org/3/library/unittest.html)

Please use git precommit hooks to style check before commiting. We created a global pre-commit hook which you have to install by calling ```./scripts/install-hooks.bash```.

For the Hook to work, you'll need to install pycodestyle: ```pip install pycodestyle```

This script creats a symlink from ```.git//hooks/pre-commit``` to ```scripts/pre-commit.bash```. It is based on a script of sigmoidal.io (https://sigmoidal.io/automatic-code-quality-checks-with-git-hooks/) and the pep8-git-hook by cbrueffer (https://github.com/cbrueffer/pep8-git-hook).


# Setup

Run the following to install all dependencies:

```bash
pip install -r requirements.txt

```

# Run the Node

```
cd scripts
python node_start.py --port 8080 --peers <ip1>:<port1> <ip2>:<port2> ...
```

`-v` and `-vv` set the log level to INFO or DEBUG.
`-p` or `--plot` enables frequent plotting of the blockchain into `~/.labchain/plot`
`--plot-dir <directory>` lets you choose a different directory for plot output
`--plot-auto-open` enables opening the plot in your browser whenever it is created (may become annoying)

# Run the Node Dashboard

```
install mosquitto and node-red
cd node-dashboard-app
node-red dash-app.js

install node-red-dashboard palette to see the dashboard

```

`--port port_number` if the given port is busy.

# Run the Client

```
cd scripts
python client-cli.py <node-ip> <node-port>
```

`-v` and `-vv` set the log level to INFO or DEBUG.

# Run using Docker

```
docker build -t labchain:latest .
docker run --name "labchain" -p 1880:1880 -p 8080:8080 labchain:latest
```
