function solution(list){
		let result = '';
		let l = list.length;
		for(var i=0; i<l; i++){
			if(list[i] == list[i+2]-2) {
				result += list[i] + '-';
				for(i; i<l; i++){
					if(list[i] != list[i+2]-2) break;
				}
			} else {
				result += list[i];
				if(i != l-1) result += ',';
			}
		}
		return result;
	}
console.log(solution([-6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 17, 18, 19, 20]))    