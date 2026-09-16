"""Informe de evidencia visual real y resultados medidos del Taller 05."""

from pathlib import Path
from xml.sax.saxutils import escape

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import Image, PageBreak, Paragraph, SimpleDocTemplate, Spacer, Table, TableStyle
from PIL import Image as PILImage

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "output/pdf/SI084-S05-Ahmed-Evidencias-capturas.pdf"
OUT.parent.mkdir(parents=True, exist_ok=True)

pdfmetrics.registerFont(TTFont("Arial", "C:/Windows/Fonts/arial.ttf"))
pdfmetrics.registerFont(TTFont("Arial-Bold", "C:/Windows/Fonts/arialbd.ttf"))
NAVY = colors.HexColor("#15275A")
TEAL = colors.HexColor("#0F766E")
INK = colors.HexColor("#283548")
PALE = colors.HexColor("#EAF1F8")
styles = getSampleStyleSheet()
styles.add(ParagraphStyle(name="TitleES", fontName="Arial-Bold", fontSize=17, leading=22, textColor=NAVY, alignment=TA_CENTER, spaceAfter=14))
styles.add(ParagraphStyle(name="HeadES", fontName="Arial-Bold", fontSize=12, leading=17, textColor=TEAL, spaceBefore=13, spaceAfter=7))
styles.add(ParagraphStyle(name="BodyES", fontName="Arial", fontSize=9, leading=13.5, textColor=INK, spaceAfter=8))
styles.add(ParagraphStyle(name="SmallES", fontName="Arial", fontSize=7.6, leading=11, textColor=INK, spaceAfter=5))
styles.add(ParagraphStyle(name="CellES", fontName="Arial", fontSize=8, leading=11, textColor=INK))
styles.add(ParagraphStyle(name="WhiteES", fontName="Arial-Bold", fontSize=8, leading=11, textColor=colors.white))


def para(value, style="BodyES"):
    return Paragraph(value, styles[style])


def table(headers, rows, widths):
    data = [[para(escape(str(v)), "WhiteES") for v in headers]]
    data.extend([[para(escape(str(v)), "CellES") for v in row] for row in rows])
    result = Table(data, colWidths=widths, repeatRows=1, hAlign="LEFT")
    result.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), NAVY),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, PALE]),
        ("GRID", (0, 0), (-1, -1), 0.3, colors.HexColor("#CBD5E1")),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 7),
        ("RIGHTPADDING", (0, 0), (-1, -1), 7),
        ("TOPPADDING", (0, 0), (-1, -1), 6),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
    ]))
    return result


def screenshot(filename, caption):
    path = ROOT / "20_evidencia/E05_app" / filename
    with PILImage.open(path) as im:
        width, height = im.size
    max_width = 17.3 * cm
    max_height = 17.0 * cm
    scale = min(max_width / width, max_height / height)
    result = Image(str(path), width=width * scale, height=height * scale)
    result.hAlign = "CENTER"
    return [result, Spacer(1, 0.35 * cm), para(escape(caption), "SmallES")]


