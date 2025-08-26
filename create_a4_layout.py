#!/usr/bin/env python3
import base64
import os

def image_to_base64(image_path):
    """Convert image to base64 string"""
    with open(image_path, 'rb') as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode('utf-8')
    return encoded_string

def create_a4_two_column_html(family_base64):
    """Create HTML with A4 two-column layout"""
    html_content = '''<!DOCTYPE html>
<html lang="de">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Elternvertretung - Maxime und Charlotte</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        /* A4 Page Setup */
        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
            line-height: 1.5;
            background: #ffffff;
            color: #32372F;
            font-size: 14px;
        }
        
        @page {
            size: A4;
            margin: 2cm;
        }
        
        .flyer {
            width: 210mm;
            min-height: 297mm;
            margin: 0 auto;
            background: white;
            padding: 0;
            box-shadow: 0 0 10px rgba(0,0,0,0.1);
        }
        
        /* Header */
        .header {
            background: #1A3553;
            color: #FFFFFF;
            padding: 20mm 15mm;
            text-align: center;
            margin-bottom: 0;
        }
        
        .header .subtitle {
            font-size: 18px;
            font-weight: 300;
            letter-spacing: 1px;
            text-transform: uppercase;
        }
        
        /* Main Content Area */
        .content-wrapper {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 10mm;
            padding: 15mm;
            min-height: calc(297mm - 60mm); /* Full page minus header/footer */
        }
        
        /* Left Column */
        .left-column {
            padding-right: 5mm;
        }
        
        /* Right Column */  
        .right-column {
            padding-left: 5mm;
        }
        
        /* Family Photo Section */
        .family-photo-section {
            text-align: center;
            margin-bottom: 15mm;
            padding: 10mm;
            background: #DFE5EC;
            border-radius: 3px;
        }
        
        .family-photo {
            width: 100%;
            max-width: 60mm;
            height: auto;
            border-radius: 3px;
            box-shadow: 0 2px 10px rgba(26, 53, 83, 0.15);
            border: 2px solid #1A3553;
        }
        
        .family-caption {
            margin-top: 5mm;
            font-size: 12px;
            color: #1A3553;
            font-weight: 500;
        }
        
        /* Intro Section */
        .intro {
            font-size: 14px;
            color: #32372F;
            margin-bottom: 12mm;
            line-height: 1.6;
            border-left: 3px solid #1A3553;
            padding-left: 8mm;
            background: #DFE5EC;
            padding: 8mm;
            border-radius: 3px;
        }
        
        /* Sections */
        .section {
            margin-bottom: 12mm;
            break-inside: avoid;
        }
        
        .section h3 {
            color: #1A3553;
            font-size: 16px;
            margin-bottom: 8mm;
            padding-bottom: 2mm;
            border-bottom: 2px solid #DFE5EC;
            font-weight: 500;
            text-transform: uppercase;
            letter-spacing: 0.5px;
        }
        
        .section p {
            color: #32372F;
            margin-bottom: 6mm;
            text-align: justify;
            line-height: 1.6;
            font-size: 13px;
        }
        
        /* Benefits Box */
        .benefits {
            background: #DFE5EC;
            padding: 8mm;
            border-radius: 3px;
            border-left: 4px solid #1A3553;
            margin-bottom: 10mm;
        }
        
        .benefits ul {
            list-style: none;
            padding-left: 0;
        }
        
        .benefits li {
            padding: 3mm 0;
            position: relative;
            padding-left: 8mm;
            color: #32372F;
            font-size: 13px;
        }
        
        .benefits li:before {
            content: "→";
            position: absolute;
            left: 0;
            color: #1A3553;
            font-weight: bold;
            font-size: 14px;
        }
        
        /* Highlight Box */
        .highlight {
            background: #DFE5EC;
            padding: 8mm;
            border-radius: 3px;
            border: 2px solid #1A3553;
            margin: 8mm 0;
            font-size: 13px;
            color: #1A3553;
            font-weight: 500;
        }
        
        /* Footer */
        .footer {
            background: #1A3553;
            color: #FFFFFF;
            padding: 15mm;
            text-align: center;
            font-size: 14px;
            margin-top: auto;
        }
        
        .footer strong {
            display: block;
            margin-top: 3mm;
            font-size: 16px;
            letter-spacing: 0.5px;
        }
        
        /* Print Styles */
        @media print {
            body {
                font-size: 12px !important;
                background: white !important;
                margin: 0 !important;
                padding: 0 !important;
            }
            
            .flyer {
                width: 100% !important;
                min-height: 100vh !important;
                box-shadow: none !important;
                margin: 0 !important;
                padding: 0 !important;
            }
            
            .content-wrapper {
                padding: 10mm !important;
            }
            
            .header, .footer, .benefits, .intro, .family-photo-section, .highlight {
                -webkit-print-color-adjust: exact !important;
                print-color-adjust: exact !important;
            }
            
            .section {
                break-inside: avoid !important;
            }
            
            .family-photo-section {
                break-inside: avoid !important;
            }
        }
        
        /* Screen Preview */
        @media screen {
            body {
                background: #f0f0f0;
                padding: 20px;
            }
        }
    </style>
</head>
<body>
    <div class="flyer">
        <div class="header">
            <div class="subtitle">Kandidaten für die Elternvertretung</div>
        </div>
        
        <div class="content-wrapper">
            <!-- Left Column -->
            <div class="left-column">
                <div class="family-photo-section">
                    <img class="family-photo" 
                         src="data:image/png;base64,''' + family_base64 + '''" 
                         alt="Familie - Charlotte, Maxime und Aljoscha">
                    <div class="family-caption">Charlotte, Maxime und Aljoscha</div>
                </div>
                
                <div class="intro">
                    <strong>Liebe Eltern des Montessori-Kinderhauses,</strong><br><br>
                    wir sind Maxime und Charlotte, die Eltern von Aljoscha aus der Igelgruppe, und möchten uns gerne für die Elternvertretung zur Verfügung stellen.
                </div>
                
                <div class="section">
                    <h3>Wer wir sind</h3>
                    <p>
                        <strong>Maxime</strong> arbeitet als selbständiger IT-Consultant im Bereich Infrastruktur – wenn also mal wieder das WLAN spinnt oder technische Fragen auftauchen, kann er gerne helfen!
                    </p>
                    <p>
                        <strong>Charlotte</strong> ist im Kulturmanagement tätig und bringt verschiedene Kulturprojekte auf die Beine. In Zeitz gehört sie zum Krimzkrams-Team und organisiert das Kulturpicknick für "Kultur auf dem Land" – sie hat also ein Händchen dafür, Menschen zusammenzubringen und Veranstaltungen zu stemmen.
                    </p>
                </div>
            </div>
            
            <!-- Right Column -->
            <div class="right-column">
                <div class="section">
                    <h3>Warum wir uns engagieren möchten</h3>
                    <p>
                        Das Montessori-Konzept hat uns von Anfang an begeistert, und wir sehen täglich, wie wunderbar Aljoscha hier aufblüht. Das Motto <em>"Hilf mir es selbst zu tun"</em> begleitet uns auch zu Hause, und wir möchten gerne etwas von dem zurückgeben, was unsere Familie hier im Kinderhaus erhalten hat.
                    </p>
                    <p>
                        Dabei haben wir immer ein offenes Ohr für die Anliegen und Ideen aller Eltern – egal ob es um den Alltag in der Einrichtung geht, gemeinsame Projekte oder auch mal spontane Aktionen. Wir sind beide unkompliziert und packen gerne mit an, wo Unterstützung gebraucht wird.
                    </p>
                </div>
                
                <div class="section">
                    <h3>Unser Angebot an euch</h3>
                    <div class="benefits">
                        <ul>
                            <li>Verlässliche Ansprechpartner für eure Anliegen</li>
                            <li>Frische Ideen aus unseren beruflichen Erfahrungen</li>
                            <li>Flexibilität bei der Umsetzung von Projekten</li>
                            <li>Eine Portion Spontaneität, wenn mal schnell etwas organisiert werden muss</li>
                        </ul>
                    </div>
                </div>
                
                <div class="highlight">
                    Falls ihr Fragen an uns habt oder einfach mal schnacken möchtet – sprecht uns gerne an! 
                    Wir freuen uns darauf, gemeinsam mit euch das Beste für unsere Kinder herauszuholen.
                </div>
            </div>
        </div>
        
        <div class="footer">
            Herzliche Grüße
            <strong>Maxime und Charlotte</strong>
        </div>
    </div>
</body>
</html>'''
    
    return html_content

if __name__ == "__main__":
    family_image = "wir.png"
    html_file = "index.html"
    
    if not os.path.exists(family_image):
        print(f"❌ Error: {family_image} not found")
        exit(1)
    
    print("Converting family photo to base64...")
    family_base64 = image_to_base64(family_image)
    
    print("Creating A4 two-column layout...")
    html_content = create_a4_two_column_html(family_base64)
    
    with open(html_file, 'w') as f:
        f.write(html_content)
    
    print("✅ HTML file updated with A4 two-column layout!")