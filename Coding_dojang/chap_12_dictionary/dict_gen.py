d=dict(health=490, mana=334, melee=550,armor=18.72)
print(d)
d=dict(zip(['h','m','me','armor'],[490,334,550,18.72])) #tuple로 넣어도 가능
print(d)
d=dict([('health',490),('mana',334),('melee',550),('armor',18.72)])
print(d)
d= dict({'health': 490, 'mana': 334, 'melee': 550, 'armor': 18.72})
print(d)