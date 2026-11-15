import os
import sys
from datetime import datetime
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, KeepTogether, HRFlowable
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.pdfgen import canvas

class NumberedCanvas(canvas.Canvas):
    def __init__(self, *args, **kwargs):
        super(NumberedCanvas, self).__init__(*args, **kwargs)
        self._saved_page_states = []

    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        num_pages = len(self._saved_page_states)
        for state in self._saved_page_states:
            self.__dict__.update(state)
            self.draw_page_decorations(num_pages)
            super(NumberedCanvas, self).showPage()
        super(NumberedCanvas, self).save()

    def draw_page_decorations(self, page_count):
        if self._pageNumber == 1:
            return  # Suppress headers/footers on cover page

        self.saveState()
        self.setFont("Helvetica-Bold", 8)
        self.setFillColor(colors.HexColor("#64748B"))
        
        # Header
        self.drawString(54, 750, "CYBERSECURITY FORENSICS & THREAT AUDIT REPORT | CONFIDENTIAL")
        self.setFont("Helvetica", 8)
        self.drawRightString(558, 750, "REF: SEC-2026-TEAMS-001")
        self.setStrokeColor(colors.HexColor("#CBD5E1"))
        self.setLineWidth(0.5)
        self.line(54, 742, 558, 742)

        # Footer
        self.line(54, 45, 558, 45)
        self.drawString(54, 32, "Target Asset: TeamsSetup.bat | Verdict: UNSAFE - DO NOT EXECUTE")
        page_str = f"Page {self._pageNumber} of {page_count}"
        self.drawRightString(558, 32, page_str)
        self.restoreState()

