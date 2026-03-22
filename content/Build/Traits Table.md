```dataviewjs
const page = dv.page("Build/Traits");
const content = await dv.io.load(page.file.path);
// dv.paragraph(content)

const pattern = /\*\*(.*?)\*\*/g;      // Regex to capture bolded text
const traitsSet = new Set();
let match;

while ((match = pattern.exec(content)) !== null) {
  // match[1] is the text between the double asterisks
  traitsSet.add(match[1].trim());
}

// Convert set to array to do anything you like with it
const traits = [...traitsSet];

const {Tables} = await cJS()
dv.paragraph(Tables.printTable(traits))
```
