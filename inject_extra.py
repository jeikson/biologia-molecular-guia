#!/usr/bin/env python3
"""Inject extra content from text files into Biologia Molecular guide."""

import re, os

HTML_PATH = "/home/jeikson/.openclaw/workspace/Biologia_Molecular_Guia_Estudio.html"
TEXT_DIR = "/home/jeikson/.openclaw/workspace/bio-molecular-temp"

def esc(t):
    return str(t).replace("&","&amp;").replace("<","&lt;").replace(">","&gt;").replace('"',"&quot;").replace("'","&#39;")

def extract_intro_and_sections(text):
    """Extract intro and numbered sections from text content."""
    # Clean text
    text = re.sub(r"[^\S\n]{3,}", " ", text)
    text = re.sub(r"\n{2,}", "\n\n", text)
    
    # Extract intro
    intro = ""
    m = re.search(r"(?:Introducción|Introducci[óo]n)(.*?)(?=\n\s*(?:\d+\.\d+|Al finalizar|$))", text, re.DOTALL)
    if m:
        intro = " ".join(m.group(1).strip().split()[:150])
    
    # Extract sections
    sections = []
    pattern = r"(\d+\.\d+(?:\.\d+)?)\.?\s*\n\s*([A-ZÁÉÍÓÚÑ][A-Za-zÁÉÍÓÚÑáéíóúñ\s,;:()]+?)(?=\n)"
    matches = list(re.finditer(pattern, text))
    for i, m in enumerate(matches):
        num, title = m.group(1), m.group(2).strip()
        start, end = m.end(), matches[i+1].start() if i+1 < len(matches) else len(text)
        content = text[start:end].strip()
        content = re.sub(r"[^\S\n]{3,}", " ", content)[:1200]
        if len(title) > 5 and len(content) > 50:
            sections.append((num, title, content))
    return intro, sections[:6]

def main():
    with open(HTML_PATH, "r", encoding="utf-8") as f:
        html = f.read()
    
    unit_files = {
        "U1": ["u1_main.txt", "u1_main_v2.txt", "u1_main2.txt"],
        "U2": ["u2_main.txt", "u2_main2.txt"],
        "U3": ["u3_main.txt", "u3_main2.txt"],
        "U4": ["u4_main.txt", "u4_main2.txt"],
        "U5": ["u5_main.txt", "u5_main2.txt"],
        "U6": ["u6_main.txt", "u6_main2.txt"],
        "U7": ["u7_main.txt", "u7_main2.txt"],
    }

    injection_count = 0
    for unit_code, fnames in unit_files.items():
        # Read first available file
        content_text = ""
        for fn in fnames:
            fp = os.path.join(TEXT_DIR, fn)
            if os.path.exists(fp):
                content_text = open(fp, "r", encoding="utf-8", errors="replace").read()
                break
        
        if not content_text:
            continue
        
        intro, sections = extract_intro_and_sections(content_text)
        if not intro and not sections:
            continue
        
        # Build extra HTML content
        extra_html = '\n<div class="secc" style="border-left:3px solid var(--b)">'
        extra_html += '<div class="sech" onclick="tsec(this)"><span class="arrow">▶</span><span class="num">📖</span>Ampliación de contenido</div><div class="secb">'
        
        if intro:
            extra_html += f'<div class="stitle purple">📖 Introducción</div><div class="cbody"><p>{esc(intro)}</p></div>'
        
        for snum, stitle, scontent in sections[:4]:
            sp = scontent.replace("\n\n", "</p><p>").replace("\n", " ")
            extra_html += f'<div class="secc" style="border-left:3px solid var(--b)"><div class="sech" onclick="tsec(this)"><span class="arrow">▶</span><span class="num">{esc(snum)}</span>{esc(stitle[:60])}</div><div class="secb"><div class="cbody"><p>{esc(sp)}</p></div></div></div>'
        
        extra_html += '</div></div>\n'
        
        # Inject after the progress bar section for this unit
        # Pattern: find </div></div> followed by next unit or </div>
        pattern = f'(<div class="nava">.*?</div></div></div>)(\\s*<div class="unit" id="u[{"".join(str(i+1) for i in range(7))}]")'
        
        # Simpler approach: inject after each unit's closing div before next unit
        # Find the progress div closing
        search = f'{unit_code}/7</span>'
        idx = html.find(search)
        if idx == -1:
            continue
        
        # Find the end of this unit (</div></div> after progress bar)
        end_search = html.find('</div></div>', idx)
        if end_search == -1:
            continue
        
        end_of_unit = end_search + len('</div></div>')
        
        # Check if we already injected for this unit
        next_chunk = html[end_of_unit:end_of_unit+200]
        if 'Ampliación de contenido' in next_chunk:
            print(f"  {unit_code}: already has ampliación, skipping")
            continue
        
        html = html[:end_of_unit] + extra_html + html[end_of_unit:]
        injection_count += 1
        print(f"  {unit_code}: injected {len(intro.split())} words intro + {min(len(sections),4)} sections")
    
    with open(HTML_PATH, "w", encoding="utf-8") as f:
        f.write(html)
    
    print(f"\n✅ Done! Injected extra content for {injection_count} units in {HTML_PATH}")

if __name__ == "__main__":
    main()
