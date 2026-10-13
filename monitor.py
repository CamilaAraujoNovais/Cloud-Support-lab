from datetime import datetime
from pathlib import Path
from urllib.request import urlopen
from urllib.error import HTTPError, URLError

url = "http://127.0.0.1:8000/index.html"
log_path = Path(__file__).resolve().parent / "monitor.log"

try:
    with urlopen(url, timeout=5) as response:
        result = f"UP | HTTP {response.status}"
except HTTPError as error:
    result = f"HTTP ERROR | {error.code}"
except (URLError, TimeoutError) as error:
    result = f"CONNECTION ERROR | {error}"

line = f"{datetime.now().isoformat(timespec='seconds')} | {result}"
print(line)

with log_path.open("a", encoding="utf-8") as log:
    log.write(line + "\n")
