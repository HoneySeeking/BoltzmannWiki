---
Cost: 2
Resist: PRE
Success: Negates
Period: 1 minute
Trappings:
  - Plants
  - Rocks
  - Air
  - Water
  - Wind
---

| Cost          | Resist          | Success          | Period          | Trappings          |
| ------------- | --------------- | ---------------- | --------------- | ------------------ |
| `= this.Cost` | `= this.Resist` | `= this.Success` | `= this.Period` | `= this.Trappings` |

```dataviewjs
const {Tables} = await cJS()
dv.paragraph(Tables.printTable(dv.current().Trappings))
```

- Affected items of trappings turn into arms of yours that can be used in place of your arm for attacks, grapples, etc
- **AoE**: all the trappings in the area are animated to serve as your limbs, allowing one action for attacks and grapples against any enemy in the area every turn
- **Target**: the specific item of trapping acts as your limb and more than one action can be taken through the plant