from re import sub, compile, match, search
from itertools import count

strong = compile('(__)([^_]*)(__)')
em = compile('(_)([^_]*)(_)')
h6 = compile('^(###### )(.+)')
h2 = compile('^(## )(.+)')
h1 = compile('^(# )(.+)')
ul = compile('^(\* )(.+)')
p = compile('^(.+)')

def parse_markdown(markdown):
    lines = markdown.split('\n')
    ul_mark = True
    new_lines = ""
    index_iterator = count(0)
    for l in lines:
        index = next(index_iterator)
        new_line = l
        if search(strong, new_line):
            new_line = sub(strong, r'<strong>\2</strong>', new_line)
        if search(em, new_line):
            new_line = sub(em, r'<em>\2</em>', new_line)
        if match(h1, new_line):
            new_line = sub(h1, r'<h1>\2</h1>', new_line)
        elif match(h2, new_line):
            new_line = sub(h2, r'<h2>\2</h2>', new_line)
        elif match(h6, new_line):
            new_line = sub(h6, r'<h6>\2</h6>', new_line)
        elif match(ul, new_line):
            if ul_mark:
                ul_mark = False
                new_line = sub(ul, r'<ul><li>\2</li>', new_line)
            try:
                if match(ul, (lines[index - 1])) and match(ul,lines[index + 1]):
                    new_line = sub(ul, r'<li>\2</li>', new_line)
            except IndexError as e:
                print(f'{e}, reach the last <li> tag')
                ul_mark = True
                new_line = sub(ul, r'<li>\2</li></ul>', new_line)
        elif match(p, new_line):
            new_line = sub(p, r'<p>\1</p>', new_line)
        new_lines += new_line
    return new_lines


