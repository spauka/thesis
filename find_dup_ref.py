import re
import os

bib = re.compile(r".*\.bib$")
expr = re.compile(r"""title\s*=\s*({)?(["'])?(.+)(?(1)}|\2)""", re.I)
doi = re.compile(r"""doi\s*=\s*({)?(["'])?(.+)(?(1)}|\2)""", re.I)

titles = []
dois = []

for f in os.listdir():
    if bib.match(f):
        with open(f, "r") as bibfile:
            for line in bibfile:
                title = expr.findall(line)
                if title:
                    print(title[0])
                    title = title[0][2].lower()
                    title = title.translate(str.maketrans("", "", '(){}.:/\\$_-'))
                    titles.append(title)
                ndoi = doi.findall(line)
                if ndoi:
                    print(ndoi[0])
                    ndoi = ndoi[0][2].lower()
                    ndoi = ndoi.translate(str.maketrans("", "", '(){}.:/\\$_-'))
                    dois.append(ndoi)

stitles = set(titles)
sdois = set(dois)
print(f"Total defined: {len(titles)}, unique: {len(stitles)}")
print(f"Total dois: {len(dois)}, unique: {len(dois)}")
if len(stitles) != len(titles):
    print("Duplicated titles:")

    titles.sort()
    for i in range(len(titles)-1):
        if titles[i] == titles[i+1]:
            print(f"\t{titles[i]}")
else:
    print("No duplicated titles")
