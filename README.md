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

