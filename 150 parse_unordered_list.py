import re

def parse_unordered_list(markdown):
    markdown = markdown.replace("\n", "")
    markdown = re.sub(r'-( )+', '</li><li>', markdown)
    markdown = markdown.replace("</li>", "<ul>", 1)
    markdown = markdown + '</li></ul>'
    return markdown

print(parse_unordered_list("- Item A\n- Item B"))
print(parse_unordered_list("-  JavaScript\n-  Python"))
print(parse_unordered_list("- 2 C Flour\n- 1/2 C Sugar\n- 1 Tsp Vanilla"))
print(parse_unordered_list("- A-1\n- A-2\n- B-1"))
