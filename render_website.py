import os
import json
from livereload import Server
from more_itertools import chunked
from jinja2 import Environment, FileSystemLoader


def on_reload():
    os.makedirs('pages', exist_ok=True)

    with open('meta_data.json', encoding='utf-8') as f:
        books = json.load(f)

    pages_books = list(chunked(books, 15))

    env = Environment(
        loader=FileSystemLoader('.'),
        autoescape=True
    )

    template = env.get_template('template.html')

    for number, books_per_page in enumerate(pages_books, start=1):
        chunked_books = list(chunked(books_per_page, 2))
        
        rendered_page = template.render(
            chunked_books=chunked_books
        )

        output_path = f'pages/index{number}.html'
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(rendered_page)


def main():
    on_reload()
    server = Server()
    server.watch("template.html", on_reload)
    server.serve(root=".", open_url="/pages/index1.html")

if __name__ == "__main__":
    main()
