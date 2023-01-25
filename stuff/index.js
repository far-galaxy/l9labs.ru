function createTab() {
	const tab = document.getElementById("tab")
	fetch("stuff/index.json")
	.then(response => response.json())
	.then(json => {json.subjects.map((subject) => buildSubject(subject))});
}

function buildSubject(subject) {
	const e = document.createElement('a');
	e.setAttribute("href", `stuff?page=${subject.key}`);
	e.innerHTML = `<img src="${subject.image}">${subject.name}`;
	tab.appendChild(e);
}
