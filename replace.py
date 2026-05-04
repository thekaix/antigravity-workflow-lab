import re

file_path = r'C:\Users\Karin\Desktop\ebook.html'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace hex backgrounds to light theme
content = content.replace('#0f172a', '#faf5f0')
content = content.replace('#1e1b4b', '#f5e8e3')
content = content.replace('#1a1f35', '#f0dcd6')
content = content.replace('#1a1f3a', '#faf5f0')
content = content.replace('#252b45', '#f5e8e3')

# Replace white text to dark brown
content = content.replace('text-white', 'text-[#8b3a62]')

# Replace slate texts to muted browns
content = content.replace('text-slate-200', 'text-[#6b5563]')
content = content.replace('text-slate-300', 'text-[#6b5563]')
content = content.replace('text-slate-400', 'text-[#9b7a89]')
content = content.replace('text-slate-500', 'text-[#8b6b7d]')

# Replace colored texts to accents
content = re.sub(r'text-(cyan|green)-[34]00', 'text-[#a16d84]', content)
content = re.sub(r'text-(purple|pink|yellow|red)-[34]00', 'text-[#be185d]', content)

# Replace inline text gradients to solid color
content = re.sub(r'style="background:\s*linear-gradient\([^)]+\);\s*-webkit-background-clip:text;\s*-webkit-text-fill-color:transparent;"', 'style="color: #8b3a62;"', content)

# Replace benefit check color
content = content.replace('color: #63d2ff;', 'color: #be185d;')

# Update glass backgrounds to pinkish glass
content = content.replace('rgba(255,255,255,0.06)', 'rgba(236,72,153,0.08)')
content = content.replace('rgba(255,255,255,0.1)', 'rgba(236,72,153,0.15)')
content = content.replace('rgba(255,255,255,0.08)', 'rgba(236,72,153,0.06)')
content = content.replace('rgba(255,255,255,0.12)', 'rgba(236,72,153,0.12)')

# Add print optimization inside @media print
print_media = r'''@media print {
      * { -webkit-print-color-adjust: exact !important; print-color-adjust: exact !important; color-adjust: exact !important; }
      html, body { background: #faf5f0 !important; }
      .slide-in { animation: none; opacity: 1; transform: none; }
      .float { animation: none; }
      section { page-break-inside: avoid; break-inside: avoid; page-break-after: always; }
      .glass { background: rgba(236, 72, 153, 0.06) !important; border: 1px solid rgba(236, 72, 153, 0.12) !important; }
      div[style*="background: linear-gradient"] { -webkit-print-color-adjust: exact !important; print-color-adjust: exact !important; }
    }'''

content = re.sub(r'@media print\s*\{[^}]+\}', print_media, content, count=1, flags=re.DOTALL)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print('Colors adapted successfully.')
