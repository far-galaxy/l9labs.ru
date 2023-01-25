const queryString = window.location.search;
const urlParams = new URLSearchParams(queryString);
const page = urlParams.get('page');

window.onload = fetch(`stuff/videos/${page}.json`)
	.then(response => response.json())
	.then(json => {
		json['page'].map((chapter) => buildChapter(chapter))
	});

const buildChapter = (chapter) => {
	const e = document.createElement('div');
	const h = document.createElement('h1');
	h.innerHTML = chapter.head;

	chapter.videos.map((video) => {
		const vid = document.createElement('iframe');
		vid.setAttribute("src", `https://www.youtube.com/embed/${video}`);
		vid.setAttribute("allow", "accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture");
		vid.setAttribute("allowfullscreen", true);
		e.appendChild(vid);
	})
	document.body.appendChild(h);
	document.body.appendChild(e);
}
