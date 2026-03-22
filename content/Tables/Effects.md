
```dataviewjs
const pages = dv.pages('"Magic/Effects"');
let effects = []
pages.forEach((p, i) => {
	effects.push(p.file.link)
})

const {Tables} = await cJS()
dv.paragraph(Tables.printTable(effects))
```