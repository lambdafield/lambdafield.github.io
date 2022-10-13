#!/bin/bash
import sys
import glob

import markdown
from jinja2 import Environment, FileSystemLoader



environment = Environment(loader=FileSystemLoader('./template'))
template = environment.get_template('base.html')

pages_dict = {}

def get_newkey():
    raw_files = glob.glob('*.txt')
    print(len(raw_files)+1)

def read_pages():
    raw_files = glob.glob('*.txt')
    total = len(raw_files)

    for i, filename in enumerate(raw_files):
        title = convert_page(filename)
        pages_dict[filename] = title
        print_progress_bar(i, total)
        break

def convert_page(filename):
    with open(filename) as rf:
        txt = rf.readlines()

        title = txt[0].strip()
        title_html = '<h1>' + title + '</h1>'
        d = '<span class="created-date">' + txt[1].strip() + '</span>'
        
        # category = '<span class="category">' + txt[2].split(',') + '</span>'
        # tags = '<span class="tags">' + txt[3].split(',') + '</span>'
        
        category = '<span class="category">' + txt[2] + '</span>'
        tags = '<span class="tags">' + txt[3] + '</span>'
        

        content = '\n'.join(txt[4:])
        content_html = markdown.markdown(content)

        content = template.render(
            title=title_html,
            d=d,
            category=category,
            content_html=content_html,
            tags=tags,
        )

        # with open('./temp/'+title+'.html', mode='w', encoding='utf-8') as wf:
        with open('./temp/'+filename.split('.')[0]+'.html', mode='w', encoding='utf-8') as wf:
            wf.write(content)
            # print(f'... wrote {filename}')

        return title

def print_progress_bar(iteration, total, prefix='', suffix='', decimals=1, length=20, fill='='):
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        length      - Optional  : character length of bar (Int)
        fill        - Optional  : bar fill character (Str)
    """
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filled_length = int(length * iteration // total)
    bar = fill * filled_length + '-' * (length - filled_length)
    sys.stderr.write('\r%s |%s| %s%% %s' % (prefix, bar, percent, suffix))
    # Print New Line on Complete
    if iteration == total: 
        sys.stderr.write('\n') 


if __name__ == '__main__':
    # get_newkey()
    read_pages()