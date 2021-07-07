MAIN() Starting Directory: ./raw-data/
DIRECTORY FOUND:./raw-data/2021-07-05_dump_lcars
JSON file found:./raw-data/2021-07-05_dump_lcars/lcars-terminal-6 [697529045562163274].json
PARSE_FILE: ./raw-data/2021-07-05_dump_lcars/lcars-terminal-6 [697529045562163274].json
=====================================================
LCARS_COMMAND: !kirk
-----------------------------------------------------
LCARS_RESPONSE:
**+8%** to all Officer stats on the Bridge
```
Command:         3 %
Engineering:     6 %
Science:         6 %
```
+% to Weapon Damage
```
Rank:       1      2      3      4      5
Value:     5%     8%    12%    15%    20%
```
```
                          Promotion Req
# Rank        MX    SH    FED     XP 
----------------------+----------------
1 Ensign I     5     4                     
2 Lt. JG II   10     8           500       
3 Lt. III     15    20         5,000       
4 Lt. Cmdr IV 20    48        50,000       
5 Commander V 30    88  1,050 100.0K       
----------------------+----------------
```
 * MX = maximum level
 * SH = shards required
 * IND/ROM/FED/KLI/AUG = independent/faction credits
 * XP = officer experience points
=====================================================
==========CONTINUED FROM ABOVE================
{'name': '**Captain Maneuver:**  `Leader`', 'value': '**40%** to all Officer stats when the ship has **Morale**', 'isInline': False}
{'name': '**Synergy**', 'value': '```\nCommand:        10 %\nEngineering:    20 %\nScience:        20 %\n```', 'isInline': False}
{'name': '**Officer Ability:**  `Inspirational`', 'value': '% chance to inspire Morale to his ship each round for 2 rounds\n```\nRank:       1      2      3      4      5\nValue:    50%    60%    70%    75%    80%\n```', 'isInline': False}
{'name': '**Ranks:**', 'value': '```\n                          Promotion Req\n# Rank        MX    SH    FED     XP CB\n----------------------+----------------\n1 Ensign I     5   100                     \n2 Lt. JG II   10   100  1,100 50,000       \n3 Lt. III     15   200  4,400 500.0K  1\n4 Lt. Cmdr IV 20   300 11,000  1.25M  2\n5 Commander V 30   800 24,200   2.5M  4\n----------------------+----------------\n```\n * MX = maximum level\n * SH = shards required\n * IND/ROM/FED/KLI/AUG = independent/faction credits\n * XP = officer experience points\n* CB = Command Badges', 'isInline': False}
==========CONTINUED FROM ABOVE================
{'name': '**Captain Maneuver:**  `3D Strategist`', 'value': '**50%** of Defense to energy damage', 'isInline': False}
{'name': '**Synergy**', 'value': '```\nCommand:        25 %\nEngineering:    50 %\nScience:        50 %\n```', 'isInline': False}
{'name': "**Officer Ability:**  `It's all we have to go on`", 'value': '% chance to give Morale\n```\nRank:       1      2      3      4      5\nValue:    75%    80%    85%    90%    95%\n```', 'isInline': False}
{'name': '**Ranks:**', 'value': '```\n                          Promotion Req\n# Rank        MX    SH    FED     XP CB\n----------------------+----------------\n1 Ensign I     5   110                     \n2 Lt. JG II   10   110  1,150 50,000       \n3 Lt. III     15   220  4,600 500.0K  1\n4 Lt. Cmdr IV 20   330 11,500  1.25M  2\n5 Commander V 30   880 25,000   2.5M  4\n----------------------+----------------\n```\n * MX = maximum level\n * SH = shards required\n * IND/ROM/FED/KLI/AUG = independent/faction credits\n * XP = officer experience points\n* CB = Command Badges', 'isInline': False}
=====================================================
LCARS_COMMAND: !james t. kirk
-----------------------------------------------------
LCARS_RESPONSE:
**+8%** to all Officer stats on the Bridge
```
Command:         3 %
Engineering:     6 %
Science:         6 %
```
+% to Weapon Damage
```
Rank:       1      2      3      4      5
Value:     5%     8%    12%    15%    20%
```
```
                          Promotion Req
# Rank        MX    SH    FED     XP 
----------------------+----------------
1 Ensign I     5     4                     
2 Lt. JG II   10     8           500       
3 Lt. III     15    20         5,000       
4 Lt. Cmdr IV 20    48        50,000       
5 Commander V 30    88  1,050 100.0K       
----------------------+----------------
```
 * MX = maximum level
 * SH = shards required
 * IND/ROM/FED/KLI/AUG = independent/faction credits
 * XP = officer experience points
=====================================================
JSON file found:./raw-data/2021-07-05_dump_lcars/lcars-terminal-16 [697529046057222150].json
PARSE_FILE: ./raw-data/2021-07-05_dump_lcars/lcars-terminal-16 [697529046057222150].json
=====================================================
LCARS_COMMAND: !pattern augur
-----------------------------------------------------
LCARS_RESPONSE:
```
     Rounds (sample)
     1  2  3  4  5  6  7  8  9
-------------------------------
K1:  .  1  .  .  1  .  .  1  .
E1:  2  2  2  2  2  2  2  2  2
E2:  2  2  2  2  2  2  2  2  2
-------------------------------
```
Weapons:
 * `  K1  ` = Obliterator `  KINETIC  `
 * `  E1  ` = Phaser Turret `  ENERGY  `
 * `  E2  ` = Phaser Turret `  ENERGY  `
=====================================================
=====================================================
LCARS_COMMAND: !pattern ente
-----------------------------------------------------
LCARS_RESPONSE:
```
     Rounds (sample)
     1  2  3  4  5  6  7  8  9
-------------------------------
E1:  1  1  1  1  1  1  1  1  1
E2:  1  1  1  1  1  1  1  1  1
E3:  .  2  .  2  .  2  .  2  .
-------------------------------
```
Weapons:
 * `  E1  ` = Phaser Bank `  ENERGY  `
 * `  E2  ` = Phaser Bank `  ENERGY  `
 * `  E3  ` = Disruptor Bank `  ENERGY  `
=====================================================
=====================================================
LCARS_COMMAND: !enterprise t2
-----------------------------------------------------
LCARS_RESPONSE:
Giving what she's got
As long as the ship has Morale, the USS ENTERPRISE heals the Shield Health by 6% whenever it gets hit.

Ship Abilities are always active.

**Ability Bonus by Level**
```
Level      Bonus
----------------
    6        6 %
    7        6 %
    8        6 %
    9        7 %
   10        7 %
----------------
```
Max Tiers: ` 9 `
Max Levels: ` 45 `
Can Scrap? ` Yes `
Req. Lvl: ` 50 `
` 65,400,000 Tritanium `
`  2,275,000 Dilithium `
`     11,150 3★ Common Gas `
`      2,775 3★ Common Ore `
`      1,865 3★ Explorer Parts `
` 380,777 Tritanium `
`  20,401 Dilithium `
Time: `7d 7h 0m`
Seconds: `630,000` **
Time: `1d 1h 4m`
Seconds: `90,270` **
```
Level  XP Required
------------------
    6        2,400
    7        2,900
    8        3,900
    9        4,600
   10        6,000
------------------
```
* **Ship Total Tiering Cost & Time** displayed are *base values only*. Buffs/Bonuses are player specific and *are not applied*.
=====================================================
JSON file found:./raw-data/2021-07-05_dump_lcars/lcars-terminal-26 [697529046447161392].json
PARSE_FILE: ./raw-data/2021-07-05_dump_lcars/lcars-terminal-26 [697529046447161392].json
=====================================================
LCARS_COMMAND: !stella t7 t9
-----------------------------------------------------
LCARS_RESPONSE:
Quantity: ` 100 `
Stella Blueprints: ` 100 each ` = ` 10,000 Total `
Stella Blueprint Reclaim: ` 1 each ` = ` 100 Total `
Stella Blueprint Reclaim: ` 1 each ` = ` 100 Total `
Stella Research: ` 1 `
Shipyard: ` 27 `
Max Tiers: ` 9 `
Max Levels: ` 45 `
Can Scrap? ` Yes `
Req. Lvl: ` 27 `
` 148,010 Uncommon Uranium `
`  29,988 Rare Uranium `
`  12,604 Epic Uranium `
`  1,925,000  `
```
                 Tiers
Component        Min Max Qty
-----------------------------
Energy Weapon      2   9   2
Kinetic Weapon     2   9   1
Shield             2   9   1
Armor              2   9   1
Impulse Engine     2   9   1
-----------------------------
```
* **Ship Total Tiering Cost & Time** displayed are *base values only*. Buffs/Bonuses are player specific and *are not applied*.
=====================================================
=====================================================
LCARS_COMMAND: !hangar 38
-----------------------------------------------------
LCARS_RESPONSE:
Defense Platform D (38)
Shipyard (38)
Operations (38)
`  50  `
Actual: `10,250`
Increase: `1,000`
` 1,156,680,000 Parsteel `
`    22,680,000 Tritanium `
`         2,100 3★ Common Crystal `
`           310 3★ Uncommon Crystal `
Time: `102d 21h 36m`
Seconds: `8,890,560` **
Hull Health Bonus: `114 %`
    Ship Inventory Slots: `58`
NIL
* **Build Cost & time** displayed are *base values only*. Buffs/Bonuses are player specific and *are not applied*.  Use `!upgrade faq` for information on how to calculate the buff adjustments.
=====================================================
=====================================================
LCARS_COMMAND: !dailies 32
-----------------------------------------------------
LCARS_RESPONSE:
```
** Milestone  1:  45 points **
   500,000 x Parsteel
        20 x Recruit Token
   100,000 x Tritanium

** Milestone  2:  85 points **
         1 x 4 Hr Peace Shield
         5 x Armada Directives
 1,300,000 x Parsteel

** Milestone  3:  130 points **
    49,000 x Dilithium
        40 x Premium Recruit Token
   325,000 x Tritanium

** Milestone  4:  180 points **
         1 x 8 Hr Peace Shield
        10 x Armada Directives
   110,000 x Dilithium

** Milestone  5:  255 points **
         1 x 12 Hr Peace Shield
        80 x Latinum
         1 x Loyalty Badge
        60 x Ultra Recruit Token

```
=====================================================
JSON file found:./raw-data/2021-07-05_dump_lcars/lcars-terminal-28 [697529046875111464].json
PARSE_FILE: ./raw-data/2021-07-05_dump_lcars/lcars-terminal-28 [697529046875111464].json
********* DUPLICATE COMMAND FOUND ***********
!hangar 38
=====================================================
LCARS_COMMAND: !kahn
-----------------------------------------------------
LCARS_RESPONSE:
**50%** chances to drastically reduce the opponent's station and ships Mitigation for 2 rounds
```
Command:        10 %
Engineering:    25 %
Science:        25 %
```
+% to Critical Hit chances every time the ship gets hit
```
Rank:       1      2      3      4      5
Value:     1%     2%     3%     4%     5%
```
```
                          Promotion Req
# Rank        MX    SH    IND     XP CB
----------------------+----------------
1 Ensign I     5   110                     
2 Lt. JG II   10   110  1,150 50,000       
3 Lt. III     15   220  4,600 500.0K  1
4 Lt. Cmdr IV 20   330 11,500  1.25M  2
5 Commander V 30   880 25,300   2.5M  4
----------------------+----------------
```
 * MX = maximum level
 * SH = shards required
 * IND/ROM/FED/KLI/AUG = independent/faction credits
 * XP = officer experience points
* CB = Command Badges
=====================================================
=====================================================
LCARS_COMMAND: !pan
-----------------------------------------------------
LCARS_RESPONSE:
**+20%** to Impulse Speed
```
Command:        15 %
Engineering:     5 %
Science:        15 %
```
% chance to apply a Hull Breach on your own ship for three rounds
```
Rank:       1      2      3      4      5
Value:    25%    35%    45%    55%    65%
```
```
                          Promotion Req
# Rank        MX    SH    IND     XP EB
----------------------+----------------
1 Ensign I     5    34                     
2 Lt. JG II   10    50        50,000       
3 Lt. III     15    80  1,050 500.0K  1
4 Lt. Cmdr IV 20   140  4,400  1.25M  2
5 Commander V 30   190 10,500   2.5M  4
----------------------+----------------
```
 * MX = maximum level
 * SH = shards required
 * IND/ROM/FED/KLI/AUG = independent/faction credits
 * XP = officer experience points