def build_pdf(output_pdf_path):
    doc = SimpleDocTemplate(
        output_pdf_path,
        pagesize=letter,
        leftMargin=54,
        rightMargin=54,
        topMargin=54,
        bottomMargin=54
    )

    styles = getSampleStyleSheet()
    
    # Custom styles
    c_navy = colors.HexColor("#0A192F")
    c_blue = colors.HexColor("#1E3A8A")
    c_red = colors.HexColor("#DC2626")
    c_slate = colors.HexColor("#334155")
    c_muted = colors.HexColor("#64748B")

    title_style = ParagraphStyle(
        'CoverTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=24,
        leading=28,
        textColor=c_navy,
        spaceAfter=10
    )
    subtitle_style = ParagraphStyle(
        'CoverSubTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=13,
        leading=16,
        textColor=c_red,
        spaceAfter=20
    )
    h1 = ParagraphStyle(
        'H1',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=15,
        leading=19,
        textColor=c_navy,
        spaceBefore=14,
        spaceAfter=6
    )
    h2 = ParagraphStyle(
        'H2',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=11,
        leading=14,
        textColor=c_blue,
        spaceBefore=10,
        spaceAfter=4
    )
    body = ParagraphStyle(
        'Body',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=9,
        leading=13,
        textColor=c_slate
    )
    body_bold = ParagraphStyle(
        'BodyBold',
        parent=body,
        fontName='Helvetica-Bold'
    )
    code_snippet = ParagraphStyle(
        'CodeSnippet',
        parent=styles['Normal'],
        fontName='Courier',
        fontSize=7.5,
        leading=10,
        textColor=colors.HexColor("#0F172A")
    )
    badge_crit = ParagraphStyle(
        'BadgeCrit',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=9,
        textColor=colors.white,
        alignment=1
    )

    story = []

    # ================= PAGE 1: COVER PAGE =================
    story.append(Spacer(1, 40))
    story.append(Paragraph("CYBERSECURITY FORENSIC AUDIT & MALWARE ANALYSIS REPORT", title_style))
    story.append(Paragraph("CRITICAL ADVISORY: SOCIAL ENGINEERING & UNAUTHORIZED RMM DROPPER", subtitle_style))
    story.append(HRFlowable(width="100%", thickness=3, color=c_red, spaceAfter=25, spaceBefore=0))

    meta_table_data = [
        [Paragraph("<b>Target Sample:</b>", body), Paragraph("TeamsSetup.bat", body)],
        [Paragraph("<b>Analysis Type:</b>", body), Paragraph("Universal Static Forensics & Execution Flow Decompilation", body)],
        [Paragraph("<b>Sample SHA256:</b>", body), Paragraph("<font size=7>3AA754DFAFBCD44D9A281C6D1F8208E61F185E04AA2AC0FAD3F5F84AD37C73D8</font>", body)],
        [Paragraph("<b>Sample MD5:</b>", body), Paragraph("78CEAFB79D73688158347D1B463C2210", body)],
        [Paragraph("<b>Audit Date:</b>", body), Paragraph(datetime.now().strftime("%Y-%m-%d"), body)],
        [Paragraph("<b>Classification:</b>", body), Paragraph("MALICIOUS DROPPER / TROJAN / RMM ABUSE", body_bold)],
        [Paragraph("<b>Final Verdict:</b>", body), Paragraph("<font color='#DC2626'><b>UNSAFE — DO NOT EXECUTE</b></font>", body_bold)],
        [Paragraph("<b>Author / Auditor:</b>", body), Paragraph("Bhupesh Chandra Dimri | Antigravity Autonomous Security Sandbox", body)]
    ]
    meta_table = Table(meta_table_data, colWidths=[130, 374])
    meta_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor("#F8FAFC")),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor("#E2E8F0")),
        ('TOPPADDING', (0,0), (-1,-1), 6),
        ('BOTTOMPADDING', (0,0), (-1,-1), 6),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
    ]))
    story.append(meta_table)

    story.append(Spacer(1, 40))
    story.append(Paragraph("<b>CONFIDENTIALITY & LEGAL NOTICE</b>", h2))
    notice_text = (
        "This security evaluation document contains proprietary threat intelligence and technical forensic "
        "reconstructions performed under strict defensive authorization. The analyzed sample exhibits severe "
        "malicious indicators designed to compromise enterprise endpoints. All testing was conducted statically "
        "within a secure containment sandbox."
    )
    story.append(Paragraph(notice_text, body))
    story.append(PageBreak())

    # ================= PAGE 2: EXECUTIVE SUMMARY & DASHBOARD =================
    story.append(Paragraph("1. Executive Summary", h1))
    story.append(HRFlowable(width="100%", thickness=1, color=c_blue, spaceAfter=10, spaceBefore=0))
    
    exec_summary = (
        "During automated and forensic triage of <b>TeamsSetup.bat</b>, our audit identified an <b>active "
        "Trojanized installer and malicious dropper</b>. The script masquerades as an official Microsoft Teams "
        "installation package while actively subverting Windows security controls. Upon execution, it forces "
        "administrative privilege elevation, constructs a deceptive Microsoft Edge modal pop-up mimicking legitimate "
        "Teams account provisioning, and silently downloads and installs a remote administration tool "
        "(ConnectWise ScreenConnect) from an unauthorized, suspicious domain (<code>zoompetr[.]com</code>). "
        "The script immediately attempts to purge all local artifacts to prevent SOC detection."
    )
    story.append(Paragraph(exec_summary, body))
    story.append(Spacer(1, 10))

    # Dashboard Table
    dash_data = [
        [Paragraph("<b>Severity</b>", body_bold), Paragraph("<b>Count</b>", body_bold), Paragraph("<b>Key Threat Area</b>", body_bold), Paragraph("<b>Risk Impact</b>", body_bold)],
        [Paragraph("<font color='#DC2626'><b>CRITICAL</b></font>", body), Paragraph("3", body), Paragraph("Silent RMM Backdoor Installation", body), Paragraph("Full System Compromise / Remote Takeover", body)],
        [Paragraph("<font color='#EA580C'><b>HIGH</b></font>", body), Paragraph("2", body), Paragraph("UAC Bypass & Defense Impairment", body), Paragraph("Privilege Escalation & Evasion", body)],
        [Paragraph("<font color='#D97706'><b>MEDIUM</b></font>", body), Paragraph("1", body), Paragraph("Decoy GUI Masquerading", body), Paragraph("High-Fidelity Social Engineering", body)],
        [Paragraph("<font color='#2563EB'><b>LOW / INFO</b></font>", body), Paragraph("1", body), Paragraph("Insecure HTTP CDN Reference", body), Paragraph("Brand Asset Misuse", body)],
    ]
    dash_table = Table(dash_data, colWidths=[80, 50, 194, 180])
    dash_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor("#0A192F")),
        ('TEXTCOLOR', (0,0), (-1,0), colors.white),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor("#CBD5E1")),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.HexColor("#FFFFFF"), colors.HexColor("#F8FAFC")]),
        ('TOPPADDING', (0,0), (-1,-1), 5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 5),
    ]))
    story.append(dash_table)
    story.append(Spacer(1, 12))

    story.append(Paragraph("2. Technical Decompilation & Execution Flow", h1))
    story.append(HRFlowable(width="100%", thickness=1, color=c_blue, spaceAfter=8, spaceBefore=0))

    flow_data = [
        [Paragraph("<b>Stage</b>", body_bold), Paragraph("<b>Technique / Mechanism</b>", body_bold), Paragraph("<b>Malicious Behavior & Forensic Evidence</b>", body_bold)],
        [
            Paragraph("<b>Stage 1: Elevation</b>", body),
            Paragraph("Hidden PowerShell UAC Escalation", body),
            Paragraph("Executes <code>net session</code>. If not elevated, executes <code>powershell -WindowStyle Hidden -Command \"Start-Process '%~f0' -Verb RunAs\"</code> to force administrative rights.", body)
        ],
        [
            Paragraph("<b>Stage 2: Deception</b>", body),
            Paragraph("Edge App-Mode Decoy UI", body),
            Paragraph("Writes fake HTML with Teams branding to <code>%TEMP%\\TeamsSetup.html</code>. Launches Edge with <code>--app=\"...\"</code> and calls Win32 <code>SetWindowPos</code> to force the window permanently on top.", body)
        ],
        [
            Paragraph("<b>Stage 3: Ingress</b>", body),
            Paragraph("Remote Ingress via curl.exe", body),
            Paragraph("Silently downloads <code>https://zoompetr.com/Bin/ScreenConnect.ClientSetup.msi?...</code> saving to <code>%TEMP%\\Microsoft-Teams.msi</code>.", body)
        ],
        [
            Paragraph("<b>Stage 4: Execution</b>", body),
            Paragraph("Unattended MSI Installation", body),
            Paragraph("Executes <code>msiexec.exe /i \"%AGENT_FILE%\" /quiet /qn /norestart</code>. Installs ScreenConnect service silently under SYSTEM context.", body)
        ],
        [
            Paragraph("<b>Stage 5: Anti-Forensics</b>", body),
            Paragraph("Process Kill & Log Purge", body),
            Paragraph("Kills the Edge decoy instance via CIM/WMI, deletes HTML, PS1 script, MSI installer, and temp profile: <code>del /f /q %AGENT_FILE%</code>.", body)
        ]
    ]
    flow_table = Table(flow_data, colWidths=[90, 140, 274])
    flow_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor("#1E3A8A")),
        ('TEXTCOLOR', (0,0), (-1,0), colors.white),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor("#CBD5E1")),
        ('TOPPADDING', (0,0), (-1,-1), 5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 5),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
    ]))
    story.append(flow_table)
    story.append(PageBreak())

    # ================= PAGE 3: DETAILED VULNERABILITY REGISTER =================
    story.append(Paragraph("3. Detailed Threat & Vulnerability Findings", h1))
    story.append(HRFlowable(width="100%", thickness=1, color=c_blue, spaceAfter=10, spaceBefore=0))

    # Finding 1
    f1_header = [
        [Paragraph("<b>FINDING ID: THREAT-001</b>", body_bold), Paragraph("<b>SEVERITY: CRITICAL (CVSS: 9.8)</b>", ParagraphStyle('W', parent=body_bold, textColor=colors.HexColor('#DC2626'), alignment=2))]
    ]
    t_f1 = Table(f1_header, colWidths=[250, 254])
    t_f1.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor("#FEE2E2")),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor("#DC2626")),
        ('PADDING', (0,0), (-1,-1), 5),
    ]))
    story.append(t_f1)
    story.append(Spacer(1, 4))
    story.append(Paragraph("<b>Title: Unauthorized Remote Access Software (ScreenConnect RAT Dropper)</b>", h2))
    f1_desc = (
        "<b>Attack Mechanics:</b> The script connects to an external command server (<code>zoompetr[.]com</code>) "
        "and downloads a pre-configured ConnectWise ScreenConnect client setup package (<code>ScreenConnect.ClientSetup.msi</code>). "
        "The URI parameters (<code>e=Access&y=Guest&c=shyshy</code>) bind the compromised endpoint to an attacker-controlled tenant.<br/>"
        "<b>Impact:</b> Full, persistent remote desktop and shell access over encrypted outbound channels (ports 8041/443), "
        "bypassing standard inbound firewall rules.<br/>"
        "<b>MITRE ATT&CK:</b> T1219 (Remote Access Software), T1105 (Ingress Tool Transfer)."
    )
    story.append(Paragraph(f1_desc, body))
    story.append(Spacer(1, 10))

    # Finding 2
    f2_header = [
        [Paragraph("<b>FINDING ID: THREAT-002</b>", body_bold), Paragraph("<b>SEVERITY: HIGH (CVSS: 8.4)</b>", ParagraphStyle('W', parent=body_bold, textColor=colors.HexColor('#EA580C'), alignment=2))]
    ]
    t_f2 = Table(f2_header, colWidths=[250, 254])
    t_f2.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor("#FFEDD5")),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor("#EA580C")),
        ('PADDING', (0,0), (-1,-1), 5),
    ]))
    story.append(t_f2)
    story.append(Spacer(1, 4))
    story.append(Paragraph("<b>Title: Masquerading & Fake Modal Decoy UI (Brand Spoofing)</b>", h2))
    f2_desc = (
        "<b>Attack Mechanics:</b> Lines 23-100 dynamically synthesize an HTML document featuring official Microsoft Teams "
        "branding, progress bars, and success messages. It leverages Microsoft Edge in borderless application mode "
        "(<code>--app=...</code>) and invokes the Win32 API <code>SetWindowPos</code> to force the decoy window into "
        "the <code>HWND_TOPMOST</code> layer.<br/>"
        "<b>Impact:</b> Users are thoroughly deceived into believing legitimate enterprise software is being configured, "
        "suppressing suspicion while malicious payloads execute in the background.<br/>"
        "<b>MITRE ATT&CK:</b> T1036.005 (Masquerading: Match Legitimate Name or Location)."
    )
    story.append(Paragraph(f2_desc, body))
    story.append(Spacer(1, 10))

    # Finding 3
    f3_header = [
        [Paragraph("<b>FINDING ID: THREAT-003</b>", body_bold), Paragraph("<b>SEVERITY: HIGH (CVSS: 7.8)</b>", ParagraphStyle('W', parent=body_bold, textColor=colors.HexColor('#EA580C'), alignment=2))]
    ]
    t_f3 = Table(f3_header, colWidths=[250, 254])
    t_f3.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor("#FFEDD5")),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor("#EA580C")),
        ('PADDING', (0,0), (-1,-1), 5),
    ]))
    story.append(t_f3)
    story.append(Spacer(1, 4))
    story.append(Paragraph("<b>Title: Anti-Forensic Evasion & Evidence Destruction</b>", h2))
    f3_desc = (
        "<b>Attack Mechanics:</b> Upon completing installation, the script forcibly terminates the decoy Edge browser "
        "process and silently executes multiple deletion commands: removing the temporary HTML, launcher script, "
        "MSI logs, and downloaded installer file.<br/>"
        "<b>Impact:</b> Thwarts superficial post-incident analysis and prevents victims from recovering the dropped installer.<br/>"
        "<b>MITRE ATT&CK:</b> T1070.004 (Indicator Removal on Host: File Deletion)."
    )
    story.append(Paragraph(f3_desc, body))
    story.append(PageBreak())

    # ================= PAGE 4: IOCS & INCIDENT RESPONSE =================
    story.append(Paragraph("4. Technical Indicators of Compromise (IOCs)", h1))
    story.append(HRFlowable(width="100%", thickness=1, color=c_blue, spaceAfter=10, spaceBefore=0))

    ioc_data = [
        [Paragraph("<b>Indicator Type</b>", body_bold), Paragraph("<b>Artifact Value / Signature</b>", body_bold), Paragraph("<b>Context / Notes</b>", body_bold)],
        [Paragraph("File (SHA256)", body), Paragraph("<font size=6.5>3AA754DFAFBCD44D9A281C6D1F8208E61F185E04AA2AC0FAD3F5F84AD37C73D8</font>", body), Paragraph("TeamsSetup.bat initial dropper script", body)],
        [Paragraph("File (MD5)", body), Paragraph("78CEAFB79D73688158347D1B463C2210", body), Paragraph("TeamsSetup.bat payload hash", body)],
        [Paragraph("Network Domain", body), Paragraph("<code>zoompetr[.]com</code>", body), Paragraph("Command & payload distribution server (Typosquatting Zoom)", body)],
        [Paragraph("IPv4 Address", body), Paragraph("<code>135.84.215.218</code>", body), Paragraph("Resolved IP for zoompetr[.]com", body)],
        [Paragraph("Network URL", body), Paragraph("<font size=6.5>https://zoompetr[.]com/Bin/ScreenConnect.ClientSetup.msi?e=Access&y=Guest&c=shyshy</font>", body), Paragraph("ScreenConnect deployment endpoint", body)],
        [Paragraph("Temporary File", body), Paragraph("<code>%TEMP%\\Microsoft-Teams.msi</code>", body), Paragraph("Staged ScreenConnect installer", body)],
        [Paragraph("Temporary File", body), Paragraph("<code>%TEMP%\\TeamsSetup.html</code>", body), Paragraph("Spoofed Teams setup user interface", body)],
        [Paragraph("Temporary File", body), Paragraph("<code>%TEMP%\\launch_ui.ps1</code>", body), Paragraph("Edge App-mode launcher script", body)],
        [Paragraph("Directory", body), Paragraph("<code>%TEMP%\\EdgeTempProfile</code>", body), Paragraph("Disposable Edge user profile", body)],
    ]
    ioc_table = Table(ioc_data, colWidths=[90, 250, 164])
    ioc_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor("#0A192F")),
        ('TEXTCOLOR', (0,0), (-1,0), colors.white),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor("#CBD5E1")),
        ('TOPPADDING', (0,0), (-1,-1), 4),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
    ]))
    story.append(ioc_table)
    story.append(Spacer(1, 14))

    story.append(Paragraph("5. Recommended Remediation & Containment Plan", h1))
    story.append(HRFlowable(width="100%", thickness=1, color=c_blue, spaceAfter=8, spaceBefore=0))

    rem_text = (
        "<b>Immediate Actions (Containment):</b><br/>"
        "1. <b>Isolate Endpoint:</b> Immediately disconnect any host where this script was executed from the local network.<br/>"
        "2. <b>Terminate ScreenConnect Services:</b> Check for running services named <code>ScreenConnect Client (...)</code> "
        "or processes named <code>ScreenConnect.ClientService.exe</code> and kill them immediately.<br/>"
        "3. <b>Uninstall Malicious MSI:</b> Query installed programs via PowerShell: "
        "<code>Get-Package -Name '*ScreenConnect*' | Uninstall-Package</code>.<br/>"
        "4. <b>Firewall & DNS Block:</b> Block domain <code>zoompetr[.]com</code> and IP <code>135.84.215.218</code> across perimeter firewalls and EDR agents.<br/><br/>"
        "<b>Long-Term Hardening:</b><br/>"
        "• Restrict batch and script execution from standard user temp directories (<code>AppData\\Local\\Temp</code>) via AppLocker / Software Restriction Policies.<br/>"
        "• Deploy EDR sensors with behavioral rules detecting unauthorized RMM software installations.<br/>"
        "• Enforce Application Control to block unapproved ScreenConnect instances."
    )
    story.append(Paragraph(rem_text, body))
    story.append(Spacer(1, 14))

    # Security Verdict Box
    verdict_data = [
        [Paragraph("<b>FINAL SECURITY VERDICT</b>", ParagraphStyle('V', parent=body_bold, textColor=colors.white, alignment=1))],
        [Paragraph("<font size=14 color='#DC2626'><b>UNSAFE — DO NOT EXECUTE</b></font><br/><br/>"
                   "This artifact is a weaponized social engineering dropper designed to install a persistent backdoor under administrative context. "
                   "Executing this file results in complete remote compromise of the host system.", ParagraphStyle('VD', parent=body, alignment=1))]
    ]
    t_v = Table(verdict_data, colWidths=[504])
    t_v.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor("#0A192F")),
        ('BACKGROUND', (0,1), (-1,1), colors.HexColor("#FEF2F2")),
        ('BOX', (0,0), (-1,-1), 2, colors.HexColor("#DC2626")),
        ('PADDING', (0,0), (-1,-1), 10),
    ]))
    story.append(t_v)

    doc.build(story, canvasmaker=NumberedCanvas)
    print(f"Report generated successfully: {output_pdf_path}")

if __name__ == "__main__":
    out_dir = r"C:\Users\bhupe\Downloads\Backend\cyber\Cybersecurity_Audit\05_Final_PDF_Report"
    os.makedirs(out_dir, exist_ok=True)
    out_file = os.path.join(out_dir, "Cybersecurity_Audit_Report_TeamsSetup_2026-11-14.pdf")
    build_pdf(out_file)
