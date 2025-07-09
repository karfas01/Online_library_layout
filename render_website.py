import json
from livereload import Server
from more_itertools import chunked
from jinja2 import Environment, FileSystemLoader


def on_reload():
    with open('meta_data.json', encoding='utf-8') as f:
        books = json.load(f)
    
    chunked_books = list(chunked(books, 2))
    env = Environment(
        loader=FileSystemLoader('.'),
        autoescape=True
    )
    template = env.get_template('template.html')
    rendered_page = template.render(  
        chunked_books=chunked_books
    )
    
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(rendered_page)


def main():
    on_reload()
    server = Server()
    server.watch("template.html", on_reload)
    server.serve(root='.', open_url=True)


if __name__ == "__main__":
    main()