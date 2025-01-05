import os

# Comments out duplicate lines of .yml files below.

# Recursively find all .yml files
file_paths = []
for root, dirs, files in os.walk("."):
    for file in files:
        if file.endswith(".yml"):
            file_paths.append(os.path.join(root, file))


# Set to false to undo
DEDUPLICATE = True

for file_path in file_paths:
    with open(file_path, "r", encoding="utf-8") as f:
        lines = f.readlines()
    
    # Remove duplicates
    if DEDUPLICATE:
        seen = set()
        with open(file_path, "w", encoding="utf-8") as f:
            for line in lines:
                # Remove everything after first '#' character, then the first ":", and then strip
                stripped_line = line.split("#")[0].split(":")[0].strip()
                if stripped_line not in seen or (line.startswith("#[RM]") or line.startswith("#") or stripped_line == ""):
                    seen.add(stripped_line)
                    f.write(line)
                else:
                    f.write("#[RM] " + line)
    
    else:
        # Uncomment lines starting with "#[RM]"
        with open(file_path, "w", encoding="utf-8") as f:
            for line in lines:
                if line.startswith("#[RM] "):
                    f.write(line[6:])
                else:
                    f.write(line)
