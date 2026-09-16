"""Consulta alertas del manager en la ventana de repetición de Nmap."""

import json
import subprocess
from datetime import datetime, timedelta, timezone
from pathlib import Path

root = Path(__file__).resolve().parents[1]
evidence = root / "20_evidencia/E05_wazuh"
times = dict(line.split("=", 1) for line in (evidence / "nmap_repeticion_tiempos.txt").read_text().splitlines())
start = datetime.fromisoformat(times["inicio_utc"].replace("Z", "+00:00"))
end = datetime.fromisoformat(times["fin_utc"].replace("Z", "+00:00")) + timedelta(seconds=20)

result = subprocess.run(
    ["docker", "exec", "single-node-wazuh.manager-1", "cat", "/var/ossec/logs/alerts/alerts.json"],
    text=True, capture_output=True, check=True, encoding="utf-8", errors="replace"
)
agent_alerts = []
scan_alerts = []
for line in result.stdout.splitlines():
    try:
        item = json.loads(line)
        stamp = datetime.fromisoformat(item["timestamp"].replace("+0000", "+00:00"))
    except (json.JSONDecodeError, KeyError, ValueError):
        continue
    if item.get("agent", {}).get("id") != "001" or not start <= stamp <= end:
        continue
    agent_alerts.append(item)
    rule = item.get("rule", {})
    labels = " ".join(rule.get("groups", [])).lower()
    if "scan" in labels or "recon" in labels or "scan" in rule.get("description", "").lower():
        scan_alerts.append(item)

(evidence / "D01_alertas_escaneo.jsonl").write_text(
    "".join(json.dumps(item, ensure_ascii=False) + "\n" for item in scan_alerts), encoding="utf-8"
)
summary = (
    f"Ventana UTC: {start.isoformat()} a {end.isoformat()}\n"
    f"Alertas del agente 001: {len(agent_alerts)}\n"
    f"Alertas de escaneo/reconocimiento: {len(scan_alerts)}\n"
    "Interpretación: si no hay alerta de escaneo, el control actual no detectó esta prueba de Nmap.\n"
)
(evidence / "D01_resultado.txt").write_text(summary, encoding="utf-8")
print(summary)
