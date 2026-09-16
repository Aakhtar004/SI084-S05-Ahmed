# PT05-C — Acta de reejecución de restauración

| Campo | Resultado |
|---|---|
| Sistema | Base de datos de prueba ERP `si084_db` |
| Fecha de prueba | 2026-09-16 UTC |
| Tipo de prueba | Reejecución, respaldo y restauración con restic |
| Población / muestra | Una base de datos de prueba / una restauración dirigida |
| Criterio | ISO/IEC 27001:2022 A.8.13; COBIT DSS04.07 |
| Excepción fijada antes | Restauración fallida, hash distinto o tiempo mayor que el RTO declarado |
| RTO declarado | No proporcionado |
| Tiempo real medido | **2,42 segundos** |
| RPO declarado | No proporcionado |
| Punto recuperado | Snapshot `8d1bf528` |
| Integridad SHA-256 | Coincide: `D3B62F9EC5732793988B28EE455C104B97E50755AA29D3CDC3B35E243522A4E2` |
| Consistencia del repositorio | `restic check --read-data`: sin errores |
| Conclusión | La restauración de esta base de prueba funcionó y conservó integridad. No se puede juzgar el cumplimiento del RTO ni del RPO sin objetivos declarados. |
| Evidencia | `20_evidencia/E05_infra/tiempo_y_hash_restauracion.txt`, `restic_check.txt`, `dump/erp.sql` y `restaurado/datos/erp.sql` |
| Ejecutado por / revisado por | Automatizado / pendiente |

La base contiene un registro de prueba creado para este ejercicio. No representa una base ERP de producción ni demuestra la eficacia histórica de sus respaldos.
