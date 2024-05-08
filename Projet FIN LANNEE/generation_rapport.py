import json
try:
    from reportlab.lib.pagesizes import letter
    from reportlab.pdfgen import canvas
    from reportlab.lib import colors
    from reportlab.lib.units import inch
    from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph
    from reportlab.lib.styles import ParagraphStyle
except:
    pass

def truncate_text(text, max_length):
    if len(text) > max_length:
        return text[:max_length - 3] + "..."  # Truncate and add ellipsis
    return text


def render_all_to_pdf(pdf_file,dns_file,nmap_file,cve_file,user_file,password_file,nikto_file,gobuster_file):
    doc = SimpleDocTemplate(pdf_file, pagesize=letter)
    elements = []
    
    intro_text = """
        Welcome to the Recon-NG penetration testing report. 
        This document outlines findings from our assessment of your cybersecurity defenses. 
        Our goal was to identify vulnerabilities and provide actionable recommendations to enhance security. 
        This report will guide you in strengthening its defenses and safeguarding against cyber threats.
    """
    
     # Read JSON data from file
    with open(dns_file, 'r') as f:
        dns_data = json.load(f)
    
    line_break_style = ParagraphStyle(name='LineBreak', fontSize=12, leading=12)
    line_breaks = Paragraph("<br/><br/>", line_break_style)
    
    
    intro_style = ParagraphStyle(name='Introduction', fontSize=12, leading=14)
    intro_paragraph = Paragraph(intro_text, style=intro_style)
    elements.append(intro_paragraph)
    elements.append(line_breaks)
    
    paragraph = Paragraph(f"{dns_data['Domain']} DNS Footprinting:", ParagraphStyle(name='Header'))
    elements.append(paragraph)
    elements.append(line_breaks)

    for record_type, records in dns_data.items():
        if record_type != 'Domain':
            elements.append(Paragraph(f"{record_type}:", ParagraphStyle(name='Subheader')))
            for record in records:
                elements.append(Paragraph(record, ParagraphStyle(name='Body')))
            elements.append(Paragraph("<br/><br/>", ParagraphStyle(name='Body')))
    elements.append(line_breaks)
    
    # Read JSON data from file
    with open(nmap_file, 'r') as f:
        nmap_data = json.load(f)
    
    nmap_header = "Nmap Scan results: "
    header = Paragraph(nmap_header, ParagraphStyle(name='Header', fontSize=16, alignment=1))
    elements.append(header)

    # Add new lines between header and table
    elements.extend([Paragraph("<br/>", ParagraphStyle(name='Header', fontSize=12, alignment=1))])
    
 # Define table data and style
    table_data = []
    seen_ports = set()
    for scan_type, scan_data in nmap_data.items():
        for port, port_data in scan_data.items():
            if port not in seen_ports:
                table_data.append([scan_type, port, port_data['state'], port_data['name']])
                seen_ports.add(port)

    style = TableStyle([('BACKGROUND', (0, 0), (-1, 0), colors.grey),
                        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
                        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
                        ('GRID', (0, 0), (-1, -1), 1, colors.black)])

    # Create table and apply style
    table = Table(table_data)
    table.setStyle(style)
    elements.append(line_breaks)
    elements.append(table)
    elements.append(line_breaks)

    
    # Read JSON data from file
    with open(cve_file, 'r') as f:
        cve_data = json.load(f)

    # Create table data
    table_data = [["CPE", "Score", "Link"]]

    # Add the sentence with IP address as a header
    ip_header = "Common Vulnerability Exploits found for: "
    for ip in cve_data:
        ip_header += ip + ", "
    ip_header = ip_header[:-2]  # Remove the last comma and space
    header = Paragraph(ip_header, ParagraphStyle(name='Header', fontSize=16, alignment=1))
    elements.append(header)

    # Add new lines between header and table
    elements.extend([Paragraph("<br/>", ParagraphStyle(name='Header', fontSize=12, alignment=1))])

    # Populate table data with vulnerability details
    for ip, ports in cve_data.items():
        for port, vulnerabilities in ports.items():
            for vuln in vulnerabilities:
                cpe = truncate_text(vuln['cpe'], 30)  # Truncate CPE to fit within 30 characters
                score = vuln['score']
                link = truncate_text(vuln['link'], 50)  # Truncate link to fit within 50 characters
                table_data.append([cpe, score, link])

    # Define table style
    style = TableStyle([('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
                        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                        ('BACKGROUND', (0, 1), (-1, 1), colors.beige),
                        ('GRID', (0, 0), (-1, -1), 1, colors.black)])

    # Create table
    table = Table(table_data, colWidths=[3*inch, 0.5*inch, 4*inch])  # Adjust column widths
    table.setStyle(style)
    elements.append(line_breaks)
    elements.append(table)

    
    with open(user_file, 'r') as f:
        user_data = json.load(f)
    
    usernames = [item['username'] for item in user_data]

    # Calculate number of rows and columns
    num_users = len(usernames)
    num_cols = 4
    num_rows = -(-num_users // num_cols)  # Ceiling division

    # Create table data
    table_data = [["Users Found"]]

    # Populate table data with usernames
    for i in range(num_rows):
        row = []
        for j in range(num_cols):
            index = i + j * num_rows
            if index < num_users:
                row.append(usernames[index])
            else:
                row.append('')
        table_data.append(row)

    # Define table style
    style = TableStyle([('BACKGROUND', (0, 0), (-1, 0), colors.grey),
                        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
                        ('GRID', (0, 0), (-1, -1), 1, colors.black),
                        ('SPAN', (0, 0), (-1, 0))])

    # Create table
    table = Table(table_data)
    table.setStyle(style)
    elements.append(line_breaks)
    elements.append(table)
    
    with open(password_file, 'r') as f:
        password_data = json.load(f)

   # Create table data
    table_data = [["Successful SSH BruteForce Connections"]]
    table_data.extend([["Username", "Password", "Password Complexity"]])

    # Populate table data with usernames, passwords, and complexities
    for username, user_data in password_data.items():
        table_data.append([username, user_data['password'], user_data['password_complexity']])

    # Define table style
    style = TableStyle([('BACKGROUND', (0, 0), (-1, 0), colors.grey),
                        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
                        ('GRID', (0, 0), (-1, -1), 1, colors.black),
                        ('SPAN', (0, 0), (-1, 0)),
                        ('ALIGN', (0, 0), (-1, 0), 'CENTER')])

    # Create table
    table = Table(table_data)
    table.setStyle(style)
    elements.append(line_breaks)
    elements.append(table)

 # Read JSON data from file
    with open(nikto_file, 'r') as f:
        nikto_data = json.load(f)

    # Extract relevant information
    host = nikto_data["host"]
    ip = nikto_data["ip"]
    port = nikto_data["port"]
    vulnerabilities = nikto_data["vulnerabilities"]

    elements.append(line_breaks)
    # Add header
    header_text = f"Vulnerabilities for {host} ({ip}:{port})"
    header = Paragraph(header_text, ParagraphStyle(name='Header', fontSize=16, alignment=1))
    elements.append(header)

    # Add new line after header
    elements.extend([Paragraph("<br/><br/>", ParagraphStyle(name='Header', fontSize=12, alignment=1))])

    # Add vulnerabilities as paragraphs
    for vulnerability in vulnerabilities:
        paragraph_text = f"<b>ID:</b> {vulnerability.get('id', '')}<br/>" \
                         f"<b>References:</b> {vulnerability.get('references', '')}<br/>" \
                         f"<b>Method:</b> {vulnerability.get('method', '')}<br/>" \
                         f"<b>URL:</b> {vulnerability.get('url', '')}<br/>" \
                         f"<b>Message:</b> {vulnerability.get('msg', '')}<br/>"
        paragraph = Paragraph(paragraph_text, ParagraphStyle(name='Body'))
        elements.append(paragraph)

        # Add new line between paragraphs
        elements.extend([Paragraph("<br/><br/>", ParagraphStyle(name='Body'))])
    
    with open(gobuster_file, 'r') as f:
        gobuster_data = json.load(f)

    # Header
    header_text = "Gobuster Results"
    header = Paragraph(header_text, ParagraphStyle(name='Header', fontSize=16, alignment=1))
    elements.append(header)

    # Add new lines between header and table
    elements.extend([Paragraph("<br/>", ParagraphStyle(name='Header', fontSize=12, alignment=1))])

    # Create table data
    table_data = [["Path", "Status Code"]]

    # Populate table data with JSON content
    for item in gobuster_data:
        table_data.append([item["path"], item["status_code"]])

    # Define table style
    style = TableStyle([('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
                        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                        ('BACKGROUND', (0, 1), (-1, 1), colors.beige),
                        ('GRID', (0, 0), (-1, -1), 1, colors.black)])

    # Create table
    table = Table(table_data, colWidths=[3*inch, 1*inch])  # Adjust column widths
    table.setStyle(style)
    elements.append(line_breaks)
    elements.append(table)  
        
    
    # Write the PDF file
    doc.build(elements)
    print(f"PDF file '{pdf_file}' generated successfully.")
