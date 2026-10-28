CREATE DATABASE gow_armors;
USE gow_armors;
drop table armors;

CREATE TABLE Armors(
ID INT AUTO_INCREMENT PRIMARY KEY, Title VARCHAR(100), Category VARCHAR(50),    -- chest, wrist, waist
Strength INT, Defence INT, Runic INT, Vitality INT, Cooldown INT, Luck INT, Skill VARCHAR(300));

INSERT INTO Armors(Title, Category,    -- chest, wrist, waist
Strength, Defence, Runic, Vitality, Cooldown, Luck, Skill)

VALUES
('Cuiras of Ares','Chest',52,42,0,31,0,31,'rage hits have a chance to deploy healthstone and grant rage'),
('Gauntlet of Ares','Wrist',113,0,0,38,0,38,'when rage meter is full using it willincrease damage for a short time'),
('Warbelt of Ares','Waist',113,0,0,38,0,38,'when rage meter is full using it willincrease damage for a short time');

INSERT INTO Armors(Title, Category,    -- chest, wrist, waist
Strength, Defence, Runic, Vitality, Cooldown, Luck, Skill)

VALUES
('Cloak of the Black Bear','Chest',120,120,0,0,40,0,'Kratos first Melee Attack immediately after evading does increased damage. (20% alone, 40% w/ Belt.).'),
('Wraps of the Black Bear','Wrist',125,25,0,0,25,0,'Increases immunity duration while evading and last-second evades fire a volley of Bifröst shards.'),
('Belt of the Black Bear ','Waist',25,125,0,0,25,0,'Kratos first Melee Attack immediately after evading does increased damage. (20% alone, 40% w/ Wraps');

INSERT INTO Armors(Title, Category,    -- chest, wrist, waist
Strength, Defence, Runic, Vitality, Cooldown, Luck, Skill)

VALUES
('Shoulder Guard of Survival','Chest',100,100,53,53,53,53,'None'),
('Wraps of Survival','Wrist',100,25,44,44,44,44,'None'),
('Belt of Survival','Waist',25,100,44,44,44,44,'None');

INSERT INTO Armors(Title, Category,    -- chest, wrist, waist
Strength, Defence, Runic, Vitality, Cooldown, Luck, Skill)

VALUES
('Fortified Husk Cuirass','Chest',100,180,0,0,0,0,'Blocks and Parries have a Moderate LUCK chance to empower Kratos next attack to strike with a damaging explosion'),
('Fortified Husk Arm Guards','Wrist',110,65,0,0,0,0,'While Blocking, take less damage from unblockable attacks and attacks from behind (25% alone, 50% w/ Girdle)'),
("Fortified Husk Girdle",'Waist',0,175,0,0,0,0,'While Blocking, take less damage from unblockable attacks and attacks from behind. (25% alone, 50% w/ Arm Guards.)');

INSERT INTO Armors(Title, Category,    -- chest, wrist, waist
Strength, Defence, Runic, Vitality, Cooldown, Luck, Skill)

VALUES
("Vidar's Pauldron of Might",'Chest',170,100,0,0,0,0,"Combo Finishers have a High LUCK chance to increase Kratos' STRENGTH and Stagger Resistance for a duration"),
("Vidar's Bracers of Might",'Wrist',169,0,0,0,0,0,'Combo Finishers do increased damage. (10% alone; 20% w/ Belt'),
("Vidar's Belt of Might",'Waist',58,100,0,0,0,0,"Combo Finishers do increased damage. (10% alone; 20% w/ Bracers");

INSERT INTO Armors(Title, Category,    -- chest, wrist, waist
Strength, Defence, Runic, Vitality, Cooldown, Luck, Skill)

VALUES
("Risen Snow Breastplate",'Chest',125,0,0,0,31,31,"Launching an enemy has a High LUCK chance to increase Kratos' STRENGTH and Stagger Resistance for a duration"),
("Risen Snow Gauntlets",'Wrist',169,0,0,0,0,0,'Increases Stun dealt to airborne enemies. (20% alone; 40% w/ Girdle)'),
("Risen Snow Girdle",'Waist',0,120,0,0,31,31,"Increases Stun dealt to airborne enemies. (20% alone; 40% w/ Gauntlets)");


INSERT INTO Armors(Title, Category,    -- chest, wrist, waist
Strength, Defence, Runic, Vitality, Cooldown, Luck, Skill)

