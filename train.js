// F-TASK:

// Yagona string argumentga ega findDoublers nomli function tuzing
// Agar stringda bittadan ortiq bir xil harflar ishtirok etgan bo'lsa
// true yokida false natija qaytarsin.

// MASALAN: findDoublers("hello"); natija true qaytadi. Sababi ikki marotaba takrorlangan 'll' harfi mavjud!

function findDoublers(str) {
	for (let i = 0; i < str.length; i++) {
		for (let j = i + 1; j < str.length; j++) {
			if (str[i] === str[j]) {
				return true
			}
		}
	}
	return false
}

const result = findDoublers('hello')
console.log(result)

// E-TASK:

// Shunday function tuzing, u bitta string argumentni qabul qilib osha stringni teskari qilib return qilsin.
// MASALAN: getReverse("hello") return qilsin "olleh"

// function getReverse(a) {
// 	const b = a.split('').reverse().join('')
// 	// console.log(b)
// 	return b
// }

// const result = getReverse('hello')
// console.log(result)
