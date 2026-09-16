"""Genera un corte verificable de las evidencias disponibles del Taller 05."""

from pathlib import Path
from xml.sax.saxutils import escape

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "output/pdf/Informe_provisional_evidencias_S05.pdf"
OUT.parent.mkdir(parents=True, exist_ok=True)

font = Path("C:/Windows/Fonts/arial.ttf")
bold = Path("C:/Windows/Fonts/arialbd.ttf")
pdfmetrics.registerFont(TTFont("Arial", str(font)))
pdfmetrics.registerFont(TTFont("Arial-Bold", str(bold)))

navy = colors.HexColor("#16285C")
teal = colors.HexColor("#0F766E")
light = colors.HexColor("#E8F1FB")
gray = colors.HexColor("#4B5563")

styles = getSampleStyleSheet()
styles.add(ParagraphStyle(name="TitleES", fontName="Arial-Bold", fontSize=17, leading=21, textColor=navy, alignment=TA_CENTER, spaceAfter=12))
styles.add(ParagraphStyle(name="SubES", fontName="Arial-Bold", fontSize=10.5, leading=14, textColor=teal, spaceBefore=12, spaceAfter=5))
styles.add(ParagraphStyle(name="BodyES", fontName="Arial", fontSize=9, leading=13, textColor=gray, spaceAfter=7))
styles.add(ParagraphStyle(name="SmallES", fontName="Arial", fontSize=7.4, leading=10, textColor=gray))
styles.add(ParagraphStyle(name="HeadCell", fontName="Arial-Bold", fontSize=7.6, leading=10, textColor=colors.white))

def p(text, style="BodyES"):
    return Paragraph(text, styles[style])

def cell(text, header=False):
    return p(escape(str(text)), "HeadCell" if header else "SmallES")

def table(headers, rows, widths):
    data = [[cell(x, True) for x in headers]] + [[cell(x) for x in row] for row in rows]
    item = Table(data, colWidths=widths, repeatRows=1, hAlign="LEFT")
    item.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,0), navy),
        ("VALIGN", (0,0), (-1,-1), "TOP"),
        ("ROWBACKGROUNDS", (0,1), (-1,-1), [colors.white, light]),
        ("GRID", (0,0), (-1,-1), 0.25, colors.HexColor("#CBD5E1")),
        ("LEFTPADDING", (0,0), (-1,-1), 6),
        ("RIGHTPADDING", (0,0), (-1,-1), 6),
        ("TOPPADDING", (0,0), (-1,-1), 5),
        ("BOTTOMPADDING", (0,0), (-1,-1), 5),
    ]))
    return item

story = []
story.append(p("UNIVERSIDAD PRIVADA DE TACNA<br/>ESCUELA PROFESIONAL DE INGENIERÍA DE SISTEMAS", "TitleES"))
story.append(p("SI-084 · Auditoría de Sistemas · Semana 05", "BodyES"))
story.append(p("Informe provisional de evidencias implementadas", "TitleES"))
story.append(p("Corte: 16 de septiembre de 2026. Este documento registra resultados observados hasta este momento. No sustituye el informe final en la plantilla obligatoria ni afirma que el taller esté terminado."))
story.append(p("1. Alcance y trazabilidad", "SubES"))
story.append(p("El alcance local se guardó en el commit <b>001493d</b> antes de iniciar pruebas. El usuario autorizó proceder en esta conversación. La firma del docente exigida por la guía todavía no se ha aportado. Los objetivos de escaneo se limitaron a la red Docker audit_net y a los servicios locales del laboratorio."))
story.append(table(["Elemento", "Evidencia comprobable"], [
    ("Repositorio", "https://github.com/Aakhtar004/SI084-S05-Ahmed"),
    ("Alcance previo", "10_planificacion/alcance_E05.md; git log: 001493d anterior a c53e34f"),
    ("Entorno", "entorno/compose.yaml; cuatro contenedores locales"),
], [4*cm, 12.4*cm]))