VALUES
("Darkdale Plackart",'Chest',100,100,50,50,0,0,"Killing an enemy while in Spartan Rage restores some Rage and Health"),
("Darkdale Arm Guards",'Wrist',125,0,31,31,0,0,'Increases the rate at which rage is gained when attacking Status-Afflicted enemies and using Runic Attacks. (20% alone; 40% w/ Waist Guard).'),
("Darkdale Waist Guard",'Waist',0,125,0,0,31,31,"Increases the rate at which rage is gained when attacking Status-Afflicted enemies and using Runic Attacks. (20% alone; 40% w/ Arm Guards).");

----------------------------------------------------------------------------------

INSERT INTO Armors(Title, Category,    -- chest, wrist, waist
Strength, Defence, Runic, Vitality, Cooldown, Luck, Skill)

VALUES
("Niðavellir's Finest Plackart",'Chest',80,140,0,80,0,0,"Stun Grabbing an enemy grants a Health Burst."),
("Niðavellir's Finest Arm Guards",'Wrist',100,38,50,0,0,0,'Reduces how quickly enemy Stun bars drain. (50% alone; 100% w/ Waist Guard)'),
("Niðavellir's Finest Waist Guard",'Waist',0,138,0,0,50,0,"Reduces how quickly enemy Stun bars drain. (50% alone; 100% w/ Arm Guards)");

INSERT INTO Armors(Title, Category,    -- chest, wrist, waist
Strength, Defence, Runic, Vitality, Cooldown, Luck, Skill)

VALUES
("Spaulders of Enlightenment",'Chest',80,100,110,0,0,0,"Frost Awaken and Flame Whiplash hits have a Moderate LUCK chance to grant a Blessing of RUNIC"),
("Bracers of Enlightenment",'Wrist',110,0,63,0,0,0,'Runic Attacks do increased damage against Status-Afflicted enemies. (15% alone; 30% w/ Belt)'),
("Belt of Enlightenment",'Waist',0,113,63,0,50,0,"Runic Attacks do increased damage against Status-Afflicted enemies. (15% alone; 30% w/ Bracers)");

INSERT INTO Armors(Title, Category,    -- chest, wrist, waist
Strength, Defence, Runic, Vitality, Cooldown, Luck, Skill)

VALUES
("Cuirass of Raven Tears",'Chest',70,160,0,0,0,70,"Hitting enemies has a Low LUCK chance to grant Healing Mist"),
("Bracers of Raven Tears",'Wrist',94,50,0,0,0,44,'Increases the healing from Healthstones, Rage, and Gear. (15% Healing Increase; 30% w/ Girdle)'),
("Girdle of Raven Tears",'Waist',0,114,0,0,0,44,"Increases the healing from Healthstones, Rage, and Gear. (15% Healing Increase; 30% w/ Bracers)");

INSERT INTO Armors(Title, Category,    -- chest, wrist, waist
Strength, Defence, Runic, Vitality, Cooldown, Luck, Skill)

VALUES
("Shoulder Straps of Radiance",'Chest',120,70,0,60,0,60,"Moderate LUCK chance to grant a Blessing of RUNIC on any last-second evade"),
("Gauntlets of Radiance",'Wrist',100,0,0,0,0,0,'A last-second evade activates Realm Shift, temporarily slowing down surrounding enemies. (1 sec alone; 1.75 secs w/ Belt)'),
("Girdle of Raven Tears",'Waist',0,100,0,0,0,0,"A last-second evade activates Realm Shift, temporarily slowing down surrounding enemies. (1 sec alone; 1.75 secs w/ Gauntlets)");

INSERT INTO Armors(Title, Category,    -- chest, wrist, waist
Strength, Defence, Runic, Vitality, Cooldown, Luck, Skill)

VALUES
("Sól's Spaulders of Courage",'Chest',80,100,0,100,100,0,"Kratos' Melee damage increases based on his Rage. Incoming damage that would be lethal is absorbed by available Rage"),
("Sól's Spaulders of Courage",'Wrist',113,0,0,63,0,0,"Chance to grant a Rage Burst when damage is taken. The LUCK chance increases the lower Kratos' Health. (12% alone; 24% w/ Belt.)"),
("Sól's Belt of Courage",'Waist',0,113,0,0,63,0,"Chance to grant a Rage Burst when damage is taken. The LUCK chance increases the lower Kratos' Health. (12% alone; 24% w/ Wraps)");

INSERT INTO Armors(Title, Category,    -- chest, wrist, waist
Strength, Defence, Runic, Vitality, Cooldown, Luck, Skill)

