import re

# def extract_ancestral_traits(md_file_path, output_file_path):

source = "../Build/Traits.md"
output = "../Build/Traits Table.md"

with open(source, 'r', encoding='utf-8') as f:
    lines = f.readlines()


collecting = False
traits = []
current_section = None
valid_sections = {"Ancestral Traits", "Learned Traits", "Magical Traits"}

for line in lines:
    header_match = re.match(r"#\s+(.*)", line.strip())
    if header_match:
        section_title = header_match.group(1)
        if section_title in valid_sections:
            collecting = True
            current_section = section_title
            continue
        elif section_title.startswith("Learned") or section_title.startswith("Magical"):
            collecting = current_section in valid_sections
            continue
        else:
            collecting = False
            current_section = None
            continue

    if collecting and line.strip().startswith("- **"):
        trait_match = re.match(r"- \*\*(.+?)\*\*", line.strip())
        if trait_match:
            traits.append(trait_match.group(1))





with open(output, 'w', encoding='utf-8') as f:
    for i, trait in enumerate(traits, start=1):
        print(i, trait)
        f.write(f"{i}. {trait}\n")


