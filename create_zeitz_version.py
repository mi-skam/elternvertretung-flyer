#!/usr/bin/env python3
import base64
import os

def image_to_base64(image_path):
    """Convert image to base64 string"""
    with open(image_path, 'rb') as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode('utf-8')
    return encoded_string

def create_zeitz_styled_html(family_base64):
    """Create HTML with Zeitz.de styling"""
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
        
        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
            line-height: 1.6;
            background: #ffffff;
            min-height: 100vh;
            padding: 0;
            font-size: 18px;
            color: #32372F;
        }
        
        .flyer {
            max-width: 800px;
            margin: 0 auto;
            background: white;
            box-shadow: 0 0 20px rgba(26, 53, 83, 0.1);
        }
        
        .header {
            background: #1A3553;
            color: #FFFFFF;
            padding: 30px;
            text-align: center;
        }
        
        .header .subtitle {
            font-size: 1.4em;
            font-weight: 300;
            letter-spacing: 1px;
            text-transform: uppercase;
        }
        
        .family-photo-section {
            display: flex;
            justify-content: center;
            padding: 40px 30px;
            background: #DFE5EC;
        }
        
        .family-photo-container {
            text-align: center;
            max-width: 500px;
        }
        
        .family-photo {
            width: 100%;
            max-width: 450px;
            height: auto;
            border-radius: 3px;
            box-shadow: 0 4px 20px rgba(26, 53, 83, 0.15);
            border: 3px solid #1A3553;
        }
        
        .family-caption {
            margin-top: 15px;
            font-size: 1em;
            color: #1A3553;
            font-weight: 500;
        }
        
        .content {
            padding: 40px;
            background: #FFFFFF;
        }
        
        .intro {
            font-size: 1.1em;
            color: #32372F;
            margin-bottom: 35px;
            line-height: 1.8;
            border-left: 3px solid #1A3553;
            padding-left: 20px;
        }
        
        .section {
            margin-bottom: 35px;
        }
        
        .section h3 {
            color: #1A3553;
            font-size: 1.4em;
            margin-bottom: 20px;
            padding-bottom: 10px;
            border-bottom: 2px solid #DFE5EC;
            font-weight: 500;
            text-transform: uppercase;
            letter-spacing: 0.5px;
        }
        
        .section p {
            color: #32372F;
            margin-bottom: 15px;
            text-align: justify;
            line-height: 1.7;
        }
        
        .benefits {
            background: #DFE5EC;
            padding: 25px;
            border-radius: 3px;
            border-left: 4px solid #1A3553;
        }
        
        .benefits ul {
            list-style: none;
            padding-left: 0;
        }
        
        .benefits li {
            padding: 10px 0;
            position: relative;
            padding-left: 30px;
            color: #32372F;
            font-size: 1em;
        }
        
        .benefits li:before {
            content: "→";
            position: absolute;
            left: 0;
            color: #1A3553;
            font-weight: bold;
            font-size: 1.2em;
        }
        
        .footer {
            background: #1A3553;
            color: #FFFFFF;
            padding: 30px;
            text-align: center;
            font-size: 1.1em;
        }
        
        .footer strong {
            display: block;
            margin-top: 10px;
            font-size: 1.2em;
            letter-spacing: 0.5px;
        }
        
        .highlight {
            background: #DFE5EC;
            padding: 25px;
            border-radius: 3px;
            border: 2px solid #1A3553;
            margin: 25px 0;
            font-size: 1.05em;
            color: #1A3553;
            font-weight: 500;
        }
        
        @media (max-width: 600px) {
            body {
                font-size: 16px;
            }
            
            .family-photo {
                max-width: 100%;
            }
            
            .content {
                padding: 25px;
            }
            
            .header {
                padding: 20px;
            }
            
            .header .subtitle {
                font-size: 1.2em;
            }
        }
        
        @media print {
            body {
                background: white !important;
                padding: 0 !important;
            }
            
            .flyer {
                box-shadow: none !important;
                max-width: none !important;
            }
            
            .header, .footer {
                -webkit-print-color-adjust: exact !important;
                print-color-adjust: exact !important;
            }
            
            .benefits, .highlight {
                -webkit-print-color-adjust: exact !important;
                print-color-adjust: exact !important;
            }
        }
    </style>
</head>
<body>
    <div class="flyer">
        <div class="header">
            <div class="subtitle">Kandidaten für die Elternvertretung</div>
        </div>
        
        <div class="family-photo-section">
            <div class="family-photo-container">
                <img class="family-photo" 
                     src="data:image/png;base64,''' + family_base64 + '''" 
                     alt="Familie - Charlotte, Maxime und Aljoscha">
                <div class="family-caption">Charlotte, Maxime und Aljoscha</div>
            </div>
        </div>
        
        <div class="content">
            <div class="intro">
                <strong>Liebe Eltern des Montessori-Kinderhauses,</strong><br>
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
    
    print("Creating Zeitz-styled HTML...")
    html_content = create_zeitz_styled_html(family_base64)
    
    with open(html_file, 'w') as f:
        f.write(html_content)
    
    print("✅ HTML file updated with Zeitz.de design!")