* EB = Engineering Badges
=====================================================
JSON file found:./raw-data/2021-07-05_dump_lcars/lcars-terminal-4 [697529045080080480].json
PARSE_FILE: ./raw-data/2021-07-05_dump_lcars/lcars-terminal-4 [697529045080080480].json
=====================================================
LCARS_COMMAND: !t1 ships
-----------------------------------------------------
LCARS_RESPONSE:
*The Romulans built the Augur class battleships as rapid-response vessels to react to attacks on their territory. These sleek warbirds come packaged with side-mounted disruptors and added armor plates across their wingspan.*
*With hostilities on the rise, the Klingon Empire knows that they will need to protect their precious mining operations. Sneering at the Federation’s trickery and the Romulans’s cowardice, the Empire have designed a ship that will guarantee their economic dominance: The B’Chor. This gargantuan vessel features fourteen compartmentalized cargo holds for storing materials, each one protected by a seven inch Tritanium hull. While their enemies flee at the first sight of danger, the B’Chor will stand strong.*
*The Klingon B’Rel class is a small explorer starship built entirely for short range excursions. Unusually, for a Klingon vessel, it is relatively light on weaponry and does not see a lot of combat maneuvers.*
*The Bortas class battleship is traditionally only found as a part of the Klingon Imperial Fleet and is one of the most recognizable ships in the Empire. Many of the flagships of the Empire over the years have been from this class and they have often been commanded by Chancellors throughout the years.*
*Much like the crew that operated it, the Botany Bay is a relic from humanity’s distant past. Built on Earth in the late 20th century, it was intended to be humanity’s foray into deep space exploration. The vessel’s engines utilized revolutionary nuclear fission technology that was believed to be a completely self-sufficient energy source and its X-25 network array could gather data at an astounding rate.*
*The elite Centurion class is a Romulan explorer most typically found in Imperial fleets. Praetor Bervas was once a General in the fleet and led from a Centurion. The battle that gained him the prestige to stake his claim for leadership of the Star Empire was when he led a squadron into Klingon territory to reclaim the Narendra system, destroying dozens of the Klingon Chancellor’s finest warriors in one ambush.*
*Historically utilized by the Klingon Imperial Defense Force, the D3 class of vessel was used primarily for escort and bombardment missions up until the 2150s. It was then re-classified as an Interceptor and has since been widely adopted as a forward scout. Its nuclear fusion impulse engines allow it to move quickly in and out of danger, and it is armed with light disruptors should it need to engage a foe larger and more heavily armored than itself. While not as well armed as its cousin, the D4 class, the D3 is still a reliable and efficient vessel that should never be underestimated.*
*The iconic Klingon D4 class is a tiny fighter vessel used to intercept and destroy enemies. The D4 has many common uses, such as a troop carrier for infiltration and extraction missions. Squadrons of D4 patrol the surface of Kronos as an elite defense force capable of chasing down, surrounding and eliminating any threat.*
*The Fortunate is an original ECS freighter, built for a high carry capacity and structural integrity at the cost of interior comfort, speed and weapon functionality. As an entry level freighter, the ECS Fortunate is very popular, but limited in its capabilities.*
*The Horizon freighter was part of the ECS's privately owned fleet and used for the transport of all types of goods, ranging from hazardous material to passengers on long-haul journeys. Originally built in the early 22nd century, they started service as pre-warp vessels but have since been maintained and upgraded for low-warp travel.*
=====================================================
==========CONTINUED FROM ABOVE================
{'name': 'ENVOY (Neutral)   2★   Common   Survey', 'value': '*The Envoy is an advanced ECS freighter with significant improvements over its older cousin, the J-Class. With more cargo holds and better internal systems, the Envoy is equipped for deep space expeditions.*', 'isInline': False}
{'name': "FERENGI D'VOR (Neutral)   3★   Epic   Survey", 'value': '*As war between the galaxy’s major factions looms over the horizon, many are left wondering about who will come out on top? What state will our galaxy be in when it ends? Then there are those enterprising few who look past these petty concerns and into profit. For those crafty minds, there is no more suitable vessel than the Ferengi D’Vor. Developed by the renowned Urata Manufacturing as a way to cheat the Latinum exchange, the D’Vor comes mounted with a Dx100 mining laser, configured specifically for the extraction of raw latinum. No other vessel in existence can gather the precious material as efficiently, a testament to the engineering prowess and latinum lust of its creators. In a time of war and strife, nothing will generate profit like the D’Vor. After all, war is good for business.*', 'isInline': False}
{'name': 'GLADIUS (Romulan)   3★   Rare   Interceptor', 'value': '*The Gladius class interceptor is a classic Romulan design, built for increased mobility and rapid change of direction. The slim hull allows for an increased chance of evading torpedo fire while on an attack run.*', 'isInline': False}
{'name': "HEGH'TA (Klingon)   4★   Epic   Interceptor", 'value': '*This Klingon interceptor class was designed with intimidation in mind. Its aggressively shaped wing pylons are intentionally designed to look familiar to Klingon warrior battle armor. The Hegh’Ta usually fight in packs and form a core ingredient of any strong Klingon fleet.*', 'isInline': False}
{'name': 'HIJACKED D3 CLASS (Klingon)   3★   Uncommon   Interceptor', 'value': '*The Augments were rarely impressed by Klingon technology. It lacked the level of grace and efficiency that they were used to in their own weaponry. However, even they could not ignore the technical ingenuity put into the D3 vessel. An older ship once thought to be obsolete, the D3 was refitted and repurposed by the Klingons into a great power. For the Augments, there was no better metaphor for their own experience in this strange, new galaxy.*', 'isInline': False}
{'name': 'HIJACKED LEGIONARY (Romulan)   3★   Uncommon   Battleship', 'value': '*In true Romulan fashion, the Legionary class Battleship was slowly phased out of frontline service in favor of the more powerful Augur class. While they were quick to abandon this robust and reliable vessel, the Augments were more than happy to adopt it for their own forces. The Augments know the true value of underestimated technology, and nothing is a better example than the Legionary.*', 'isInline': False}
{'name': 'HIJACKED USS MAYFLOWER (Federation)   3★   Uncommon   Explorer', 'value': '*For the Augments, the opportunity to turn Starfleet’s technology against them was a satisfying turn of events. Their new Mayflower flies Augment colors, a blatant insult to their most hated enemies. Joaquin took the time to update the Mayflower’s nacelles, greatly reducing power drain during long voyages.*', 'isInline': False}
{'name': 'ISS JELLYFISH (Neutral)   4★   Rare   Explorer', 'value': '*The ISS Jellyfish is a testament to the technological prowess of the Terran Empire. Far more versatile than its counterpart in our universe, this Jellyfish uses an experimental dark matter warp drive, capable of travelling vast distances quickly and without appearing on enemy scanners. Originally intended as an espionage vessel, it would allow the Empire to spy on its allies and root out dissent before it began. It is also equipped with powerful T-38 Disruptor cannons, making it more than capable of wiping out rebellious activity whenever it is encountered.\r\n\r\nThe ISS Jellyfish was to be the pride of the Terran Empire, a symbol of their cunning and omniscience. However, the Empire never came into possession of the ship. Spock had other plans for his prized creation...*', 'isInline': False}
{'name': 'JELLYFISH (Federation)   2★   Rare   Explorer', 'value': '*The Jellyfish is a scout ship from the future and another dimension. It was once piloted by Ambassador Spock on his mission to save Romulus from destruction in the Prime reality. Since its arrival in this dimension, the Jellyfish has been extensively studied by Federation scientists for its extremely advanced technology. Despite it being a high-tech vessel, the Jellyfish was designed as a science vessel and has relatively weak defenses and is now commonly used as a fast Explorer.*', 'isInline': False}
{'name': "K'T'INGA (Klingon)   4★   Uncommon   Battleship", 'value': '*A sister class of ship to the Bortas, the K’T’inga is a Klingon battleship with huge arsenal of torpedo launchers. The main launcher is positioned right at the central section of the bow, below the bridge, giving the Captain of each K’T’inga as close a view of every volley from the main launcher.*', 'isInline': False}
==========CONTINUED FROM ABOVE================
{'name': "K'VORT (Klingon)   3★   Rare   Survey", 'value': '*The Klingons retrofitted a standard cargo hauler with design improvements from an early human transport vessel to create their new warp-capable Survey vessels.*', 'isInline': False}
{'name': 'KEHRA (Neutral)   3★   Common   Interceptor', 'value': '*The Kehra is a Tellarite interceptor named after one of the moons that orbits Tellar Prime. These vessels were at the forefront of the Tellarite conflict with the Andorians and later the Romulan Star Empire in the mid 22nd century. The Kehra has gone through few iterations over the following century and is still one of the main designs in use by the Tellarites in their local defense forces.*', 'isInline': False}
{'name': 'KORINAR (Klingon)   4★   Rare   Explorer', 'value': '*The central column of strength in the Klingon Defense Force, the Korinar class is most prevalent in the Kronos system as the eyes and ears of the Chancellor in local space. A formidable reactionary vessel, the Korinar is a strong all-rounder.*', 'isInline': False}
{'name': 'KUMARI (Neutral)   3★   Common   Battleship', 'value': '*The Kumari is an Andorian battle cruiser class named after the legendary Andorian Imperial Guard ship that assisted Earth’s mission to unravel the mystery of the Xindi in 2153. The Andorians built so many of these ships in anticipation of all-out war with the Vulcans that many of the older models can be found in large numbers to this day.*', 'isInline': False}
{'name': 'LEGIONARY (Romulan)   3★   Uncommon   Battleship', 'value': '*The Legionary class Battleship has been in production on Romulus since the early 2100s. Using a prototype forced quantum singularity engine that would later become a mainstay for the Romulan fleet, the Legionary was once one of the most advanced starships on Romulus. Many of its designs eventually made it into the Augur class, which now serves as Romulus’ primary Battleship. With hostilities around the galaxy growing, the Legionary has seen a resurgence within the Romulan fleet, as it makes an ideal support vessel.*', 'isInline': False}
{'name': 'NORTH STAR (Neutral)   3★   Rare   Survey', 'value': '*The ECS North Star is a freighter and survey vessel that has been in service for almost 100 years. Boomer communities in the mid-2100s favored the North Star for space faring and as a colonization ship. Families and communities were born and raised on vessels of this class for generations and an entire network of trade ships has grown over the years.*', 'isInline': False}
{'name': 'ORION CORVETTE (Neutral)   1★   Common   Battleship', 'value': '*The Orions use the Corvette as a nimble smuggling vessel, but it is strong enough in a firefight to act as a viable warship. Despite its hard outer shell, the powerful thrusters give the Corvette a deceptively strong maneuverability.*', 'isInline': False}
{'name': 'PHINDRA (Neutral)   2★   Common   Interceptor', 'value': '*The Phindra Class is Tellarite in origin, now commonly built in mass quantities by Independents, as its sturdy design and capacity for multiple kinetic weapons make it an ideal short range Interceptor.*', 'isInline': False}
{'name': 'PILUM (Romulan)   4★   Rare   Interceptor', 'value': '*The Pilum class was developed in secret by the Tal Shiar intelligence division of the Romulan Star Empire. Designed with stealth and speed in mind, the Pilum was instrumental in retaining the control of the borders along the Neutral Zone in the early stages of the Cold War.*', 'isInline': False}
{'name': 'REALTA (Neutral)   1★   Common   Explorer', 'value': '*The Realta Class is a reliable, if old-fashioned Explorer based on early Earth-made starship designs. Due to its simple components and small size, many Realta hulls were commissioned in the early 2100s and have become synonymous with the Independent movement.*', 'isInline': False}
==========CONTINUED FROM ABOVE================
{'name': 'SARCOPHAGUS (Neutral)   3★   Epic   Battleship', 'value': '*An ancient Klingon ship, revered as holy by the Klingon Empire. The ship is seen as a symbol of all that the Klingons hold dear: brutal power, honour through battle, and an unwavering tenacity. Now in the possession of House T’Kuvma, it is seen as the ship that will lead the Klingons to ultimate victory against those that threaten their empire.*', 'isInline': False}
{'name': 'SEPARATIST D3 CLASS (Klingon)   3★   Uncommon   Interceptor', 'value': '*When House Antaak broke apart from the Klingon Empire during the Separatist movement, they took whatever they could with them. The D3 class vessel, which was, up until this point, primarily a support vessel for the more robust B’Rel, became their primary combat vessel. Refitted with heavy duty disruptor weapons and housed in a six-inch thick tritanium armor plating, the Separatist D3 is a force to be reckoned with and a testament to the tenacity and ingenuity of House Antaak’s Separatist forces.*', 'isInline': False}
{'name': 'STELLA (Rogue)   3★   Uncommon   Battleship', 'value': '*The Stella is a marvel of engineering and criminal ingenuity. The vessel is unique in its modularity. Every component works in concert with its siblings, but is also completely self sufficient, allowing a savvy engineer to swap out and upgrade those parts with ease.\nThis means that the ship can very easily be broken down into its base components and reassembled again. Harry Mudd has taken advantage of this particular element of the ship’s design, breaking it down to avoid detection whenever he pulls off a heist, only to reassemble it with different signatures in another part of the galaxy.\nWith this ingenious method, Mudd has achieved the dream of every criminal in the galaxy. He has rendered himself untraceable.*', 'isInline': False}
{'name': 'TALLA (Neutral)   2★   Common   Battleship', 'value': '*This Battleship is an old Andorian design from the mid-2100s that specializes in strong structural armor and a large quantity of energy weapon banks. The ship was named after Talla, the half-Aenar daughter of the historical figure, Commander Shran, as a symbol of the unity of the Andorian and Aenar races as one galactic community.*', 'isInline': False}
{'name': 'TRIBUNE (Romulan)   4★   Epic   Battleship', 'value': '*The elegant Romulan Tribune class is the most prominent battleship in the Star Empire fleet as the war rages on with the Federation and the Klingons. Mass produced by Reman construction sites, the birdlike feather-plated wing span of the Tribune is gargantuan in breadth and houses a vast array of weaponry for combat situations.*', 'isInline': False}
{'name': 'TURAS (Neutral)   2★   Common   Explorer', 'value': '*The Turas Class is a heavily modified update of the Realta with significantly more power and capability. This Explorer is common with more advanced Independent groups and a staple addition to many fleets in contested, neutral space.*', 'isInline': False}
{'name': 'USS ANTARES (Federation)   3★   Rare   Survey', 'value': "*This Federation Survey ship is an updated design of the old Earth Cargo Ship company's Y-Class vessels that dominated the early intergalactic shipping routes to and from Sol.*", 'isInline': False}
{'name': 'USS DISCOVERY (Neutral)   3★   Rare   Explorer', 'value': '*All things can be understood once they are discovered; the point is to discover them."\nThis was the motto of the USS Discovery when it was launched into service. Officially designated a Crossfield class science vessel, the Discovery\'s facilities could accommodate 300 discrete scientific investigations at any one time.\nHowever, Discovery\'s mission statement would change drastically after the Battle at the Binary Stars in 2256. \nWith Starfleet stretched thin and the Klingons advancing toward Federation space, Discovery was pressed into service as a warship, one that would turn the tide of the conflict. The key to Discovery\'s military success was its unique spore drive, which allowed it to travel galactic distances in the blink of an eye.*', 'isInline': False}
{'name': 'USS ENTERPRISE (Federation)   3★   Epic   Explorer', 'value': '*The Starfleet flagship, the USS Enterprise, is one in the line of iconic Constitution class starships. These phenomenal spacecraft have become the backbone of a rebuilding and reinvigorated Federation. Each model in the class is fitted with the latest technology the Federation has to offer.*', 'isInline': False}
{'name': 'USS ENTERPRISE A (Federation)   4★   Epic   Explorer', 'value': '*The USS Enterprise-A stands as both a fond tribute to its fallen predecessor and as a hopeful look into the future. Commissioned by Starfleet and constructed in Yorktown station in 2263, the ship was completed soon after the destruction of the previous Enterprise, which fell at the hands of Krall and his Swarm. The Enterprise-A follows the same basic configuration as its predecessor but was given more than a few notable upgrades. With the trials of the past behind them and the wonders of tomorrow ahead, this magnificent vessel will carry its crew into the far unknowns... To boldly go where no-one has gone before.*', 'isInline': False}
==========CONTINUED FROM ABOVE================
{'name': 'USS FRANKLIN (Neutral)   3★   Uncommon   Explorer', 'value': "*The USS Franklin is one of Starfleet's most decorated ships, despite having disappeared over 100 years ago. It was the first ever Earth ship capable of reaching warp 4. After many successful missions, the Franklin mysteriously vanished after travelling through the Gagarin Radiation Belt. It was found in the year 2263 by the crew of the Enterprise. They were able to utilize the ship's antiquated technology to defeat Krall and his Swarm.*", 'isInline': False}
{'name': 'USS FRANKLIN-A (Augment)   4★   Uncommon   Explorer', 'value': '*After the unexpected return of the USS Franklin in 2263, Starfleet began to examine the many upgrades and jury-rigged fixes applied to the ancient vessel by Jaylah. At first, it was decided that the ship be scrapped for materials and a statue made in its honor, but then the Swarm returned.\nZenith’s invasion changed everything. The Franklin was pressed back into service and upgraded by a mysterious Independent Commander to take the fight to the Swarm. They were victorious, if only barely.\nIt was only a matter of time before Zenith returned, so the decision was made to retrofit the Franklin and bring it up to the modern standard of Starfleet vessels. So it was, the USS Franklin-A was born.\nThe Franklin-A has been custom-built to combat the Swarm threat. Armed with a special volumetric wavelength amplifier, it is capable of disrupting an entire Swarm cluster in a matter of seconds by overwhelming their shared frequency.*', 'isInline': False}
{'name': 'USS HYDRA (Federation)   4★   Rare   Survey', 'value': '*The USS Hydra is the Federation’s answer to aggressive Klingon raids on their mining operations. The Hydra is made up of three conjoined saucer sections that can be separated at a moment’s notice. Though only the rearmost saucer has access to Nacelles, the others are fitted with smaller, almost imperceptible impulse engines, allowing each section to make their own escape in the event of an attack. Living up to its name, so long as one head survives, the Hydra can never truly be taken down.*', 'isInline': False}
{'name': 'USS INTREPID (Federation)   3★   Rare   Battleship', 'value': '*The Intrepid class starship was originally built by Starfleet as a part of the United Earth military fleet and first began service in aid of the Enterprise NX-01 crew’s search for the Xindi. The latest version of this ship is primarily used by the Federation in short range combat to protect border colonies from Klingon ambushes.*', 'isInline': False}
{'name': 'USS KELVIN (Federation)   4★   Uncommon   Interceptor', 'value': '*The USS Kelvin was the first ship to encounter the Narada in 2233. The ship, under the command of George Kirk, collided with Nero’s in order to allow the escape of its crew. The class lives on under the Kelvin name and because of its age, it has become a common site in contested space for many years, either refitted or in its original guise.*', 'isInline': False}
{'name': 'USS MAYFLOWER (Federation)   3★   Uncommon   Explorer', 'value': '*The streamlined Mayflower class is designed for speed and efficiency. Starfleet have mounted extra-long nacelles directly under the Mayflower’s saucer section to increase its effectiveness in low orbit planetary scouting missions. The titular USS Mayflower was destroyed by Nero’s Narada in 2258 but many of its sister vessels are still in service today.*', 'isInline': False}
{'name': 'USS NEWTON (Federation)   4★   Rare   Battleship', 'value': '*The Newton class is named after iconic human scientist, Sir Isaac Newton, a legend of his field on Earth in the 1600s. The eponymous ship, the USS Newton, was destroyed instantly in the Battle of Vulcan by Nero’s mining behemoth, the Narada. The name lives on as the class continues to be built by Starfleet to field the front lines as the war escalates with the Romulans and Klingons.*', 'isInline': False}
{'name': 'USS SALADIN (Federation)   3★   Uncommon   Interceptor', 'value': '*The Saladin class interceptor is a small Starfleet construction used for dogfighting scenarios, mainly in the defense of outposts and Space Stations. Unlike its older cousin, the Mayflower class, the Saladin relies on a single nacelle and an array of thrusters along the saucer section to provide its maneuverability.*', 'isInline': False}
{'name': 'VAHKLAS (Neutral)   3★   Common   Explorer', 'value': '*The Vahklas was built as a transport ship by the Vulcans in the early 2100s and has had multiple iterations over the following decades. It is a reliable exploration vessel that was mass produced around Vulcan before the planet’s destruction, making it very commonly used by Independents.*', 'isInline': False}
{'name': 'VALDORE (Romulan)   4★   Uncommon   Explorer', 'value': '*The prototype Romulan explorer class, the Valdore, is named after the infamous Senator and Admiral Valdore. The ship is an extremely minimalistic vision of Romulan engineering, designed for immense speed at warp and impulse.*', 'isInline': False}
JSON file found:./raw-data/2021-07-05_dump_lcars/lcars-terminal-3 [697529045080080479].json
PARSE_FILE: ./raw-data/2021-07-05_dump_lcars/lcars-terminal-3 [697529045080080479].json
=====================================================
LCARS_COMMAND: !res ship component efficiency 5
-----------------------------------------------------
LCARS_RESPONSE:
Energy Guerilla Warfare (9)
Foundry (38)
Shipyard (39)
NIL
`  10  `
Outlaw
Column: `  21  `
Row: `  1  `
`       5,350 Outlaw Research Credits `
` 268,500,000 Parsteel `
`  65,800,000 Dilithium `
`      71,280 Stella Particle `
Time: `93d 6h 32m`
Seconds: `8,058,720` **
Actual: `55,500`
Increase: `9,000`
`9.00 %`
NIL
* **Research Cost & time** displayed are *base values only*. Buffs/Bonuses are player specific and *are not applied*.  Use `!research faq` for information on how to calculate the buff adjustments.
=====================================================
=====================================================
LCARS_COMMAND: !res energy guerilla warfare 9
-----------------------------------------------------
LCARS_RESPONSE:
Foundry (38)
Ship Component Efficiency (5)
`  15  `
Outlaw
Column: `  20  `
Row: `  1  `
`     5,350 Outlaw Research Credits `
` 6,955,200 Dilithium `
`    36,480 Stella Particle `
Time: `12d 10h 18m`
Seconds: `1,073,880` **
Actual: `17,250`
Increase: `1,750`
`58,000`
NIL
* **Research Cost & time** displayed are *base values only*. Buffs/Bonuses are player specific and *are not applied*.  Use `!research faq` for information on how to calculate the buff adjustments.
=====================================================
=====================================================
LCARS_COMMAND: !res energy guerilla warfare 8
-----------------------------------------------------
LCARS_RESPONSE:
Ship Component Efficiency (4)
Foundry (38)
Shipyard (37)
NIL
`  15  `
Outlaw
Column: `  20  `
Row: `  1  `
`     5,300 Outlaw Research Credits `
` 5,800,000 Dilithium `
`    38,000 Stella Particle `
Time: `10d 8h 35m`
Seconds: `894,900` **
Actual: `15,500`
Increase: `1,750`
`52,000`
NIL
* **Research Cost & time** displayed are *base values only*. Buffs/Bonuses are player specific and *are not applied*.  Use `!research faq` for information on how to calculate the buff adjustments.
=====================================================
JSON file found:./raw-data/2021-07-05_dump_lcars/lcars-terminal-10 [697529045562163279].json
PARSE_FILE: ./raw-data/2021-07-05_dump_lcars/lcars-terminal-10 [697529045562163279].json
=====================================================
LCARS_COMMAND: ! shops bortas
-----------------------------------------------------
LCARS_RESPONSE:
Revenge
When defending the Station, The BORTAS increases the damage of all the other ships and Defense Platforms by 10%.

Ship Abilities are always active.

**Ability Bonus by Level**
```
Level      Bonus
----------------
    1       10 %
    2       10 %
    3       11 %
    4       11 %
    5       12 %
----------------
```
Quantity: ` 100 `
Bortas Class Blueprint: ` 200 each ` = ` 20,000 Total `
Shipyard: ` 28 `
Max Tiers: ` 9 `
Max Levels: ` 45 `
Can Scrap? ` Yes `
Req. Lvl: ` 42 `
` 1,900,000 Tritanium `
`    42,500 Dilithium `
`       275 3★ Common Crystal `
`     2,200 3★ Common Ore `
` 52,640 Tritanium `
`  1,522 Dilithium `
Time: `17d 0h 0m`
Seconds: `1,468,800` **
Time: `8h 20m`
Seconds: `30,000` **
```
Level  XP Required
------------------
    2          800
    3        1,000
    4        1,400
    5        1,700
------------------
```
```
                 Tiers
Component        Min Max Qty
-----------------------------
Energy Weapon      2   9   1
Kinetic Weapon     2   9   2
Cargo Bay          2   9   1
Warp Engine        2   9   1
Armor              2   9   1
-----------------------------
```
* **Ship Total Tiering Cost & Time** displayed are *base values only*. Buffs/Bonuses are player specific and *are not applied*.
=====================================================
=====================================================
LCARS_COMMAND: !shuttle bay 34
-----------------------------------------------------
LCARS_RESPONSE:
Operations (34)
`  50  `
Actual: `14,250`
Increase: `1,250`
` 175,918,200 Parsteel `
`   2,874,500 Tritanium `
`       4,750 3★ Common Ore `
`         785 3★ Uncommon Ore `
Time: `24d 7h 12m`
Seconds: `2,099,520` **
Service Award Cost Efficiency: `50 %`
    Weapon Damage Bonus: `70 %`
NIL
* **Build Cost & time** displayed are *base values only*. Buffs/Bonuses are player specific and *are not applied*.  Use `!upgrade faq` for information on how to calculate the buff adjustments.
=====================================================
=====================================================
LCARS_COMMAND: !shuttle bay 35
-----------------------------------------------------
LCARS_RESPONSE:
Operations (35)
`  50  `
Actual: `15,500`
Increase: `1,250`
` 272,248,550 Parsteel `
`   4,448,550 Tritanium `
`       5,600 3★ Common Ore `
`         950 3★ Uncommon Ore `
Time: `32d 0h 48m`
Seconds: `2,767,680` **
Service Award Cost Efficiency: `54 %`
    Weapon Damage Bonus: `75 %`
NIL
* **Build Cost & time** displayed are *base values only*. Buffs/Bonuses are player specific and *are not applied*.  Use `!upgrade faq` for information on how to calculate the buff adjustments.
=====================================================
JSON file found:./raw-data/2021-07-05_dump_lcars/lcars-terminal-23 [697529046447161388].json
PARSE_FILE: ./raw-data/2021-07-05_dump_lcars/lcars-terminal-23 [697529046447161388].json
=====================================================
LCARS_COMMAND: !scrap franklin 45
-----------------------------------------------------
LCARS_RESPONSE:
Can Scrap? ` Yes `
Req. Lvl: ` 35 `
`  1,643,809 Dilithium `
` 11,814,900 Tritanium `
`        910 3★ Common Gas `
`      3,359 3★ Explorer Parts `
`     51,234 Ship XP `
`        200 Franklin Advanced Data Core `
Time: `1d 18h 0m`
Seconds: `151,200` **
* Scrap time is dependent on the level of your Scrapyard
* Tier total for Trit & Dil is based on all components upgraded
=====================================================
=====================================================
LCARS_COMMAND: !mission "dark space"
-----------------------------------------------------
LCARS_RESPONSE:
Explore some strange new worlds.
`  Auto  Link / Continuation  `
>>> **Objective  -  Deliver:**
:small_blue_diamond: `  10,000  ` x `  3★ Raw Ore  `
`      1 Balduk to Ty'Rall`
`      1 Haakona to Garadius`
`      1 Haakona to Garadius`
`      1 Bolarus to Fibona`
`      1 Bolarus to Fibona`
The Primeval
The Singularity
=====================================================
=====================================================
LCARS_COMMAND: !shipyard 28
-----------------------------------------------------
LCARS_RESPONSE:
Defense Platform A (28)
Operations (28)
R&D Department (28)
`  50  `
Actual: `7,500`
Increase: `750`
` 10,244,880 Parsteel `
`    167,400 Tritanium `
`      1,200 3★ Common Crystal `
`        230 3★ Uncommon Crystal `
Time: `9d 21h 12m`
Seconds: `853,920` **
Tier Up Speed: `62 %`
    Ship Construction Speed: `62 %`
