import os

def generate_index(directory):
    html_files = [f for f in os.listdir(directory) if f.endswith('.html')]
    with open(os.path.join(directory, 'index.html'), 'w') as index_file:
        index_file.write('<html><head><title>Index of HTML Files</title></head><body>\n')
        index_file.write('<h1>Index of HTML Files</h1>\n')
        index_file.write('<ul>\n')
        for html_file in html_files:
            index_file.write(f'<li><a href="{html_file}">{html_file}</a></li>\n')
        index_file.write('</ul>\n')
        index_file.write('</body></html>\n')

if __name__ == "__main__":
    directory = '.'  # Change this to your directory path
    generate_index("./")
