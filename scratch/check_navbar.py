import glob
for f in glob.glob('*.html'):
    with open(f, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        has_printed_file = False
        for i, line in enumerate(lines):
            if 'class="navbar' in line or '<footer' in line:
                if not has_printed_file:
                    print(f"--- {f} ---")
                    has_printed_file = True
                print(f"L{i}: {line.strip()}")
