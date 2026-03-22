<%* 
// https://www.reddit.com/r/d100/comments/i1853a/d100_memorable_npc_behaviors/
const names = [
  "Sitting", "Axe", "Running", "Claw", "Whispering", "Arrow", "Hidden", "Stone",
  "Burning", "Root", "Fallen", "Branch", "Broken", "Flame", "Dancing", "Smoke",
  "Howling", "Ash", "Wandering", "Storm", "Cracked", "Moon", "Purple", "Sun",
  "Silent", "Fang", "Frozen", "Thorn", "Roaring", "Bone", "Flickering", "Mask",
  "Gnawed", "Foot", "Darkened", "Hand", "Coiled", "Eye", "Shivering", "Ear",
  "Drifting", "Song", "Tangled", "Drum", "Crimson", "Trail", "Quiet", "Path",
  "Leaping", "Knife", "Crooked", "Flint", "Whistling", "Fur", "Yellow", "Howl",
  "Eternal", "Roar", "Bleeding", "Wind", "Crushing", "Bark", "Emerald", "Leaf",
  "Wounded", "Bloom", "Ashen", "Moss", "Glorious", "Morning", "Jagged", "Evening",
  "Glistening", "Echo", "Feral", "Cave", "Thunderous", "Twilight", "Valley",
  "Nostalgia", "Disastrous", "Stream", "Scarred", "River", "Hollow", "Pond",
  "Snarling", "Fog", "Bristling", "Mist", "Drowsy", "Web", "Grinning", "Thread",
  "Shattered", "Feather", "Mossy", "Wing", "Rugged", "Talon", "Shadowed", "Snout",
  "Stalking", "Scent", "Pale", "Track", "Flicked", "Spore", "Blooming", "Flesh",
  "Withered", "Scar", "Gnarled", "Shell", "Cursed", "Antler", "Ancient", "Horn",
  "Piercing", "Scale", "Echoing", "Voice", "Nostaligc", "Infinity", "Profound",
  "Groan", "Feathered", "Snarl", "Glowing", "Gaze", "Captivating", "Weeping",
  "Throat", "Hunched", "Scream", "Painted", "Shade", "Numb", "Husk", "Greedy",
  "Wrath", "Scraped", "Grin", "Wilted", "Bite", "Crushed", "Dusking", "Chirp",
  "Thundering", "Nest", "Matted", "Carved", "Dust", "Sunken", "Cinder", "Moonlit",
  "Mark", "Pecked", "Marking", "Glare", "Quivering", "Hiss", "Wheezing",
  "Whisker", "Crawling", "Paw", "Step", "Frostbitten", "Glint", "Grumbling",
  "Flake", "Drumming", "Burrow", "Gnashing", "Wisp", "Torn", "Trunk", "Soaked",
  "Spike", "Murmuring", "Tusk", "Smudged", "Knuckle", "Stained", "Drip",
  "Rattling", "Ridge", "Moldy", "Hide", "Soaring", "Scratch", "Humming", "Pelt",
  "Trembling", "Gloom", "Lake", "Winter", "Summer", "Spring", "Fall", "Return", "Twice", "Twin", "Once", "Thrice", "Hundred", "Thousand", "Son", "Before", "Upon"
];

const gender = ["M", "F"];

