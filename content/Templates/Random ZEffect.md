<%*
const folder = "Magic/Effects"; // change this

const mdFiles = app.vault.getFiles()
  .filter(f => f.path.startsWith(folder + "/") && f.path.endsWith(".md"));

const randomFile = mdFiles[Math.floor(Math.random() * mdFiles.length)];

// remove .md
const cleanPath = randomFile.path.replace(/\.md$/, "");
const fileName = randomFile.basename;

tR += `[[${cleanPath}|${fileName}]]`;
%>