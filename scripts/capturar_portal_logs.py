"""Copia en tiempo real los registros de acceso Apache del contenedor testigo."""

import subprocess
from pathlib import Path

root = Path(__file__).resolve().parents[1]
dest = root / "20_evidencia/E05_wazuh/portal_access.log"
dest.parent.mkdir(parents=True, exist_ok=True)

with subprocess.Popen(
    ["docker", "logs", "--follow", "--tail", "0", "si084_portal"],
    stdout=subprocess.PIPE,
    stderr=subprocess.DEVNULL,
    text=True,
    encoding="utf-8",
    errors="replace",
    bufsize=1,
) as proc, dest.open("a", encoding="utf-8", buffering=1) as out:
    for line in proc.stdout:
        if " - - [" in line and line[:1].isdigit():
            out.write(line)
