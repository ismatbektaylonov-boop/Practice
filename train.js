// TASK L:

// Shunday function yozing, u string qabul qilsin va string ichidagi hamma sozlarni chappasiga yozib va sozlar ketma-ketligini buzmasdan stringni qaytarsin.
// MASALAN: reverseSentence("we like coding!") return "ew ekil gnidoc";

function reverseSentence(str) {
	const words = str.split(' ')
	let newSentence = ''

	for (let word of words) {
		let reversedWord = word.split('').reverse().join('')
		// Boshlanishida bo'sh joy qo'shilmasligi uchun:
		newSentence = newSentence ? newSentence + ' ' + reversedWord : reversedWord
	}

	return newSentence
}

const result = reverseSentence('we like coding')
console.log(result) // "ew ekil gnidoc"

// TASK K:

// Shunday function yozing, u string qabul qilsin va string ichidagi unli harflar sonini qaytarsin.
// MASALAN: countVowels("string") return 1;

// function countVowels(str) {
//     let lowStr = str.toLowerCase()
//     let count = 0;
//     for(let char of lowStr) {
//         if(char === "a" || char === "o" || char === "e" || char === "i" || char === "u" || char === "y") {
//             count++
//         }
//     }
//     return count
// }
// const result = countVowels("agentic")
// console.log(result)

// function countVowels(str) {
// 	count = ''
// 	vowels = 'aeiouAEIOU'
// 	for (let i = 0; i < str.length; i++) {
// 		if (vowels.includes(str[i])) {
// 			count++
// 		}
// 	}
// 	return count
// }
// console.log(countVowels('agentic'))
// TASK G:

// Yagona parametrga ega function tuzing.
// Va bu function parametr orqalik integer ma'lumot turlariga ega bo'lgan bir arrayni qabul qilsin.
// Ushbu function bizga arrayning tarkibidagi birinchi eng katta qiymatning indeksini qaytarsin.

// MASALAN: getHighestIndex([5, 21, 12, 21 ,8]); return qiladi 1 sonini
// Yuqoridagi misolda, birinchi indeksda 21 joylashgan.
// Va bu 21 soni arrayning tarkibidagi birinchi eng katta son hisobladi va bizga uning indeksi 1 qaytadi.

// function getHighestIndex(arr) {
//     const maxNumber = Math.max(...arr);
//     return arr.indexOf(maxNumber);
// }

// function getHighestIndex(a) {
// 	let highestIndex = 0
// 	for (i = 0; i < a.length; i++) {
// 		if (a[i] > a[highestIndex]) {
// 			highestIndex = i
// 		}
// 	}
// 	return highestIndex
// }

// console.log(getHighestIndex([5, 21, 12, 212, 8]))

// F-TASK:

// Yagona string argumentga ega findDoublers nomli function tuzing
// Agar stringda bittadan ortiq bir xil harflar ishtirok etgan bo'lsa
// true yokida false natija qaytarsin.

// MASALAN: findDoublers("hello"); natija true qaytadi. Sababi ikki marotaba takrorlangan 'll' harfi mavjud!

// function findDoublers(str) {
// 	for (let i = 0; i < str.length; i++) {
// 		for (let j = i + 1; j < str.length; j++) {
// 			if (str[i] === str[j]) {
// 				return true
// 			}
// 		}
// 	}
// 	return false
// }

// const result = findDoublers('hello')
// console.log(result)

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
