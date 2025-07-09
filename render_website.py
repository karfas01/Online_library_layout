import json
from livereload import Server
from jinja2 import Environment, FileSystemLoader


def render_template():
    with open('meta_data.json', encoding='utf-8') as f:
        books = json.load(f)
    env = Environment(
        loader=FileSystemLoader('.'),
        autoescape=True
    )
    template = env.get_template('template.html')
    rendered_page = template.render(books=books)
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(rendered_page)

def main():
    render_template()
    server = Server()
    server.watch("template.html", render_template)
    server.serve(root='.', open_url=True)

if __name__ == "__main__":
    main()