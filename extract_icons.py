import re

# Read the HTML file
with open('medical-icons', 'r', encoding='utf-8') as file:
    html_content = file.read()

# Extract icon names using regex
icon_name_pattern = r'<span class="icon-name">([^<]+)</span>'
icon_names = re.findall(icon_name_pattern, html_content)

# Print the results
print("Extracted Icon Names:")
print("=" * 50)
for i, name in enumerate(icon_names, 1):
    print(f"{i:3d}. {name}")

print(f"\nTotal icons found: {len(icon_names)}")

# Save to a text file
with open('medical_icon_names_list.txt', 'w', encoding='utf-8') as output_file:
    for name in icon_names:
        output_file.write(name + '\n')

print("Icon names saved to 'medical_icon_names_list.txt'")

# Also save as a Python list for easy use
with open('medical_icon_names.py', 'w', encoding='utf-8') as py_file:
    py_file.write("medical_icons = [\n")
    for name in icon_names:
        py_file.write(f"    '{name}',\n")
    py_file.write("]\n")

print("Icon names saved as Python list to 'medical_icon_names.py'")