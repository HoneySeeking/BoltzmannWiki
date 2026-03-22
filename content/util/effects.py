## commpiles the effect files into a single
## rollable file because dataview doesn't
## work when exported

import os

text = ""
for i, effect in enumerate(sorted(os.listdir("../Effects"))):
    print(effect)
    # text += f"{i+1}. [[Boltzmann/TTRPG/Effects/{effect[:-3]}|{effect[:-3]}]]\n"
    text += f"{i+1}. [[Effects/{effect[:-3]}|{effect[:-3]}]]\n"

# print(text)
with open("../Effects.md", "w") as file:
    file.write(text)

