import os
import subprocess

target_folder = "/home/me/philnik.github.io/"

source_file = "/home/me/org/equations.html"
source_file = "/home/me/org/FEM.html"

str_make_index = """tree -H '.' -L 1 --noreport --dirsfirst -T './*html' -s -D --charset utf-8 -I "index.html" -o index.html"""


def send_html_file(source_file):
    add_file = f"""
    cp {source_file} {target_folder}
    cd {target_folder}
    git add *.html
    chmod 777 *.html
    {str_make_index}
    git commit -am "add FEM.html"
    git push
    """
    os.system(add_file)

send_html_file(source_file)
