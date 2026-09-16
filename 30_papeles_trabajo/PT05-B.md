# PT05-B — Contraste del inventario

**Objetivo:** comparar los servicios reales de `audit_net` con un inventario aprobado antes de la prueba. **Criterio:** ISO/IEC 27001:2022, A.5.9. **Prueba:** inspección del sistema con Nmap. **Población:** cuatro contenedores del laboratorio; cobertura de la muestra: cuatro de cuatro. **Excepción predefinida:** servicio abierto ausente del inventario aprobado, sin dueño o fuera del SGSI.

| Servicio | Puerto | Versión observada | Inventario previo | Dueño | SGSI | Observación |
|---|---:|---|---|---|---|---|
| Juice Shop | 3000 | HTTP; versión no identificada por Nmap | No aportado | No informado | No informado | Observado en `nmap_servicios_verificacion.txt` |
| MariaDB | 3306 | MariaDB 11.8.9, identificación de Nmap | No aportado | No informado | No informado | Observado en `nmap_servicios_verificacion.txt` |
| WordPress | 80 | Apache httpd 2.4.68 | No aportado | No informado | No informado | Observado en `nmap_servicios.nmap` |
| ERP PostgreSQL | 5432 | PostgreSQL 9.6 o posterior, estimación de Nmap | No aportado | No informado | No informado | Observado en `nmap_servicios.nmap` |

El archivo `entorno/compose.yaml` documenta los cuatro servicios de **este laboratorio**. No equivale a un inventario organizacional aprobado. Por ello no se declara un servicio no inventariado ni se redacta un hallazgo sin contraste independiente. Faltan el inventario declarado, dueños y alcance del SGSI.

**Ejecutado:** 2026-09-16 UTC, automatizado. **Revisado por:** pendiente. **Evidencia:** `20_evidencia/E05_infra/nmap_servicios.nmap` y `targets.txt`.
