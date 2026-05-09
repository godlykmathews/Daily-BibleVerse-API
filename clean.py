import csv
import re

def process_bible_text(input_file, output_file):
    # ഫയലിലെ പൂർണ്ണ രൂപത്തിലുള്ള ടെക്സ്റ്റ് വായിക്കുന്നു
    with open(input_file, 'r', encoding='utf-8') as f:
        raw_text = f.read()

    # പുസ്തകത്തിന്റെ പേരും അധ്യായം:വാക്യം നമ്പറുകളും കണ്ടെത്താനുള്ള റെഗുലർ എക്സ്പ്രഷൻ പാറ്റേൺ
    pattern = re.compile(r'((?:\d\s+)?[^\s0-9\.\,]+?\d*\s+\d+:\d+(?:(?:,\s*|-)\d+)*)')
    
    matches = list(pattern.finditer(raw_text))
    data = []
    last_idx = 0
    
    # ഓരോ വാക്യവും റഫറൻസും വേർതിരിക്കുന്നു
    for match in matches:
        ref = match.group(1).strip()
        start, end = match.span()
        
        verse = raw_text[last_idx:start].strip()
        if verse:
            data.append([verse, ref])
        
        last_idx = end

    # പുതിയ CSV ഫയലിലേക്ക് എഴുതുന്നു
    with open(output_file, 'w', newline='', encoding='utf-8-sig') as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        writer.writerow(['verse', 'reference']) # കോളം ഹെഡിംഗുകൾ
        writer.writerows(data)
        
    print("CSV ഫയൽ വിജയകരമായി നിർമ്മിച്ചു!")

# നിങ്ങളുടെ ഫയലുകളുടെ പേരുകൾ ഇവിടെ നൽകുക
process_bible_text('input.txt', 'perfect_output.csv')