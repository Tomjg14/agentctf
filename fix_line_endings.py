import os

def fix_line_endings(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.sh'):
                filepath = os.path.join(root, file)
                with open(filepath, 'rb') as f:
                    content = f.read()
                if b'\r\n' in content:
                    with open(filepath, 'wb') as f:
                        f.write(content.replace(b'\r\n', b'\n'))
                    print(f"Fixed line endings for: {filepath}")

if __name__ == "__main__":
    fix_line_endings(".")