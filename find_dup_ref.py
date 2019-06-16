import re
import os

bib = re.compile(r".*\.bib$")
expr = re.compile(r"title\s*=\s*[{\"']([^\"'}]+)[\"'}]", re.I)

titles = []

for f in os.listdir():
    if bib.match(f):
        with open(f, "r") as bibfile:
            for line in bibfile:
                title = expr.findall(line)
                if title:
                    print(f, title)
                    titles.append(title[0].lower())

stitles = set(titles)
print(f"Total defined: {len(titles)}, unique: {len(stitles)}")
print("Duplicated titles:")

titles.sort()
for i in range(len(titles)-1):
    if titles[i] == titles[i+1]:
        print(f"\t{titles[i]}")