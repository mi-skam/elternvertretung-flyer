#!/usr/bin/env python3
import base64
import os

def image_to_base64(image_path):
    """Convert image to base64 string"""
    with open(image_path, 'rb') as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode('utf-8')
    return encoded_string

def create_updated_html(family_base64):
    """Create updated HTML with family photo"""
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
            font-family: 'Georgia', serif;
            line-height: 1.6;
            background: white;
            min-height: 100vh;
            padding: 0;
        }
        
        .flyer {
            max-width: 800px;
            margin: 0 auto;
            background: white;
        }
        
        .header {
            background: linear-gradient(135deg, #20b2aa 0%, #00ced1 50%, #40e0d0 100%);
            color: white;
            padding: 15px 30px;
            text-align: center;
        }
        
        .header .subtitle {
            font-size: 1.2em;
            font-weight: 500;
            letter-spacing: 0.5px;
        }
        
        .family-photo-section {
            display: flex;
            justify-content: center;
            padding: 30px;
            background: #f8f9fa;
        }
        
        .family-photo-container {
            text-align: center;
            max-width: 500px;
        }
        
        .family-photo {
            width: 100%;
            max-width: 450px;
            height: auto;
            border-radius: 10px;
            box-shadow: 0 4px 15px rgba(0,0,0,0.1);
            border: 4px solid #20b2aa;
        }
        
        .family-caption {
            margin-top: 15png;
            font-size: 1.1em;
            color: #333;
            font-style: italic;
        }
        
        .content {
            padding: 40px;
        }
        
        .intro {
            font-size: 1.1em;
            color: #2c3e50;
            margin-bottom: 30px;
            line-height: 1.8;
        }
        
        .section {
            margin-bottom: 30px;
        }
        
        .section h3 {
            color: #20b2aa;
            font-size: 1.3em;
            margin-bottom: 15px;
            border-bottom: 2px solid #20b2aa;
            padding-bottom: 5px;
        }
        
        .section p {
            color: #34495e;
            margin-bottom: 15px;
            text-align: justify;
        }
        
        .benefits {
            background: #f8f9fa;
            padding: 20px;
            border-radius: 5px;
            border-left: 4px solid #20b2aa;
        }
        
        .benefits ul {
            list-style: none;
            padding-left: 0;
        }
        
        .benefits li {
            padding: 8px 0;
            position: relative;
            padding-left: 25px;
            color: #2c3e50;
        }
        
        .benefits li:before {
            content: "✓";
            position: absolute;
            left: 0;
            color: #20b2aa;
            font-weight: bold;
        }
        
        .footer {
            background: linear-gradient(135deg, #20b2aa 0%, #00ced1 50%, #40e0d0 100%);
            color: white;
            padding: 25px;
            text-align: center;
            font-size: 1.1em;
        }
        
        .highlight {
            background: #fff3cd;
            padding: 20px;
            border-radius: 5px;
            border: 1px solid #ffeaa7;
            margin: 20px 0;
        }
        
        @media (max-width: 600px) {
            .family-photo {
                max-width: 100%;
            }
            
            .content {
                padding: 25px;
            }
            
            .header h1 {
                font-size: 1.8em;
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
                border-radius: 0 !important;
            }
            
            .header, .footer {
                -webkit-print-color-adjust: exact !important;
                color-adjust: exact !important;
            }
            
            .benefits, .highlight {
                border-radius: 0 !important;
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
                    Das Montessori-Konzept hat uns von Anfan an begeistert, und wir sehen täglich, wie wunderbar Aljoscha hier aufblüht. Das Motto <em>"Hilf mir es selbst zu tun"</em> begleitet uns auch zu Hause, und wir möchten gerne etwas von dem zurückgeben, was unsere Familie hier im Kinderhaus erhalten hat.
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
            Herzliche Grüße<br>
            <strong>Maxime und Charlotte</strong>
        </div>
    </div>
</body>
</html>'''
    
    return html_content

if __name__ == "__main__":
    family_image = "wir.png"
    html_file = "eltern_flyer.html"
    
    if not os.path.exists(family_image):
        print(f"❌ Error: {family_image} not found")
        exit(1)
    
    print("Converting family photo to base64...")
    family_base64 = image_to_base64(family_image)
    
    print("Creating updated HTML with family photo...")
    html_content = create_updated_html(family_base64)
    
    with open(html_file, 'w') as f:
        f.write(html_content)
    
    print("✅ HTML file updated with family photo!")