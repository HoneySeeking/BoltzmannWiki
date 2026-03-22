module.exports = function (list) {
	const randomIndex = Math.floor(Math.random() * list.length);
	return list[randomIndex];
}
