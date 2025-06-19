"""
Main that handles most of the actual generation 
+ automation of content, delegating to other files
"""
from gpt.generate_carousel import generate_slides
from render.renderer import render_slides
from utils.sanitize_filename import safe_name

with open('problems/problems.txt') as f:
    problems = f.read().splitlines()

for prob in problems:
    print(f"Generating for: {prob}")
    slides = generate_slides(prob)
    dirname = f"output/{safe_name(prob)}"
    render_slides(slides, dirname)
