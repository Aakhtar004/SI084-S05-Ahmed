# PT05-D — Control detectivo Wazuh

**Objetivo:** determinar si el área de explotación registra, alerta y comunica las pruebas del auditor. **Criterios:** ISO/IEC 27001:2022 A.8.15, A.8.16 y A.5.25. **Alcance:** laboratorio `audit_net` y portal local. **Excepción predefinida:** ausencia de evento o alerta para una prueba efectivamente generada, latencia superior al umbral declarado, o alerta sin destinatario.

El stack Wazuh 4.9.0 levantó manager, indexer y dashboard. Se verificó la respuesta del dashboard en `https://127.0.0.1:8444` (HTTP 302 a `/app/login?`). El listado de agentes solo contiene el manager local (`ID 000`); no hay agente testigo en el portal. Por ello, los escaneos realizados hasta ahora no constituyen una prueba válida de eficacia detectiva del portal.

| Prueba | Veredicto sustentado | Evidencia / límite |
|---|---|---|
| D-01 Escaneo de puertos registrado | No evaluable | No había agente de portal durante Nmap; `wazuh_agentes.txt` muestra solo ID 000 |
| D-02 Intentos de inyección registrados | No evaluable | No hay agente ni ingesta de registros web del portal; no se atribuyen alertas del manager a ZAP |
| D-03 Tiempo medio de detección | No medido | Sin par evento-alerta del mismo ataque, no se puede calcular MTTD |
| D-04 Alerta notificada a alguien | No configurado por correo | `ossec.conf` contiene `<email_notification>no</email_notification>` y direcciones de ejemplo; faltaría revisar otros canales si se configuran |
| D-05 Inalterabilidad de registros | No demostrada | `alerts.json` pertenece a `wazuh:wazuh` con modo 640; no se observó un mecanismo de inmutabilidad ni una política de retención en la evidencia recolectada |

**Trabajo pendiente para concluir eficacia:** desplegar un agente testigo, conectar los logs de Apache del portal, repetir Nmap y ZAP en una ventana controlada, conservar marcas de tiempo del log fuente y la alerta, calcular MTTD y capturar el panel. No se registra un MTTD ficticio.

**Ejecutado:** 2026-09-16 UTC, automatizado. **Revisado por:** pendiente. **Evidencia:** `docs/evidencias/S05/salidas/wazuh_estado_8444.txt`, `wazuh_http_8444.txt`, `wazuh_agentes.txt` y `wazuh_config_alertas.txt`.
