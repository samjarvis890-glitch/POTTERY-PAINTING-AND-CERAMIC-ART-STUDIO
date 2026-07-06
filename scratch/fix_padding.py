import glob
for f in glob.glob('*.html'):
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    content = content.replace('<ul class="navbar-nav gap-3">', '<ul class="navbar-nav gap-1">')
    content = content.replace('<div class="d-none d-xl-flex align-items-center gap-4 text-white">', '<div class="d-none d-xl-flex align-items-center gap-2 text-white">')
    with open(f, 'w', encoding='utf-8') as file:
        file.write(content)
print("Done")