VALUES
("Spiritual Shoulder Straps",'Chest',100,80,0,60,100,0,"Runic or Relic Attack hits stack a buff increasing Kratos' Melee and Ranged damage by 15% with each stack. (Maximum 3 stacks)"),
("Spiritual Wraps",'Wrist',113,0,0,0,63,0,"Melee Attacks have a Low LUCK chance to restore some Cooldown for the equipped weapon's Runic Attacks. (10% alone; 20% w/ Belt.)"),
("Spiritual Belt",'Waist',0,113,0,0,63,0,"Melee Attacks have a Low LUCK chance to restore some Cooldown for the equipped weapon's Runic Attacks. (10% alone; 20% w/ Wraps.)");

INSERT INTO Armors(Title, Category,    -- chest, wrist, waist
Strength, Defence, Runic, Vitality, Cooldown, Luck, Skill)

VALUES
("Sól's Spaulders of Courage",'Chest',80,100,0,100,100,0,"Kratos' Melee damage increases based on his Rage. Incoming damage that would be lethal is absorbed by available Rage"),
("Sól's Spaulders of Courage",'Wrist',113,0,0,63,0,0,"Chance to grant a Rage Burst when damage is taken. The LUCK chance increases the lower Kratos' Health. (12% alone; 24% w/ Belt.)"),
("Sól's Belt of Courage",'Waist',0,113,0,0,63,0,"Chance to grant a Rage Burst when damage is taken. The LUCK chance increases the lower Kratos' Health. (12% alone; 24% w/ Wraps)");

INSERT INTO Armors(Title, Category,    -- chest, wrist, waist
Strength, Defence, Runic, Vitality, Cooldown, Luck, Skill)

VALUES
("Lúnda's Lost Cuirass",'Chest',100,80,40,0,0,80,"Bare-Handed attacks, Parrying, and Blocking have a High LUCK chance to deal bonus damage and Poison enemies, lowering their Power Level"),
("Lúnda's Lost Bracers",'Wrist',113,0,50,0,0,25,"Melee Attacks against Poisoned enemies do increased damage. (20% alone; 40% w/ Belt)"),
("Lúnda's Lost Belt",'Waist',0,113,25,0,0,50,"Melee Attacks against Poisoned enemies do increased damage. (20% alone; 40% w/ Bracers)");

INSERT INTO Armors(Title, Category,    -- chest, wrist, waist
Strength, Defence, Runic, Vitality, Cooldown, Luck, Skill)

VALUES("Breastplate of Guiding Light",'Chest',100,80,0,0,0,100,"Moderate LUCK chance on any hit to increase the STRENGTH, RUNIC, and LUCK of one of Kratos' Weapons"),
("Gauntlets of Guiding Light",'Wrist',113,0,0,0,0,63,"Melee Attacks have a LUCK chance to critically strike, creating a Damaging Explosion. (4% Base Chance alone; 8% w/ Waist Guard)"),
("Waist Guard of Guiding Light",'Waist',0,113,0,0,0,63,"Melee Attacks have a LUCK chance to critically strike, creating a Damaging Explosion. (4% Base Chance alone; 8% w/ Gauntlets)");

INSERT INTO Armors(Title, Category,    -- chest, wrist, waist
Strength, Defence, Runic, Vitality, Cooldown, Luck, Skill)

VALUES
("Giptumaðr's Breastplate",'Chest',80,100,30,0,0,90,"Moderate LUCK chance when using a Runic Attack or Relic to immediately restore 70% of its Cooldown"),
("Giptumaðr's Gauntlets",'Wrist',113,0,19,0,0,56,"Hitting enemies with a Runic Attack or Relic has a LUCK chance to drop a Healthstone or Ragestone. (10% alone; 20% w/ Waist Guard)"),
("Giptumaðr's Waist Guard",'Waist',0,113,19,0,0,56,"Hitting enemies with a Runic Attack or Relic has a LUCK chance to drop a Healthstone or Ragestone. (10% alone; 20% w/ Gauntlets)");

INSERT INTO Armors(Title, Category,    -- chest, wrist, waist
Strength, Defence, Runic, Vitality, Cooldown, Luck, Skill)

