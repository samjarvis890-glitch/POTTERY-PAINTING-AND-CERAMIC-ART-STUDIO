import glob

for f in glob.glob('*.html'):
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Nav padding py-3 -> py-4
    content = content.replace('sticky-top py-3 shadow-sm', 'sticky-top py-4 shadow-sm')
    
    # Footer padding pt-5 pb-3 -> py-4
    content = content.replace('bg-clay-dark text-white pt-5 pb-3', 'bg-clay-dark text-white py-4')
    
    # Previous fix: gap-3 to gap-1 for menus
    content = content.replace('<ul class="navbar-nav gap-3">', '<ul class="navbar-nav gap-1">')
    
    # Previous fix: gap-4 to gap-2 for desktop right icons
    content = content.replace('<div class="d-none d-xl-flex align-items-center gap-4 text-white">', '<div class="d-none d-xl-flex align-items-center gap-2 text-white">')
    
    # Previous fix: gap-4 to gap-3 for mobile right icons
    content = content.replace('gap-4 text-white mt-3 mb-2 ps-2', 'gap-3 text-white mt-3 mb-2 ps-2')
    
    with open(f, 'w', encoding='utf-8') as file:
        file.write(content)

print("Padding and gaps updated successfully.")