story = [
    para("UNIVERSIDAD PRIVADA DE TACNA<br/>INGENIERÍA DE SISTEMAS", "TitleES"),
    para("SI-084 · Auditoría de Sistemas · Semana 05", "TitleES"),
    para("Evidencias reales del laboratorio", "TitleES"),
    Spacer(1, 0.5 * cm),
    para("<b>Estudiante:</b> Ahmed Hasan Akhtar Oviedo<br/><b>Código:</b> 2022074261<br/><b>Modalidad:</b> individual<br/><b>Fecha:</b> 16 de septiembre de 2026"),
    para("Este documento reúne todas las capturas obtenidas hasta este corte y enlaza los registros técnicos. Las imágenes provienen de un navegador automatizado conectado a los servicios locales reales. No son capturas del escritorio Windows."),
    para("1. Alcance y cadena de evidencia", "HeadES"),
    para("El alcance quedó registrado antes de las pruebas en el commit 001493d. Las pruebas se limitaron a los contenedores locales de la red audit_net. Las capturas y mediciones están en el commit local 8a7c1d0 y los hashes de 31 archivos constan en 20_evidencia/SHA256SUMS_E05.txt."),
    table(["Componente", "Evidencia"], [
        ("Aplicación", "Juice Shop en 127.0.0.1:3000; ZAP baseline y full"),
        ("Portal", "WordPress en 127.0.0.1:8082; pantalla de instalación"),
        ("Infraestructura", "Nmap, cuatro hosts de laboratorio y contraste documentado"),
        ("Detección", "Wazuh 4.9.0; agente 001; tres alertas web reales"),
        ("Recuperación", "Restic: restauración 2,42 s y SHA-256 coincidente"),
    ], [4.2 * cm, 13.1 * cm]),
    Spacer(1, 0.4 * cm),
    para("Límites: no se aportó inventario organizacional aprobado, firma del docente ni número de grupo. El portal de WordPress aún muestra el instalador. Este PDF documenta evidencia observada; no sustituye las firmas ni el formato final que exija la asignatura."),
    PageBreak(),
    para("2. Captura 1 · Juice Shop al abrir", "HeadES"),
    para("La aplicación respondió en el puerto 3000 y mostró su ventana inicial de bienvenida."),
]
story.extend(screenshot("01_juiceshop_real.png", "Figura 1. Captura real del navegador: Juice Shop con el diálogo inicial. Archivo: 20_evidencia/E05_app/01_juiceshop_real.png."))
story.extend([
    PageBreak(),
    para("3. Captura 2 · Juice Shop sin diálogos", "HeadES"),
    para("Se cerraron el mensaje de bienvenida y el aviso de cookies para documentar la portada operativa."),
])
story.extend(screenshot("02_juiceshop_portada_real.png", "Figura 2. Captura real del navegador: catálogo de Juice Shop. Archivo: 20_evidencia/E05_app/02_juiceshop_portada_real.png."))
story.extend([
    PageBreak(),
    para("4. Captura 3 · Portal WordPress", "HeadES"),
    para("El puerto 8082 abrió el instalador de WordPress. La captura demuestra respuesta del servicio, sin afirmar que la instalación esté configurada."),
])
story.extend(screenshot("03_wordpress_instalacion_real.png", "Figura 3. Captura real del navegador: selección de idioma en el instalador de WordPress. Archivo: 20_evidencia/E05_app/03_wordpress_instalacion_real.png."))
story.extend([
    PageBreak(),
    para("5. Resultados técnicos asociados", "HeadES"),
    para("ZAP produjo reportes baseline y full para Juice Shop en HTML y JSON. La matriz de cinco alertas y su mapeo se conserva en 40_hallazgos/PT05_alertas_zap.csv. Las alertas requieren validación manual para sostener un hallazgo definitivo."),
    para("Nmap identificó los servicios de los cuatro contenedores de laboratorio: Juice Shop (3000), WordPress/Apache (80), MariaDB (3306) y PostgreSQL (5432). No hay inventario previo aprobado para calificar uno como servicio no inventariado."),
    para("Wazuh recibió el registro Apache del portal mediante el agente 001. Tres solicitudes de prueba marcadas e05_01, e05_02 y e05_03 produjeron alertas reales del manager. Esta tabla transcribe los valores del CSV y JSONL originales; no representa una captura del panel."),
    table(["Evento", "Regla Wazuh", "Latencia"], [
        ("e05_01", "31164", "2,933 s"),
        ("e05_02", "31106", "3,004 s"),
        ("e05_03", "31106", "4,016 s"),
        ("Promedio", "MTTD", "3,318 s"),
    ], [5.3 * cm, 5.3 * cm, 6.7 * cm]),
    Spacer(1, 0.3 * cm),
    para("En la repetición de Nmap con el agente activo no apareció alerta de escaneo en la ventana de observación más 20 segundos. El correo de alertas estaba desactivado y no se demostró inmutabilidad o retención de registros."),
    para("La restauración restic de la base ERP de prueba tomó 2,42 segundos, con SHA-256 original y restaurado idénticos. La revisión restic check --read-data terminó sin errores. No se aportaron objetivos RTO/RPO para comparar el resultado."),
    para("<b>Rutas de respaldo:</b> 20_evidencia/E05_app/zap_*.{html,json}; 20_evidencia/E05_infra/; 20_evidencia/E05_wazuh/alertas_prueba.jsonl; 30_papeles_trabajo/PT05-D-mttd.csv; 30_papeles_trabajo/PT05-B.md, PT05-C.md y PT05-D.md."),
    para("<b>Captura del panel Wazuh:</b> no disponible en este corte. Computer Use no pudo conectarse a Windows (os error 2) y el navegador de prueba rechazó el certificado local autofirmado del dashboard. Las alertas se verificaron directamente en el manager y se preservaron en JSONL."),
])


def footer(canvas, doc):
    canvas.saveState()
    canvas.setStrokeColor(colors.HexColor("#CBD5E1"))
    canvas.line(1.8 * cm, 1.45 * cm, 19.1 * cm, 1.45 * cm)
    canvas.setFont("Arial", 8)
    canvas.setFillColor(INK)
    canvas.drawString(1.8 * cm, 1.15 * cm, "SI-084 · Taller 05 · Ahmed Hasan Akhtar Oviedo")
    canvas.drawRightString(19.1 * cm, 1.15 * cm, f"Página {doc.page}")
    canvas.restoreState()


doc = SimpleDocTemplate(str(OUT), pagesize=(21 * cm, 29.7 * cm), leftMargin=1.8 * cm,
                        rightMargin=1.9 * cm, topMargin=1.7 * cm, bottomMargin=1.9 * cm,
                        title="SI084 S05 - Evidencias y capturas reales")
doc.build(story, onFirstPage=footer, onLaterPages=footer)
print(OUT)