VALUES
("Máni's Pauldron of Wisdom",'Chest',80,100,40,0,80,0,"Increases the damage caused by the Extinguish Flames and Vaporize Frost skills"),
("Máni's Bracers of Wisdom",'Wrist',113,0,25,0,50,0,"Increases the duration of all Status Effects applied to enemies. (25% Increase alone; 50% w/ Belt)"),
("Máni's Belt of Wisdom",'Waist',0,113,25,0,50,0,"Increases the duration of all Status Effects applied to enemies. (25% Increase alone; 50% w/ Bracers)");

INSERT INTO Armors(Title, Category,    -- chest, wrist, waist
Strength, Defence, Runic, Vitality, Cooldown, Luck, Skill)

VALUES
("Berserker Cuirass",'Chest',100,40,60,60,60,60,"Using a Relic massively increases the damage of Kratos' Melee Attacks, but also the damage received, for a duration"),
("Berserker Gauntlets",'Wrist',113,0,31,31,31,31,"Low LUCK chance for successful hits to cause a Soul Explosion, dealing damage and restoring some Cooldown of the Relic"),
("Berserker Waist Guard",'Waist',0,113,31,31,31,31, "Taking damage, Blocking, and Parrying all have a Moderate LUCK chance to cause a Soul Explosion, dealing damage and restoring some Cooldown of the Relic");

INSERT INTO Armors(Title, Category,    -- chest, wrist, waist
Strength, Defence, Runic, Vitality, Cooldown, Luck, Skill)

VALUES("Steinbjörn Plackart",'Chest',280,0,0,0,0,0,"After significant damage is taken, Kratos' attacks will restore some lost Health for a time"),
("Steinbjörn Gauntlets",'Wrist',50,125,0,0,0,0,"Moderate LUCK chance to stagger and inflict Stun damage to nearby enemies when damage is taken. (25% Stun Damage Inflicted alone; 50% w/ Waist Guard)"),
("Steinbjörn Waist Guard",'Waist',0,175,0,0,0,0,"Moderate LUCK chance to stagger and inflict Stun damage to nearby enemies when damage is taken. (25% Stun Damage Inflicted alone; 50% w/ Gauntlets)");

INSERT INTO Armors(Title, Category,    -- chest, wrist, waist
Strength, Defence, Runic, Vitality, Cooldown, Luck, Skill)

VALUES
("Plackart of Fallen Stars",'Chest',80,100,90,30,0,0,"Greatly reduces damage taken when using a Runic Attack or Relic"),
("Bracers of Fallen Stars",'Wrist',113,0,56,19,0,0,"Getting hit while using a Runic Attack or Relic will restore a portion of the Cooldown after use. (15% Cooldown Restored alone; 30% w/ Waist Guard)"),
("Waist Guard of Fallen Stars",'Waist',0,113,56,19,0,0,"Getting hit while using a Runic Attack or Relic will restore a portion of the Cooldown after use. (15% Cooldown Restored alone; 30% w/ Bracers)");

INSERT INTO Armors(Title, Category,    -- chest, wrist, waist
Strength, Defence, Runic, Vitality, Cooldown, Luck, Skill)

VALUES
("Dragon Scaled Breastplate",'Chest',140,140,0,0,0,0,"Blocks and Parries grant a buff of increasing STRENGTH and DEFENSE with each stack. Resets when damage is taken"),
("Bracers of Fallen Stars",'Wrist',137,38,0,0,0,0,"Increases all Shield damage, and successful Blocks or Parries now deal Shield damage to nearby enemies. (25% Shield Damage Increase alone; 50% w/ Girdle)"),
("Dragon Scaled Girdle",'Waist',38,137,0,0,0,0,"Getting hit while using a Runic Attack or Relic will restore a portion of the Cooldown after use. (15% Cooldown Restored alone; 30% w/ Bracers)");

INSERT INTO Armors(Title, Category,    -- chest, wrist, waist
Strength, Defence, Runic, Vitality, Cooldown, Luck, Skill)

VALUES
("Shoulder Guard of Undying Pyres",'Chest',100,80,80,0,40,0,"When the Permafrost, Immolation, or Maelstrom skill gauge is fully charged, Kratos gains a shield that prevents the first hit taken from resetting the gauge"),
(" Bracers of Undying Pyres",'Wrist',113,50,0,0,25,0,"Increases the gain rate of Permafrost, Immolation, and Maelstrom skill gauges. (15% alone, 30% w/ Girdle)"),
("Girdle of Undying Pyres",'Waist',0,113,0,0,25,0,"Increases the gain rate of Permafrost, Immolation, and Maelstrom skill gauges. (15% alone, 30% w/ Bracers)");

