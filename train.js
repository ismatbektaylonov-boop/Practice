// E-TASK:

// Shunday function tuzing, u bitta string argumentni qabul qilib osha stringni teskari qilib return qilsin.
// MASALAN: getReverse("hello") return qilsin "olleh"

function getReverse(a) {
	const b = a.split('').reverse().join('')
	// console.log(b)
	return b
}

const result = getReverse('hello')
console.log(result)
