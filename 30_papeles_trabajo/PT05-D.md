# PT05-D — Control detectivo Wazuh

**Objetivo:** comprobar registro, alerta y comunicación de pruebas del auditor. **Criterios:** ISO/IEC 27001:2022 A.8.15, A.8.16 y A.5.25. **Alcance:** portal y agente testigo del laboratorio `audit_net`.

Wazuh 4.9.0 está activo con manager, indexer y dashboard en `https://127.0.0.1:8444`. El agente ID 001 `si084_portal_testigo` está activo y recibe el registro Apache del contenedor WordPress mediante el capturador `scripts/capturar_portal_logs.py`. Las tres solicitudes marcadas `e05_01` a `e05_03` constan en `eventos_prueba.txt`, `portal_access.log` y en alertas reales del manager `alertas_prueba.jsonl`.

| Prueba | Resultado medido | Evidencia y límite |
|---|---|---|
| D-01 Escaneo de puertos | No detectado | Nmap se repitió con agente activo. Ninguna alerta del agente 001 apareció en la ventana de ejecución más 20 s. El agente recibe logs HTTP, no telemetría de paquetes. |
| D-02 Inyección en el portal | Detectada | Tres solicitudes de prueba HTTP 200 generaron alertas Wazuh: regla 31164 una vez y 31106 dos veces. |
| D-03 Tiempo medio de detección | 3,318 s | Pares evento-alerta de los tres marcadores: 2,933; 3,004; 4,016 s. Apache registra la hora fuente con precisión de un segundo. |
| D-04 Notificación | No configurada por correo | `ossec.conf` tiene `<email_notification>no</email_notification>`; no se demostró otro canal. |
| D-05 Inalterabilidad y retención | No demostradas | `alerts.json` tiene modo 640 y dueño `wazuh:wazuh`. No se obtuvo política de retención ni mecanismo de inmutabilidad. |

Las alertas de D-02 prueban detección de solicitudes de prueba en logs Apache. No prueban explotación ni bloqueo del ataque. La falta de alerta en D-01 se limita a la configuración ensayada.

**Evidencia:** `20_evidencia/E05_wazuh/` (eventos, alertas JSONL, Nmap, resultado D01 y resumen MTTD), `30_papeles_trabajo/PT05-D-mttd.csv`, `docs/evidencias/S05/salidas/wazuh_config_alertas.txt`. **Fecha:** 2026-09-16 UTC. **Revisión:** pendiente.