INSERT INTO Armors(Title, Category,    -- chest, wrist, waist
Strength, Defence, Runic, Vitality, Cooldown, Luck, Skill)

VALUES
("Hunter's Pauldron",'Chest',100,80,80,0,40,0,"When the Permafrost, Immolation, or Maelstrom skill gauge is fully charged, Kratos gains a shield that prevents the first hit taken from resetting the gauge"),
("Hunter's Gauntlets",'Wrist',131,56,0,0,0,0,"Increases the damage of all of Kratos' Ranged Attacks and Abilities. (10% Ranged Damage Increase alone; 20% w/ Belt)"),
("Hunter's Belt",'Waist',38,94,0,0,56,0,"Increases the damage of all of Kratos' Ranged Attacks and Abilities. (10% Ranged Damage Increase alone; 20% w/ Gauntlets)");

INSERT INTO Armors(Title, Category,    -- chest, wrist, waist
Strength, Defence, Runic, Vitality, Cooldown, Luck, Skill)

VALUES
("Fate Breaker Shoulder Guard",'Chest',100,80,0,90,30,0,"After returning from Rage, get a brief buff to STRENGTH, DEFENCE, RUNIC and Stagger Resistance"),
("Fate Breaker Wraps",'Wrist',113,56,0,0,0,19,"Increases the rate at which Rage is gained. (10% Rage Gain Increase alone; 20% w/ Belt)"),
("Fate Breaker Belt",'Waist',0,113,0,19,0,0,"Increases the rate at which Rage is gained. (10% Rage Gain Increase alone; 20% w/ Wraps)");

INSERT INTO Armors(Title, Category,    -- chest, wrist, waist
Strength, Defence, Runic, Vitality, Cooldown, Luck, Skill)

VALUES
("Surtr's Scorched Cuirass",'Chest',120,100,0,70,0,0,"Kratos' attacks that hit enemies during their attacks do bonus damage"),
(" Surtr's Scorched Arm",'Wrist',138,0,0,44,0,0,"Kratos takes reduced damage and has increased Stagger Resistance during his basic attacks and skills. (20% Damage Reduction alone; 40% w/ Girdle)"),
("Surtr's Scorched Girdle",'Waist',25,112,0,44,0,0,"Kratos takes reduced damage and has increased Stagger Resistance during his basic attacks and skills. (20% Damage Reduction alone; 40% w/ Arm)");

INSERT INTO Armors(Title, Category,    -- chest, wrist, waist
Strength, Defence, Runic, Vitality, Cooldown, Luck, Skill)

VALUES
("Sorrow of Sparta",'Chest',0,0,0,0,0,0,"None"),
("Scars of Sparta",'Wrist',0,0,0,0,0,0,"None"),
("Woe of Sparta",'Waist',0,0,0,0,0,0,"None");

INSERT INTO Armors(Title, Category,    -- chest, wrist, waist
Strength, Defence, Runic, Vitality, Cooldown, Luck, Skill)

VALUES
("Glory of Sparta",'Chest',190,80,0,100,0,0,"None"),
("Pride of Sparta",'Wrist',169,0,0,63,0,0,"None"),
("Mark of Sparta",'Waist',69,100,0,63,0,0,"None");

INSERT INTO Armors(Title, Category,    -- chest, wrist, waist
Strength, Defence, Runic, Vitality, Cooldown, Luck, Skill)

VALUES
("Cuirass of Zeus",'Chest',100,100,80,0,0,0,"Increases Kratos' Melee and Runic Damage by 40%, but increases damage received by 100%. (Stacks with other sources of Divine Edge)"),
("Gauntlets of Zeus",'Wrist',125,0,50,0,0,0,"Increases Kratos' Melee and Runic Damage by 20%, but increases damage received by 40%. (Stacks with other sources of Divine Edge)"),
("War Belt of Zeus",'Waist',0,120,50,0,0,0,"Increases Kratos' Melee and Runic Damage by 20%, but increases damage received by 40%. (Stacks with other sources of Divine Edge)");



SELECT armor_name, strength FROM armors;
SELECT armor_name, defense FROM armors;
SELECT * FROM armors WHERE strength > 100;

CREATE TABLE Relics(
ID INT AUTO_INCREMENT PRIMARY KEY, Title VARCHAR(30), Effect VARCHAR(400), Cooldown VARCHAR(400), Overview VARCHAR(400));

