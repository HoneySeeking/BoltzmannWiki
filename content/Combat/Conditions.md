
```dataviewjs
for (let file of dv.pages('"Conditions"')) {
    dv.paragraph(`![[${file.file.name}]]`);
}
```
