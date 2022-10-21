#!/bin/bash
import sys
import glob
from datetime import datetime
from operator import attrgetter

import markdown
from jinja2 import Environment, FileSystemLoader


environment = Environment(loader=FileSystemLoader('./template'))
template = environment.get_template('base.html')
template2 = environment.get_template('index_base.html')


class Page:
    def __init__(self, lines, infilename):
        title = lines[0].strip()
        d = lines[1].strip()
        category = lines[2]
        tags = lines[3]
        content = '\n'.join(lines[4:])

        self.infilename = infilename
        self.create(title, d, category, tags, content)


    def create(self, title, d, category, tags, content):
        self.title = title.strip()
        self.title_html = '<h2>' + self.title + '</h2>'

        self.d = d.strip()
        self.ddate = datetime.strptime(self.d, '%m/%d/%Y, %H:%M:%S')
        self.d_post_html = '<span class="created-date">' + self.d + '</span>'
        self.d_list_html = '<span class="created-date-in-list">' + self.d + '</span>'

        self.category = category.strip()
        self.category_html = '<span class="category">' + self.category + '</span>'

        self.tags = tags.strip()
        self.tags_html = '<span class="tags">' + self.tags + '</span>'

        self.content = content.strip()
        self.content_html = markdown.markdown(content, extensions=['extra', 'smarty', 'toc'])


    def save_as_html(self, pre_page, next_page):
        content = template.render(
            title=self.title_html,
            d=self.d_post_html,
            category=self.category_html,
            content_html=self.content_html,
            tags=self.tags_html,
            idx=self.infilename,
            pre_page=pre_page,
            next_page=next_page
        )

        # with open('./temp/'+title+'.html', mode='w', encoding='utf-8') as wf:
        outfilename = self.title + '.html'

        with open('../page/'+outfilename, mode='w', encoding='utf-8') as wf:
            wf.write(content)

def get_newkey():
    raw_files = glob.glob('*.txt')
    print(len(raw_files)+1)

def read_pages():
    raw_files = glob.glob('*.txt')
    total_page_count = len(raw_files)

    # pages_dict = {}
    pages = []

    pre_page = None
    next_page = None

    for infilename in raw_files:
        p = convert_page(infilename)
        pages.append(p)
        
    pages.sort(key=attrgetter('ddate'), reverse=False)

    for i, page in enumerate(pages):

        if i > 0:
            pre_page = pages[i-1]

        if i < total_page_count-1:
            next_page = pages[i+1]

        page.save_as_html(pre_page, next_page)


    content = template2.render(
        pages=pages,
    )

    with open('../index.html', mode='w', encoding='utf-8') as wf:
        wf.write(content)

def convert_page(infilename):
    with open(infilename) as rf:
        lines = rf.readlines()
        return Page(lines, infilename)


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