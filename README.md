# purple_template

capstone idea:
Create a character builder for the game New World that both saves and allows users to share them.

Currently there aren't any very good ways of doing this, as they either lack a way to save them, are clunky in their design or lack any sort of filtering.

New World is a game with "random" loot.  The main thing that changes is the "perks" on each item, with the highest level items having three on them.  The issue is that there are currently 900~ or so perks available, so there is a huge range in what gear can have on it.  Luckily, the perks are split up in to different pools and for the most part, can only have one perk from each of those pools, greatly reducing the amount of possible combinations, but still offering a massive amount of them.  With 10 slots of gear, there is a very wide variety of ways to gear a character.


What I would like to create:

1. A UI that offers a reletively easy way of selecting perks for each gear slot, while eliminating the other perks from the same pool if one is picked.
2. A log in that lets users save their builds and be able to revisit them again with ease.
3. Quicklinks.  Be able to generate a link to a custom build that isn't necessarily attached to any one account.
4. The homepage will have space for the most common builds and news.
5. A login page that shows an accounts saved builds and allows them to be edited and saved again.

quicklinks = having a url link that stores the build within the link.  say it reads armor slots top to bottom first, then weapons top to bottom.  Each item has unique values to show which it is.  Say each slot gets 8 characters, first one is type, then stat type, perk1, perk2, perk3.  

Storing data.
items will have slot, type (armor: light/med/heavy weapons: 14 different types), stat (type: str, dex, etc), perks.
perks will need to have their unique ID, name, pool, unique tag for quick links(a-z,A-Z,0-9.  Two char should be enough).  List of lists?  Put each pool within it's own list? [ID, name, unique tag]. Might need to first define each slot and then add what pools it can accept and which perks out of those pools it can take.

Need to define what perk pools each slot can accept.
Some pools have have perks that are certain item specific.  "Proc" pool is a hot mess of these.  Unique perks to amulet, ring, all weapons, melee weapons, ranged weapons, helmet, shield, chest, gloves, pants.  Give each item slot a value 1-11 and include a list of available slots?  Skill perks also have different values for armor/weapons.

pools:

2hAxe

2hHammer
Accuracy (not as important) bow/musket/hatchet/blunder
ArmorHealth armor
Blocking 
Blunderbuss
Bow
BuffDur amulet
CDR
Consume earring
ConsumeAdd
ConsumeCDR
CritDef
CritHeadshot
Critical
DebuffDur
Defense amulet/shield
DmgAbsorb armor/shield
DmgCategory weapon
DmgCon melee,ranged,ring
DmgType ring
Elemental weapons/armor (chain/shirking/conditioning)
FireStaff
GreatSword
Hatchet
Healing amulet/ring
Health amulet
IceGauntlet
LifeStaff
Musket
OnKill
Proc 
Rapier
Regen earring
Shield
Skill
Spear
Stam ring
Sword
Threat
VoidGauntlet


idea for laying out perks (unique value, name, discription, unique tag):
DmgCon = [[1, "Vicious", "+12% critical damage.", "aa"], [2, "enchanted", "light and heavy attacks deal 9.8% more damage.", "ab"], [3, "rogue", "+19% more backstab damage.", "ac"] ... ]

