"""Extrae alertas reales de ZAP; el mapeo es una guía de prueba, no un hallazgo confirmado."""

import csv
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "20_evidencia/E05_app/zap_full_juiceshop.json"
if not SOURCE.exists():
    SOURCE = ROOT / "20_evidencia/E05_app/zap_baseline_juiceshop.json"
DEST = ROOT / "40_hallazgos/PT05_alertas_zap.csv"

MAP = {
    "Content Security Policy (CSP) Header Not Set": ("WSTG-CONF-12", "A05", "A.8.9"),
    "Cross-Domain Misconfiguration": ("WSTG-CLNT-07", "A05", "A.8.9"),
    "Timestamp Disclosure - Unix": ("WSTG-INFO-05", "A05", "A.8.12"),
    "Storable and Cacheable Content": ("WSTG-ATHN-06", "A05", "A.8.12"),
    "Storable but Non-Cacheable Content": ("WSTG-ATHN-06", "A05", "A.8.12"),
}

data = json.loads(SOURCE.read_text(encoding="utf-8"))
rows = []
for site in data.get("site", []):
    for alert in site.get("alerts", []):
        name = alert.get("alert", "")
        wstg, top10, iso = MAP.get(name, ("", "", ""))
        rows.append({
            "fuente": SOURCE.name,
            "riesgo_zap": alert.get("riskdesc", ""),
            "alerta": name,
            "cwe": alert.get("cweid", ""),
            "instancias": len(alert.get("instances", [])),
            "wstg": wstg,
            "owasp_top10_2021": top10,
            "iso_27001_2022": iso,
            "validacion": "Pendiente: comprobar exposición y relevancia para el dato concreto",
        })

DEST.parent.mkdir(parents=True, exist_ok=True)
with DEST.open("w", newline="", encoding="utf-8-sig") as file:
    writer = csv.DictWriter(file, fieldnames=rows[0].keys())
    writer.writeheader()
    writer.writerows(rows)

print(f"Fuente: {SOURCE.name}; alertas: {len(rows)}; mapeadas: {sum(bool(r['wstg']) for r in rows)}")
