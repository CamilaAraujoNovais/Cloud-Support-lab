# Linux Web Support Lab

Local troubleshooting lab built with Kali Linux and Python.
This project runs locally and does not use AWS resources.

## Tools
- Python HTTP server
- Python monitoring script
- curl
- ss

## Incident 1: Website unavailable
Symptom: The monitoring script reported connection refused.
Cause: The HTTP server was not running.
Resolution: Started the server on 127.0.0.1:8000.
Verification: The monitoring script returned UP | HTTP 200.

## Incident 2: Missing page
Symptom: A request for missing.html returned HTTP 404.
Cause: The requested file did not exist.
Resolution: Created missing.html in the server directory.
Verification: The same URL returned HTTP 200.

## Monitoring
monitor.py checks index.html once per execution.
Results are appended to monitor.log.  

## How to run

Requirements: Linux and Python 3.

Start the web server from the project directory:

```bash
python3 -m http.server 8000 --bind 127.0.0.1 --directory .
```

Keep that terminal open. In a second terminal, open the project
directory and run:

```bash
python3 monitor.py
```

Expected result: UP | HTTP 200.

Open http://127.0.0.1:8000/index.html in a browser on the same machine.

## Test a connection failure

1. Stop the server with Ctrl+C in the server terminal.
2. Run monitor.py in the second terminal.
3. Confirm that it reports CONNECTION ERROR.
4. Restart the server using the command above.
5. Run monitor.py again and confirm UP | HTTP 200.

## Scope

This is a local learning lab, not an AWS deployment.
The server listens only on the local machine.
The monitor performs one check each time it is run.

