# Taller 05 — estado de la evidencia

**Repositorio:** `https://github.com/Aakhtar004/SI084-S05-Ahmed`. **Entorno:** laboratorio local desechable creado para esta ejecución. **Fecha:** 2026-09-16.

**Modalidad:** individual. **Estudiante:** Ahmed Hasan Akhtar Oviedo. **Código:** 2022074261.

## Alcance y método

El alcance se registró en el commit `001493d9a2771388d3c3390bdded28b3afcbe458` antes de ejecutar pruebas. Solo se dirigieron herramientas a la red local `audit_net` y a servicios del laboratorio. El usuario autorizó proceder en la conversación; queda pendiente la firma del docente para cumplir literalmente la exigencia del taller. El puerto 3000 estaba ocupado por otro servicio y quedó libre antes de levantar Juice Shop.

## Resultados verificados

| # | Resultado | Estado | Evidencia |
|---|---|---|---|
| 1 | Alcance previo | Parcial: commit previo, firma docente pendiente | `10_planificacion/alcance_E05.md` y `git log` |
| 2 | ZAP baseline y full | Ambos generados en HTML y JSON | `20_evidencia/E05_app/` |
| 3 | Cinco alertas mapeadas | Cinco correspondencias registradas; validación manual pendiente | `40_hallazgos/PT05_alertas_zap.csv` |
| 4 | Nmap y contraste | Escaneo realizado; inventario organizacional no aportado | `20_evidencia/E05_infra/nmap_*`; `30_papeles_trabajo/PT05-B.md` |
| 5 | Servicio no inventariado con hallazgo | No demostrado sin inventario previo aprobado | `30_papeles_trabajo/PT05-B.md` |
| 6 | Wazuh y D-01 a D-05 | Tres contenedores levantados; panel local accesible en 8444; sin agente testigo ni MTTD | `30_papeles_trabajo/PT05-D.md` y salidas `wazuh_*` |
| 7 | Restauración con tiempo y hash | Logrado en base de prueba: 2,42 s, SHA-256 idéntico | `30_papeles_trabajo/PT05-C.md`; `20_evidencia/E05_infra/` |
| 8 | Cadena de custodia y commit | Hashes y commits existentes; resellado necesario tras archivos nuevos | `20_evidencia/SHA256SUMS_E05.txt` y `git log` |

Juice Shop y el portal respondieron HTTP 200. Nmap encontró cuatro hosts en `audit_net`: Juice Shop (3000), MariaDB (3306), ERP PostgreSQL (5432) y WordPress/Apache (80). No hubo servicios TLS en 443 u 8443. El respaldo restaurado coincide bit a bit con el original y restic no informó errores. No se puede comparar el tiempo observado con un RTO ni el punto recuperado con un RPO, porque no se proporcionaron objetivos declarados.

## Problemas y mejoras

- Falta el inventario organizacional aprobado previo al escaneo, junto con dueños y alcance del SGSI. No se debe fabricar un hallazgo de servicio olvidado a partir del propio archivo Compose.
- La base ERP del ejercicio es una base de prueba creada en este entorno; la conclusión de restauración se limita a ella.
- La entrega es individual; el estudiante y código están identificados. Falta saber qué número de grupo exige el aula virtual para el nombre final `SI084-S05-TALLER-Grupo<N>.pdf`.
- La firma del docente para el alcance y las actas no fue proporcionada.
- La descarga y el análisis activo excedieron la ventana de cinco minutos solicitada; ambos reportes ZAP quedaron generados.
- Los contenedores Wazuh figuran `Up`. El puerto 443 respondió desde Apache de Windows, ajeno al dashboard. Se publicó el dashboard en `https://127.0.0.1:8444` y se verificó su redirección HTTP 302 al inicio de sesión. Falta conectar un agente testigo y medir D-01 a D-05.

## Transferencia

En una organización real, escanear fuera de un alcance firmado expondría sistemas ajenos a pruebas no autorizadas. Afirmar que un control detecta ataques o restaura datos sin medirlo ocultaría fallas operativas críticas.
