import glob
for f in glob.glob('*.html'):
    print(f"--- {f} ---")
    with open(f, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        for i, line in enumerate(lines):
            if '<nav ' in line or '<footer ' in line:
                print(f"L{i}: {line.strip()}")
                # print next line to see container
                if i+1 < len(lines):
                    print(f"L{i+1}: {lines[i+1].strip()}")
