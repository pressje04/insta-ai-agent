from html2image import Html2Image
import os

def render_slides(slides, output_dir):
    os.makedirs(output_dir, exist_ok=True)
    hti = Html2Image(output_path=output_dir)

    for i, slide in enumerate(slides):
        html = f"""
        <html>
        <body style="font-family:sans-serif;padding:40px;">
            <h1>{slide['title']}</h1>
            <p>{slide['content']}</p>
        </body>
        </html>
        """
        hti.screenshot(html_str=html, save_as=f"slide_{i+1}.png")