INSERT INTO Relics(Title, Effect, Cooldown, Overview) values("Talisman of Meign", "Grants a bonus to Melee damage for a short duration. Upgrades increase this effects and its duration.", "120 Seconds", "A talisman so precious to the previous owner, they held it close until their last moment. Would they have survived if they had dropped it?"),
("Hilt of Gram", "Grants a burst of Rage and applies Stun to nearby enemies. Upgrades increase the amount of Rage gained,", "120 Seconds", "Once referred to as the Dragon's Bane, Gram isn't what it once was, but will fell many more foes before its days are done."),
("Glaive of Dødher", "Throw a Bifröst chakram that swerves into enemies. Upgrades increase the number of chakrams thrown.", "120 Seconds", "The glaive thrown by the Einherjar is synonymous with death. It's said there is no surface it cannot cut."),
("Hilt of Hofuð", "	Distort space and time by creating a Realm Shift. Upgrades increase the duration of this effect.", "260 Seconds", "The sword once wielded by the Watchdog of the Aesir, Heimdall. It has separated many heads from their bodies."),
("Hilt of Hrotti", "Applies a mark to nearby enemies. Attacking a marked enemy reduces Runic Cooldowns of the equipped weapon. Killing a marked enemy grants a Blessing of Runic. Upgrades increase the duration of the mark.", "180 Seconds", "Said to be kept in Fafnir's Storeroom. It must have been looted before our visit."),
("Hilt of Forsbrandr", "Push enemies back with force and grant an aura of protection. Upgrades increase the duration of this effect.", "120 Seconds", "A sword forged to bring justice, protecting those with righteous cause."),
("Huldra Project", "Turn Mimir's discomfort into a bifröst blast against nearby enemies. Upgrades increase the strength of this effect.", "240 Seconds", "Brok and Sindri carefully measured and constructed a harness to weaponise the Smartest Man Alive."),
("Mótsognir's Call", "Create a shockwave that deals high Stun to surrounding enemies. Upgrades increase the strength of this effect.", "200 Seconds", "Sindri's tuning fork. Somehow it survived Ragnarök"), 
("Hilt of Skofnung", "The sword unleashes its power from the souls within... Upgrades increase the strength of this effect.", "325 Seconds", "The broken hilt of the King Hrólf Kraki. Once known as the sharpest sword in the realm, it houses the souls of the King's 12 bodyguards."),
("Hilt of Angrvaðall", "Slash forward three waves of light that deal increased damage against enemies afflicted with Sonic. Upgrades reduce this ability's cooldown.", "90 Seconds (Level III)","Known as 'The Stream of Anguish', the broken sword hilt of Frithiof is said to burn brightest in war time."),
("Hilt of Dáinsleif", "Slam the ground to create an explosion of Seiðr Poison, leaving behind a hazard. Upgrades increase the amount of hazards.", "200 Seconds", "Formerly the sword of King Högni. It is renowned for creating wounds that never heal."),
("Hilt of Ridill", "Unleash a wave of Shock to electrify enemies. Upgrades increase the area of effect.", "180 Seconds", "It's said the sword once belonged to the Dwarf Reginn. The sword now possesses the power of its former owner."),
("Hilt of Tyrfing", "Charge the sword to sacrifice Health and deal damage based on the amount of Health lost. Upgrades reduce this ability's cooldown.", "35 Seconds (Level III)",	"Tyrfing has a long and bloody history. Perhaps it is better that only the hilt remains");

CREATE TABLE Axe(
ID INT AUTO_INCREMENT PRIMARY KEY, Title VARCHAR(50), Category VARCHAR(50), Strength INT, Defence INT, Runic INT, Vitality INT, Cooldown INT, 
luck INT,Skill VARCHAR(100) );

