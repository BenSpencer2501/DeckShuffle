from cards import cards

import random




def deck():
    modern_robots=[
    cards("mox opal1", "0", "legendary artifact", "mirroden", "card text", None),
    cards("mox opal2", "0", "legendary artifact", "mirroden", "card text", None),
    cards("mox opal3", "0", "legendary artifact", "mirroden", "card text", None),
    cards("mox opal4", "0", "legendary artifact", "mirroden", "card text", None),

    cards("memnite1",  "0", "artifact creature", "mirroden", "card text", "1/1"),
    cards("memnite2",  "0", "artifact creature", "mirroden", "card text", "1/1"),
    cards("memnite3",  "0", "artifact creature", "mirroden", "card text", "1/1"),
    cards("memnite4",  "0", "artifact creature", "mirroden", "card text", "1/1"),

    cards("vault skirge1", "1,PBA", "artifact creature", "phyrexia", "flying.lifelink", "1/1"),
    cards("vault skirge2", "1,PBA", "artifact creature", "phyrexia", "flying.lifelink", "1/1"),
    cards("vault skirge3", "1,PBA", "artifact creature", "phyrexia", "flying.lifelink", "1/1"),
    cards("vault skirge4", "1,PBA", "artifact creature", "phyrexia", "flying.lifelink", "1/1"),

    cards("arcbound ravager1", "2", "artifact creture", "old thingy mabob", "not typing that", "1/1"),
    cards("arcbound ravager2", "2", "artifact creture", "old thingy mabob", "not typing that", "1/1"),
    cards("arcbound ravager3", "2", "artifact creture", "old thingy mabob", "not typing that", "1/1"),
    cards("arcbound ravager4", "2", "artifact creture", "old thingy mabob", "not typing that", "1/1"),

    cards("signal pest1", "1", "artifact creature", "mirroden", "battle cry BS flying", "0/1"),
    cards("signal pest2", "1", "artifact creature", "mirroden", "battle cry BS flying", "0/1"),
    cards("signal pest3", "1", "artifact creature", "mirroden", "battle cry BS flying", "0/1"),
    cards("signal pest4", "1", "artifact creature", "mirroden", "battle cry BS flying", "0/1"),

    cards("ornithropter1", "0", "artifact creature", "mirroden", "flying", "1/1"),
    cards("ornithropter2", "0", "artifact creature", "mirroden", "flying", "1/1"),
    cards("ornithropter3", "0", "artifact creature", "mirroden", "flying", "1/1"),
    cards("ornithropter4", "0", "artifact creature", "mirroden", "flying", "1/1"),

    cards("darksteel forge1", None, "artifact land", "some", None, None),
    cards("darksteel forge2", None, "artifact land", "some", None, None),
    cards("darksteel forge3", None, "artifact land", "some", None, None),
    cards("darksteel forge4", None, "artifact land", "some", None, None),

    cards("crainal plating1", "2", "artifact", "time spiral", "make big boi", None),
    cards("crainal plating2", "2", "artifact", "time spiral", "make big boi", None),
    cards("crainal plating3", "2", "artifact", "time spiral", "make big boi", None),
    cards("crainal plating4", "2", "artifact", "time spiral", "make big boi", None),

    cards("springleaf drum1", "1", "artifact", "born of the gods", "mana fix", None),
    cards("springleaf drum2", "1", "artifact", "born of the gods", "mana fix", None),
    cards("springleaf drum3", "1", "artifact", "born of the gods", "mana fix", None),
    cards("springleaf drum4", "1", "artifact", "born of the gods", "mana fix", None),

    cards("galvanic blast1", "R", "instant", "mirroden", "dmg ham", None),
    cards("galvanic blast2", "R", "instant", "mirroden", "dmg ham", None),
    cards("galvanic blast3", "R", "instant", "mirroden", "dmg ham", None),
    cards("galvanic blast4", "R", "instant", "mirroden", "dmg ham", None),

    cards("thoughtcast1", "4,BU","instant", "mirroden", "draw for me", None),
    cards("thoughtcast2", "4,BU","instant", "mirroden", "draw for me", None),
    cards("thoughtcast3", "4,BU","instant", "mirroden", "draw for me", None),
    cards("thoughtcast4", "4,BU","instant", "mirroden", "draw for me", None),

    cards("etched champion1", "3", "artifact creature", "mirroden", "i dont die", None),
    cards("etched champion2", "3", "artifact creature", "mirroden", "i dont die", None),
    cards("etched champion3", "3", "artifact creature", "mirroden", "i dont die", None),
    cards("etched champion4", "3", "artifact creature", "mirroden", "i dont die", None),

    cards("emry lurker of the loch1", "2, BU","legendary creture", "mirroden", "give me all the things", "1/2"),
    cards("emry lurker of the loch2", "2, BU","legendary creture", "mirroden", "give me all the things", "1/2"),
    cards("emry lurker of the loch3", "2, BU","legendary creture", "mirroden", "give me all the things", "1/2"),
    cards("emry lurker of the loch4", "2, BU","legendary creture", "mirroden", "give me all the things", "1/2"),

    cards("glimmer void1", None, "legendary land", None, "sac unless u have robots", None),
    cards("glimmer void2", None, "legendary land", None, "sac unless u have robots", None),
    cards("glimmer void3", None, "legendary land", None, "sac unless u have robots", None),
    cards("glimmer void4", None, "legendary land", None, "sac unless u have robots", None),

    cards("dispatch1", "W", "instant", "new phyrexia", "goodbye sucker", None),
    cards("dispatch2", "W", "instant", "new phyrexia", "goodbye sucker", None),
    cards("dispatch3", "W", "instant", "new phyrexia", "goodbye sucker", None),
    cards("dispatch4", "W", "instant", "new phyrexia", "goodbye sucker", None),
    ]
    return modern_robots    
#number_of_ele=len(modern_robots)
#print(modern_robots[3])
#print(modern_robots[3:5])

