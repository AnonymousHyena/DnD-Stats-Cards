from db_setup import *

from sqlalchemy.orm import sessionmaker

DBSession = sessionmaker(bind = engine)
session = DBSession()

if __name__ == '__main__':
    session.query(Creatures).delete()
    #name stamina armor damage accuracy skill stats
    #Creatures
    creature = Creatures('Goblin',7,15,5,4,2,[-1,2,0,0,-1,-1])
    session.add(creature)
    creature = Creatures('Goblin-Boss',21,17,10,4,2,[0,2,0,0,-1,0])
    session.add(creature)
    creature = Creatures('Orc',15,13,9,5,2,[3,1,3,-2,0,0])
    session.add(creature)
    creature = Creatures('Twig-Blight',4,13,3,3,2,[-2,1,1,-3,-1,-4],
    	immunities='blinded, deafened',
    	notes='blindsight, Weak to Fire')
    session.add(creature)
    creature = Creatures('Needle-Blight',11,12,7,3,2,[1,1,1,-3,-1,-4],
    	immunities='blinded, deafened',
    	notes='blindsight')
    session.add(creature)
    creature = Creatures('Vine-Blight',26,12,9,4,2,[2,-1,2,-3,0,-4],
        immunities='blinded, deafened',
        notes='blindsight, false appearance')
    session.add(creature)
    creature = Creatures('Dryad',22,11,8,2,2,[0,1,0,2,2,4],
        resistances='magic',
        notes='Moves through trees, Watch appearance')
    session.add(creature)
    creature = Creatures('Faerie-Dragon',14,15,1,7,2,[-4,5,1,2,1,3],
        resistances='magic',
        notes='invisible, telepathic, master of illusion, color dictates age: red, orange, yellow, green, blue, indigo, violet')
    session.add(creature)
    creature = Creatures('Hobgoblin',11,18,13,3,2,[1,1,1,0,0,-1],
        notes='expert fighters in groups')
    session.add(creature)
    creature = Creatures('Ice-Mephit',21,11,5,3,2,[-2,1,0,-1,0,1],
        vulnerabilities='bludgeoning, fire',
        immunities='cold poison',
        notes='explode on death, indistinguisable from an ice shard if motionless')
    session.add(creature)
    creature = Creatures('Worg',26,13,10,5,2,[3,1,1,-2,0,-1],
        notes='good at tracking')
    session.add(creature)
    #NPCs
    creature = Creatures('Jakka',128,24,56,12,4,[6,5,7,1,7,4],
        resistances='fire, cold, magic',
        notes='utilizes ice as armor, avoid hits at all cost')
    session.add(creature)
    #Characters
    #name stamina armor damage accuracy skill stats
    creature = Creatures('Ivar-the-Black',11,18,11,6,2,[7,1,1,1,3,5],
        resistances='fire')
    session.add(creature)
    creature = Creatures('Pitaa-Polla',9,15,8,5,2,[2,5,1,0,2,1])
    session.add(creature)
    creature = Creatures('Armodios-Fostiras',12,16,7,6,2,[0,0,3,1,6,1],
        resistances='poison')
    session.add(creature)
    creature = Creatures('Oya',21,14,15,5,2,[-1,5,1,2,1,2],
            resistances='charm',
            immunities='magical sleep')
    session.add(creature)
    creature = Creatures('Alektor',10,14,8,5,2,[4,5,0,0,3,-1])
    session.add(creature)
    creature = Creatures('Loramae',22,15,9,9,2,[5,6,3,1,4,1])
    session.add(creature)
    creature = Creatures('Mua',25,13,10,6,2,[-1,2,2,-1,2,6],
        resistances='fire')
    session.add(creature)


    session.commit()