// in vault at scripts/coolString.js
class Tables {

	printTable(data) {
		let target = data.length
		let dice = [4,6,8,10,12,20]
		let output = ""
		
		if (data.length <= 20) {
			let bestDie = 0
			for (const die of dice) {
				if (die > target) {
					bestDie = 4
					break
				}
			}

			output += `d${bestDie}\n`
			for (let i = 0; i < bestDie; i++) {
				let addition = data[i] == undefined ? "Roll again" : data[i]
				output += `- ${i+1}. ${addition}\n`
			}

		} else {
			let bestPair = [0,0]
			let bestDistance = Infinity
			
			for (const die1 of dice) {
				for (const die2 of dice) {
					let size = die1 * die2 
					if (size >= target && size - target < bestDistance) {
						bestPair = [die1, die2]
						bestDistance = size - target
					}
				}
			}
			
			let d1 = bestPair[0]
			let d2 = bestPair[1]
			// if (quickRoll) {
				// output += "Quick Random Roll: **" + data[Math.floor(Math.random()*data.length)] + "**\n"
				// output += "Refresh page for another automatic random roll\n"
			// }

			output += `d${d1}, d${d2}\n`
			
			for (let i = 0; i < d1; i++) {
				for (let j = 0; j < d2; j++) {
					let addition = data[i*d2+j] == undefined ? "Roll again" : data[i*d2+j]
					output += `- ${i+1}-${j+1}. ${addition}\n`
				}
			}
		}


		return output
	}
}

// dataviewjs block in *.md
// ```dataviewjs
// const {CoolString} = await cJS()
// dv.list(dv.pages().file.name.map(n => CoolString.coolify(n)))
// ```