NIL
* **Build Cost & time** displayed are *base values only*. Buffs/Bonuses are player specific and *are not applied*.  Use `!upgrade faq` for information on how to calculate the buff adjustments.
=====================================================
JSON file found:./raw-data/2021-07-05_dump_lcars/lcars-terminal-2 [697529045080080477].json
PARSE_FILE: ./raw-data/2021-07-05_dump_lcars/lcars-terminal-2 [697529045080080477].json
=====================================================
LCARS_COMMAND: !scrap lvl45 frank
-----------------------------------------------------
LCARS_RESPONSE:
Can Scrap? ` Yes `
Req. Lvl: ` 35 `
`  1,643,809 Dilithium `
` 11,814,900 Tritanium `
`        910 3★ Common Gas `
`      3,359 3★ Explorer Parts `
`     51,234 Ship XP `
`        200 Franklin Advanced Data Core `
Time: `1d 18h 0m`
Seconds: `151,200` **
* Scrap time is dependent on the level of your Scrapyard
* Tier total for Trit & Dil is based on all components upgraded
=====================================================
=====================================================
LCARS_COMMAND: !scrap lvl35 frank
-----------------------------------------------------
LCARS_RESPONSE:
Can Scrap? ` Yes `
Req. Lvl: ` 35 `
`  1,643,809 Dilithium `
` 11,814,900 Tritanium `
`        910 3★ Common Gas `
`      3,359 3★ Explorer Parts `
`     51,234 Ship XP `
`        200 Franklin Advanced Data Core `
Time: `1d 18h 0m`
Seconds: `151,200` **
* Scrap time is dependent on the level of your Scrapyard
* Tier total for Trit & Dil is based on all components upgraded
=====================================================
=====================================================
LCARS_COMMAND: !scrap lvl 30 frank
-----------------------------------------------------
LCARS_RESPONSE:
Can Scrap? ` Yes `
Req. Lvl: ` 35 `
`  48,010 Dilithium `
` 634,210 Tritanium `
`      89 3★ Common Gas `
`     463 3★ Explorer Parts `
`  17,509 Ship XP `
`      25 Franklin Advanced Data Core `
Time: `1d 9h 20m`
Seconds: `120,000` **
* Scrap time is dependent on the level of your Scrapyard
* Tier total for Trit & Dil is based on all components upgraded
=====================================================
JSON file found:./raw-data/2021-07-05_dump_lcars/lcars-terminal-15 [697529046057222148] [part 2].json
PARSE_FILE: ./raw-data/2021-07-05_dump_lcars/lcars-terminal-15 [697529046057222148] [part 2].json
=====================================================
LCARS_COMMAND: !bp kting
-----------------------------------------------------
LCARS_RESPONSE:
=====================================================
=====================================================
LCARS_COMMAND: !ship kting t2 t12
-----------------------------------------------------
LCARS_RESPONSE:
Quantity: ` 150 `
Klingon Loyalty Pack VI: ` 1,725 `(1 only)
K’Tinga Class Blueprint: ` 1,320 each ` = ` 198.0K Total `
Grade 4 Ship Research: ` 1 `
Shipyard: ` 42 `
Max Tiers: ` 12 `
Max Levels: ` 60 `
Can Scrap? ` No `
` 2,158,854,400,000 Tritanium `
`    91,125,800,000 Dilithium `
`            27,415 4★ Common Crystal `
`            44,615 4★ Uncommon Crystal `
`            63,815 4★ Rare Crystal `
`            58,005 4★ Epic Crystal `
`           374,195 4★ Common Ore `
`           390,085 4★ Uncommon Ore `
`           333,305 4★ Rare Ore `
`            92,260 4★ Epic Ore `
`        10,526,695 4★ Common Battleship Parts `
`           392,970 4★ Rare Battleship Parts `
`           937,845 4★ Uncommon Battleship Parts `
`  169,039,000  `
```
                 Tiers
Component        Min Max Qty
-----------------------------
Energy Weapon      2  12   2
Kinetic Weapon     2  12   1
Cargo Bay          2  12   1
Warp Engine        2  12   1
Armor              2  12   1
Impulse Engine     2  12   1
-----------------------------
```
* **Ship Total Tiering Cost & Time** displayed are *base values only*. Buffs/Bonuses are player specific and *are not applied*.
=====================================================
JSON file found:./raw-data/2021-07-05_dump_lcars/lcars-terminal-34 [697529046875111470].json
PARSE_FILE: ./raw-data/2021-07-05_dump_lcars/lcars-terminal-34 [697529046875111470].json
=====================================================
LCARS_COMMAND: !armarda
-----------------------------------------------------
LCARS_RESPONSE:
Aonad Beta (20) ` origin-deep `- Neutral  -  Warp: 20  A: [UNC]
Temeri Beta (20) ` origin-deep `- Neutral  -  Warp: 20  A: [UNC]
Zamaro Beta (20) ` origin-deep `- Neutral  -  Warp: 20  A: [UNC]
Thosz Beta (20) ` origin-deep `- Neutral  -  Warp: 20  A: [UNC]
Ruhe Beta (20) ` origin-deep `- Neutral  -  Warp: 20  A: [UNC]
Stilhe Beta (20) ` origin-deep `- Neutral  -  Warp: 20  A: [UNC]
Perim Beta (20) ` origin-deep `- Neutral  -  Warp: 20  A: [UNC]
Voss (20) - Federation  -  Warp: 13  A: [UNC]  H: [EXP BAT SUR]
Parturi Beta (20) ` origin-deep `- Neutral  -  Warp: 20  A: [UNC]
Saldeti Beta (20) ` origin-deep `- Neutral  -  Warp: 20  A: [UNC]
Asiti Beta (20) ` origin-deep `- Neutral  -  Warp: 20  A: [UNC]
Klefaski Beta (20) ` origin-deep `- Neutral  -  Warp: 20  A: [UNC]
Ezla Beta (20) ` origin-deep `- Neutral  -  Warp: 20  A: [UNC]
Beku Beta (20) ` origin-deep `- Neutral  -  Warp: 20  A: [UNC]
Innlasn Beta (20) ` origin-deep `- Neutral  -  Warp: 20  A: [UNC]
Ber'Tho Beta (20) ` origin-deep `- Neutral  -  Warp: 20  A: [UNC]
Nujord Beta (20) ` origin-deep `- Neutral  -  Warp: 20  A: [UNC]
Kolava Beta (20) ` origin-deep `- Neutral  -  Warp: 20  A: [UNC]
Sorenle (21) - Neutral  -  Warp: 15  A: [UNC]  H: [EXP]
BeK (21) - Klingon  -  Warp: 18  A: [UNC]  H: [SUR BAT INT]
Antonehk (21) - Klingon  -  Warp: 13  A: [UNC]  H: [SUR BAT INT]
V'varia (21) - Romulan  -  Warp: 13  A: [UNC]  H: [SUR EXP BAT]
Iocau (22) - Federation  -  Warp: 18  A: [UNC RAR]  H: [EXP SUR]
Maclyyn (22) - Klingon  -  Warp: 16  A: [UNC RAR]  H: [INT]
Nabok (22) - Romulan  -  Warp: 17  A: [RAR UNC]  H: [BAT]
=====================================================
JSON file found:./raw-data/2021-07-05_dump_lcars/lcars-terminal-1 [697529045080080475] [part 2].json
PARSE_FILE: ./raw-data/2021-07-05_dump_lcars/lcars-terminal-1 [697529045080080475] [part 2].json
=====================================================
LCARS_COMMAND: !starbase chart
-----------------------------------------------------
LCARS_RESPONSE:
To view, click or tap the image. To download:
* PC/MAC: Right-click > Open Link. Will open in your web browser.
* Android/iOS: Tap to view, then tap the Download arrow
=====================================================
JSON file found:./raw-data/2021-07-05_dump_lcars/lcars-terminal-24 [697529046447161389].json
PARSE_FILE: ./raw-data/2021-07-05_dump_lcars/lcars-terminal-24 [697529046447161389].json
=====================================================
LCARS_COMMAND: !? scrap
-----------------------------------------------------
LCARS_RESPONSE:
```asciidoc
!ship <name> <mode> <filters> <sort>
!<name> <mode> <filters> <sort>

Name ::
 * Full/partial/nickname ship name

Mode ::
 * blueprint - cost & where
 * cargo     - protected/capacity by tier
 * crewslots - # of crew by level
 * crewstats - crew stat bonus
 * firingpattern - ship weapon firing pattern (fp)
 * stats   - ship statistics
 * info    - Tier + component
 * levels  - XP by tier
 * repair  - cost by tier
 * scrap   - requires level and tier
 * warp    - warp/impulse range/speed by tier
 * cost    - search in field
 * list    - compact list of ship by
               faction/type/rarity/grade

Filters ::
 * tier    - ship or Component tier/mk
 * faction - neutral, federation, romulan, klingon
 * grade   - G1 to G4 / 1* to 4*
 * rarity  - common, uncommon, rare, epic
 * tco     - total cost of ownership
 * type    - interceptor, explorer, battleship,
               survey
Sort ::
 * byFaction, byGrade, byRarity, byType
```
```asciidoc
!ship byfaction     = list sorted by faction
!ship list          = compact list of all ships
!ship list byRarity = list sorted by rarity
!ship g4            = all G4 ships
!ship fed           = all federation ships
!envoy T5           = ECS Envoy Tier 5 total costs
!bortas T5 T9       = Bortas total cost Tiers 5 to 9
!cent T5 warp       = Centurion MK5 warp engine cost
!cent lvls          = XP by level - all tiers
!pizza cutter repair  = Saladin repair cost/tier
!mf warp            = Mayflower Warp and impulse
!scrap list         = list of scrappable ships
!scrap fed 3*       = Fed 3* recyclable ships
!intrepid scrap T9 45 = Recycle Lvl 45 ship, T9
           components reward Resources + base time
!augur stats        = Augur T1 stats sunmmary
!augur stats t7     = Augur T7 stats summary
!augur stats t7 36  = Ops 36 specific details
!ship cost          = list of all cost resources
!4* rare ship "rare ore" cost
    = list by "rare ore" costs for Rare G4 ships

```
```
 * Part/Components: armor, cargo, impulse engine,
                    mining laser, shield, warp
                    engine, weapon, energy, kinetic
 * Total per tier: All Components + Tier upgrade
    eg: T5 = upgrade all MK4 to MK5 + tier 5

 ** For Skins and Projectiles, see !refit help
```
=====================================================
=====================================================
LCARS_COMMAND: !scrap stella t5 25
-----------------------------------------------------
LCARS_RESPONSE:
Can Scrap? ` Yes `
Req. Lvl: ` 27 `
` 140,450 Tritanium `
`   7,175 Dilithium `
`       1 Stella Hull Scan `
`  11,180 Stella Particle `
Time: `1d 15h 9m`
Seconds: `140,940` **
* Scrap time is dependent on the level of your Scrapyard
* Tier total for Trit & Dil is based on all components upgraded
=====================================================
=====================================================
LCARS_COMMAND: !ops 34
-----------------------------------------------------
LCARS_RESPONSE:
Shipyard (33)
Defense Platform D (33)
`  50  `
Actual: `42,500`
Increase: `4,000`
` 177,480,000 Parsteel `
`   3,262,500 Tritanium `
`   1,087,500 Dilithium `
`       2,800 3★ Common Ore `
`         950 3★ Uncommon Ore `
Time: `60d 18h 0m`
Seconds: `5,248,800` **
Weapon Damage Bonus: `34 %`
`   2 2 Day Speed Up `
`   3 1 Day Peace Shield `
` 150 Latinum `
* **Build Cost & time** displayed are *base values only*. Buffs/Bonuses are player specific and *are not applied*.  Use `!upgrade faq` for information on how to calculate the buff adjustments.
=====================================================
JSON file found:./raw-data/2021-07-05_dump_lcars/lcars-terminal-33 [697529046875111469].json
PARSE_FILE: ./raw-data/2021-07-05_dump_lcars/lcars-terminal-33 [697529046875111469].json
=====================================================
LCARS_COMMAND: !ship sarcophagus
-----------------------------------------------------
LCARS_RESPONSE:
Close-Quarters Combat
When attacking or defending on a capture or mining node in an active Takeover, the Sarcophagus' Weapon Damage is increased by 86000%.
Ship Abilities are always active.
The Sarcophagus' shields receive 10% of the total damage instead of 80%.

**Ability Bonus by Level**
```
Level      Bonus
----------------
    1   86,000 %
    2   87,000 %
    3   88,000 %
    4   89,000 %
    5   90,000 %
----------------
```
Quantity: ` 80 `
Shipyard: ` 30 `
Max Tiers: ` 12 `
Max Levels: ` 60 `
Can Scrap? ` No `
```
Tier   1  2  3  4  5  6  7  8  9 10 11 12
Level 30 30 34 34 34 37 37 37 41 41 41 41
```
` 1,400,000 Tritanium `
`    82,500 Dilithium `
`       250 3★ Common Crystal `
`     1,000 3★ Common Ore `
` 24,400 Fortified Baakonite `
Time: `19d 10h 40m`
Seconds: `1,680,000` **
Time: `10h 50m`
Seconds: `39,000` **
```
Level  XP Required
------------------
    2          800
    3        1,000
    4        1,400
    5        1,700
------------------
```
```
                 Tiers
Component        Min Max Qty
-----------------------------
Energy Weapon      2  12   2
Kinetic Weapon     2  12   2
Cargo Bay          2  12   1
Warp Engine        2  12   1
Armor              2  12   1
-----------------------------
```
* **Ship Total Tiering Cost & Time** displayed are *base values only*. Buffs/Bonuses are player specific and *are not applied*.
=====================================================
=====================================================
LCARS_COMMAND: ! ?
-----------------------------------------------------
LCARS_RESPONSE:
```asciidoc
!armada         :: Armada location & detailed specs
!badges         :: Information on Officer Badges
!blueprint      :: Where to find Ship blueprint
!hostile        :: Summary/detailed hostile information
!mission        :: List/details & rewards
!nearest        :: Find nearby systems
!officer        :: Officer ability, costs, and more
!parts          :: Information on Ship Parts
!planet         :: Find system(s) by planet name
!refit          :: Ship skins and projectiles
!research       :: Research information
!resource       :: Summary/detailed mining information
!route          :: Path between 2 systems
!scrap          :: Ship rewards and time
!ship           :: Ship information & upgrades
!starbase       :: Starbase upgrade information
!system         :: Summary/detailed system information
!zone           :: Territory zones in Origin Sector
```
```asciidoc
!abbreviations  :: List of BOT abbreviations
!alliancelevel  :: Summary/details for Alliance Level
!chart          :: Charts/infographics maintained/tracked
!daily          :: Daily Goals & Milestones
!factionevent   :: Faction event tiers and rewards
!factionlevel   :: Reputation required for each level
!factionmessage :: Faction Message Information
!faq            :: Information on a command or topic
!hello          :: Start Private session
!help           :: This help information
!invite         :: Discord Invite
!plutonium      :: Plutonium location information
!pvplevel       :: Player vs player attack levels
!relocation     :: Where to get Relocation Token
!triangle       :: Describes the battle triangle
```
```asciidoc
!beer           :: Hear a witty one liner from our bot
!coffee         :: Juice up the Code Monkeys
!quote          :: Random favorite Star Trek quotes
!roa            :: Ferengi Rules of Acquisition
!sleep          :: Tell Code Monkeys to sleep!
!stardate       :: Converts from/to Kelvin stardate
!tea            :: Deliver tea to the boss
!vodka, etc     :: Hear a fun quote
```
For help with a specific command, use the following:
```
!help command_name 
```
For example, for more information on the Ship command, like modes, filters, etc, use: `!help ship` or you can shorten it to: `!? ship`
=====================================================
JSON file found:./raw-data/2021-07-05_dump_lcars/lcars-terminal-25 [697529046447161391] [part 2].json
PARSE_FILE: ./raw-data/2021-07-05_dump_lcars/lcars-terminal-25 [697529046447161391] [part 2].json
JSON file found:./raw-data/2021-07-05_dump_lcars/lcars-terminal-30 [697529046875111466].json
PARSE_FILE: ./raw-data/2021-07-05_dump_lcars/lcars-terminal-30 [697529046875111466].json
=====================================================
LCARS_COMMAND: !tco saladin
-----------------------------------------------------
LCARS_RESPONSE:
Quantity: ` 100 `
Saladin Class Interceptor Blueprint: ` 200 each ` = ` 20,000 Total `
Shipyard: ` 28 `
Max Tiers: ` 9 `
Max Levels: ` 45 `
Can Scrap? ` Yes `
Req. Lvl: ` 42 `
` 682,600,000 Tritanium `
`  15,434,000 Dilithium `
`      18,355 3★ Common Crystal `
`       7,617 3★ Uncommon Crystal `
`       1,056 3★ Rare Crystal `
`       3,280 3★ Common Gas `
`       2,402 3★ Uncommon Gas `
`         263 3★ Rare Gas `
`      40,287 3★ Interceptor Parts `
`  2,561,700  `
```
                 Tiers
Component        Min Max Qty
-----------------------------
Energy Weapon      2   9   1
Kinetic Weapon     2   9   1
Cargo Bay          2   9   1
Warp Engine        2   9   1
Impulse Engine     2   9   1
-----------------------------
```
* **Ship Total Tiering Cost & Time** displayed are *base values only*. Buffs/Bonuses are player specific and *are not applied*.
=====================================================
=====================================================
LCARS_COMMAND: !tco enterprise
-----------------------------------------------------
LCARS_RESPONSE:
Quantity: ` 150 `
Enterprise Class Blueprint: ` 1,200 each ` = ` 180.0K Total `
Shipyard: ` 34 `
Max Tiers: ` 9 `
Max Levels: ` 45 `
Can Scrap? ` Yes `
Req. Lvl: ` 50 `
` 10,211,000,000 Tritanium `
`    670,895,000 Dilithium `
`        112,750 3★ Common Gas `
`         51,000 3★ Uncommon Gas `
`         10,450 3★ Rare Gas `
`         20,750 3★ Common Ore `
`         16,150 3★ Uncommon Ore `
`          2,587 3★ Rare Ore `
`        330,830 3★ Explorer Parts `
`  2,561,700  `
```
                 Tiers
Component        Min Max Qty
-----------------------------
Energy Weapon      2   9   3
Cargo Bay          2   9   1
Warp Engine        2   9   1
Shield             2   9   1
-----------------------------
```
* **Ship Total Tiering Cost & Time** displayed are *base values only*. Buffs/Bonuses are player specific and *are not applied*.
=====================================================
=====================================================
LCARS_COMMAND: !ent t1 t4
-----------------------------------------------------
LCARS_RESPONSE:
Quantity: ` 150 `
Enterprise Class Blueprint: ` 1,200 each ` = ` 180.0K Total `
Shipyard: ` 34 `
Max Tiers: ` 9 `
Max Levels: ` 45 `
Can Scrap? ` Yes `
Req. Lvl: ` 50 `
` 421,600,000 Tritanium `
`  19,345,000 Dilithium `
`      49,500 3★ Common Gas `
`       5,400 3★ Uncommon Gas `
`      13,250 3★ Common Ore `
`       1,275 3★ Uncommon Ore `
`      12,130 3★ Explorer Parts `
`  174,200  `
```
                 Tiers
Component        Min Max Qty
-----------------------------
Energy Weapon      2   9   3
Cargo Bay          2   9   1
Warp Engine        2   9   1
Shield             2   9   1
-----------------------------
```
* **Ship Total Tiering Cost & Time** displayed are *base values only*. Buffs/Bonuses are player specific and *are not applied*.
=====================================================
JSON file found:./raw-data/2021-07-05_dump_lcars/lcars-terminal-20 [697529046447161384].json
PARSE_FILE: ./raw-data/2021-07-05_dump_lcars/lcars-terminal-20 [697529046447161384].json
=====================================================
LCARS_COMMAND: !franklin-a
-----------------------------------------------------
LCARS_RESPONSE:
Swarm Hunter
When fighting Swarm Hostiles or Swarm Armadas, The Franklin-A's Damage is increased by 3500%
Ship Abilities are always active.

**Ability Bonus by Level**
```
Level      Bonus
----------------
    1    3,500 %
    2    3,600 %
    3    3,700 %
    4    3,850 %
    5    4,000 %
----------------
```
Quantity: ` 200 `
Shipyard: ` 35 `
Max Tiers: ` 12 `
Max Levels: ` 60 `
Can Scrap? ` No `
```
Tier   1  2  3  4  5  6  7  8  9 10 11 12
Level 35 37 39 41 43 44 45 46 47 48 49 50
```
` 20,000,000 Tritanium `
`    300,000 Dilithium `
`        300 3★ Common Crystal `
`         30 3★ Uncommon Crystal `
`         50 3★ Common Gas `
` 2,000,000 Tritanium `
`    18,000 Dilithium `
Time: `165d 0h 0m`
Seconds: `14,256,000` **
Time: `23h 20m`
Seconds: `84,000` **
```
Level  XP Required
------------------
    2        8,000
    3       12,000
    4       20,000
    5       29,000
------------------
```
```
                 Tiers
Component        Min Max Qty
-----------------------------
Energy Weapon      2  12   1
Kinetic Weapon     2  12   2
Cargo Bay          2  12   1
Warp Engine        2  12   1
Shield             2  12   1
-----------------------------
```
* **Ship Total Tiering Cost & Time** displayed are *base values only*. Buffs/Bonuses are player specific and *are not applied*.
=====================================================
=====================================================
LCARS_COMMAND: ! upgrade defence technology 24
-----------------------------------------------------
LCARS_RESPONSE:
Operations (24)
R&D Department (24)
Science Lab (20)
`  50  `
Actual: `7,000`
Increase: `750`
` 981,240 Parsteel `
` 115,440 Tritanium `
`     150 3★ Common Gas `
Time: `1d 23h 36m`
Seconds: `171,360` **
Defense Platform Damage Bonus: `24 %`
    Defense Platform Defensive Bonus: `96 %`
NIL
* **Build Cost & time** displayed are *base values only*. Buffs/Bonuses are player specific and *are not applied*.  Use `!upgrade faq` for information on how to calculate the buff adjustments.
=====================================================
=====================================================
LCARS_COMMAND: ! upgrade defence technology 25
-----------------------------------------------------
LCARS_RESPONSE:
Science Lab (25)
Engine Technology Lab (25)
Foundry (25)
`  50  `
Actual: `8,000`
Increase: `1,000`
` 1,591,200 Parsteel `
`   187,200 Tritanium `
`       190 3★ Common Gas `
`         1 3★ Uncommon Gas `
Time: `1d 20h 0m`
Seconds: `158,400` **
Defense Platform Defensive Bonus: `100 %`
    Defense Platform Damage Bonus: `25 %`
NIL
* **Build Cost & time** displayed are *base values only*. Buffs/Bonuses are player specific and *are not applied*.  Use `!upgrade faq` for information on how to calculate the buff adjustments.
=====================================================
JSON file found:./raw-data/2021-07-05_dump_lcars/lcars-terminal-12 [697529046057222145].json
PARSE_FILE: ./raw-data/2021-07-05_dump_lcars/lcars-terminal-12 [697529046057222145].json
=====================================================
LCARS_COMMAND: !rouge reputation
-----------------------------------------------------
LCARS_RESPONSE:
```
     Points       Reputation    L D
-----------------------------------
   -2,000,000  is max negative
     -500,000+ is ENEMY
      -25,000+ is HOSTILE
         -500+ is UNTRUSTWORTHY
  -499 to 499  is NEUTRAL
          500+ is TOLERATED
        2,000+ is TOLERATED       D
        5,000+ is NEIGHBOR
       25,000+ is FRIENDLY
      100,000+ is FAVORED
      200,000+ is FAVORED         D
      500,000+ is CONSORT
    1,200,000+ is CONSORT         D
    2,000,000+ is ASSOCIATE
    5,000,000+ is ASSOCIATE       D
   10,000,000+ is RESPECTED     L
   30,000,000+ is CELEBRATED
   50,000,000+ is ADMIRED
   80,000,000+ is ESTEEMED
  140,000,000+ is COMMENDED
  260,000,000+ is COMMENDED       D
  440,000,000+ is GLORIFIED
  700,000,000+ is GLORIFIED       D
1,000,000,000+ is CHAMPION
1,000,000,500  is [LOCKED IN]
-----------------------------------
* L = Lock, D = Dailies Barrier
```
```
     Points     Reputation
--------------------------------
          0  is NEUTRAL
        250+ is SERVANT
      2,500+ is PAWN
     50,000+ is ASSOCIATE
    250,000+ is FRIEND
  1,000,000+ is ALLY
  1,000,500  is [LOCKED IN]
--------------------------------
```
```
     Points     Reputation
--------------------------------
          0+ is LACKEY
        500+ is ABETTOR
      5,000+ is TROUBLE-MAKER
     25,000+ is SCOUNDREL
    100,000+ is ACCOMPLICE
    500,000+ is KNOWN ASSOCIATE
  2,000,000+ is PARTNER
 10,000,000+ is OUTLAW
 30,000,500  is [LOCKED IN]
--------------------------------
```
=====================================================
JSON file found:./raw-data/2021-07-05_dump_lcars/lcars-terminal-19 [697529046057222153].json
PARSE_FILE: ./raw-data/2021-07-05_dump_lcars/lcars-terminal-19 [697529046057222153].json
=====================================================
LCARS_COMMAND: !?
-----------------------------------------------------
LCARS_RESPONSE:
```asciidoc
!armada         :: Armada location & detailed specs
!badges         :: Information on Officer Badges
!blueprint      :: Where to find Ship blueprint
!hostile        :: Summary/detailed hostile information
!mission        :: List/details & rewards
!nearest        :: Find nearby systems
!officer        :: Officer ability, costs, and more
!parts          :: Information on Ship Parts
!planet         :: Find system(s) by planet name
!refit          :: Ship skins and projectiles
!research       :: Research information
!resource       :: Summary/detailed mining information
!route          :: Path between 2 systems
!scrap          :: Ship rewards and time
!ship           :: Ship information & upgrades
!starbase       :: Starbase upgrade information
!system         :: Summary/detailed system information
!zone           :: Territory zones in Origin Sector
```
```asciidoc
!abbreviations  :: List of BOT abbreviations
!alliancelevel  :: Summary/details for Alliance Level
!chart          :: Charts/infographics maintained/tracked
!daily          :: Daily Goals & Milestones
!factionevent   :: Faction event tiers and rewards
!factionlevel   :: Reputation required for each level
!factionmessage :: Faction Message Information
!faq            :: Information on a command or topic
!hello          :: Start Private session
!help           :: This help information
!invite         :: Discord Invite
!plutonium      :: Plutonium location information
!pvplevel       :: Player vs player attack levels
!relocation     :: Where to get Relocation Token
!triangle       :: Describes the battle triangle
```
```asciidoc
!beer           :: Hear a witty one liner from our bot
!coffee         :: Juice up the Code Monkeys
!quote          :: Random favorite Star Trek quotes
!roa            :: Ferengi Rules of Acquisition
!sleep          :: Tell Code Monkeys to sleep!
!stardate       :: Converts from/to Kelvin stardate
!tea            :: Deliver tea to the boss
!vodka, etc     :: Hear a fun quote
```
For help with a specific command, use the following:
```
!help command_name 
```
For example, for more information on the Ship command, like modes, filters, etc, use: `!help ship` or you can shorten it to: `!? ship`
=====================================================
=====================================================
LCARS_COMMAND: !chart armada
-----------------------------------------------------
LCARS_RESPONSE:
To view, click or tap the image. To download:
* PC/MAC: Right-click > Open Link. Will open in your web browser.
* Android/iOS: Tap to view, then tap the Download arrow
=====================================================
JSON file found:./raw-data/2021-07-05_dump_lcars/lcars-terminal-22 [697529046447161387].json
PARSE_FILE: ./raw-data/2021-07-05_dump_lcars/lcars-terminal-22 [697529046447161387].json
=====================================================
LCARS_COMMAND: !chart pvp
-----------------------------------------------------
LCARS_RESPONSE:
To view, click or tap the image. To download:
* PC/MAC: Right-click > Open Link. Will open in your web browser.
* Android/iOS: Tap to view, then tap the Download arrow
=====================================================
=====================================================
LCARS_COMMAND: !chart rr
-----------------------------------------------------
LCARS_RESPONSE:
To view, click or tap the image. To download:
* PC/MAC: Right-click > Open Link. Will open in your web browser.
* Android/iOS: Tap to view, then tap the Download arrow
=====================================================
JSON file found:./raw-data/2021-07-05_dump_lcars/lcars-terminal-8 [697529045562163277].json
PARSE_FILE: ./raw-data/2021-07-05_dump_lcars/lcars-terminal-8 [697529045562163277].json
=====================================================
LCARS_COMMAND: !r "1* isogen extraction" 2
-----------------------------------------------------
LCARS_RESPONSE:
R&D Department (26)
NIL
`  15  `
Territory
Column: `  1  `
Row: `  2  `
`    260 Iso-emulsion `
` 24,250 Dilithium `
Time: `4d 20h 7m`
Seconds: `418,020` **
Actual: `6,000`
Increase: `750`
`15.00 %`
NIL
* **Research Cost & time** displayed are *base values only*. Buffs/Bonuses are player specific and *are not applied*.  Use `!research faq` for information on how to calculate the buff adjustments.
=====================================================
=====================================================
LCARS_COMMAND: !up defense platform d t1 t10
-----------------------------------------------------
LCARS_RESPONSE:
No building level was specified. Please add a building level, range 1 to 50, to your command.

