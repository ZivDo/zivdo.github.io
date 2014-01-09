def recieveDmg( _dmg ):
	print( "monster recieveDmg ", _dmg )

monster = {
	"name":"Little Jim",
	"level":1,
	"hp":[100,200,300,400,500],
	"speed":[1, 1.2, 1.4, 1.6, 1.8],
	"recieveDmg":recieveDmg,
}

level = monster["level"]-1

def attack( _target, _dmg ):
	m = _target
	print( "tower attack monster", m["name"] )
	m["recieveDmg"]( _dmg )

tower = {
	"level":1,
	"dmg":[100, 120, 140, 160, 180],
	"range":[0.8, 1, 1.2, 1.4, 1.6],
	"attack":attack,
}

towerDmg = tower["dmg"][tower["level"]]
towerAttack = tower["attack"]( monster, towerDmg )