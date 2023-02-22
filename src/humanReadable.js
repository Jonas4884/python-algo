function formatDuration (seconds) {
  
	let str = '';

	let years = Math.floor(seconds / 31536000);
	let days = Math.floor((seconds - years * 31536000) / 86400);
	let hour = Math.floor(((seconds - years * 31536000) - days * 86400) / 3600);
	let min = Math.floor((((seconds - years * 31536000) - days * 86400) - hour * 3600) / 60);
	let sec = (((seconds - years * 31536000) - days * 86400) - hour * 3600) - min * 60;

	if (years == 0) years = '';
	if (days == 0) days = '';
	if (hour == 0) hour = '';
	if (min == 0) min = '';
	if (sec == 0) sec = '';

	if (years == 1) years = years + ' year';
	if (days == 1) days = days + ' day';
	if (hour == 1) hour = hour + ' hour';
	if (min == 1) min = min + ' minute';
	if (sec == 1) sec = sec + ' second';

	if (years > 1) years = years + ' years';
	if (days > 1) days = days + ' days';
	if (hour > 1) hour = hour + ' hours';
	if (min > 1) min = min + ' minutes';
	if (sec > 1) sec = sec + ' seconds';

	str = `${years}, ${days}, ${hour}, ${min}, ${sec}`

	let res = str.match(/\d+\s\w+/g);

	if (seconds == 0) return('now');
	else if (res.length == 1) return(res.join(' '));
	else {
		res[res.length - 1] = `and ${res[res.length - 1]}`;
		for (let i = 0; i < res.length - 2; i++) {
			res[i] = `${res[i]},`;
		}
		return(res.join(' '));
	}
}

console.log(formatDuration(8))