For more information, type ` !upgrade help`.
=====================================================
=====================================================
LCARS_COMMAND: !up defense platform d 1 10
-----------------------------------------------------
LCARS_RESPONSE:
Defense Platform D (10)
Drydock D (10)
Defense Platform D (9)
Drydock D (9)
Defense Platform D (8)
Drydock D (8)
Defense Platform D (7)
Drydock D (7)
Defense Platform D (6)
Drydock D (6)
Defense Platform D (5)
Drydock D (5)
Defense Platform D (4)
Drydock D (4)
Defense Platform D (3)
Drydock D (3)
Defense Platform D (2)
Drydock D (2)
Defense Platform D (1)
` 118,386 Parsteel `
`   5,435 Tritanium `
`     486 Dilithium `
Actual: `37,757`
Increase: `10,305`
Time: `11h 21m`
Seconds: `40,890` **
NIL
* **Build Cost & time** displayed are *base values only*. Buffs/Bonuses are player specific and *are not applied*.  Use `!upgrade faq` for information on how to calculate the buff adjustments.
=====================================================
JSON file found:./raw-data/2021-07-05_dump_lcars/lcars-terminal-27 [697529046447161393] [part 2].json
PARSE_FILE: ./raw-data/2021-07-05_dump_lcars/lcars-terminal-27 [697529046447161393] [part 2].json
=====================================================
LCARS_COMMAND: !r combat 4★ tactical battleships 10
-----------------------------------------------------
LCARS_RESPONSE:
4★ Battleship Penetration (6)
R&D Department (49)
4★ Fortified Battleships (7)
`  10  `
Combat
Column: `  41  `
Row: `  3  `
` 5,187,000,000 Dilithium `
`        24,000 4★ Common Ore `
`         9,300 4★ Uncommon Ore `
Time: `2,265d 10h 14m`
Seconds: `195,732,840` **
Actual: `117,000`
Increase: `7,000`
`22.00 %`
NIL
* **Research Cost & time** displayed are *base values only*. Buffs/Bonuses are player specific and *are not applied*.  Use `!research faq` for information on how to calculate the buff adjustments.
=====================================================
JSON file found:./raw-data/2021-07-05_dump_lcars/lcars-terminal-21 [697529046447161386].json
PARSE_FILE: ./raw-data/2021-07-05_dump_lcars/lcars-terminal-21 [697529046447161386].json
=====================================================
LCARS_COMMAND: ! upg botany bay t4
-----------------------------------------------------
LCARS_RESPONSE:
Data Mining

The Botany Bay's Mining Bonus from the Mining Laser is increased by  31450% when mining Corrupted Data and Decoded Data.

Ship Abilities are always active.

**Ability Bonus by Level**
```
Level      Bonus
----------------
   16        314
   17        318
   18        321
   19        324
   20        328
----------------
```
Max Tiers: ` 9 `
Max Levels: ` 45 `
Can Scrap? ` No `
` 85,500 Tritanium `
`  5,000 Dilithium `
`    406 2★ Common Gas `
`     34 2★ Uncommon Gas `
`  1,620 2★ Common Ore `
`    243 2★ Uncommon Ore `
`  1,280 2★ Survey Parts `
`    510 Common Plutonium `
` 1,163 Tritanium `
`   141 Dilithium `
Time: `3d 16h 53m`
Seconds: `320,000` **
Time: `53m`
Seconds: `3,226` **
```
Level  XP Required
------------------
   16       15,000
   17       17,500
   18       19,500
   19       23,000
   20       25,000
------------------
```
* **Ship Total Tiering Cost & Time** displayed are *base values only*. Buffs/Bonuses are player specific and *are not applied*.
=====================================================
=====================================================
LCARS_COMMAND: ! mayflower t1 to t2
-----------------------------------------------------
LCARS_RESPONSE:
Quantity: ` 80 `
Mayflower Blueprint: ` 125 each ` = ` 10,000 Total `
Shipyard: ` 26 `
Max Tiers: ` 9 `
Max Levels: ` 45 `
Can Scrap? ` Yes `
Req. Lvl: ` 34 `
` 2,600,000 Tritanium `
`   116,000 Dilithium `
`     1,600 3★ Common Gas `
`       293 3★ Common Ore `
`       281 3★ Explorer Parts `
`  24,700  `
```
                 Tiers
Component        Min Max Qty
-----------------------------
Energy Weapon      2   9   3
Cargo Bay          2   9   1
Warp Engine        2   9   1
Shield             2   9   1
-----------------------------
```
* **Ship Total Tiering Cost & Time** displayed are *base values only*. Buffs/Bonuses are player specific and *are not applied*.
=====================================================
=====================================================
LCARS_COMMAND: ! mayflower t2 to t3
-----------------------------------------------------
LCARS_RESPONSE:
Quantity: ` 80 `
Mayflower Blueprint: ` 125 each ` = ` 10,000 Total `
Shipyard: ` 26 `
Max Tiers: ` 9 `
Max Levels: ` 45 `
Can Scrap? ` Yes `
Req. Lvl: ` 34 `
` 5,140,000 Tritanium `
`   247,000 Dilithium `
`     1,920 3★ Common Gas `
`       123 3★ Uncommon Gas `
`       543 3★ Common Ore `
`        30 3★ Uncommon Ore `
`       848 3★ Explorer Parts `
`  69,300  `
```
                 Tiers
Component        Min Max Qty
-----------------------------
Energy Weapon      2   9   3
Cargo Bay          2   9   1
Warp Engine        2   9   1
Shield             2   9   1
-----------------------------
```
* **Ship Total Tiering Cost & Time** displayed are *base values only*. Buffs/Bonuses are player specific and *are not applied*.
=====================================================
JSON file found:./raw-data/2021-07-05_dump_lcars/lcars-terminal-1 [697529045080080475].json
PARSE_FILE: ./raw-data/2021-07-05_dump_lcars/lcars-terminal-1 [697529045080080475].json
=====================================================
LCARS_COMMAND: ! mission "so it has come to this"
-----------------------------------------------------
LCARS_RESPONSE:
Join the fray.
`  Auto  Link / Continuation  `
>>> **Objective  -  Travel to:**
:small_blue_diamond: Destination: ` Deneva (15) `  -  Warp: ` 11 `
>>> **Objective  -  Choose:**
:regional_indicator_a: Federation
:regional_indicator_b: Klingons
:regional_indicator_c: Romulans
>>> **Objective  -  Destroy Hostile Target:**
:small_blue_diamond: Destination: ` Deneva (15) `  -  Warp: ` 11 `
:small_orange_diamond: Destroy Klingon D4
>>> **Objective  -  Destroy Hostile Target:**
:small_blue_diamond: Destination: ` Deneva (15) `  -  Warp: ` 11 `
:small_orange_diamond: Destroy IRW Magnifica
>>> **Objective  -  Travel to:**
:small_blue_diamond: Destination: ` Lorillia (18) `  -  Warp: ` 13 `
>>> **Objective  -  Return:**
:small_blue_diamond: Return your ship to your station.
`     15 Federation Credits`
`    500 Federation Recruit Token`
`    240 Federation Points`
`    -35 Romulan Points`
`   -156 Klingon Points`
>>> **Objective  -  Destroy Hostile Target:**
:small_blue_diamond: Destination: ` Deneva (15) `  -  Warp: ` 11 `
:small_orange_diamond: Destroy IRW Magnifica
>>> **Objective  -  Destroy Hostile Target:**
:small_blue_diamond: Destination: ` Deneva (15) `  -  Warp: ` 11 `
:small_orange_diamond: Destroy USS Everest
>>> **Objective  -  Travel to:**
:small_blue_diamond: Destination: ` Krah'Hor (18) `  -  Warp: ` 13 `
>>> **Objective  -  Return:**
:small_blue_diamond: Return your ship to your station.
`    500 Klingon Recruit Token`
`     15 Klingon Credits`
`    -52 Federation Points`
`   -138 Romulan Points`
`    240 Klingon Points`
>>> **Objective  -  Destroy Hostile Target:**
:small_blue_diamond: Destination: ` Deneva (15) `  -  Warp: ` 11 `
:small_orange_diamond: Destroy USS Everest
>>> **Objective  -  Destroy Hostile Target:**
:small_blue_diamond: Destination: ` Deneva (15) `  -  Warp: ` 11 `
:small_orange_diamond: Destroy Klingon D4
>>> **Objective  -  Travel to:**
:small_blue_diamond: Destination: ` Kaikara (18) `  -  Warp: ` 13 `
>>> **Objective  -  Return:**
:small_blue_diamond: Return your ship to your station.
`    500 Romulan Recruit Token`
`     15 Romulan Credits`
`   -104 Federation Points`
`    240 Romulan Points`
`    -69 Klingon Points`
The Calm Before the Storm
:regional_indicator_a: To Seek Out New Life Forms
:regional_indicator_b: First Blood
:regional_indicator_c: For the Glory of Romulus
=====================================================
=====================================================
LCARS_COMMAND: ! mission "the calm before the storm"
-----------------------------------------------------
LCARS_RESPONSE:
Assist Toryn with his experiment.
`  Auto  Link / Continuation  `
>>> **Objective  -  Travel to:**
:small_blue_diamond: Destination: ` Bharani (16) `  -  Warp: ` 13 `
>>> **Objective  -  Deliver:**
:small_blue_diamond: `  2,000  ` x `  Dilithium  `
>>> **Objective  -  Travel to:**
:small_blue_diamond: Destination: ` Kepler-018 (20) `  -  Warp: ` 13 `
>>> **Objective  -  Destroy Hostile Target:**
:small_blue_diamond: Destination: ` Kepler-018 (20) `  -  Warp: ` 13 `
:small_orange_diamond: Destroy Gorn Marauder
>>> **Objective  -  Travel to:**
:small_blue_diamond: Destination: ` Bharani (16) `  -  Warp: ` 13 `
>>> **Objective  -  Return:**
:small_blue_diamond: Return your ship to your station.
`      4 2★ Uncommon Crystal`
`      4 2★ Uncommon Gas`
`      4 2★ Uncommon Ore`
The Ends Justify the Means
So It Has Come to This
=====================================================
=====================================================
LCARS_COMMAND: ! mission "for the empire"
-----------------------------------------------------
LCARS_RESPONSE:
Assist the Klingons with their research.
`  Auto  Link / Continuation  `
>>> **Objective  -  Travel to:**
:small_blue_diamond: Destination: ` Vindemiatrix (15) `  -  Warp: ` 11 `
>>> **Objective  -  Travel to:**
:small_blue_diamond: Destination: ` Amador (19) `  -  Warp: ` 12 `
>>> **Objective  -  Destroy Hostile Target:**
:small_blue_diamond: Destination: ` Amador (19) `  -  Warp: ` 12 `
:small_orange_diamond: Destroy Suliban Explorer
>>> **Objective  -  Destroy Hostile Target:**
:small_blue_diamond: Destination: ` Amador (19) `  -  Warp: ` 12 `
:small_orange_diamond: Destroy Suliban Destroyer
>>> **Objective  -  Travel to:**
:small_blue_diamond: Destination: ` Krah'Hor (18) `  -  Warp: ` 13 `
:small_blue_diamond: Planet: `  Vos'Keth Station  `
` 43,000 Officer XP`
`      3 Kerla`
Transgressions
A Second Opinion
=====================================================
JSON file found:./raw-data/2021-07-05_dump_lcars/lcars-terminal-35 [697529046875111471] [part 2].json
PARSE_FILE: ./raw-data/2021-07-05_dump_lcars/lcars-terminal-35 [697529046875111471] [part 2].json
=====================================================
LCARS_COMMAND: !dpa 38 info
-----------------------------------------------------
LCARS_RESPONSE:
Drydock A (38)
`  50  `
Actual: `1,940,043`
Increase: `228,653`
` 771,120,000 Parsteel `
`  22,680,000 Tritanium `
`   2,268,000 Dilithium `
`       2,100 3★ Common Gas `
`         310 3★ Uncommon Gas `
Time: `48d 0h 24m`
Seconds: `4,148,640` **
Power Level: `38`
NIL
* **Build Cost & time** displayed are *base values only*. Buffs/Bonuses are player specific and *are not applied*.  Use `!upgrade faq` for information on how to calculate the buff adjustments.
=====================================================
=====================================================
LCARS_COMMAND: !dpa 39 info
-----------------------------------------------------
LCARS_RESPONSE:
Drydock A (39)
Defense Technologies (39)
`  50  `
Actual: `2,222,894`
Increase: `282,851`
` 1,315,800,000 Parsteel `
`    38,700,000 Tritanium `
`     3,870,000 Dilithium `
Time: `63d 17h 36m`
Seconds: `5,506,560` **
Power Level: `39`
NIL
* **Build Cost & time** displayed are *base values only*. Buffs/Bonuses are player specific and *are not applied*.  Use `!upgrade faq` for information on how to calculate the buff adjustments.
=====================================================
JSON file found:./raw-data/2021-07-05_dump_lcars/lcars-terminal-11 [697529046057222144].json
PARSE_FILE: ./raw-data/2021-07-05_dump_lcars/lcars-terminal-11 [697529046057222144].json
=====================================================
LCARS_COMMAND: !res “explorer shields” 10
-----------------------------------------------------
LCARS_RESPONSE:
*Increases the Shield Health of Grade 4 Explorers when defending in the station*
*Shield Health is increased for all Explorers.*
*Increases shield health for Explorers.*
=====================================================
==========CONTINUED FROM ABOVE================
{'name': 'Requirements', 'value': 'Battleship Shields (8)\nFoundry (34)\nScience Lab (37)', 'isInline': False}
{'name': 'Required By:', 'value': 'Explorer Hull Boost (10)', 'isInline': False}
{'name': 'Levels', 'value': '`  10  `', 'isInline': True}
{'name': 'Tab', 'value': 'Combat\nColumn: `  20  `\nRow: `  3  `', 'isInline': True}
{'name': 'Research Costs', 'value': '`\xa024,450,000\xa0Tritanium\xa0`\n`\xa014,650,000\xa0Dilithium\xa0`\n`\xa0\xa0\xa0\xa0\xa0\xa02,080\xa03★\xa0Common\xa0Gas\xa0`\n`\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0440\xa03★\xa0Uncommon\xa0Gas\xa0`\n`\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa039\xa03★\xa0Rare\xa0Gas\xa0`', 'isInline': False}
{'name': 'Build Time', 'value': 'Time:\xa0`40d\xa07h\xa046m`\nSeconds:\xa0`3,483,960`\xa0**', 'isInline': True}
{'name': 'Power', 'value': 'Actual: `37,500`\nIncrease: `3,500`', 'isInline': True}
{'name': 'Bonuses', 'value': '`150.00 %`', 'isInline': False}
{'name': 'Rewards', 'value': 'NIL', 'isInline': False}
{'name': '**NOTE:**', 'value': '* **Research Cost & time** displayed are *base values only*. Buffs/Bonuses are player specific and *are not applied*.  Use `!research faq` for information on how to calculate the buff adjustments.', 'isInline': False}
==========CONTINUED FROM ABOVE================
{'name': 'Requirements', 'value': 'R&D Department (45)', 'isInline': False}
{'name': 'Required By:', 'value': 'NIL', 'isInline': False}
{'name': 'Levels', 'value': '`  12  `', 'isInline': True}
{'name': 'Tab', 'value': 'Territory\nColumn: `  8  `\nRow: `  1  `', 'isInline': True}
{'name': 'Research Costs', 'value': '`\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0550\xa0Quantum\xa0Particle\xa0`\n`\xa0\xa0\xa0\xa0330,000\xa0Iso-emulsion\xa0`\n`\xa070,800,000\xa0Dilithium\xa0`', 'isInline': False}
{'name': 'Build Time', 'value': 'Time:\xa0`591d\xa07h\xa047m`\nSeconds:\xa0`51,090,420`\xa0**', 'isInline': True}
{'name': 'Power', 'value': 'Actual: `35,500`\nIncrease: `5,000`', 'isInline': True}
{'name': 'Bonuses', 'value': '`150.00 %`', 'isInline': False}
{'name': 'Rewards', 'value': 'NIL', 'isInline': False}
{'name': '**NOTE:**', 'value': '* **Research Cost & time** displayed are *base values only*. Buffs/Bonuses are player specific and *are not applied*.  Use `!research faq` for information on how to calculate the buff adjustments.', 'isInline': False}
=====================================================
LCARS_COMMAND: !faction rep
-----------------------------------------------------
LCARS_RESPONSE:
```
     Points       Reputation    L D
-----------------------------------
   -2,000,000  is max negative
     -500,000+ is ENEMY
      -25,000+ is HOSTILE
         -500+ is UNTRUSTWORTHY
  -499 to 499  is NEUTRAL
          500+ is TOLERATED
        2,000+ is TOLERATED       D
        5,000+ is NEIGHBOR
       25,000+ is FRIENDLY
      100,000+ is FAVORED
      200,000+ is FAVORED         D
      500,000+ is CONSORT
    1,200,000+ is CONSORT         D
    2,000,000+ is ASSOCIATE
    5,000,000+ is ASSOCIATE       D
   10,000,000+ is RESPECTED     L
   30,000,000+ is CELEBRATED
   50,000,000+ is ADMIRED
   80,000,000+ is ESTEEMED
  140,000,000+ is COMMENDED
  260,000,000+ is COMMENDED       D
  440,000,000+ is GLORIFIED
  700,000,000+ is GLORIFIED       D
1,000,000,000+ is CHAMPION
1,000,000,500  is [LOCKED IN]
-----------------------------------
* L = Lock, D = Dailies Barrier
```
```
     Points     Reputation
--------------------------------
          0  is NEUTRAL
        250+ is SERVANT
      2,500+ is PAWN
     50,000+ is ASSOCIATE
    250,000+ is FRIEND
  1,000,000+ is ALLY
  1,000,500  is [LOCKED IN]
--------------------------------
```
```
     Points     Reputation
--------------------------------
          0+ is LACKEY
        500+ is ABETTOR
      5,000+ is TROUBLE-MAKER
     25,000+ is SCOUNDREL
    100,000+ is ACCOMPLICE
    500,000+ is KNOWN ASSOCIATE
  2,000,000+ is PARTNER
 10,000,000+ is OUTLAW
 30,000,500  is [LOCKED IN]
--------------------------------
```
=====================================================
JSON file found:./raw-data/2021-07-05_dump_lcars/lcars-terminal-27 [697529046447161393].json
PARSE_FILE: ./raw-data/2021-07-05_dump_lcars/lcars-terminal-27 [697529046447161393].json
=====================================================
LCARS_COMMAND: ! scrap legionary l45
-----------------------------------------------------
LCARS_RESPONSE:
Can Scrap? ` Yes `
Req. Lvl: ` 34 `
`  3,448,313 Dilithium `
` 52,551,000 Tritanium `
`     28,171 4★ Common Crystal `
`      1,597 4★ Uncommon Crystal `
`        251 4★ Rare Crystal `
`     52,316 4★ Common Ore `
`      2,965 4★ Uncommon Ore `
`        466 4★ Rare Ore `
`    107,247 4★ Common Battleship Parts `
`      8,044 4★ Uncommon Battleship Parts `
`     51,234 Ship XP `
Time: `14d 8h 0m`
Seconds: `1,238,400` **
* Scrap time is dependent on the level of your Scrapyard
* Tier total for Trit & Dil is based on all components upgraded
=====================================================
=====================================================
LCARS_COMMAND: !scrap mayflower l45
-----------------------------------------------------
LCARS_RESPONSE:
Can Scrap? ` Yes `
Req. Lvl: ` 34 `
` 30,077,500 Tritanium `
`  3,727,525 Dilithium `
`     54,630 4★ Common Gas `
`      3,096 4★ Uncommon Gas `
`        486 4★ Rare Gas `
`     29,416 4★ Common Ore `
`      1,667 4★ Uncommon Ore `
`        262 4★ Rare Ore `
`    111,486 4★ Common Explorer Parts `
`      8,362 4★ Uncommon Explorer Parts `
`     51,234 Ship XP `
Time: `14d 8h 0m`
Seconds: `1,238,400` **
* Scrap time is dependent on the level of your Scrapyard
* Tier total for Trit & Dil is based on all components upgraded
=====================================================
=====================================================
LCARS_COMMAND: !scrap d3 l45
-----------------------------------------------------
LCARS_RESPONSE:
Can Scrap? ` Yes `
Req. Lvl: ` 34 `
`  1,400,339 Dilithium `
` 36,307,500 Tritanium `
`     50,968 4★ Common Crystal `
`      2,889 4★ Uncommon Crystal `
`        454 4★ Rare Crystal `
`     27,444 4★ Common Gas `
`      1,556 4★ Uncommon Gas `
`        244 4★ Rare Gas `
`    104,555 4★ Common Interceptor Parts `
`      7,842 4★ Uncommon Interceptor Parts `
`     51,234 Ship XP `
Time: `14d 8h 0m`
Seconds: `1,238,400` **
* Scrap time is dependent on the level of your Scrapyard
* Tier total for Trit & Dil is based on all components upgraded
=====================================================
JSON file found:./raw-data/2021-07-05_dump_lcars/lcars-terminal-17 [697529046057222151].json
PARSE_FILE: ./raw-data/2021-07-05_dump_lcars/lcars-terminal-17 [697529046057222151].json
=====================================================
LCARS_COMMAND: ! mayflower t1 t3
-----------------------------------------------------
LCARS_RESPONSE:
Quantity: ` 80 `
Mayflower Blueprint: ` 125 each ` = ` 10,000 Total `
Shipyard: ` 26 `
Max Tiers: ` 9 `
Max Levels: ` 45 `
Can Scrap? ` Yes `
Req. Lvl: ` 34 `
` 6,030,000 Tritanium `
`   289,500 Dilithium `
`     2,420 3★ Common Gas `
`       123 3★ Uncommon Gas `
`       543 3★ Common Ore `
`        30 3★ Uncommon Ore `
`       848 3★ Explorer Parts `
`  74,200  `
```
                 Tiers
Component        Min Max Qty
-----------------------------
Energy Weapon      2   9   3
Cargo Bay          2   9   1
Warp Engine        2   9   1
Shield             2   9   1
-----------------------------
```
* **Ship Total Tiering Cost & Time** displayed are *base values only*. Buffs/Bonuses are player specific and *are not applied*.
=====================================================
=====================================================
LCARS_COMMAND: !upgrades list 31
-----------------------------------------------------
LCARS_RESPONSE:
```
                               Power
Name                   Increase     Actual
---------------------------------------------
Academy                   1,500     15,750
Armada Control Center     1,500     15,750
Astronautics Studio       1,500     15,750
Defense Platform A      102,800    801,587
Defense Platform B      102,800    801,587
Defense Platform C      102,800    801,587
Defense Platform D      102,800    801,587
Defense Platform E      102,800    801,587
Defense Platform F      102,800    801,587
Defense Technologies      1,500     15,750
---------------------------------------------
```
```
                               Power
Name                   Increase     Actual
---------------------------------------------
Dilithium Generator A       550      5,250
Dilithium Generator B       550      5,250
Dilithium Generator C       550      5,250
Dilithium Generator D       550      5,250
Dilithium Generator E       550      5,250
Dilithium Generator F       550      5,250
Dilithium Generator G       550      5,250
Dilithium Generator H       550      5,250
Dilithium Vault           2,000     21,000
Dilithium Warehouse       1,000     10,500
---------------------------------------------
```
```
                               Power
Name                   Increase     Actual
---------------------------------------------
Drydock A                 3,000     31,500
Drydock B                 3,000     31,500
Drydock C                 3,000     31,500
Drydock D                 3,000     31,500
Drydock E                 3,000     31,500
Drydock F                 3,000     31,500
Engine Technology Lab     1,500     15,750
Foundry                   1,500     15,750
Operations                3,000     31,500
Parsteel Generator A        550      5,250
---------------------------------------------
```
```
                               Power
Name                   Increase     Actual
---------------------------------------------
Parsteel Generator B        550      5,250
Parsteel Generator C        550      5,250
Parsteel Generator D        550      5,250
Parsteel Generator E        550      5,250
Parsteel Generator F        550      5,250
Parsteel Generator G        550      5,250
Parsteel Generator H        550      5,250
Parsteel Vault            2,000     21,000
Parsteel Warehouse        1,000     10,500
R&D Department            1,500     15,750
---------------------------------------------
```
```
                               Power
Name                   Increase     Actual
---------------------------------------------
Refinery                  1,500     15,750
Science Lab               1,500     15,750
Scrapyard                 1,000     10,500
Ship Hangar                 550      5,250
Shipyard                  1,000     10,500
Shuttle Bay               1,000     10,500
Tritanium Generator A       550      5,250
Tritanium Generator B       550      5,250
Tritanium Generator C       550      5,250
Tritanium Generator D       550      5,250
---------------------------------------------
```
```
                               Power
Name                   Increase     Actual
---------------------------------------------
Tritanium Generator E       550      5,250
Tritanium Generator F       550      5,250
Tritanium Generator G       550      5,250
Tritanium Generator H       550      5,250
Tritanium Vault           2,000     21,000
Tritanium Warehouse       1,000     10,500
---------------------------------------------
```
=====================================================
==========CONTINUED FROM ABOVE================
{'name': 'Legend', 'value': '***Power:*** \n` Increase ` = The difference between building levels\n` Actual ` = Total power for that level', 'isInline': False}
{'name': 'Note', 'value': 'For a list of abbreviation meanings, use command: ` !abbr `', 'isInline': False}
JSON file found:./raw-data/2021-07-05_dump_lcars/lcars-terminal-27 [697529046447161393] [part 6].json
PARSE_FILE: ./raw-data/2021-07-05_dump_lcars/lcars-terminal-27 [697529046447161393] [part 6].json
==========CONTINUED FROM ABOVE================
{'name': 'Build Costs', 'value': '`\xa08,110,800,000\xa0Tritanium\xa0`\n`\xa0\xa0\xa0278,900,000\xa0Dilithium\xa0`\n`\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa06,765\xa04★\xa0Uncommon\xa0Gas\xa0`\n`\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa03,120\xa04★\xa0Uncommon\xa0Ore\xa0`\n`\xa0\xa0\xa0\xa0\xa0\xa0\xa0192,325\xa04★\xa0Common\xa0Explorer\xa0Parts\xa0`\n`\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa015,860\xa04★\xa0Uncommon\xa0Explorer\xa0Parts\xa0`', 'isInline': False}
{'name': 'Repair Costs', 'value': '`\xa099,864,000\xa0Tritanium\xa0`\n`\xa0\xa02,289,500\xa0Dilithium\xa0`', 'isInline': False}
{'name': 'Quantity', 'value': '` 1 `', 'isInline': False}
{'name': 'Shield Health', 'value': '`  544,180  `', 'isInline': True}
{'name': 'Shield Deflection', 'value': '`  40,116  `', 'isInline': True}
=====================================================
LCARS_COMMAND: !ship korinar info t7
-----------------------------------------------------
LCARS_RESPONSE:
Loot the Weak
The Korinar gains 52% more resources from Hostiles.

