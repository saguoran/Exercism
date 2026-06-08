from re import sub, compile, match, search
from itertools import count

strong = compile('(__)([^_]*)(__)')
em = compile('(_)([^_]*)(_)')
h = compile('^(#{1,6}) (.+)')
ul = compile('^(\* )(.+)')


def sub_headers(line):
    hashes = match(h, line)
    length = len(hashes.group(1))
    return sub(h, fr'<h{length}>\2</h{length}>', line)


def parse_markdown(markdown):
    lines = markdown.split('\n')
    ul_mark = True
    new_lines = ""
    index_iterator = count(0)
    for line in lines:
        index = next(index_iterator)
        if search(strong, line):
            line = sub(strong, r'<strong>\2</strong>', line)
        if search(em, line):
            line = sub(em, r'<em>\2</em>', line)
        if match(ul, line):
            if ul_mark:
                ul_mark = False
                line = sub(ul, r'<ul><li>\2</li>', line)
            elif not ul_mark:
                try:
                    if match(ul, (lines[index - 1])) and match(ul,lines[index + 1]):
                        line = sub(ul, r'<li>\2</li>', line)
                    else:
                        line = sub(ul, r'<li>\2</li></ul>', line)
                        ul_mark = True
                except IndexError as e:
                    print(f'{e}, reach the last line')
                    line = sub(ul, r'<li>\2</li></ul>', line)
        elif match(h, line):
            line = sub_headers(line)
        else:
            line = fr'<p>{line}</p>'
        new_lines += line
    return new_lines
