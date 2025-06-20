from html2image import Html2Image
from jinja2 import Environment, FileSystemLoader
import os

env = Environment(loader=FileSystemLoader('render/templates'))

def render_slides(slides, output_dir):
    os.makedirs(output_dir, exist_ok=True)
    hti = Html2Image(output_path=output_dir, size=(1080, 1080))
    template = env.get_template('base.html')

    for i, slide in enumerate(slides, start=1):
        html = template.render(title=slide['title'], content=slide['content'], index=i)
        hti.screenshot(html_str=html, save_as=f"slide_{i}.png")