Ship Abilities are always active.

**Ability Bonus by Level**
```
Level      Bonus
----------------
   31       52 %
   32       54 %
   33       56 %
   34       58 %
   35       60 %
----------------
```
Max Tiers: ` 12 `
Max Levels: ` 60 `
Can Scrap? ` No `
` 159,451,500,000 Tritanium `
`   6,655,900,000 Dilithium `
`         106,820 4★ Uncommon Gas `
`          41,105 4★ Rare Gas `
`          32,950 4★ Rare Ore `
`         941,765 4★ Common Explorer Parts `
`         254,655 4★ Uncommon Explorer Parts `
` 935,543,000 Tritanium `
`  25,472,125 Dilithium `
Time: `182d 7h 0m`
Seconds: `15,750,000` **
Time: `2d 8h 25m`
Seconds: `203,121` **
```
Level  XP Required
------------------
   31    1,825,000
   32    1,948,000
   33    2,075,000
   34    2,293,000
   35    2,433,000
------------------
```
* **Ship Total Tiering Cost & Time** displayed are *base values only*. Buffs/Bonuses are player specific and *are not applied*.
=====================================================
==========CONTINUED FROM ABOVE================
{'name': 'Build Costs', 'value': '`\xa023,917,700,000\xa0Tritanium\xa0`\n`\xa0\xa0\xa0\xa0998,400,000\xa0Dilithium\xa0`\n`\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa022,985\xa04★\xa0Uncommon\xa0Gas\xa0`\n`\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa06,085\xa04★\xa0Rare\xa0Gas\xa0`\n`\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa04,780\xa04★\xa0Rare\xa0Ore\xa0`\n`\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa038,175\xa04★\xa0Uncommon\xa0Explorer\xa0Parts\xa0`', 'isInline': False}
{'name': 'Repair Costs', 'value': '`\xa0112,361,500\xa0Tritanium\xa0`\n`\xa0\xa0\xa03,127,000\xa0Dilithium\xa0`', 'isInline': False}
{'name': 'Quantity', 'value': '` 1 `', 'isInline': False}
{'name': 'Min Damage', 'value': '`  78,382  `', 'isInline': True}
{'name': 'Max Damage', 'value': '`  94,057  `', 'isInline': True}
{'name': 'Accuracy', 'value': '`  99,869  `', 'isInline': True}
{'name': 'Armor Pierce', 'value': '`  12,983  `', 'isInline': True}
{'name': 'Shield Pierce', 'value': '`  9,987  `', 'isInline': True}
{'name': 'Crit Chance', 'value': '`  10.00 %  `', 'isInline': True}
{'name': 'Crit Modifier', 'value': '`  150.00 %  `', 'isInline': True}
{'name': 'Firing Pattern', 'value': '```\n     Rounds (sample)\n     1  2  3  4  5  6  7  8  9\n-------------------------------\nEN:  3  .  .  3  .  .  3  .  .\n-------------------------------\n```', 'isInline': False}
==========CONTINUED FROM ABOVE================
{'name': 'Build Costs', 'value': '`\xa047,835,500,000\xa0Tritanium\xa0`\n`\xa0\xa01,996,800,000\xa0Dilithium\xa0`\n`\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa045,705\xa04★\xa0Uncommon\xa0Gas\xa0`\n`\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa010,540\xa04★\xa0Rare\xa0Gas\xa0`\n`\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa06,340\xa04★\xa0Rare\xa0Ore\xa0`\n`\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa075,920\xa04★\xa0Uncommon\xa0Explorer\xa0Parts\xa0`', 'isInline': False}
{'name': 'Repair Costs', 'value': '`\xa0112,361,500\xa0Tritanium\xa0`\n`\xa0\xa0\xa03,127,000\xa0Dilithium\xa0`', 'isInline': False}
{'name': 'Quantity', 'value': '` 1 `', 'isInline': False}
{'name': 'Min Damage', 'value': '`  24,495  `', 'isInline': True}
{'name': 'Max Damage', 'value': '`  29,392  `', 'isInline': True}
{'name': 'Accuracy', 'value': '`  99,869  `', 'isInline': True}
{'name': 'Armor Pierce', 'value': '`  12,983  `', 'isInline': True}
{'name': 'Shield Pierce', 'value': '`  9,987  `', 'isInline': True}
{'name': 'Crit Chance', 'value': '`  10.00 %  `', 'isInline': True}
{'name': 'Crit Modifier', 'value': '`  150.00 %  `', 'isInline': True}
{'name': 'Firing Pattern', 'value': '```\n     Rounds (sample)\n     1  2  3  4  5  6  7  8  9\n-------------------------------\nEN:  2  2  2  2  2  2  2  2  2\n-------------------------------\n```', 'isInline': False}
JSON file found:./raw-data/2021-07-05_dump_lcars/lcars-terminal-14 [697529046057222147].json
PARSE_FILE: ./raw-data/2021-07-05_dump_lcars/lcars-terminal-14 [697529046057222147].json
=====================================================
LCARS_COMMAND: !operations 26
-----------------------------------------------------
LCARS_RESPONSE:
Shipyard (25)
Defense Platform C (25)
`  50  `
Actual: `18,000`
Increase: `2,000`
` 5,967,000 Parsteel `
`   109,688 Tritanium `
`    36,563 Dilithium `
`       860 3★ Common Ore `
`       120 3★ Uncommon Ore `
Time: `15d 14h 0m`
Seconds: `1,346,400` **
Weapon Damage Bonus: `26 %`
` 100 Latinum `
`   2 1 Day Peace Shield `
`   3 15 Hour Speed Up `
* **Build Cost & time** displayed are *base values only*. Buffs/Bonuses are player specific and *are not applied*.  Use `!upgrade faq` for information on how to calculate the buff adjustments.
=====================================================
=====================================================
LCARS_COMMAND: !operations 27
-----------------------------------------------------
LCARS_RESPONSE:
Foundry (26)
Shipyard (26)
`  50  `
Actual: `20,500`
Increase: `2,500`
` 9,106,560 Parsteel `
`   167,400 Tritanium `
`    55,800 Dilithium `
`     1,030 3★ Common Ore `
`       170 3★ Uncommon Ore `
Time: `17d 18h 0m`
Seconds: `1,533,600` **
Weapon Damage Bonus: `27 %`
`   2 1 Day Peace Shield `
`   3 15 Hour Speed Up `
` 100 Latinum `
* **Build Cost & time** displayed are *base values only*. Buffs/Bonuses are player specific and *are not applied*.  Use `!upgrade faq` for information on how to calculate the buff adjustments.
=====================================================
=====================================================
LCARS_COMMAND: !operations 26 27
-----------------------------------------------------
LCARS_RESPONSE:
Operations (27)
Foundry (26)
R&D Department (26)
Academy (26)
Shipyard (26)
Astronautics Studio (26)
Operations (26)
Shipyard (25)
Drydock C (25)
R&D Department (25)
Dilithium Warehouse (25)
Dilithium Generator A (25)
Tritanium Warehouse (25)
Tritanium Generator A (25)
Parsteel Warehouse (25)
Parsteel Generator A (25)
Academy (25)
Drydock B (25)
Drydock A (25)
Defense Platform C (25)
Defense Technologies (25)
Science Lab (25)
Engine Technology Lab (25)
Foundry (25)
` 70,168,860 Parsteel `
`  2,150,551 Tritanium `
`    301,501 Dilithium `
`      1,980 3★ Common Crystal `
`        207 3★ Uncommon Crystal `
`      1,980 3★ Common Gas `
`        209 3★ Uncommon Gas `
`      2,310 3★ Common Ore `
`        303 3★ Uncommon Ore `
Actual: `571,722`
Increase: `53,550`
Time: `95d 10h 24m`
Seconds: `8,245,440` **
`   4 1 Day Peace Shield `
`   6 15 Hour Speed Up `
` 200 Latinum `
` 200 Premium Recruit Token `
` 400 Ultra Recruit Token `
* **Build Cost & time** displayed are *base values only*. Buffs/Bonuses are player specific and *are not applied*.  Use `!upgrade faq` for information on how to calculate the buff adjustments.
=====================================================
JSON file found:./raw-data/2021-07-05_dump_lcars/lcars-terminal-7 [697529045562163275].json
PARSE_FILE: ./raw-data/2021-07-05_dump_lcars/lcars-terminal-7 [697529045562163275].json
=====================================================
LCARS_COMMAND: ! officers kahn t3
-----------------------------------------------------
LCARS_RESPONSE:
**50%** chances to drastically reduce the opponent's station and ships Mitigation for 2 rounds
```
Command:        10 %
Engineering:    25 %
Science:        25 %
```
+% to Critical Hit chances every time the ship gets hit
```
Rank:       1      2      3      4      5
Value:     1%     2%     3%     4%     5%
```
```
Lvl    Atk    Def     HP      Str       XP
---------------------------------+--------
 11    679    113    415    4,828   120.0K
 12    745    124    455    5,296   150.0K
 13    814    136    497    5,788   174.0K
 14    885    147    541    6,292   192.0K
 15    958    160    585    6,812   198.0K
---------------------------------+--------
 * XP = Officer XP
```
=====================================================
=====================================================
LCARS_COMMAND: !officers kahn
-----------------------------------------------------
LCARS_RESPONSE:
**50%** chances to drastically reduce the opponent's station and ships Mitigation for 2 rounds
```
Command:        10 %
Engineering:    25 %
Science:        25 %
```
+% to Critical Hit chances every time the ship gets hit
```
Rank:       1      2      3      4      5
Value:     1%     2%     3%     4%     5%
```
```
                          Promotion Req
# Rank        MX    SH    IND     XP CB
----------------------+----------------
1 Ensign I     5   110                     
2 Lt. JG II   10   110  1,150 50,000       
3 Lt. III     15   220  4,600 500.0K  1
4 Lt. Cmdr IV 20   330 11,500  1.25M  2
5 Commander V 30   880 25,300   2.5M  4
----------------------+----------------
```
 * MX = maximum level
 * SH = shards required
 * IND/ROM/FED/KLI/AUG = independent/faction credits
 * XP = officer experience points
* CB = Command Badges
=====================================================
JSON file found:./raw-data/2021-07-05_dump_lcars/lcars-terminal-27 [697529046447161393] [part 4].json
PARSE_FILE: ./raw-data/2021-07-05_dump_lcars/lcars-terminal-27 [697529046447161393] [part 4].json
=====================================================
LCARS_COMMAND: !r outlaw dilithium upgrades 8
-----------------------------------------------------
LCARS_RESPONSE:
R&D Department (50)
NIL
`  10  `
Outlaw
Column: `  29  `
Row: `  3  `
`          6,400 Outlaw Research Credits `
` 28,917,000,000 Parsteel `
`  7,088,000,000 Dilithium `
`          7,800 4★ Uncommon Crystal `
`          2,860 4★ Rare Crystal `
Time: `3,509d 16h 39m`
Seconds: `303,237,540` **
Actual: `150,000`
Increase: `9,000`
`32.00 %`
NIL
* **Research Cost & time** displayed are *base values only*. Buffs/Bonuses are player specific and *are not applied*.  Use `!research faq` for information on how to calculate the buff adjustments.
=====================================================
=====================================================
LCARS_COMMAND: !r outlaw dilithium upgrades 9
-----------------------------------------------------
LCARS_RESPONSE:
R&D Department (51)
NIL
`  10  `
Outlaw
Column: `  29  `
Row: `  3  `
`          6,500 Outlaw Research Credits `
` 44,018,000,000 Parsteel `
` 10,789,000,000 Dilithium `
Time: `4,280d 20h 46m`
Seconds: `369,866,760` **
Actual: `161,000`
Increase: `11,000`
`36.00 %`
NIL
* **Research Cost & time** displayed are *base values only*. Buffs/Bonuses are player specific and *are not applied*.  Use `!research faq` for information on how to calculate the buff adjustments.
=====================================================
JSON file found:./raw-data/2021-07-05_dump_lcars/lcars-terminal-29 [697529046875111465].json
PARSE_FILE: ./raw-data/2021-07-05_dump_lcars/lcars-terminal-29 [697529046875111465].json
=====================================================
LCARS_COMMAND: !bortas max
-----------------------------------------------------
LCARS_RESPONSE:
Revenge
When defending the Station, The BORTAS increases the damage of all the other ships and Defense Platforms by 10%.

Ship Abilities are always active.

**Ability Bonus by Level**
```
Level      Bonus
----------------
    1       10 %
    2       10 %
    3       11 %
    4       11 %
    5       12 %
----------------
```
Quantity: ` 100 `
Bortas Class Blueprint: ` 200 each ` = ` 20,000 Total `
Shipyard: ` 28 `
Max Tiers: ` 9 `
Max Levels: ` 45 `
Can Scrap? ` Yes `
Req. Lvl: ` 42 `
` 1,900,000 Tritanium `
`    42,500 Dilithium `
`       275 3★ Common Crystal `
`     2,200 3★ Common Ore `
` 52,640 Tritanium `
`  1,522 Dilithium `
Time: `17d 0h 0m`
Seconds: `1,468,800` **
Time: `8h 20m`
Seconds: `30,000` **
```
Level  XP Required
------------------
    2          800
    3        1,000
    4        1,400
    5        1,700
------------------
```
```
                 Tiers
Component        Min Max Qty
-----------------------------
Energy Weapon      2   9   1
Kinetic Weapon     2   9   2
Cargo Bay          2   9   1
Warp Engine        2   9   1
Armor              2   9   1
-----------------------------
```
* **Ship Total Tiering Cost & Time** displayed are *base values only*. Buffs/Bonuses are player specific and *are not applied*.
=====================================================
=====================================================
LCARS_COMMAND: ! sally t8
-----------------------------------------------------
LCARS_RESPONSE:
Protector
When the Station or the USS SALADIN gets attacked, it increases the Shield Health of all the ships and Defense Platforms by 34%.

Ship Abilities are always active.

**Ability Bonus by Level**
```
Level      Bonus
----------------
   36       34 %
   37       34 %
   38       35 %
   39       35 %
   40       36 %
----------------
```
Max Tiers: ` 9 `
Max Levels: ` 45 `
Can Scrap? ` Yes `
Req. Lvl: ` 42 `
` 186,700,000 Tritanium `
`   4,280,000 Dilithium `
`       1,000 3★ Uncommon Crystal `
`         350 3★ Rare Crystal `
`         900 3★ Uncommon Gas `
`          72 3★ Rare Gas `
`      11,400 3★ Interceptor Parts `
` 535,481 Tritanium `
`  59,380 Dilithium `
Time: `30d 2h 13m`
Seconds: `2,600,000` **
Time: `22h 45m`
Seconds: `81,916` **
```
Level  XP Required
------------------
   36      105,000
   37      116,000
   38      122,000
   39      134,000
   40      140,000
------------------
```
* **Ship Total Tiering Cost & Time** displayed are *base values only*. Buffs/Bonuses are player specific and *are not applied*.
=====================================================
=====================================================
LCARS_COMMAND: ! sally t9
-----------------------------------------------------
LCARS_RESPONSE:
Protector
When the Station or the USS SALADIN gets attacked, it increases the Shield Health of all the ships and Defense Platforms by 36%.

Ship Abilities are always active.

