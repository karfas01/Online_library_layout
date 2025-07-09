import json
from jinja2 import Environment, FileSystemLoader

def main():
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

if __name__ == "__main__":
    main()