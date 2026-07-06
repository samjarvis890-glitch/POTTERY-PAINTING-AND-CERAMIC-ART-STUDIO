import glob

for f in glob.glob('*.html'):
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Remove the bad padding
    content = content.replace(' style="padding: 2% !important;"', '')
    
    with open(f, 'w', encoding='utf-8') as file:
        file.write(content)

print("Removed body padding successfully.")
