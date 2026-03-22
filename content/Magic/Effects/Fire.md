---
Cost: 1
Resist: AGI
Success: Half
Period: 1 minute
---


| Cost          | Resist          | Success          | Period          | Trappings          |
| ------------- | --------------- | ---------------- | --------------- | ------------------ |
| `= this.Cost` | `= this.Resist` | `= this.Success` | `= this.Period` | `= this.Trappings` |

- Creates fire that deals 2d6 energy damage for each level, halved on successful resist
- Applies [[Burning]] on all affected for Cd4 turns, going up a size for every 2 levels, capped at Cd12, regardless of save:

| Level | Countdown |
| ----- | --------- |
| 1-2   | Cd4       |
| 3-4   | Cd6       |
| 5-6   | Cd8       |
| 7-8   | Cd10      |
| >= 9  | Cd12      |