const traits = [
  "Grim", "Proper", "Chatty", "Childminded", "Sadistic", "Stoic", "Drunkard",
  "Nervous", "Proud", "Absentminded", "Bitter", "Forgetful", "Sly",
  "Sleepy", "Depressed", "Kind", "Arrogant", "Hopeful", "Blunt",
  "Brooding", "Greedy", "Cheery", "Impulsive", "Judgy", "Warm",
  "Paranoid", "Helpful", "Dour", "Fidgety", "Softspoken", "Suspicious",
  "Anxious", "Loyal", "Brusque", "Dreamy", "Irritable", "Cocky",
  "Melancholic", "Wary", "Polite", "Boastful", "Abrasive", "Curious",
  "Timid", "Guarded", "Whimsical", "Grumpy", "Smug", "Distracted",
  "Apathetic", "Awkward", "Pessimistic", "Playful", "Stern", "Shy",
  "Rigid", "Enthusiastic", "Cold", "Sarcastic", "Lonely", "Gentle",
  "Tense", "Mournful", "Earnest", "Clingy", "Rash", "Caring",
  "Spacey", "Frenzied", "Quiet", "Noble", "Skeptical", "Blustering",
  "Mellow", "Driven", "Awestruck", "Distrustful", "Meek", "Bold",
  "Polished", "Spiteful", "Jovial", "Coy", "Tired",
  "Impish", "Dutiful", "Cynical", "Shaken", "Serene", "Obsessive",
  "Aloof", "Stubborn", "Bashful", "Rude", "Optimistic", "Broke",
  "Compassionate", "Skittish", "Pompous", "Dazed", "Eccentric", "Gloomy",
  "Scatterbrained", "Snappish", "Steady", "Jittery", "Brutal", "Prim",
  "Zealous", "Flirtatious", "Withdrawn", "Vain", "Mirthful",
  "Childlike", "Hardheaded", "Disciplined", "Optimistic", "Fussy", "Erratic"
];

const characteristic = [
  "Muscular", "Lots of tattoos", "Very neat/tidy", "Clumsy", "Unusually short", "Unusually tall", "Lots of Piercings", "Fidgets", "Loves storytelling", "Smokes pipe",
  "Always reading", "Missing Finger", "Extravagant clothing", "Lots of jewellery", "Covered in dirt" , "Always sketching",
  "Loves gambling", "Attractive"
];

const habit = [
  "Talks to their tools", "Constantly scratching", "Always looking over shoulder", "Energetic and enthusiastic hand gestures", "Constantly hums old chants", "Shares food with vermin",
  "Recites stories to trees", "Smears ash on face", "Carries herbs everywhere",
  "Collects feathers", "Draws spirals in dirt", "Counts every step they take",
  "Fidgets with carved beads", "Sings to rivers", "Grinds teeth while thinking",
  "Stares into fire often", "Taps wood before speaking", "Refuses to eat wild fruit",
  "Marks territory with stones", "Laughs at odd moments", "Speaks in riddles"
];

const appearance = [
  "Scarred muzzle", "Missing ear", "Woven moss cloak", "Bone piercings",
  "Patchy fur", "Extra-long tail", "Glassy eyes", "Twisted horn",
  "Burned paw", "Dappled fur", "Branch antlers", "Mangled snout",
  "Leaf-stained fur", "Old ritual tattoos", "Crooked claws",
  "Thick whiskers", "Hollow-sounding voice", "Uneven tusks",
  "Covered in soot", "Bone necklace"
];

const oddBehavior = [
  "Greets every tree they pass", "Flinches at their own reflection",
  "Always checks behind them", "Avoids stepping on shadows",
  "Collects oddly-shaped stones", "Traces circles with a finger",
  "Whispers apologies to the wind", "Stares too long at the sky",
  "Eats facing away from others", "Sleeps sitting upright",
  "Never turns their back on water", "Mutters names of plants constantly",
  "Laughs quietly at bad news", "Spits before speaking to spirits",
  "Taps their chest twice when nervous", "Stops talking mid-sentence to listen",
  "Walks in wide arcs around stones", "Never speaks above a whisper",
  "Obsessed with cleaning their hands", "Smells everything before touching it"
];

const speech = ["High-pitched","Excited","Always whispers","Nasal","Gruff","Breathy","Stutters","Fast-talker","Tense","Thick accent","Sing-song voice","Dark tone","Aggressive","Complex vocab","Slow, deep voice","Lisp","Relaxed","Booming voice","Never tells truth","Third person"];

%>- **<% tp.user.choice(names) %> <% tp.user.choice(names) %>**. <% tp.user.choice(gender) %> <% tp.user.choice(traits) %> <% tp.user.choice(traits) %>. <% tp.user.choice(characteristic) %>. <% tp.user.choice(appearance) %>. <% tp.user.choice(habit) %>. <% tp.user.choice(oddBehavior) %>. <% tp.user.choice(speech) %>