**Ability Bonus by Level**
```
Level      Bonus
----------------
   41       36 %
   42       37 %
   43       37 %
   44       38 %
   45       40 %
----------------
```
Max Tiers: ` 9 `
Max Levels: ` 45 `
Can Scrap? ` Yes `
Req. Lvl: ` 42 `
` 297,000,000 Tritanium `
`   7,000,000 Dilithium `
`       1,700 3★ Uncommon Crystal `
`         590 3★ Rare Crystal `
`         163 3★ Rare Gas `
`      17,200 3★ Interceptor Parts `
` 818,828 Tritanium `
` 105,124 Dilithium `
Time: `37d 0h 53m`
Seconds: `3,200,000` **
Time: `1d 2h 53m`
Seconds: `96,834` **
```
Level  XP Required
------------------
   41      154,000
   42      161,000
   43      176,000
   44      183,000
   45      200,000
------------------
```
* **Ship Total Tiering Cost & Time** displayed are *base values only*. Buffs/Bonuses are player specific and *are not applied*.
=====================================================
JSON file found:./raw-data/2021-07-05_dump_lcars/lcars-terminal-32 [697529046875111468] [part 2].json
PARSE_FILE: ./raw-data/2021-07-05_dump_lcars/lcars-terminal-32 [697529046875111468] [part 2].json
==========CONTINUED FROM ABOVE================
{'name': 'Requirements', 'value': 'Tritanium Generator B (30)\nOperations (30)', 'isInline': True}
{'name': 'Levels', 'value': '`  50  `', 'isInline': True}
{'name': 'Power', 'value': 'Actual: `4,700`\nIncrease: `400`', 'isInline': True}
{'name': 'Build Cost', 'value': '`\xa013,260,000\xa0Parsteel\xa0`\n`\xa0\xa0\xa0\xa0\xa078,000\xa0Dilithium\xa0`', 'isInline': False}
{'name': 'Build Time', 'value': 'Time:\xa0`1d\xa023h\xa012m`\nSeconds:\xa0`169,920`\xa0**', 'isInline': True}
{'name': 'Bonuses', 'value': 'Tritanium Production: `820`\n    Tritanium Storage: `11,500`', 'isInline': True}
{'name': 'Rewards', 'value': 'NIL', 'isInline': False}
{'name': '**NOTE:**', 'value': '* **Build Cost & time** displayed are *base values only*. Buffs/Bonuses are player specific and *are not applied*.  Use `!upgrade faq` for information on how to calculate the buff adjustments.', 'isInline': False}
=====================================================
LCARS_COMMAND: !shipyard 47
-----------------------------------------------------
LCARS_RESPONSE:
R&D Department (47)
Operations (47)
`  50  `
Actual: `41,000`
Increase: `3,000`
` 47,736,000,000 Parsteel `
`    390,000,000 Tritanium `
`         12,000 4★ Uncommon Crystal `
`          8,000 4★ Rare Crystal `
Time: `1,007d 2h 48m`
Seconds: `87,014,880` **
Tier Up Speed: `149 %`
    Ship Construction Speed: `149 %`
NIL
* **Build Cost & time** displayed are *base values only*. Buffs/Bonuses are player specific and *are not applied*.  Use `!upgrade faq` for information on how to calculate the buff adjustments.
=====================================================
=====================================================
LCARS_COMMAND: !upg trit gen 29
-----------------------------------------------------
LCARS_RESPONSE:
Operations (29)
`  50  `
Actual: `4,300`
Increase: `500`
` 9,061,000 Parsteel `
`    53,300 Dilithium `
Time: `1d 19h 36m`
Seconds: `156,960` **
Tritanium Production: `710`
    Tritanium Storage: `9,900`
NIL
* **Build Cost & time** displayed are *base values only*. Buffs/Bonuses are player specific and *are not applied*.  Use `!upgrade faq` for information on how to calculate the buff adjustments.
=====================================================
JSON file found:./raw-data/2021-07-05_dump_lcars/lcars-terminal-27 [697529046447161393] [part 3].json
PARSE_FILE: ./raw-data/2021-07-05_dump_lcars/lcars-terminal-27 [697529046447161393] [part 3].json
=====================================================
LCARS_COMMAND: !r galaxy parsteel hunter 10
-----------------------------------------------------
LCARS_RESPONSE:
Parsteel Miner (12)
Dilithium Warehouse (32)
Dilithium Hunter (10)
`  10  `
Galaxy
Column: `  6  `
Row: `  1  `
` 2,400,000 Dilithium `
`     2,500 3★ Common Ore `
`       150 3★ Uncommon Ore `
`        15 3★ Rare Ore `
Time: `9d 1h 27m`
Seconds: `782,820` **
Actual: `17,500`
Increase: `1,750`
`125.00 %`
NIL
* **Research Cost & time** displayed are *base values only*. Buffs/Bonuses are player specific and *are not applied*.  Use `!research faq` for information on how to calculate the buff adjustments.
=====================================================
=====================================================
LCARS_COMMAND: !r galaxy tritanium hunter 6
-----------------------------------------------------
LCARS_RESPONSE:
Dilithium Hunter (6)
R&D Department (28)
Tritanium Miner (8)
`  10  `
Galaxy
Column: `  6  `
Row: `  2  `
` 448,000 Dilithium `
`   2,000 3★ Common Crystal `
Time: `5d 8h 24m`
Seconds: `462,240` **
Actual: `11,500`
Increase: `1,250`
`53.00 %`
NIL
* **Research Cost & time** displayed are *base values only*. Buffs/Bonuses are player specific and *are not applied*.  Use `!research faq` for information on how to calculate the buff adjustments.
=====================================================
JSON file found:./raw-data/2021-07-05_dump_lcars/lcars-terminal-31 [697529046875111467].json
PARSE_FILE: ./raw-data/2021-07-05_dump_lcars/lcars-terminal-31 [697529046875111467].json
=====================================================
LCARS_COMMAND: !ship saladin warp
-----------------------------------------------------
LCARS_RESPONSE:
=====================================================
=====================================================
LCARS_COMMAND: !ship vidar t8
-----------------------------------------------------
LCARS_RESPONSE:
Cybernetic Augmentation The Vi'dar's Damage is increased by 32750% against Borg hostiles.

Ship Abilities are always active.

**Ability Bonus by Level**
```
Level      Bonus
----------------
   36   32,750 %
   37   33,000 %
   38   33,250 %
   39   33,500 %
   40   33,750 %
----------------
```
Max Tiers: ` 9 `
Max Levels: ` 45 `
Can Scrap? ` No `
` 61,260,499 Tritanium `
`  1,750,300 Dilithium `
`        707 3★ Uncommon Crystal `
`         78 3★ Rare Crystal `
`        164 3★ Uncommon Gas `
`         18 3★ Rare Gas `
`      4,377 3★ Interceptor Parts `
`    284,420 Charged Nanoprobe `
` 249,600 Tritanium `
`   5,615 Dilithium `
Time: `12d 20h 45m`
Seconds: `1,111,500` **
Time: `9h 29m`
Seconds: `34,142` **
```
Level  XP Required
------------------
   36      105,000
   37      116,000
   38      122,000
   39      134,000
   40      140,000
------------------
```
* **Ship Total Tiering Cost & Time** displayed are *base values only*. Buffs/Bonuses are player specific and *are not applied*.
=====================================================
=====================================================
LCARS_COMMAND: !ship vidar t9
-----------------------------------------------------
LCARS_RESPONSE:
Cybernetic Augmentation The Vi'dar's Damage is increased by 34000% against Borg hostiles.

Ship Abilities are always active.

**Ability Bonus by Level**
```
Level      Bonus
----------------
   41   34,000 %
   42   34,250 %
   43   34,500 %
   44   34,750 %
   45   35,000 %
----------------
```
Max Tiers: ` 9 `
Max Levels: ` 45 `
Can Scrap? ` No `
` 102,650,626 Tritanium `
`   2,932,874 Dilithium `
`         947 3★ Uncommon Crystal `
`         105 3★ Rare Crystal `
`         220 3★ Uncommon Gas `
`          21 3★ Rare Gas `
`       5,866 3★ Interceptor Parts `
`     662,830 Charged Nanoprobe `
` 422,400 Tritanium `
`   9,503 Dilithium `
Time: `15d 20h 0m`
Seconds: `1,368,000` **
Time: `11h 23m`
Seconds: `40,982` **
```
Level  XP Required
------------------
   41      154,000
   42      161,000
   43      176,000
   44      183,000
   45      200,000
------------------
```
* **Ship Total Tiering Cost & Time** displayed are *base values only*. Buffs/Bonuses are player specific and *are not applied*.
=====================================================
JSON file found:./raw-data/2021-07-05_dump_lcars/lcars-terminal-13 [697529046057222146].json
PARSE_FILE: ./raw-data/2021-07-05_dump_lcars/lcars-terminal-13 [697529046057222146].json
=====================================================
LCARS_COMMAND: !augur t5
-----------------------------------------------------
LCARS_RESPONSE:
Obliterate
As long as the opponent's ship is Burning, if the opponent is hit with the Obliterator weapon, the AUGUR increases all weapon damage by 90.00% (cumulative).

Ship Abilities are always active.

**Ability Bonus by Level**
```
Level      Bonus
----------------
   21       90 %
   22       92 %
   23       94 %
   24       96 %
   25       98 %
----------------
```
Max Tiers: ` 9 `
Max Levels: ` 45 `
Can Scrap? ` Yes `
Req. Lvl: ` 50 `
` 479,800,000 Tritanium `
`  17,550,000 Dilithium `
`       7,500 3★ Common Crystal `
`       2,125 3★ Uncommon Crystal `
`       8,250 3★ Common Ore `
`      10,000 3★ Uncommon Ore `
`      10,825 3★ Battleship Parts `
` 748,962 Tritanium `
`  66,442 Dilithium `
Time: `36d 11h 0m`
Seconds: `3,150,000` **
Time: `1d 10h 0m`
Seconds: `122,445` **
```
Level  XP Required
------------------
   21       29,000
   22       31,500
   23       36,000
   24       39,000
   25       42,000
------------------
```
* **Ship Total Tiering Cost & Time** displayed are *base values only*. Buffs/Bonuses are player specific and *are not applied*.
=====================================================
=====================================================
LCARS_COMMAND: !franklin t1-7
-----------------------------------------------------
LCARS_RESPONSE:
Sabotage

When fighting Swarm ships, The Franklin's Damage is increased by 4800%

Ship Abilities are always active.

**Ability Bonus by Level**
```
Level      Bonus
----------------
    1    4,800 %
    2    4,860 %
    3    4,900 %
    4    4,960 %
    5    5,000 %
----------------
```
Quantity: ` 90 `
Shipyard: ` 17 `
Max Tiers: ` 9 `
Max Levels: ` 45 `
Can Scrap? ` Yes `
Req. Lvl: ` 35 `
```
Tier   1  2  3  4  5  6  7  8  9
Level 17 18 19 22 24 26 28 30 32
```
` 35,000 Tritanium `
`  1,400 Dilithium `
`     50 2★ Common Gas `
`    300 Frequency Modulators `
` 412 Tritanium `
`  28 Dilithium `
Time: `18h 0m`
Seconds: `64,800` **
Time: `28m`
Seconds: `1,722` **
```
Level  XP Required
------------------
    2          800
    3        1,000
    4        1,400
    5        1,700
------------------
```
```
                 Tiers
Component        Min Max Qty
-----------------------------
Energy Weapon      2   9   3
Cargo Bay          2   9   1
Warp Engine        2   9   1
Shield             2   9   1
-----------------------------
```
* **Ship Total Tiering Cost & Time** displayed are *base values only*. Buffs/Bonuses are player specific and *are not applied*.
=====================================================
=====================================================
LCARS_COMMAND: !franklin t7
-----------------------------------------------------
LCARS_RESPONSE:
Sabotage

When fighting Swarm ships, The Franklin's Damage is increased by 17650%

Ship Abilities are always active.

**Ability Bonus by Level**
```
Level      Bonus
----------------
   31   17,650 %
   32   18,450 %
   33   19,250 %
   34   20,050 %
   35   20,850 %
----------------
```
Max Tiers: ` 9 `
Max Levels: ` 45 `
Can Scrap? ` Yes `
Req. Lvl: ` 35 `
```
Tier   1  2  3  4  5  6  7  8  9
Level 17 18 19 22 24 26 28 30 32
```
` 10,200,000 Tritanium `
`    734,000 Dilithium `
`        400 3★ Common Crystal `
`      1,100 3★ Common Gas `
`      4,210 3★ Explorer Parts `
`  2,450,000 Frequency Modulators `
`          1 Franklin Warp Containment `
` 76,210 Tritanium `
` 12,356 Dilithium `
Time: `1d 17h 40m`
Seconds: `150,000` **
Time: `4h 31m`
Seconds: `16,302` **
```
Level  XP Required
------------------
   31       72,000
   32       81,000
   33       86,000
   34       95,000
   35      100,000
------------------
```
* **Ship Total Tiering Cost & Time** displayed are *base values only*. Buffs/Bonuses are player specific and *are not applied*.
=====================================================
JSON file found:./raw-data/2021-07-05_dump_lcars/lcars-terminal-9 [697529045562163278].json
PARSE_FILE: ./raw-data/2021-07-05_dump_lcars/lcars-terminal-9 [697529045562163278].json
=====================================================
LCARS_COMMAND: !upg d3 t6 t7
-----------------------------------------------------
LCARS_RESPONSE:
Quantity: ` 80 `
D3 Blueprint: ` 125 each ` = ` 10,000 Total `
Shipyard: ` 26 `
Max Tiers: ` 9 `
Max Levels: ` 45 `
Can Scrap? ` Yes `
Req. Lvl: ` 34 `
` 79,100,000 Tritanium `
`  1,978,000 Dilithium `
`      5,600 3★ Common Crystal `
`      1,750 3★ Uncommon Crystal `
`         96 3★ Rare Crystal `
`        655 3★ Uncommon Gas `
`         22 3★ Rare Gas `
`      8,355 3★ Interceptor Parts `
`  719,000  `
```
                 Tiers
Component        Min Max Qty
-----------------------------
Kinetic Weapon     2   9   2
Cargo Bay          2   9   1
Warp Engine        2   9   1
Impulse Engine     2   9   1
-----------------------------
```
* **Ship Total Tiering Cost & Time** displayed are *base values only*. Buffs/Bonuses are player specific and *are not applied*.
=====================================================
=====================================================
LCARS_COMMAND: !upg d3 t7 t8
-----------------------------------------------------
LCARS_RESPONSE:
Quantity: ` 80 `
D3 Blueprint: ` 125 each ` = ` 10,000 Total `
Shipyard: ` 26 `
Max Tiers: ` 9 `
Max Levels: ` 45 `
Can Scrap? ` Yes `
Req. Lvl: ` 34 `
` 154,950,000 Tritanium `
`   3,980,000 Dilithium `
`       3,900 3★ Common Crystal `
`       1,875 3★ Uncommon Crystal `
`         326 3★ Rare Crystal `
`       1,055 3★ Uncommon Gas `
`          71 3★ Rare Gas `
`      16,500 3★ Interceptor Parts `
`  1,051,000  `
```
                 Tiers
Component        Min Max Qty
-----------------------------
Kinetic Weapon     2   9   2
Cargo Bay          2   9   1
Warp Engine        2   9   1
Impulse Engine     2   9   1
-----------------------------
```
* **Ship Total Tiering Cost & Time** displayed are *base values only*. Buffs/Bonuses are player specific and *are not applied*.
=====================================================
=====================================================
LCARS_COMMAND: !upg d3 t8 t9
-----------------------------------------------------
LCARS_RESPONSE:
Quantity: ` 80 `
D3 Blueprint: ` 125 each ` = ` 10,000 Total `
Shipyard: ` 26 `
Max Tiers: ` 9 `
Max Levels: ` 45 `
Can Scrap? ` Yes `
Req. Lvl: ` 34 `
` 256,700,000 Tritanium `
`   6,800,000 Dilithium `
`       1,750 3★ Uncommon Crystal `
`         670 3★ Rare Crystal `
`         600 3★ Uncommon Gas `
`         170 3★ Rare Gas `
`      26,950 3★ Interceptor Parts `
`  1,491,000  `
```
                 Tiers
Component        Min Max Qty
-----------------------------
Kinetic Weapon     2   9   2
Cargo Bay          2   9   1
Warp Engine        2   9   1
Impulse Engine     2   9   1
-----------------------------
```
* **Ship Total Tiering Cost & Time** displayed are *base values only*. Buffs/Bonuses are player specific and *are not applied*.
=====================================================
JSON file found:./raw-data/2021-07-05_dump_lcars/lcars-terminal-5 [697529045562163273].json
PARSE_FILE: ./raw-data/2021-07-05_dump_lcars/lcars-terminal-5 [697529045562163273].json
=====================================================
LCARS_COMMAND: ! enterprise t8?
-----------------------------------------------------
LCARS_RESPONSE:
Giving what she's got
As long as the ship has Morale, the USS ENTERPRISE heals the Shield Health by 20% whenever it gets hit.

Ship Abilities are always active.

**Ability Bonus by Level**
```
Level      Bonus
----------------
   36       20 %
   37       20 %
   38       21 %
   39       21 %
   40       22 %
----------------
```
Max Tiers: ` 9 `
Max Levels: ` 45 `
Can Scrap? ` Yes `
Req. Lvl: ` 50 `
` 2,880,000,000 Tritanium `
`   192,100,000 Dilithium `
`         6,500 3★ Uncommon Gas `
`         3,325 3★ Rare Gas `
`         6,000 3★ Uncommon Ore `
`           740 3★ Rare Ore `
`        93,350 3★ Explorer Parts `
` 1,742,675 Tritanium `
`   431,497 Dilithium `
Time: `78d 23h 50m`
Seconds: `6,825,000` **
Time: `2d 0h 2m`
Seconds: `172,979` **
```
Level  XP Required
------------------
   36      105,000
   37      116,000
   38      122,000
   39      134,000
   40      140,000
------------------
```
* **Ship Total Tiering Cost & Time** displayed are *base values only*. Buffs/Bonuses are player specific and *are not applied*.
=====================================================
=====================================================
LCARS_COMMAND: ! enterprise t9?
-----------------------------------------------------
LCARS_RESPONSE:
Giving what she's got
As long as the ship has Morale, the USS ENTERPRISE heals the Shield Health by 22% whenever it gets hit.

Ship Abilities are always active.

**Ability Bonus by Level**
```
Level      Bonus
----------------
   41       22 %
   42       23 %
   43       23 %
   44       24 %
   45       25 %
----------------
```
Max Tiers: ` 9 `
Max Levels: ` 45 `
Can Scrap? ` Yes `
Req. Lvl: ` 50 `
` 4,114,000,000 Tritanium `
`   284,500,000 Dilithium `
`        11,000 3★ Uncommon Gas `
`         5,700 3★ Rare Gas `
`         1,505 3★ Rare Ore `
`       140,750 3★ Explorer Parts `
` 2,795,310 Tritanium `
`   824,548 Dilithium `
Time: `97d 5h 20m`
Seconds: `8,400,000` **
Time: `2d 4h 35m`
Seconds: `189,300` **
```
Level  XP Required
------------------
   41      154,000
   42      161,000
   43      176,000
   44      183,000
   45      200,000
------------------
```
* **Ship Total Tiering Cost & Time** displayed are *base values only*. Buffs/Bonuses are player specific and *are not applied*.
=====================================================
=====================================================
LCARS_COMMAND: ! hydra t2?
-----------------------------------------------------
LCARS_RESPONSE:
Gas Mining Laser
The Mining Rate of Gas is increased by 138%.

Ship Abilities are always active.

**Ability Bonus by Level**
```
Level      Bonus
----------------
    6   138.00 %
    7   141.00 %
    8   144.00 %
    9   147.00 %
   10   150.00 %
----------------
```
Max Tiers: ` 12 `
Max Levels: ` 60 `
Can Scrap? ` No `
` 480,000,000 Tritanium `
`  19,300,000 Dilithium `
`       9,770 4★ Common Gas `
`       5,720 4★ Common Ore `
`      22,685 4★ Common Survey Parts `
` 41,595,000 Tritanium `
`  1,244,000 Dilithium `
Time: `10d 22h 30m`
Seconds: `945,000` **
Time: `1d 3h 14m`
Seconds: `98,086` **
```
Level  XP Required
------------------
    6       41,000
    7       59,000
    8       78,000
    9      100,000
   10      130,000
------------------
```
* **Ship Total Tiering Cost & Time** displayed are *base values only*. Buffs/Bonuses are player specific and *are not applied*.
=====================================================
JSON file found:./raw-data/2021-07-05_dump_lcars/lcars-terminal-32 [697529046875111468].json
PARSE_FILE: ./raw-data/2021-07-05_dump_lcars/lcars-terminal-32 [697529046875111468].json
=====================================================
LCARS_COMMAND: !mission “angel in disguise”
-----------------------------------------------------
LCARS_RESPONSE:
Escort a Romulan fleet through dangerous space.
`  Auto  Link / Continuation  `
>>> **Objective  -  Travel to:**
:small_blue_diamond: Destination: ` Beta Niobe (43) `  -  Warp: ` 80 `
>>> **Objective  -  Travel to:**
:small_blue_diamond: Destination: ` Stradania (42) `  -  Warp: ` 70 `
>>> **Objective  -  Travel to:**
:small_blue_diamond: Destination: ` Nikola (41) `  -  Warp: ` 56 `
>>> **Objective  -  Kill Hostile Ships:**
:small_red_triangle: Defeat 18 hostiles of level 40 or higher.
>>> **Objective  -  Travel to:**
:small_blue_diamond: Destination: ` Mina (40) `  -  Warp: ` 56 `
>>> **Objective  -  Destroy Hostile Target:**
:small_blue_diamond: Destination: ` Mina (40) `  -  Warp: ` 56 `
:small_orange_diamond: Destroy Vulcan Explorer
>>> **Objective  -  Travel to:**
:small_blue_diamond: Destination: ` Vola (41) `  -  Warp: ` 70 `
`      1 Warp Particle`
`     24 1 Hour Repair Speed Up`
`  9.45M Tritanium`
The Tables Turn
Due Process
=====================================================
=====================================================
LCARS_COMMAND: !mission “the tables turn”
-----------------------------------------------------
LCARS_RESPONSE:
Investigate another distress signal.
`  Auto  Link / Continuation  `
>>> **Objective  -  Travel to:**
:small_blue_diamond: Destination: ` Hannlaw (44) `  -  Warp: ` 90 `
>>> **Objective  -  Destroy Hostile Target:**
:small_blue_diamond: Destination: ` Hannlaw (44) `  -  Warp: ` 90 `
:small_orange_diamond: Destroy Vulcan Explorer
>>> **Objective  -  Destroy Hostile Target:**
:small_blue_diamond: Destination: ` Hannlaw (44) `  -  Warp: ` 90 `
:small_orange_diamond: Destroy Vulcan Battleship
>>> **Objective  -  Travel to:**
:small_blue_diamond: Destination: ` Rowla (40) `  -  Warp: ` 64 `
>>> **Objective  -  Destroy Hostile Target:**
:small_blue_diamond: Destination: ` Rowla (40) `  -  Warp: ` 64 `
:small_orange_diamond: Destroy Vulcan Captain
`    500 4★ Common Battleship Parts`
`    500 4★ Common Explorer Parts`
`    500 4★ Common Interceptor Parts`
Reality Sinks In
Angel In Disguise
=====================================================
=====================================================
LCARS_COMMAND: !mission “reality sinks in”
-----------------------------------------------------
LCARS_RESPONSE:
Witness the aftermath of the Vulcan attacks.
`  Auto  Link / Continuation  `
>>> **Objective  -  Travel to:**
:small_blue_diamond: Destination: ` Ortexa (41) `  -  Warp: ` 75 `
>>> **Objective  -  Travel to:**
:small_blue_diamond: Destination: ` Ortexa (41) `  -  Warp: ` 75 `
>>> **Objective  -  Choose:**
:regional_indicator_a: Improve their defenses.
:regional_indicator_b: Destroy the bandits.
>>> **Objective  -  Deliver:**
:small_blue_diamond: `  1  ` x `  Parsteel  `
>>> **Objective  -  Return:**
:small_blue_diamond: Return your ship to your station.
`    100 4★ Uncommon Gas`
`    190 4★ Uncommon Survey Parts`
>>> **Objective  -  Destroy Hostile Target:**
:small_blue_diamond: Destination: ` Ortexa (41) `  -  Warp: ` 75 `
:small_orange_diamond: Destroy Bandit
>>> **Objective  -  Destroy Hostile Target:**
:small_blue_diamond: Destination: ` Ortexa (41) `  -  Warp: ` 75 `
:small_orange_diamond: Destroy Bandit Leader
>>> **Objective  -  Return:**
:small_blue_diamond: Return your ship to your station.
`  58.8M Parsteel`
`  8.82M Tritanium`
Middle Ground
The Tables Turn
=====================================================
JSON file found:./raw-data/2021-07-05_dump_lcars/lcars-terminal-18 [697529046057222152].json
PARSE_FILE: ./raw-data/2021-07-05_dump_lcars/lcars-terminal-18 [697529046057222152].json
=====================================================
LCARS_COMMAND: !ent t1
-----------------------------------------------------
LCARS_RESPONSE:
Giving what she's got
As long as the ship has Morale, the USS ENTERPRISE heals the Shield Health by 5% whenever it gets hit.

