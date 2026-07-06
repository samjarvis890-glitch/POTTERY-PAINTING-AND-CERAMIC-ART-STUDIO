import glob
import re

for f in glob.glob('*.html'):
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Replace plain <body>
    if '<body>' in content:
        content = content.replace('<body>', '<body style="padding: 2% !important;">')
    else:
        # For tags like <body class="...">
        content = re.sub(r'<body([^>]*)>', r'<body\1 style="padding: 2% !important;">', content)
        
    with open(f, 'w', encoding='utf-8') as file:
        file.write(content)

print("Full page padding added successfully.")