story.append(p("2. Aplicación web: OWASP ZAP", "SubES"))
story.append(p("Juice Shop respondió HTTP 200 en 127.0.0.1:3000. ZAP produjo reportes baseline y full en HTML y JSON. El full scan exploró cuatro URL y registró seis tipos de alertas; esto no prueba por sí solo explotación exitosa. El CSV de trabajo conserva cinco correspondencias temáticas con WSTG, OWASP Top 10:2021 e ISO/IEC 27001:2022, pendientes de validación manual."))
story.append(table(["Alerta observada", "Instancias full", "Criterio de prueba"], [
    ("CSP Header Not Set", "3", "WSTG-CONF-12"),
    ("Cross-Domain Misconfiguration", "4", "WSTG-CLNT-07"),
    ("CORS Misconfiguration", "4", "WSTG-CLNT-07"),
    ("Timestamp Disclosure - Unix", "6", "WSTG-INFO-05"),
], [8.2*cm, 2.5*cm, 5.7*cm]))
story.append(p("Archivos: 20_evidencia/E05_app/zap_baseline_juiceshop.{html,json}, zap_full_juiceshop.{html,json}; 40_hallazgos/PT05_alertas_zap.csv."))

story.append(PageBreak())
story.append(p("3. Infraestructura: Nmap", "SubES"))
story.append(p("La prueba se dirigió a cuatro direcciones internas de audit_net. Nmap confirmó cuatro hosts. El barrido TLS no halló servicios en 443 ni 8443. La versión de PostgreSQL es una estimación de Nmap, no la versión exacta certificada del servidor."))
story.append(table(["Host", "Puerto", "Servicio observado"], [
    ("si084_juiceshop", "3000", "HTTP (firma no identificada)"),
    ("si084_mariadb", "3306", "MariaDB 11.8.9 (Nmap)"),
    ("si084_db", "5432", "PostgreSQL 9.6 o posterior (Nmap)"),
    ("si084_portal", "80", "Apache httpd 2.4.68 (Nmap)"),
], [5.5*cm, 2.5*cm, 8.4*cm]))
story.append(p("Evidencia: 20_evidencia/E05_infra/nmap_hosts.txt, nmap_servicios_verificacion.txt y nmap_tls.txt. El PT05-B documenta el contraste. Falta un inventario organizacional aprobado previo al escaneo; por eso no se afirma que alguno de estos servicios sea un hallazgo de activo olvidado."))

story.append(p("4. Restauración: restic", "SubES"))
story.append(p("Se generó un dump de la base ERP de prueba, se respaldó con restic y se restauró desde el snapshot 8d1bf528. El cronómetro de la operación de restauración marcó <b>2,42 segundos</b>. El SHA-256 original y restaurado coincide. restic check --read-data informó que no se encontraron errores."))
story.append(table(["Control", "Resultado"], [
    ("Tiempo real", "2,42 segundos"),
    ("SHA-256 original y restaurado", "D3B62F9EC5732793988B28EE455C104B97E50755AA29D3CDC3B35E243522A4E2"),
    ("Integridad", "Coincide"),
    ("Consistencia restic", "Sin errores"),
    ("RTO/RPO", "No proporcionados; no es posible evaluar cumplimiento"),
], [5.2*cm, 11.2*cm]))
story.append(p("Evidencia: 30_papeles_trabajo/PT05-C.md, 20_evidencia/E05_infra/tiempo_y_hash_restauracion.txt y restic_check.txt. La base usada es de prueba; esta medición no caracteriza una restauración de producción."))

story.append(p("5. Estado de Wazuh y pendientes", "SubES"))
story.append(p("Los contenedores de Wazuh 4.9.0 (manager, indexer y dashboard) fueron creados y figuran en estado Up. La consulta a https://127.0.0.1:443 devolvió una respuesta de Apache de Windows ajena al dashboard, por lo que no se considera verificado el acceso al panel. Aún no hay agente testigo, tabla D-01 a D-05 ni MTTD medido. También faltan inventario previo, firma del docente y datos del grupo para el PDF final."))
story.append(p("Hashes del corte: 20_evidencia/SHA256SUMS_E05.txt. Los reportes nuevos requieren resellado."))

def footer(canvas, doc):
    canvas.saveState()
    canvas.setStrokeColor(colors.HexColor("#CBD5E1"))
    canvas.line(1.8*cm, 1.45*cm, 19.2*cm, 1.45*cm)
    canvas.setFont("Arial", 8)
    canvas.setFillColor(gray)
    canvas.drawString(1.8*cm, 1.15*cm, "SI-084 · Taller 05 · Evidencia provisional")
    canvas.drawRightString(19.2*cm, 1.15*cm, f"Página {doc.page}")
    canvas.restoreState()

doc = SimpleDocTemplate(str(OUT), pagesize=(21*cm, 29.7*cm), leftMargin=1.8*cm,
                        rightMargin=1.8*cm, topMargin=1.7*cm, bottomMargin=1.8*cm,
                        title="Informe provisional de evidencias - Taller 05")
doc.build(story, onFirstPage=footer, onLaterPages=footer)
print(OUT)
