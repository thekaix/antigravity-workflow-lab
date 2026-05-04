import re

file_path = r'c:\Users\Karin\Desktop\ebook.html'
output_path = r'c:\Users\Karin\Desktop\ebookfinal.html'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace the messy print block entirely.
style_pattern = re.compile(r'(<style>)(.*?)(</style>)', re.DOTALL)
styles = style_pattern.findall(content)

if styles:
    first_style_content = styles[0][1]
    
    # We strip out any @media print blocks to start fresh
    clean_style = re.sub(r'@media print\s*\{.*?\}\s*\}', '', first_style_content, flags=re.DOTALL)
    clean_style = re.sub(r'@media print\s*\{[^\}]+\}', '', clean_style, flags=re.DOTALL)
    # Strip any dangling brackets/classes left behind from the bad regex earlier
    clean_style = re.sub(r'\s*\.float\s*\{\s*animation:\s*none;\s*\}\s*section\s*\{\s*page-break-inside:\s*avoid;\s*break-inside:\s*avoid;\s*\}\s*\.glass\s*\{\s*background:\s*rgba\([^)]+\);\s*border:\s*1px\s*solid\s*rgba\([^)]+\);\s*\}\s*\}', '', clean_style, flags=re.DOTALL)
    
    new_print_css = r'''
    @page { size: A4; margin: 0; }
    @media print {
      * { -webkit-print-color-adjust: exact !important; print-color-adjust: exact !important; color-adjust: exact !important; }
      html, body { 
          background-color: #faf5f0 !important; 
          margin: 0 !important; 
          padding: 0 !important; 
          width: 100% !important; 
      }
      .slide-in { animation: none !important; opacity: 1 !important; transform: none !important; }
      .float { animation: none !important; transform: none !important; }
      
      section, #cover { 
          page-break-inside: avoid !important; 
          break-inside: avoid !important; 
          page-break-after: always !important; 
          padding: 20mm !important; 
          margin: 0 !important; 
          border: none !important; 
          box-sizing: border-box !important; 
          background-color: #faf5f0 !important;
          min-height: 100vh !important;
      }
      
      #cover { 
          display: flex !important; 
          flex-direction: column !important; 
          justify-content: center !important; 
      }
      
      .glass, .glass-pink { 
          background: rgba(236, 72, 153, 0.04) !important; 
          border: 1px solid rgba(236, 72, 153, 0.1) !important; 
          box-shadow: none !important; 
      }
      
      div[style*="background: linear-gradient"] { 
          -webkit-print-color-adjust: exact !important; 
          print-color-adjust: exact !important; 
      }
    }
'''
    new_style_content = clean_style + new_print_css
    content = content.replace(first_style_content, new_style_content)

# Add Karin Padilla
# Look for the subtitle to insert the author
author_html = r'''<p id="subtitle" class="text-lg font-light text-[#6b5563] italic" style="font-family:'DM Sans',sans-serif;">De la Teoría a la Acción</p>
     <p class="text-xl font-bold mt-4 relative z-10" style="color: #be185d;">Por Karin Padilla</p>'''

content = content.replace(r'''<p id="subtitle" class="text-lg font-light text-[#6b5563] italic" style="font-family:'DM Sans',sans-serif;">De la Teoría a la Acción</p>''', author_html)

# Also ensure any lingering text-white from gradient clips is replaced
content = content.replace('text-white', 'text-[#8b3a62]')

with open(output_path, 'w', encoding='utf-8') as f:
    f.write(content)

print('ebookfinal.html created successfully.')
