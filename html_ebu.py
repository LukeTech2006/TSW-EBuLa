import csv, queue, sys, time, easygui
from tabulate import tabulate
from render_html import render_in_browser as ren

#fahrplandatei auswählen
path = easygui.fileopenbox(title='Fahrplan auswählen',default='./*.csv')

#fahrplandatei einlesen
fpl_roh = [row for row in csv.DictReader(open(path,mode='r',encoding='UTF-8'))]
tbl_html = tabulate(fpl_roh, headers='keys', tablefmt='html')

for char in ['¥', '&lt;', '&gt;']:
    replacers = {
        '¥': '&yen;',
        '&lt;': '<',
        '&gt;': '>'
    }
    tbl_html = tbl_html.replace(char, replacers[char])

style = r"""
<style>
table {width: 100%; font-family: sans-serif}
td, th {outline: 0.5px solid black;}
</style>
"""

ren(style + tbl_html)