import xml.etree.ElementTree as ET
tree = ET.parse('source.xml')
root = tree.getroot()
for child in root.iter():
    print(child.tag)