Ship Abilities are always active.

**Ability Bonus by Level**
```
Level      Bonus
----------------
    1        5 %
    2        5 %
    3        5 %
    4        6 %
    5        6 %
----------------
```
Quantity: ` 150 `
Enterprise Class Blueprint: ` 1,200 each ` = ` 180.0K Total `
Shipyard: ` 34 `
Max Tiers: ` 9 `
Max Levels: ` 45 `
Can Scrap? ` Yes `
Req. Lvl: ` 50 `
` 6,000,000 Tritanium `
`   300,000 Dilithium `
`     8,250 3★ Common Gas `
`     1,375 3★ Common Ore `
` 340,200 Tritanium `
`   5,103 Dilithium `
Time: `34d 12h 0m`
Seconds: `2,980,800` **
Time: `23h 22m`
Seconds: `84,162` **
```
Level  XP Required
------------------
    2          800
    3        1,000
    4        1,400
    5        1,700
------------------
```
```
                 Tiers
Component        Min Max Qty
-----------------------------
Energy Weapon      2   9   3
Cargo Bay          2   9   1
Warp Engine        2   9   1
Shield             2   9   1
-----------------------------
```
* **Ship Total Tiering Cost & Time** displayed are *base values only*. Buffs/Bonuses are player specific and *are not applied*.
=====================================================
=====================================================
LCARS_COMMAND: !ent t2
-----------------------------------------------------
LCARS_RESPONSE:
Giving what she's got
As long as the ship has Morale, the USS ENTERPRISE heals the Shield Health by 6% whenever it gets hit.

Ship Abilities are always active.

**Ability Bonus by Level**
```
Level      Bonus
----------------
    6        6 %
    7        6 %
    8        6 %
    9        7 %
   10        7 %
----------------
```
Max Tiers: ` 9 `
Max Levels: ` 45 `
Can Scrap? ` Yes `
Req. Lvl: ` 50 `
` 65,400,000 Tritanium `
`  2,275,000 Dilithium `
`     11,150 3★ Common Gas `
`      2,775 3★ Common Ore `
`      1,865 3★ Explorer Parts `
` 380,777 Tritanium `
`  20,401 Dilithium `
Time: `7d 7h 0m`
Seconds: `630,000` **
Time: `1d 1h 4m`
Seconds: `90,270` **
```
Level  XP Required
------------------
    6        2,400
    7        2,900
    8        3,900
    9        4,600
   10        6,000
------------------
```
* **Ship Total Tiering Cost & Time** displayed are *base values only*. Buffs/Bonuses are player specific and *are not applied*.
=====================================================
=====================================================
LCARS_COMMAND: !ent t3
-----------------------------------------------------
LCARS_RESPONSE:
Giving what she's got
As long as the ship has Morale, the USS ENTERPRISE heals the Shield Health by 7% whenever it gets hit.

Ship Abilities are always active.

**Ability Bonus by Level**
```
Level      Bonus
----------------
   11        7 %
   12        8 %
   13        8 %
   14        9 %
   15        9 %
----------------
```
Max Tiers: ` 9 `
Max Levels: ` 45 `
Can Scrap? ` Yes `
Req. Lvl: ` 50 `
` 131,300,000 Tritanium `
`   5,420,000 Dilithium `
`       8,200 3★ Common Gas `
`       1,275 3★ Uncommon Gas `
`       2,500 3★ Common Ore `
`         300 3★ Uncommon Ore `
`       3,765 3★ Explorer Parts `
` 445,162 Tritanium `
`  58,180 Dilithium `
Time: `14d 14h 0m`
Seconds: `1,260,000` **
Time: `1d 3h 45m`
Seconds: `99,942` **
```
Level  XP Required
------------------
   11        7,000
   12        8,500
   13        9,500
   14       11,000
   15       13,500
------------------
```
* **Ship Total Tiering Cost & Time** displayed are *base values only*. Buffs/Bonuses are player specific and *are not applied*.
=====================================================
JSON file found:./raw-data/2021-07-05_dump_lcars/lcars-terminal-34 [697529046875111470] [part 2].json
PARSE_FILE: ./raw-data/2021-07-05_dump_lcars/lcars-terminal-34 [697529046875111470] [part 2].json
=====================================================
LCARS_COMMAND: !zone 2 avansa
-----------------------------------------------------
LCARS_RESPONSE:
`Thu 12:00 `
` 45 minutes `
`  50,000 Progenitor Core `
` 500,000 2⇴ Isogen `
Corvallen
Quantum
→  Advanced Quantum Generator
→  Improved 3⇴ Isogen Refinery
→  Officer Attack Enhancer
```
Level Name                 Warp Hubs Nodes
-------------------------------------------
   30 Avansa Alpha           20  Yes     9
   30 Avansa Beta            20   No    18
-------------------------------------------
```
```
Tier   Systems UTC [Day + Time]        Duration
| Name       | EU        US        APAC       |
-+----------+-+---------+---------+---------+--
2 Roshar     2 Mon 14:00 Mon 21:00 Mon 07:00 45
1 Ruhe       2 Fri 11:00 Fri 18:00 Fri 04:00 30
1 Otima      2 Wed 10:00 Wed 17:00 Wed 03:00 30
3 Corva      3 Sat 14:00 Sat 21:00 Sat 07:00 60
-+----------+-+---------+---------+---------+--
```
Times displayed are UTC for each region. Add the timezone adjustment [+ daylight saving] for your local time.

For Example:
1. West Virginia, USA
   = `US (UTC) - 5`
   = `Thu 18 - 5`
   = `Thu 13:00 `

2. Sydney, Australia
   = `APAC (UTC) + 10 (AEST) + 1 (daylight saving is active)`
   = `Thu 4 + 10 + 1`
   = `Thu 15:00 `
=====================================================
=====================================================
LCARS_COMMAND: !zone 2 avansa  alpha
-----------------------------------------------------
LCARS_RESPONSE:
`Thu 12:00 `
` 45 minutes `
`  50,000 Progenitor Core `
` 500,000 2⇴ Isogen `
Corvallen
Quantum
→  Advanced Quantum Generator
→  Improved 3⇴ Isogen Refinery
→  Officer Attack Enhancer
```
Level Name                 Warp Hubs Nodes
-------------------------------------------
   30 Avansa Alpha           20  Yes     9
   30 Avansa Beta            20   No    18
-------------------------------------------
```
```
Tier   Systems UTC [Day + Time]        Duration
| Name       | EU        US        APAC       |
-+----------+-+---------+---------+---------+--
2 Roshar     2 Mon 14:00 Mon 21:00 Mon 07:00 45
1 Ruhe       2 Fri 11:00 Fri 18:00 Fri 04:00 30
1 Otima      2 Wed 10:00 Wed 17:00 Wed 03:00 30
3 Corva      3 Sat 14:00 Sat 21:00 Sat 07:00 60
-+----------+-+---------+---------+---------+--
```
Times displayed are UTC for each region. Add the timezone adjustment [+ daylight saving] for your local time.

For Example:
1. West Virginia, USA
   = `US (UTC) - 5`
   = `Thu 18 - 5`
   = `Thu 13:00 `

2. Sydney, Australia
   = `APAC (UTC) + 10 (AEST) + 1 (daylight saving is active)`
   = `Thu 4 + 10 + 1`
   = `Thu 15:00 `
=====================================================
JSON file found:./raw-data/2021-07-05_dump_lcars/lcars-terminal-15 [697529046057222148].json
PARSE_FILE: ./raw-data/2021-07-05_dump_lcars/lcars-terminal-15 [697529046057222148].json
=====================================================
LCARS_COMMAND: !valdore
-----------------------------------------------------
LCARS_RESPONSE:
Advanced Cloaking
When defending, at the start of each round, the Valdore increases the Shield Deflection, Armor and Dodge of all ships and Defense platforms by 30%.

Ship Abilities are always active.

**Ability Bonus by Level**
```
Level      Bonus
----------------
    1       30 %
    2       70 %
    3       72 %
    4       72 %
    5       74 %
----------------
```
Quantity: ` 150 `
Valdore Class Blueprint: ` 1,320 each ` = ` 198.0K Total `
Romulan Loyalty Pack VI: ` 1,725 `(1 only)
Grade 4 Ship Research: ` 1 `
Shipyard: ` 42 `
Max Tiers: ` 12 `
Max Levels: ` 60 `
Can Scrap? ` No `
` 25,000,000 Tritanium `
`  1,600,000 Dilithium `
`      7,000 4★ Common Gas `
`      2,450 4★ Common Ore `
` 31,185,000 Tritanium `
`  1,275,750 Dilithium `
Time: `150d 0h 0m`
Seconds: `12,960,000` **
Time: `22h 19m`
Seconds: `80,398` **
```
Level  XP Required
------------------
    2        8,000
    3       12,000
    4       20,000
    5       29,000
------------------
```
```
                 Tiers
Component        Min Max Qty
-----------------------------
Energy Weapon      2  12   3
Cargo Bay          2  12   1
Warp Engine        2  12   1
Shield             2  12   1
Armor              2  12   1
-----------------------------
```
* **Ship Total Tiering Cost & Time** displayed are *base values only*. Buffs/Bonuses are player specific and *are not applied*.
=====================================================
=====================================================
LCARS_COMMAND: !valdore tier 1
-----------------------------------------------------
LCARS_RESPONSE:
Advanced Cloaking
When defending, at the start of each round, the Valdore increases the Shield Deflection, Armor and Dodge of all ships and Defense platforms by 30%.

Ship Abilities are always active.

**Ability Bonus by Level**
```
Level      Bonus
----------------
    1       30 %
    2       70 %
    3       72 %
    4       72 %
    5       74 %
----------------
```
Quantity: ` 150 `
Valdore Class Blueprint: ` 1,320 each ` = ` 198.0K Total `
Romulan Loyalty Pack VI: ` 1,725 `(1 only)
Grade 4 Ship Research: ` 1 `
Shipyard: ` 42 `
Max Tiers: ` 12 `
Max Levels: ` 60 `
Can Scrap? ` No `
` 25,000,000 Tritanium `
`  1,600,000 Dilithium `
`      7,000 4★ Common Gas `
`      2,450 4★ Common Ore `
` 31,185,000 Tritanium `
`  1,275,750 Dilithium `
Time: `150d 0h 0m`
Seconds: `12,960,000` **
Time: `22h 19m`
Seconds: `80,398` **
```
Level  XP Required
------------------
    2        8,000
    3       12,000
    4       20,000
    5       29,000
------------------
```
```
                 Tiers
Component        Min Max Qty
-----------------------------
Energy Weapon      2  12   3
Cargo Bay          2  12   1
Warp Engine        2  12   1
Shield             2  12   1
Armor              2  12   1
-----------------------------
```
* **Ship Total Tiering Cost & Time** displayed are *base values only*. Buffs/Bonuses are player specific and *are not applied*.
=====================================================
=====================================================
LCARS_COMMAND: !valdore t2
-----------------------------------------------------
LCARS_RESPONSE:
Advanced Cloaking
When defending, at the start of each round, the Valdore increases the Shield Deflection, Armor and Dodge of all ships and Defense platforms by 74%.

Ship Abilities are always active.