INSERT INTO Axe (Title, Category, Strength, Defence, Runic, Vitality, Cooldown, lucK, Skill)VALUES
("Wooden Knob", "Knob", 43, 0, 26, 26, 26, 26, "None"),
("The Furious Maul","Maul", 94, 0, 0, 0, 0, 0, "None"),
("Grip of Darkdale (Deluxe Edition Exclusive)", "Grip", 64, 0, 0, 0, 34, 0, "Deadly Awakening"),
("Fortified Frost Knob", "Knob", 43, 0, 0, 0,51,0, "Frost Resolve"),
("Haur's Lucky Knob", "Knob", 43, 0, 0, 0, 0, 51, "Marksman's Stun"),
("Grip of Weighted Recovery", "Grip", 43, 0, 51, 0, 0, 0, "Seized Refresh"), 
("Stonecutter's Knob", "Grip", 68, 34, 0, 0, 0, 0, "Slicing Finish"), 
("Grip of Healing Harmony", "Grip", 43, 51, 0, 0, 0, 0, "Permafrost Lifesteal"),
("Grip of the Fallen Alchemist", "Grip", 43, 0, 0, 34, 0, 34, "Serpent's Health Burst"),
("Grip of Radiant Reflection", "Grip", 60, 0, 26, 0, 26, 0, "Precision Momentum"),
("Banahogg Knob", "Knob", 43, 0, 0, 51, 0, 0, "Bare Force"),
("Runic Hailstone Knob", "Knob", 34, 0, 34, 0, 0, 34, "Prey Upon Frost"),
("Grip of the Nine Realms", "Grip", 0, 0, 38, 0, 38, 38, "Momentous Shift");


CREATE TABLE Blades(
ID INT AUTO_INCREMENT PRIMARY KEY, Title VARCHAR(50), Category VARCHAR(50), Strength INT, Defence INT, Runic INT, Vitality INT, Cooldown INT, 
luck INT, Skill VARCHAR(100));

INSERT INTO Blades(Title, Category, Strength, Defence, Runic, Vitality, Cooldown, lucK, Skill)
VALUES
("Steel Handles (Default)", "Handles", 43, 0, 26, 26, 26, 26, "None"),
("Deadly Obsidian Handles", "Handles", 94, 0, 0, 0, 0, 0, "Slayer's Rage Burst" ),
("Darkdale Handles (Deluxe Edition Exclusive)", "Handles", 64, 0, 0, 0, 0, 34, "Deadly Flames"),
("Cursed Empress Handles", "Handles", 43, 0, 0, 0, 0, 51, "Power of the Empress"),
("Pommels of the Undying Spark", "Pommels", 68, 0, 34, 0, 0, 0, "Scorching Burn"),
("Radiant Warden Handles", "Handles", 43, 0, 0, 0, 51, 0, "Whiplash Deflection"),
("Pommels of Agile Deceit", "Pommels", 43, 0, 0, 51, 0, 0, "Blade Dancer"),
("Pommels of Brutal Might", "Pommels", 43, 51, 0, 0, 0, 0, "Seized Strength"),
("Hardened War Handles", "Handles", 60, 26, 0, 26, 0, 0, "Banishing Blade"),
("Pommels of the True Flame", "Pommels", 34, 0, 43, 0, 34, 0, "Runic Immolation"),
("Pommels of the Nine Realms", "Pommels",0, 0, 38, 38, 0, 38, "Momentous Shift"),
("Pommels of Burning Unity", "Pommels", 43, 0, 51, 0, 0, 0, "Burning Immolation"),
("Luminous Recovery Handles", "Handles", 34, 0, 0, 0, 43, 34, "Whiplash Refresh");

select * from Axe;






ALTER TABLE Armors RENAME COLUMN Stregnth TO Strength ;

ALTER TABLE Armors CHANGE Stregnth Strength INT;

select * from Armors;
select * from Blades;

CREATE TABLE Spear(
ID INT AUTO_INCREMENT PRIMARY KEY, Title VARCHAR(50), Category VARCHAR(50), Strength INT, Defence INT, Runic INT, Vitality INT, Cooldown INT, 
luck INT, Skill VARCHAR(100));

INSERT INTO Spear(Title, Category, Strength, Defence, Runic, Vitality, Cooldown, lucK, Skill)
VALUES
("Soldier's Sauroter (Default)", "Sauroter", 0, 43, 26, 26, 26, 26, "None"),
("Lion's Roar Sauroter", "Sauroter", 0, 94, 0, 0, 0, 0, "Stunning Blast"),
("Charging Assault Sauroter", "Sauroter", 0, 68, 0, 21, 21, 0, "Fearless Sprinter"),
("Mighty Olympic Sauroter", "Sauroter", 0, 26, 0, 0, 51, 34, "Detonator's Might"),
("Hind of Attuned Elements", "Hind", 0, 43, 51, 0, 0, 0, "Extinguish and Vaporise"),
("Battle-Scarred Sauroter", "Sauroter", 0, 60, 0, 43, 0, 0, "Seized Rage Burst"),
("Hind of Weightless Recovery", "Hind", 0, 43, 0, 0, 0, 51, "Maelstrom Refresh" ),
("Hind of Volatile Might", "Hind", 0, 43, 0, 51, 0, 0, "Siphoned Strength"),
("Hind of the Nine Realms", "Hind", 0, 0, 38, 38, 38, 0, "Momentous Shift"),
("Hind of the Four Winds", "Hind", 51, 43, 0, 0, 0, 0, "Slicing Finish"),
("Warrior's Echo Sauroter", "Sauroter", 34, 34, 34, 0, 0, 0, "Sonic Piercer"),
("Hind of Deadly Vitality", "Hind", 0, 43, 0, 0, 34, 34, "Slayer's Health Burst");

