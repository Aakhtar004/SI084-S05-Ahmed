"""Calcula MTTD desde el log Apache incorporado a cada alerta real de Wazuh."""

import csv
import json
import re
import statistics
from datetime import datetime
from pathlib import Path

root = Path(__file__).resolve().parents[1]
source = root / "20_evidencia/E05_wazuh/alertas_prueba.jsonl"
dest = root / "30_papeles_trabajo/PT05-D-mttd.csv"
rows = []

for line in source.read_text(encoding="utf-8-sig").splitlines():
    if not line.strip():
        continue
    item = json.loads(line)
    marker = re.search(r"audit=(e05_\d+)", item["data"]["url"])
    log_time = re.search(r"\[([^]]+)\]", item["full_log"])
    if not marker or not log_time:
        continue
    event_dt = datetime.strptime(log_time.group(1), "%d/%b/%Y:%H:%M:%S %z")
    alert_dt = datetime.fromisoformat(item["timestamp"].replace("+0000", "+00:00"))
    latency = round((alert_dt - event_dt).total_seconds(), 3)
    rows.append({
        "evento": marker.group(1),
        "marca_log_utc": event_dt.isoformat(),
        "marca_alerta_utc": alert_dt.isoformat(),
        "latencia_segundos": latency,
        "regla": item["rule"]["id"],
        "agente": item["agent"]["name"],
        "id_alerta": item["id"],
    })

if len(rows) != 3:
    raise SystemExit(f"Se esperaban 3 alertas enlazadas; hay {len(rows)}")

with dest.open("w", newline="", encoding="utf-8-sig") as file:
    writer = csv.DictWriter(file, fieldnames=rows[0].keys())
    writer.writeheader()
    writer.writerows(rows)

mean = round(statistics.mean(row["latencia_segundos"] for row in rows), 3)
summary = f"MTTD medido: {mean} segundos sobre {len(rows)} eventos; precisión del log fuente: 1 segundo."
(root / "20_evidencia/E05_wazuh/mttd_resumen.txt").write_text(summary + "\n", encoding="utf-8")
print(summary)