**Ability Bonus by Level**
```
Level      Bonus
----------------
    6       74 %
    7       76 %
    8       76 %
    9       78 %
   10       80 %
----------------
```
Max Tiers: ` 12 `
Max Levels: ` 60 `
Can Scrap? ` No `
` 1,267,300,000 Tritanium `
`    69,500,000 Dilithium `
`        19,305 4★ Common Gas `
`        13,300 4★ Common Ore `
`        46,035 4★ Common Explorer Parts `
` 63,273,000 Tritanium `
`  2,588,250 Dilithium `
Time: `14d 14h 0m`
Seconds: `1,260,000` **
Time: `1d 15h 15m`
Seconds: `141,347` **
```
Level  XP Required
------------------
    6       41,000
    7       59,000
    8       78,000
    9      100,000
   10      130,000
------------------
```
* **Ship Total Tiering Cost & Time** displayed are *base values only*. Buffs/Bonuses are player specific and *are not applied*.
=====================================================
JSON file found:./raw-data/2021-07-05_dump_lcars/lcars-terminal-27 [697529046447161393] [part 5].json
PARSE_FILE: ./raw-data/2021-07-05_dump_lcars/lcars-terminal-27 [697529046447161393] [part 5].json
=====================================================
LCARS_COMMAND: !r awayteams infamy and heroism 3
-----------------------------------------------------
LCARS_RESPONSE:
Academy (41)
Federation Demolition (2)
Klingon Demolition (2)
Romulan Demolition (2)
`  5  `
AwayTeams
Column: `  33  `
Row: `  2  `
`      35 Merit of Honor `
` 335,040 Service Award `
Time: `124d 14h 15m`
Seconds: `10,764,900` **
Actual: `26,000`
Increase: `4,000`
`14.00 %`
NIL
* **Research Cost & time** displayed are *base values only*. Buffs/Bonuses are player specific and *are not applied*.  Use `!research faq` for information on how to calculate the buff adjustments.
=====================================================
=====================================================
LCARS_COMMAND: !r awayteams infamy and heroism 4
-----------------------------------------------------
LCARS_RESPONSE:
Academy (43)
Federation Demolition (4)
Klingon Demolition (4)
Romulan Demolition (4)
`  5  `
AwayTeams
Column: `  33  `
Row: `  2  `
`      65 Merit of Honor `
` 657,834 Service Award `
Time: `271d 15h 44m`
Seconds: `23,471,040` **
Actual: `30,500`
Increase: `4,500`
`23.00 %`
NIL
* **Research Cost & time** displayed are *base values only*. Buffs/Bonuses are player specific and *are not applied*.  Use `!research faq` for information on how to calculate the buff adjustments.
=====================================================
=====================================================
LCARS_COMMAND: !r awayteams infamy and heroism 5
-----------------------------------------------------
LCARS_RESPONSE:
Battleship Focus Shot (2)
Explorer Focus Shot (2)
Interceptor Focus Shot (2)
Academy (45)
Science Lab (45)
Federation Demolition (6)
Klingon Demolition (6)
Romulan Demolition (6)
`  5  `
AwayTeams
Column: `  33  `
Row: `  2  `
`       125 Merit of Honor `
` 1,259,626 Service Award `
Time: `473d 1h 25m`
Seconds: `40,872,300` **
Actual: `35,500`
Increase: `5,000`
`35.00 %`
NIL
* **Research Cost & time** displayed are *base values only*. Buffs/Bonuses are player specific and *are not applied*.  Use `!research faq` for information on how to calculate the buff adjustments.
=====================================================
JSON file found:./raw-data/2021-07-05_dump_lcars/lcars-terminal-26 [697529046447161392] [part 2].json
PARSE_FILE: ./raw-data/2021-07-05_dump_lcars/lcars-terminal-26 [697529046447161392] [part 2].json
==========CONTINUED FROM ABOVE================
{'name': "L'Nar - Uncommon", 'value': "L'Nar led a failed attempt to destroy the heart of the Romulan Empire; he allied with Section 31 to launch an assault on Qo'nos and attempted to deposit the last remnant of red matter in the High Council chamber. Unfortunately, he chose his allies poorly, as Section 31 ultimately betrayed him and stole the red matter.\n```\nClass:   Engineering\nGroup:   ROMULAN PATRIOTS\nFaction: Romulan\n```", 'isInline': False}
{'name': 'Leonard McCoy - Rare', 'value': "Leonard 'Bones' McCoy is the chief medical officer of the Enterprise, and a good friend and advisor to Captain Kirk. McCoy's skill as a surgeon is renowned, and his work on the Enterprise has included curing diseases, transfusing blood from augments into tribbles, operating on torpedoes, and resuscitating dead captains.\n```\nClass:   Science\nGroup:   ENTERPRISE CREW\nFaction: Federation\n```", 'isInline': False}
{'name': 'Linkasa - Uncommon', 'value': 'Linkasa is a prickly and cold Klingon lady; she has rebuffed the advances of her peers bloodily. She is also a capable engineer, earning glory for the Empire by keeping its fleet in good repair.\n```\nClass:   Engineering\nGroup:   BLOOD & HONOR\nFaction: Klingon\n```', 'isInline': False}
{'name': 'Liviana Charvanek - Epic', 'value': 'Liviana Charvanek only recently earned her command, but has distinguished herself as a clever and ruthless strategist, and a true daughter of Romulus. While she favors to strike from positions of strength, she has earned the respect of the Klingons by her ability to fight them toe to toe.\n```\nClass:   Command\nGroup:   ROMULAN PATRIOTS\nFaction: Romulan\n```', 'isInline': False}
{'name': 'Livis - Rare', 'value': "Livis manned the comms and operations systems on board the Narada. Loyalty to Romulus came first for Livis, and vengeance became the only motivation left for him.\n```\nClass:   Engineering\nGroup:   NERO'S CREW\nFaction: Romulan\n```", 'isInline': False}
==========CONTINUED FROM ABOVE================
{'name': 'Lucia Gonzales - Uncommon', 'value': "Lucia Gonzales is the easy-going leader of a troupe of the Academy's finest. Lucia specializes in diplomacy; it shows in the ease with which she appraises others and makes friends, including the frosty vulcan T'Laan and the pugnacious andorian Shev Akria.\n```\nClass:   Command\nGroup:   STARFLEET ACADEMY\nFaction: Federation\n```", 'isInline': False}
{'name': "M'Ral - Uncommon", 'value': "M'Ral is a junior assault officer in Gorkon's fleet; she's picked up the nickname 'Screaming Blade' for her piercing war cries when she charges with a bat'leth in hand.\n```\nClass:   Command\nGroup:   KLINGON PATRIOTS\nFaction: Klingon\n```", 'isInline': False}
{'name': 'Mae Darwin - Common', 'value': 'Mae is the second shift navigator on the Enterprise. Brave and dutiful, Mae is loyal to her fellow crewmen, willing to sacrifice greatly for them.\n```\nClass:   Engineering\nGroup:   SHAKEDOWN CRUISE\nFaction: Federation\n```', 'isInline': False}
{'name': 'Mara - Rare', 'value': "Mara is Kang's wife and science officer. She is gentle, for a Klingon, but has aided her husband in countless battles. Where Kang commands, Mara coaxes; between the both of them, the soldiers are brought to their best performance.\n```\nClass:   Science\nGroup:   BLOOD & HONOR\nFaction: Klingon\n```", 'isInline': False}
{'name': 'Marla McGivers - Rare', 'value': "Marla McGivers was one of Starfleet’s top historians and a specialist in the late-20th century Eugenics Wars. This put her in a rather unique position; she is one of the only people in the galaxy to know of Khan’s true history.\n\nMarla was appalled by Starfleet’s treatment of Khan during his trial and subsequent sentencing. To her, Khan was the greatest discovery in the history of the Federation. Shortly after Khan was imprisoned once more, Marla handed in her resignation. She couldn’t possibly stay with an organization that would spit in the face of discovery.\n\nMarla now works with the Augments, attempting to act as their link to modern humanity. As the only one of them who truly understands this new galaxy, Marla has proven herself a valuable ally to the Augments.\n```\nClass:   Engineering\nGroup:   KHAN'S CREW\nFaction: Augment\n```", 'isInline': False}
==========CONTINUED FROM ABOVE================
{'name': 'Marlena Moreau - Rare', 'value': "Marlena Moreau is an up and coming officer in the science division, with an expertise in stellar cartography and astrophysics. She's known for her warm personality and diligent work ethic, often putting in extra hours to help out her fellow officers. She's shown considerable aptitude for people management and morale, so Christopher Pike picked her out for potential command training in the future.\n```\nClass:   Science\nGroup:   SHAKEDOWN CRUISE\nFaction: Federation\n```", 'isInline': False}
{'name': 'Michael Burnham - Epic', 'value': 'Once meant to stand as the living embodiment of Human and Vulcan potential, Michael Burnham’s life took a disastrous turn after the Battle at the Binary Stars. Branded a mutineer and sentenced to imprisonment for life, she had given up all hope of living up to her incredible potential.\n\nHowever, the war was not finished and Burnham still had a part to play. She was brought aboard the USS Discovery to serve under Captain Gabriel Lorca. She would pay off her debt to society by helping him win the war against the Klingons.\n\nLorca gave her the greatest gift she ever could have received... Something to fight for. Michael has come to see the Discovery’s crew as her own family and will stop at nothing to defend them.\n```\nClass:   Science\nGroup:   DISCOVERY CREW\nFaction: Federation\n```', 'isInline': False}
{'name': 'Mirek - Rare', 'value': "Mirek is Charvanek's younger sister, and a capable science officer. Her expertise is in deflection fields and radiation phenomena, and has aided her sister in tracking wilier Klingon opponents.\n```\nClass:   Science\nGroup:   ROMULAN PATRIOTS\nFaction: Romulan\n```", 'isInline': False}
{'name': 'Montgomery Scott - Uncommon', 'value': "Montgomery Scott is the eccentric but brilliant chief engineer of the Enterprise. Though his early career suffered due to an incident involving a transporter experiment and Admiral Archer's beagle, he has gone on to see the Enterprise through thick and thin. His care has kept the ship functioning through the wear and tear of daily use and unexpected crises alike.\n```\nClass:   Engineering\nGroup:   ENTERPRISE CREW\nFaction: Federation\n```", 'isInline': False}
{'name': 'Navi - Rare', 'value': "Exceptional from birth, Navi was one of the chosen few to be subjected to the Augment experiments of the 1990s. However, unlike many of her fellow subjects, she managed to retain her humanity, compassion, and level-headedness.\nNavi and Khan quickly became friends during the experiments and their subsequent training. Where Khan was equal parts calculating and raw fury, Navi was compassionate and calm. She acted as a positive influence on Khan and was often the only one who could talk him down.\nAfter Khan freed Navi from her cryosleep, she saw immediately that he was in desperate need of her counsel. He had become consumed by rage and his desire for vengeance. Only she could pull him back from the brink of darkness.\nOf course, she is still willing to bend the rules as necessary, if it means that she can better serve Khan and her Augment family, so long as it does not involve cruelty or unnecessary violence.\n```\nClass:   Science\nGroup:   KHAN'S CREW\nFaction: Augment\n```", 'isInline': False}
==========CONTINUED FROM ABOVE================
{'name': 'Nero - Epic', 'value': "Nero is a Romulan mining ship Captain who comes from an alternate future. In his timeline's 2387, Nero witnessed the destruction of his homeworld of Romulus.\n\nThe untimely efforts of Ambassador Spock to contain the supernova that engulfed his planet resulted in the creation of an artificial black hole, which created this offshoot reality. On arrival, Nero's vessel, the Narada, was heavily damaged in combat with the USS Kelvin, leaving Nero and his crew stranded.\n\nNero lost his family when the disaster occurred and on that day, promised himself retribution against Spock for his failure.\n```\nClass:   Engineering\nGroup:   NERO'S CREW\nFaction: Romulan\n```", 'isInline': False}
{'name': 'Next Gen Crusher - Common', 'value': 'Having lost her parents as a child, Beverly Crusher had to become independent at an early age, an independence that left her feeling isolated and unable to relate to children in her age group. She became inspired to pursue medicine after witnessing her grandmother use organic remedies to treat those wounded in the tragic disaster on the Arvada III colony.\n\nWhile she doesn’t always think before speaking, Crusher has worked hard to become more conscious of others’ feelings, knowing how important her bedside manner will be as she pursues her medical career. Now, as part of Starfleet, she has been identified as one of the most promising up-and-coming doctors in the academy.\n```\nClass:   Science\nGroup:   NEXT GEN\nFaction: Federation\n```', 'isInline': False}
{'name': 'Next Gen Data - Common', 'value': 'Data is a Soong-type android, the fifth of six developed by Dr. Noonien Soong. Deactivated and abandoned by his creator, he was eventually found by the USS Tripoli on Omicron Theta. With Starfleet realizing Data’s potential upon reactivation, and the android searching for a purpose, he was admitted into the Starfleet Academy.\n\nDespite excelling scholastically, as well as in all physical examinations, Data still found himself dealing with major obstacles that threatened his Starfleet career, facing prejudice from some of the other cadets and officers, as well as struggling with the social and psychological elements of his training. However, Data is determined to overcome these challenges to become the most effective Starfleet officer he can be.\n```\nClass:   Command\nGroup:   NEXT GEN\nFaction: Federation\n```', 'isInline': False}
{'name': 'Next Gen La Forge - Common', 'value': 'Geordi La Forge is no stranger to overcoming adversity, having dealt with a birth defect that left him blind. Upon receiving his first VISOR at the age of eight which allowed him to see for the first time in his life, he became fascinated with the inner workings of its technology, as well as all technology around him.\n\nLa Forge’s thirst for knowledge, along with his natural talent for engineering has made him a stand-out in his academy class. With his specializations in antimatter power and Dilithium regulators – subjects that often confound even the most experienced of engineers – Geordi has already garnered a reputation as something of a wunderkind in his field.\n```\nClass:   Engineering\nGroup:   NEXT GEN\nFaction: Federation\n```', 'isInline': False}
{'name': 'Next Gen Riker - Common', 'value': 'With ancestors that include Thaddius Riker, a Union Army Colonel, William Riker’s family name gave him a lot to live up to. Raised by his father in the harsh Tundra of Alaska, Riker dreamed of a life in Starfleet as a child, craving adventure and excitement that Alaska simply couldn’t give him.\n\nDespite his natural charisma and talent for decision making, his now-strained relationship with his father has left Riker with something of a rebellious streak, as he constantly clashes with his peers and his commanding officers. And with his middling performance in Starfleet Academy belying his lofty ambitions, Riker will need to shape up if he wants to achieve his ultimate goal of becoming a Starfleet Captain.\n```\nClass:   Command\nGroup:   NEXT GEN\nFaction: Federation\n```', 'isInline': False}
==========CONTINUED FROM ABOVE================
{'name': 'Next Gen Troi - Common', 'value': 'An aspiring Starfleet counsellor, Deanna Troi is half Betazoid and half Human, and has extra-sensory empathy, giving her a keen insight into the emotional state of those around her. However, her ability is limited when it comes to beings with different brain structures to Humans and Betazoids, and so she spends as much time as she can studying the psychology of unfamiliar species.\n\nHaving suffered through tragedy at an early age from the loss of her sister, Troi chose to dedicate her life to helping others through loss and trauma, and help heal those who have suffered emotional damage. With an unmatched sense of compassion, and a penchant for quick thinking and decision making, Troi can be a tremendous asset for Starfleet.\n```\nClass:   Science\nGroup:   NEXT GEN\nFaction: Federation\n```', 'isInline': False}
{'name': 'Nine of Ten - Uncommon', 'value': 'When the USS Sterling went missing in action at the borders of Borg-occupied space, Cadet Gonzales was among the first crew assigned to investigate the ship’s disappearance. However, it was not long before members of this search party were greeted with the same fate as the Sterling’s crew - a forced, painful assimilation into the Borg Collective. Lucia Gonzales is dead. All that remains is Nine of Ten, Septenary Adjunct of Unimatrix Twelve.\n```\nClass:   Command\nGroup:   UNIMATRIX TWELVE\nFaction: Neutral\n```', 'isInline': False}
{'name': 'Nyota Uhura - Rare', 'value': "Nyota Uhura is the Chief Communications Officer aboard the Federation flagship, the USS Enterprise. She met James T. Kirk and Spock at Starfleet Academy in 2255 and went on to serve with them on their five-year mission.\n\nUhura has an incredible talent for xenolinguistics, showing an acute capability to recognize multiple alien languages and engage in spoken Klingon.\n\nShe was instrumental in the detection of Nero's attack on Vulcan and was a key player in the capture of Khan Noonien Singh on Kronos in 2259.\n```\nClass:   Engineering\nGroup:   ENTERPRISE CREW\nFaction: Federation\n```", 'isInline': False}
{'name': 'Officer 0718 - Uncommon', 'value': "Officer 0718 is a cybernetic life form created when the Enterprise was temporarily controlled by a mysterious alien entity. He has the ability to interface directly with the Enterprise's computer and input commands and data more rapidly than the rest of the crew. When not on duty, 0718 often spends time in the botanical lab.\n```\nClass:   Science\nGroup:   AUXILIARY CONTROLS\nFaction: Federation\n```", 'isInline': False}
{'name': 'One of Ten - Rare', 'value': 'An engineer assigned to active duty aboard the USS Westchester, Daniel Morgan was a promising young officer with a potentially bright future in Starfleet Operations. However, when the Westchester encountered the Borg in the mid 23rd century, this future was irrevocably altered. With his fellow crewmates quickly assimilated into the Borg Collective, Morgan was the last to undergo this procedure. With a fateful last-minute intervention from a Starfleet rescue fleet, the assimilation of Morgan was interrupted and he was returned to the care of the Federation. With both the memories and scars of the incident now a part of him for the rest of his life, Morgan uses his brief experience as part of the Collective in order to combat the Borg threat.\n```\nClass:   Command\nGroup:   UNIMATRIX TWELVE\nFaction: Neutral\n```', 'isInline': False}
JSON file found:./raw-data/2021-07-05_dump_lcars/lcars-terminal-25 [697529046447161391].json
PARSE_FILE: ./raw-data/2021-07-05_dump_lcars/lcars-terminal-25 [697529046447161391].json
=====================================================
LCARS_COMMAND: !ship d4 fp
-----------------------------------------------------
LCARS_RESPONSE:
```
     Rounds (sample)
     1  2  3  4  5  6  7  8  9
-------------------------------
K1:  2  .  2  .  2  .  2  .  2
K2:  .  2  .  2  .  2  .  2  .
-------------------------------
```
Weapons:
 * `  K1  ` = Left Kinetic Cannon `  KINETIC  `
 * `  K2  ` = Right Kinetic Cannon `  KINETIC  `
=====================================================
JSON file found:./raw-data/2021-07-05_dump_lcars/lcars-terminal-35 [697529046875111471].json
PARSE_FILE: ./raw-data/2021-07-05_dump_lcars/lcars-terminal-35 [697529046875111471].json
=====================================================
LCARS_COMMAND: !scout kronos
-----------------------------------------------------
LCARS_RESPONSE:
Has scouts★ hostiles
Kronos (60)
60
```
System Jumps:         1
Ship Warp Required:  39
Warp Distance:       39
```
```
System Jumps:         1
Ship Warp Required:  40
Warp Distance:       40
```
```
System Jumps:         2
Ship Warp Required:  38
Warp Distance:       75
```
```
System Jumps:         3
Ship Warp Required:  38
Warp Distance:      113
```
```
System Jumps:         4
Ship Warp Required:  38
Warp Distance:      139
```
```
System Jumps:         4
Ship Warp Required:  39
Warp Distance:      151
```
```
System Jumps:         5
Ship Warp Required:  38
Warp Distance:      157
```
```
System Jumps:         5
Ship Warp Required:  38
Warp Distance:      158
```
```
System Jumps:         6
Ship Warp Required:  38
Warp Distance:      184
```
```
System Jumps:         6
Ship Warp Required:  38
Warp Distance:      187
```
=====================================================
=====================================================
LCARS_COMMAND: !cent t1-t9
-----------------------------------------------------
LCARS_RESPONSE:
Territorial
When defending , The CENTURION increases the Armor, Shield deflection and Dodge of all ships and defense platforms by 20%.

Ship Abilities are always active.

**Ability Bonus by Level**
```
Level      Bonus
----------------
    1       20 %
    2       20 %
    3       22 %
    4       22 %
    5       23 %
----------------
```
Quantity: ` 100 `
Centurion Class Blueprint: ` 200 each ` = ` 20,000 Total `
Shipyard: ` 28 `
Max Tiers: ` 9 `
Max Levels: ` 45 `
Can Scrap? ` Yes `
Req. Lvl: ` 42 `
` 1,600,000 Tritanium `
`    53,000 Dilithium `
`     2,200 3★ Common Gas `
`       275 3★ Common Ore `
` 39,472 Tritanium `
`  2,060 Dilithium `
Time: `17d 0h 0m`
Seconds: `1,468,800` **
Time: `8h 20m`
Seconds: `30,000` **
```
Level  XP Required
------------------
    2          800
    3        1,000
    4        1,400
    5        1,700
------------------
```
```
                 Tiers
Component        Min Max Qty
-----------------------------
Energy Weapon      2   9   3
Cargo Bay          2   9   1
Warp Engine        2   9   1
Shield             2   9   1
-----------------------------
```
* **Ship Total Tiering Cost & Time** displayed are *base values only*. Buffs/Bonuses are player specific and *are not applied*.
=====================================================
=====================================================
LCARS_COMMAND: !cent t1-9
-----------------------------------------------------
LCARS_RESPONSE:
Territorial
When defending , The CENTURION increases the Armor, Shield deflection and Dodge of all ships and defense platforms by 20%.

Ship Abilities are always active.

**Ability Bonus by Level**
```
Level      Bonus
----------------
    1       20 %
    2       20 %
    3       22 %
    4       22 %
    5       23 %
----------------
```
Quantity: ` 100 `
Centurion Class Blueprint: ` 200 each ` = ` 20,000 Total `
Shipyard: ` 28 `
Max Tiers: ` 9 `
Max Levels: ` 45 `
Can Scrap? ` Yes `
Req. Lvl: ` 42 `
` 1,600,000 Tritanium `
`    53,000 Dilithium `
`     2,200 3★ Common Gas `
`       275 3★ Common Ore `
` 39,472 Tritanium `
`  2,060 Dilithium `
Time: `17d 0h 0m`
Seconds: `1,468,800` **
Time: `8h 20m`
Seconds: `30,000` **
```
Level  XP Required
------------------
    2          800
    3        1,000
    4        1,400
    5        1,700
------------------
```
```
                 Tiers
Component        Min Max Qty
-----------------------------
Energy Weapon      2   9   3
Cargo Bay          2   9   1
Warp Engine        2   9   1
Shield             2   9   1
-----------------------------
```
* **Ship Total Tiering Cost & Time** displayed are *base values only*. Buffs/Bonuses are player specific and *are not applied*.
=====================================================
JSON file found:./raw-data/2021-07-05_dump_lcars/lcars-terminal-27 [697529046447161393] [part 7].json
PARSE_FILE: ./raw-data/2021-07-05_dump_lcars/lcars-terminal-27 [697529046447161393] [part 7].json
==========CONTINUED FROM ABOVE================
{'name': 'Build Costs', 'value': '`\xa0108,652,300,000\xa0Tritanium\xa0`\n`\xa0\xa0\xa04,582,400,000\xa0Dilithium\xa0`\n`\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa04,470\xa04★\xa0Epic\xa0Crystal\xa0`\n`\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa06,180\xa04★\xa0Epic\xa0Ore\xa0`\n`\xa0\xa0\xa0\xa0\xa0\xa0\xa01,152,925\xa04★\xa0Common\xa0Battleship\xa0Parts\xa0`\n`\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa025,400\xa04★\xa0Rare\xa0Battleship\xa0Parts\xa0`', 'isInline': False}
{'name': 'Repair Costs', 'value': '`\xa0374,165,000\xa0Tritanium\xa0`\n`\xa0\xa010,520,000\xa0Dilithium\xa0`', 'isInline': False}
{'name': 'Quantity', 'value': '` 1 `', 'isInline': False}
{'name': 'Warp Engine', 'value': '`     4.6 Warp Speed`\n`   225   Warp Distance`', 'isInline': False}
==========CONTINUED FROM ABOVE================
{'name': 'Build Costs', 'value': '`\xa0149,397,000,000\xa0Tritanium\xa0`\n`\xa0\xa0\xa06,300,700,000\xa0Dilithium\xa0`\n`\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa04,965\xa04★\xa0Epic\xa0Crystal\xa0`\n`\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa07,590\xa04★\xa0Epic\xa0Ore\xa0`\n`\xa0\xa0\xa0\xa0\xa0\xa0\xa01,585,275\xa04★\xa0Common\xa0Battleship\xa0Parts\xa0`\n`\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa031,065\xa04★\xa0Rare\xa0Battleship\xa0Parts\xa0`', 'isInline': False}
{'name': 'Repair Costs', 'value': '`\xa0374,165,000\xa0Tritanium\xa0`\n`\xa0\xa010,520,000\xa0Dilithium\xa0`', 'isInline': False}
{'name': 'Quantity', 'value': '` 1 `', 'isInline': False}
{'name': 'Shield Health', 'value': '`  737,034  `', 'isInline': True}
{'name': 'Shield Deflection', 'value': '`  8,385  `', 'isInline': True}
=====================================================
LCARS_COMMAND: !ship uss enterprise a info t10
-----------------------------------------------------
LCARS_RESPONSE:
Optimized Crew Interface
As long as the USS Enterprise A has Morale , everytime it gets hit, it increases the Weapon Damage by 7%.

Ship Abilities are always active.

**Ability Bonus by Level**
```
Level      Bonus
----------------
   46        7 %
   47        7 %
   48        8 %
   49        8 %
   50        8 %
----------------
```
Max Tiers: ` 12 `
Max Levels: ` 60 `
Can Scrap? ` No `
` 871,100,000,000 Tritanium `
`  37,897,700,000 Dilithium `
`         140,475 4★ Rare Gas `
`          65,220 4★ Epic Gas `
`          48,455 4★ Epic Ore `
`       4,101,300 4★ Common Explorer Parts `
`         265,065 4★ Rare Explorer Parts `
` 5,068,314,500 Tritanium `
`   144,470,000 Dilithium `
Time: `486d 2h 40m`
Seconds: `42,000,000` **
Time: `6d 17h 55m`
Seconds: `582,925` **
```
Level  XP Required
------------------
   46    4,923,000
   47    5,143,000
   48    5,370,000
   49    5,798,000
   50    6,040,000
------------------
```
* **Ship Total Tiering Cost & Time** displayed are *base values only*. Buffs/Bonuses are player specific and *are not applied*.
=====================================================
==========CONTINUED FROM ABOVE================
{'name': 'Build Costs', 'value': '`\xa0174,220,000,000\xa0Tritanium\xa0`\n`\xa0\xa0\xa07,579,500,000\xa0Dilithium\xa0`\n`\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa046,825\xa04★\xa0Rare\xa0Gas\xa0`\n`\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa011,500\xa04★\xa0Epic\xa0Gas\xa0`\n`\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa07,685\xa04★\xa0Epic\xa0Ore\xa0`\n`\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa046,635\xa04★\xa0Rare\xa0Explorer\xa0Parts\xa0`', 'isInline': False}
{'name': 'Repair Costs', 'value': '`\xa0664,573,500\xa0Tritanium\xa0`\n`\xa0\xa019,275,000\xa0Dilithium\xa0`', 'isInline': False}
{'name': 'Quantity', 'value': '` 1 `', 'isInline': False}
{'name': 'Min Damage', 'value': '`  37,960  `', 'isInline': True}
{'name': 'Max Damage', 'value': '`  45,554  `', 'isInline': True}
{'name': 'Accuracy', 'value': '`  175,890  `', 'isInline': True}
{'name': 'Armor Pierce', 'value': '`  17,587  `', 'isInline': True}
{'name': 'Shield Pierce', 'value': '`  17,587  `', 'isInline': True}
{'name': 'Crit Chance', 'value': '`  10.00 %  `', 'isInline': True}
{'name': 'Crit Modifier', 'value': '`  150.00 %  `', 'isInline': True}
{'name': 'Firing Pattern', 'value': '```\n     Rounds (sample)\n     1  2  3  4  5  6  7  8  9\n-------------------------------\nEN:  3  3  3  3  3  3  3  3  3\n-------------------------------\n```', 'isInline': False}
['! ?', '! enterprise t8?', '! enterprise t9?', '! hydra t2?', '! mayflower t1 t3', '! mayflower t1 to t2', '! mayflower t2 to t3', '! mission "for the empire"', '! mission "so it has come to this"', '! mission "the calm before the storm"', '! officers kahn t3', '! sally t8', '! sally t9', '! scrap legionary l45', '! shops bortas', '! upg botany bay t4', '! upgrade defence technology 24', '! upgrade defence technology 25', '!?', '!? scrap', '!armarda', '!augur t5', '!bortas max', '!bp kting', '!cent t1-9', '!cent t1-t9', '!chart armada', '!chart pvp', '!chart rr', '!dailies 32', '!dpa 38 info', '!dpa 39 info', '!ent t1', '!ent t1 t4', '!ent t2', '!ent t3', '!enterprise t2', '!faction rep', '!franklin t1-7', '!franklin t7', '!franklin-a', '!hangar 38', '!james t. kirk', '!kahn', '!kirk', '!mission "dark space"', '!mission “angel in disguise”', '!mission “reality sinks in”', '!mission “the tables turn”', '!officers kahn', '!operations 26', '!operations 26 27', '!operations 27', '!ops 34', '!pan', '!pattern augur', '!pattern ente', '!r "1* isogen extraction" 2', '!r awayteams infamy and heroism 3', '!r awayteams infamy and heroism 4', '!r awayteams infamy and heroism 5', '!r combat 4★ tactical battleships 10', '!r galaxy parsteel hunter 10', '!r galaxy tritanium hunter 6', '!r outlaw dilithium upgrades 8', '!r outlaw dilithium upgrades 9', '!res energy guerilla warfare 8', '!res energy guerilla warfare 9', '!res ship component efficiency 5', '!res “explorer shields” 10', '!rouge reputation', '!scout kronos', '!scrap d3 l45', '!scrap franklin 45', '!scrap lvl 30 frank', '!scrap lvl35 frank', '!scrap lvl45 frank', '!scrap mayflower l45', '!scrap stella t5 25', '!ship d4 fp', '!ship korinar info t7', '!ship kting t2 t12', '!ship saladin warp', '!ship sarcophagus', '!ship uss enterprise a info t10', '!ship vidar t8', '!ship vidar t9', '!shipyard 28', '!shipyard 47', '!shuttle bay 34', '!shuttle bay 35', '!starbase chart', '!stella t7 t9', '!t1 ships', '!tco enterprise', '!tco saladin', '!up defense platform d 1 10', '!up defense platform d t1 t10', '!upg d3 t6 t7', '!upg d3 t7 t8', '!upg d3 t8 t9', '!upg trit gen 29', '!upgrades list 31', '!valdore', '!valdore t2', '!valdore tier 1', '!zone 2 avansa', '!zone 2 avansa  alpha']