select * from Spear;

CREATE TABLE Rönd(
ID INT AUTO_INCREMENT PRIMARY KEY, Title VARCHAR(50), Strength INT, Defence INT, Runic INT, Vitality INT, Cooldown INT, 
luck INT, Skill VARCHAR(100), Perk VARCHAR(100));

INSERT INTO Rönd(Title, Strength, Defence, Runic, Vitality, Cooldown, lucK, Skill, Perk)
VALUES
("Rönd of Volition (Default)", 0, 43, 26, 26, 26, 26, "None", "None"), 
("Rönd of Aggravation", 0, 43, 0, 34, 0, 34, "Riposte Rage Burst","None"),
("Rönd of Expedition", 0, 43, 0, 0, 51, 0, "Riposte Refresh","None"),
("Rönd of Affliction", 0, 43, 34, 0, 34, 0, "Strike of Affliction","None"),
("Rönd of Restoration", 0, 43, 0, 51, 0, 0, "Restoring Shield","None"),
("Rönd of Deflection", 0, 43, 0, 0, 0, 0, "Agile Deflection","None"),
("Rönd of Purification", 51, 43, 0, 0, 0, 0, "Contagion Discharge" ,"None"),
("Rönd of the Nine Realms", 0, 43, 0, 0, 0, 51, "Riposte Realm Shift","None"),
("Rönd of Fortification", 0, 94, 0, 0, 0, 0, "Fortification","None"),
("Rönd of Absorption", 0, 43, 51, 0, 0, 0, "Defender's Momentum", "The Permafrost, Immolation and Maelstrom skill gauges increase when Blocking or Parrying."),
("Rönd of Disruption",  0, 43, 34, 0, 0, 34, "Elemental Storm","None"),
("Rönd of Obliteration", 17, 17, 21, 21, 21, 21, "Shards of the Valkyrie","None");


CREATE TABLE Shield(
ID INT AUTO_INCREMENT PRIMARY KEY, Title VARCHAR(50), Strength INT, Defence INT, Runic INT, Vitality INT, Cooldown INT, 
luck INT, Application VARCHAR(100), Strike VARCHAR(600));

INSERT INTO Shield(Title, Strength, Defence, Runic, Vitality, Cooldown, lucK, Application, Strike)
VALUES
("Guardian Shield", 0, 190, 0, 0, 0, 0, "A shield fit for a balance of defensive options", "Double Tap L1 to quickly Shield Check an enemy and break their guard. Parry (Press L1 right before getting hit) and then immediately Press R1 or R2 to do special counterattacks"), 
("Stone Wall Shield", 0, 190, 0, 38, 0, 0, "None","Double tapping L1 will enact a Shield Slam, launching enemies back when fully charged. Charges are built up by absorbing attacks and up to four charges can be held at a time. Regular attacks build up one charge per attack. When the shield is not fully charged, guard-break attacks can be blocked and build up two charges per attack"),
("Dauntless Shield", 0, 190, 0, 0, 38, 0, "None","Double tapping L1 will enact a Shield Bash for high stun damage. Parry to deal stun to the attacker and empower your next Shield Bash. Perfectly timed parries with Shield Bashes significantly improve this effect"),
("Shatter Star Shield", 0, 190, 38, 0, 0, 0, "None","Holding L1 charges the shield up, up to two charges. Blocking an attack depletes some charge, while Shield Punching right before an attack hits will absorb the attack and gain a burst of charge. Charges also drain if the shield is stowed for too long. Double tapping L1 will enact a Shield Punch and blow enemies backwards, increasing in power when fully charged"),
("Onslaught Shield", 0, 190, 0, 0, 0, 38, "None","Double tapping L1 will enact a Shield Rush, charging forward into an enemy while blocking incoming attacks. Using Shield Rush from a greater distance will launch enemies on impact");

drop table Shield;
select * from Shield;

-- END OF DATA --


