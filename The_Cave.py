from sys import exit

### Endgame Fuctions ###########################################################

def win(ending):
# Tells the user which ending they got (evil, bad, sad, neutral, or good)
# based on how they interacted with the King.
    print ""
    print "GAME OVER! You've achieved the [{0}] ending.".format(ending)
    print "There are four other endings."
    
    # Prompts the user to try again or exit the game.
    while True:
        print "Play again?"
        print ""
        retry = raw_input("> ").lower()
        
        if retry == "yes" or retry == "y":
            start_rm(False)
        elif retry == "no" or retry == "n":
            print "Press ENTER to exit."
            ready = raw_input("> ").lower()
            exit(0)
        else:
            print "Enter 'Yes' or 'Y' to play again, or 'No' or 'N' to quit."
            continue


def dead():
    print ""
    print "GAME OVER.\n"
    print ""
    print "Play again?"
    print ""
    
    # Prompts the user to try again or exit the game.
    while True:
        retry = raw_input("> ").lower()
        
        if retry == "yes" or retry == "y":
            start_rm(False)
        elif retry == "no" or retry == "n":
            print "Press ENTER to exit."
            ready = raw_input("> ").lower()
            exit(0)
        else:
            print "Enter 'Yes' or 'Y' to play again, or 'No' or 'N' to quit."
            continue


def fight():
# This function.. another day, another commit. I apologize to anyone reading this.
# The essential structure is simple though.
# Before the next prompt, the a while loop begins, allowing the user to fail to
# answer as many times as they want.
# Next, the prompt, and then, the various dialogue paths.
    while True:
        print "The spear is no longer yours to command. Without a weapon, he will surely kill you."
        next = raw_input("> ").lower()
        
        if "flee" in next or "leave" in next:
            print "If you try to squeeze through the doors again, the King will surely kill you."
            print "There's only one way out of this."
            continue
        
        elif "spear" in next:
            print "The spear is no longer yours to command. Without a weapon, he will surely kill you."
            print "The King raises his arm high, preparing to strike."
            
            
        elif "attack" in next or "kill" in next:
            print "You charge at the King wielding nothing but fists and rage."
            print "The King is prepared, and plunges the spear deep into you."
            dead()
            
        elif "search" in next or "find weapon" in next or "get weapon":
            print "Where do you want to search for a weapon?"
            
            while True:
                next = raw_input("> ").lower()
                if "guard" in next or "corpse" in next or "body" in next or "bodies" in next:
                    print "You scramble to a nearby corpse, searching for anything usable."
                    print "You find a Guard's Shortsword! The King raises his arm vertically, preparing to strike."
                    
                    while True:
                        next = raw_input("> ").lower()
                        if "attack" in next or "kill" in next or "sword" in next:
                            print "You swing your Guard's Shortsword at the King, but you are too slow."
                            print "The King's vertical strike impales you. Perhaps if you had dodged.."
                            dead()
                        elif "dodge" in next or ("jump" in next and "side" in next):
                            print "You dodge to the side just in time for the King's spear to pierce the floor."
                            print "The spear is lodged in the floor."
                            while True:
                                next = raw_input("> ").lower()
                                if "attack" in next or "kill" in next or "sword" in next:
                                    print "You swing hard at the disadvantaged King, slashing his side."
                                    print "The King screams in agony. \"DAMN YOU! I\'LL KILL YOU!\""
                                    print "The King takes a step towards you, but he collapses on one knee."
                                    print '"Just kill me already! You monsters have taken everything else from me."'
                                    print "Kill or spare the King, or flee while you can."
                                    while True:
                                        next = raw_input("> ").lower()
                                        if "attack" in next or "kill" in next or "sword" in next:
                                            print '"You approach the King, sword at your side. "Wait.. no, no. It cannot be.." he begins.'
                                            print 'You raise your sword high. "WAIT, NO STO-" You strike the King down.'
                                            print ""
                                            print 'With his dying breath, the King whispers.. "My daughter.. why.."'
                                            win("bad")
                                            ### BAD ENDING ###
                                        elif "wait" in next or "spare" in next or "stop" in next or "don't attack" or "don't kill" in next:
                                            print '"What.. why.. why won\'t you just kill me.."'
                                            print '"Oh my god.. you.. you\'re.."'
                                            print ""
                                            print '"my.. daughter.."'
                                            print "The King is dead."
                                            print ""
                                            print "Now however, a large ornate metal gate stands where before stood stone wall."
                                            print "It's open. And you can see moonlight."
                                            win("sad")
                                            ### SAD ENDING ###
                                        elif "flee" in next or "leave" in next:
                                            print "While the King is mortally wounded, you take your chance and flee."
                                            print "Upon exploring the room, you discover a gate, magically hidden and sealed."
                                            print "You have no idea how to open it."
                                            print "While you fled, the King whispered his last words.."
                                            print ""
                                            print "Guess you'll have to find another way out."
                                            win("neutral")
                                            ### NEUTRAL ENDING ###
                                        else:
                                            print "I didn't understand that."
                                            continue
                                elif "flee" in next or "leave" in next:
                                    print "Now's your chance! You bolt for the golden doors."
                                    print "And with a twang, the spear pins you to them."
                                    dead()
                                
                                else:
                                    print "I didn't understand that."
                                    continue
                                
                        else:
                            print "I didn't understand that."
                            continue
                else:
                    print "You look, but there's nothing of use."
                    print "It's too late.. the King plunges the spear deep into you."
                    dead()
        else:
            print "I didn't understand that."
            continue


def good():
    # At this point, no matter what the user answers, they'll get the good 
    # ending.
    print '".."'
    print '"Who are you?"'
    print ""
    print "[You do not know.]"
    print ""
    print "The King walks towards you. In the dim torchlight, you can tell he's mostly blind."
    print '"Where did you get that spear?"'
    
    while True:
        next = raw_input("> ").lower()
        if "monster" in next or "spider" in next or "nightmare" in next or "centipede" in next or "creature" in next or "killed" in next:
            print '"You.. you killed one of them?"'
        elif "armory" in next:
            print '"You.. you found it in the old armory?"'
        elif "found" in next:
            print '"You.. you just found it?"'
        else:
            print '"I\'m not sure what you mean.."'
            continue
        
        print "The King walks very close to you."
        print '"That\'s.. it can\'t be.."'
        print ""
        print "The King is inches away from you, his eyes desperately searching yours."
        print "Then he embraces you, with tears in his eyes."
        print '"My daughter.. I\'m so sorry.. I thought I\'d lost you.."'
        print '"Thank you."'
        print ""
        print "You close your eyes, and just like that, the King is gone."
        print "Now however, a large ornate metal gate stands where before stood stone wall."
        print "It's open. And you can see sunlight."
        ### GOOD ENDING ###
        win("good")


### Room Functions (Start Room, Trap Room, etc.) ###############################


def start_rm(r_blocked):
    if r_blocked == True:
        print "You're back in the cave."
    else:
        for x in range(0,3):
            print ""
        print "You wake up in a dark cave."
        print "Before you are two ancient metal doors."
        print "The left door is covered in thick, mucousy cobwebs."
        print "The right door is seeping blood."
    
    while True:
        next = raw_input("> ").lower()
        print ""
        
        if next == "king":
            throne_rm()
            # debugging cheat code
        elif "left" in next:
            spider_rm()
        elif "right" in next:
            if r_blocked == True:
                print "The door lays bent on the ground."
                print "The entry is blocked by the destroyed stone trap."
                continue
            else:
                trap_rm()
        else:
            print "I didn't understand that."
            continue


def trap_rm():
    print "As soon as you release the metal door behind you, it slams shut."
    print "You notice a mangled skeleton in the corner, and realize too late."
    print "Exposed gears in the wall screech as the spiked cieling begins to descend."
    print "You can either try to block the gears or pry the door open."
    
    while True:
        next = raw_input("> ").lower()
        print ""
    
        if "block" in next or "gears" in next:
            print "Using what?"
            next = raw_input("> ").lower()
            print ""
            
            if "skeleton" in next or "bone" in next:
                print "You tear a femur from the nearby corpse, and jam it in the gears."
                print "The bone is too brittle, and is shattered by the immense machinery."
                print "You frantically look around for something else, anythi-."
                print "The stone cieling impales you instantly."
                dead()
            else:
                print "It doesn't work."
                print "You frantically look around for something else, anythi-."
                print "The stone cieling impales you instantly."
                dead()
        elif "pry" in next or "door" in next:
            print "There's no handle in sight, and the door is locked."
            print "However, its hinges are ancient and worn."
            print "With a hefty kick, the door collapses outward."
            print "You leap out just as the cieling crashes to the floor."

            start_rm(True)
        else:
            print "I didn't understand that."
            continue


def spider_rm():
    print "The door makes a revolting, moist, sound as you push it open."
    print "Cobwebs cover nearly every surface of what used to be an armory."
    print "You sigh a relief at the absence of corpses. Torchlight is visible to your left."
    print "A glint of light catches your eye from your right though.."
    
    while True:
        next = raw_input("> ").lower()
        print ""
        
        if "torchlight" in next or "left" in next or "torch" in next:
            print "You power forward towards the warm glow."
            castle_rm(False, True, False)
        elif "glint" in next or "right" in next:
            print "The twinkling light grows brighter as your approach."
            print "Just as you begin to make it out, you're deafened by a hoarse shriek."
            print "A jet-black, fleshy creature with dozens of legs is barreling down to you."
            print "Investigate the contents of the webs, or flee?"
            
            while True:
                next = raw_input("> ").lower()
                print ""
                
                if "flee" in next:
                    print "You run as hard as you can, but its legs are blindingly fast."
                    print "You turn your head to see, and your cheek brushes wet flesh."
                    print "Its face is nearly human. You don't have time to scream."
                    dead()
                elif "inv" in next or "web" in next or "content" in next:
                    print "You dive forward just in time to hear an enormous, wet, impact."
                    print "In front of you lies an ornate metal spear, with a leather sash."
                    print "It's warm to the touch."
                    while True:
                        next = raw_input("> ").lower()
                        print 
                        if "flee" in next or "leave" in next or "run" in next:
                            print "You stumble away from the artifact, and into the creature."
                            print "Its face is nearly human. You don't have time to scream."
                            dead()
                        elif "take" in next or "grab" in next:
                            print "You grab it with both hands, and feel the webs fade from your skin."
                            print "You charge forward, sinking the speartip into the creature."
                            print "An awful, shrill, cry fills the air as web-mucous spews violently from the wound."
                            print "You run as fast as you can towards a lit opening in a stone wall."
                            castle_rm(True, True, False)
                        else:
                            print "I didn't understand that."
                            continue
                else:
                    print "I didn't understand that."
                    continue
        elif "light" in next:
            print "Which light do you want to go towards?"
            continue
        elif "spear" in next:
        # My favorite line
            print "What spear?"
            continue
        else:
            print "I didn't understand that."
            continue


def castle_rm(spear, first_time, trap_blocked):
    if first_time == True:
        print "Muffled impacts from behind you shake the walls. Poom. Poom."
        print "A large brick, then another, then the whole opening collapses behind you."
        if spear == True:
            print "You shoulder the ornate spear."
        print ""
        print "You stop for a moment, in awe. You find yourself in a long, stone, arcade."
        print "The arched passage surrounds a great hall, long abandoned. Moonlight beams"
        print "down in thin rays through small, vertical, windows below a tiled vault cieling."
        print ""
        print "Across the hall, in the shadow of the arcade, sits a small wooden door."
        print "A recently built scaffold of wooden machinery snakes up the walls to the vault."
        print "A conspicuous lever protrudes from the machinery, at chest height."
    else:
        print "You are back in the great hall."
        if trap_blocked == True:
            print "The trap has been destroyed. Behind its remains lies a golden door."
    while True:
        next = raw_input("> ").lower()
        print ""
        
        if "door" in next:
            dungeon_rm(spear, False)
        elif "lever" in next:
            if trap_blocked == True:
                print "The lever is already flipped. The trap is destroyed."
                continue
            else:
                print "With surprisingly little effort, you flip the lever down."
                print "You are immediately met with the whipping sound of rope untwining."
                print "You've no idea where the trap will spring. Dodge out of the way?"
            if spear == True:
                print "You feel a warmth radiate from your back."
            
            while True:
                next = raw_input("> ").lower()
                print ""
                
                if spear == False and "spear" in next:
                    print "What spear?"
                    continue
                elif spear == True and "spear" in next:
                    print "You grab hold of the spear and launch it into the machinery."
                    print "The spear flies into the wood with a loud crack, slashing the rope."
                    print "You're blasted with air as an enourmous spike crashes to the floor"
                    print "inches behind you, its limp pendulum severed."
                    print ""
                    print "As the dust settles, a pair of huge golden doors is revealed behind ripped-off boards."
                    
                    while True:
                        next = raw_input("> ").lower()
                        print ""
                        
                        if "wooden" in next and "door" in next:
                            dungeon_rm(spear, True)
                        elif "gold" in next:
                            throne_rm()
                        elif "door" and not ("wooden" in next or "golden" in next):
                            print "Which door?"
                            continue
                        else:
                            print "I didn't understand that."
                            continue
                elif "dodge" in next or "yes" in next or "yeah" in next:
                    print "You dodge backwards.. right into the enormous swinging spike."
                    dead()
                else:
                    print "I didn't understand that."
                    continue
        
        else:
            print "I didn't understand that."
            continue


def dungeon_rm(spear, trap_blocked):
    print "As you push open the wooden door, you notice the smell first."
    print "It's faded, masked by humid old stone, but there's no mistaking the smell of death."
    print "You see the shackles on the wall, and realize you must be in the castle's dungeon."
    print "Piles of bone and rot sit below empty locked shackles, long since decomposed."
    print "One corpse, however, still hangs. Search it?"
    
    while True:
        next = raw_input("> ").lower().lower()
        print ""
        if "yes" in next or "yeah" in next or "search" in next or "corpse" in next:
            print "You approach the corpse to see if it has anything of use."
            print "As soon as you do, its porous, jet-black, face twists up to meet yours."
            print '"Aaahhh.. yess.. a vistor, yes, hmmm? It\'ssss been ssso long."'
            print '"Would you like to know my sssecretsss, yesss?"'
            print "Do you accept, reject, or attack the corpse?"
            # read:"How would you like to die?"
            
            while True:
                next = raw_input("> ").lower().lower()
                print ""
                
                if "attack" in next:
                    if spear == True:
                        print "In a swift move, you brandish your metal spear. It's cool to the touch."
                        print '"Whaat?! WHAT are you doing? How DARE YOU I\'LL KILL YOU!"'
                        print "The corpse roars as its chest collapses, revealing rows of serrated teeth."
                        print "As it does, your spear surges with heat, and plunges itself forward."
                        print "The monster shrieks in pain, but it's too close already. It sinks its teeth into you."
                        dead()
                    else:
                        print "You grab the corpse's head and smash it against the wall. Its spongey skull splatters on the wall."
                        print "The corpse shrieks from a place you can't tell as you lean back to kick it in the chest."
                        print "As you do, your leg plunges straight through. Rows of serrated teeth sink into you."
                        dead()
                elif "yes" in next or "accept" in next:
                    print "Mmmm.. vvverry goooood.."
                    print "The corpse smiles a toothless smile, and you feel a sudden pain-"
                    print "its legs clasp around you with incredible strength."
                    print "The corpse's chest opens with a wet crack to reveal rows of serrated teeth."
                    dead()
                elif "no" in next or "n" in next or "reject" in next:
                    print '"Mmmm.. but you ssseee.. I don\'t care.." the corpse cackles.'
                    print "The corpse smiles a toothless smile, and you feel a sudden pain-"
                    print "its legs clasp around you with incredible strength."
                    print "The corpse's chest opens with a wet crack to reveal rows of serrated teeth."
                    dead() 
                else:
                    print "I didn't understand that."
                    continue
        elif ("no" or "leave" or "flee") in next:
            print "Perhaps some things are better left hidden.."
            castle_rm(spear, False, trap_blocked)
        else:
            print "I didn't understand that."
            continue


def throne_rm():
    print "The golden doors only give a few inches, evidently barricaded from the other side."
    print "You unshoulder your spear to try and reach through and pry the doors free"
    print "when you realize it's warmer than you've yet felt it. In fact, it seems to glow dimly."
    print "Once in place, you ram the spear with your shoulder and the doors break free."
    print ""
    print "Inside, you see the barricade: a large wood-carved throne, splintered and knocked over."
    print "The Throne Room is scattered with fallen guard, long since decomposed and fused to the floor."
    print '"You\'re one of Them.." a voice says from the shadows. "You\'ve finally come to take my life."'
    
    # This x counts the number of times the user has entered an unknown answer
    # to trigger the evil ending. Once x == 3, all other endings are locked out.
    x = 0
    while True:
        next = raw_input("> ").lower()
        print ""
             
        if "attack" in next or "kill" in next or "spear" in next:
            if instakill == True:
                print "You walk towards the defeated King. He makes no reaction, save to sob silently."
                print "You pick up the spear, which is slowly rolling on the smooth stone floor."
                print "It's cold to the touch, and feels heavier somehow."
                print ""
                print 'You raise the spear, preparing to strike. "Just do it, demon." says the King.'
                print 'You stab the spear into the King. "Finally.." he whispers hoarsely.'
                print ""
                print "As the blood begins to run from the King's body, it begins to darken."
                print "Darkening more and more until it becomes thick, and jet-black."
                print "It runs deeper and deeper, more than the King could possibly hold."
                print "It swallows the floor."
                print "Then the walls."
                print ""
                print "Then you."
                win("evil")
                ### EVIL ENDING ###
            else:
                print "You charge at the King wielding nothing but fists and rage."
                print "The King is prepared, and plunges the spear deep into you."
                dead()
        elif x >= 3:
            print "The King makes no reaction.. he is truly defeated."
            print "What are you going to do?"
            continue
        
        elif x >= 4:
            print "Just put him out of his misery. Finish what you started."
            continue            
        elif "i don't know" in next or "i dont know" in next:
            print '"YOU DON\'T KNOW?! YOU DON\'T.. you don\'t know.."'
            print '"And I\'m supposed to believe that?"'
            
            while True:
                next = raw_input("> ").lower()
                
                if "i don't know" in next or "i dont know" in next:
                    good()
        
        elif "yes" in next or "I have" in next or "I am" in next:
            print '"Then finish what you started, vile creature. If you can."'
            print "A hand shoots out from the shadows, outstretched, and your spear flies to its grip."
            print "The King emerges from the shadows. What will you do?"
            
            fight()

######## MIXED #################################################################

        elif "no" in next or "i'm not" in next or "not true" in next:
            print '"You lie! I\'ll kill you, every last one of you!"'
            next = raw_input("> ").lower()
            if "attack" in next or "kill" in next or "spear" in next:
                print "You charge towards the King with both hands on the spear."
                print '"Very well." says the King, with weary relief in his voice.'
                print "Just as you reach the King, the spear flies from your hands and into his."
                print '"Do your best, vile creature."'
                fight()
                
            elif "stop" in next or "dont" in next or "don't" or "truth" in next or "i'm not" in next or "lying" in next:
                good()
            else:
                print "I didn't understand that."
                continue
            
        elif "who are you" in next:
            print '"You mock me, creature? You know exactly who I am. I care not for your games."' 
            print '"I wish only to join my loved ones."'
            next = raw_input("> ").lower()
            print ""
            
            if "attack" in next or "kill" in next or "spear" in next:
                print "You charge towards the King with both hands on the spear."
                print '"Very well." says the King, with weary relief in his voice.'
                print "Just as you reach the King, the spear flies from your hands and into his."
                print '"Do your best, vile creature."'
                
                fight()
                
            elif "where are" in next:
                print '"WHERE ARE THEY? THEY.. they\'re dead. All dead.. I couldn\'t save them."'
                good()
            elif "what happened" in next:
                print '"WHAT HAPPENED? WHAT.. what happened.. they\'re all dead.. I couldn\'t save them."'
                good()
            elif "who are you" in next:
                print '"WHO AM I? WHO.. am I.. I am a failure. I couldn\'t save them.. any of them."'
                good()
                
######## GOOD ##################################################################             
        
        elif ("who are they" in next or "who's they" in next or "whos they" in next or "i don't want" in next 
        or "please don't" in next or "i'm not" in next or "lying" in next or "they?" in next):
            print '"WHO ARE THEY? DO YOU JEST, YOU.. you.." screams the King.'
            print '"You.. really have no idea? You\'re really not one of Them?"'
            print "[You shake your head.]"
            print '"We have no name for Them. Unnatural creatures.. manifestations of death."'
            print '"They.. They killed everyone.. I\'m.. the only one left. I\'m sorry. I do not wish to continue."'
            good()
            
######## EVIL COUNTER ##########################################################            
        else:
            x += 1
            if x == 1:
                print '"I do not understand.."'
                print "A hand shoots out from the shadows, outstretched, and your spear flies to its grip."
                print '"Speak clearly. Are you here to kill me?."'
                continue
            elif x == 2:
                print '"ENOUGH RIDDLES! Haven\'t I suffered for long enough? An ETERNITY! An eternity"'
                print '"I\'ve spent, waiting to be freed from this cursed loneliness."'
                print '"Just give me a straight answer! Please.. is this the end.."'
                continue
            elif x == 3:
                words = (next).split()
                wordcount = len(next)
                if next == "":
                    print '"Silence.. just.. silence."'
                elif wordcount == 1:
                    zero = next
                    print '"{0}.." the voice struggles to understand your cruel riddles.'.format(zero)
                elif wordcount == 2:
                    zero = words[0]
                    one = words[1]
                    print '"{0}.. ..{1}.." the voice struggles to understand your cruel riddles.'.format(zero, one)
                elif wordcount == 3:
                    zero = words[0]
                    one = words[1]
                    two = words[2]
                    print '"{0}.. ..{1}.." the voice struggles to understand your cruel riddles.'.format(zero + one, two)
                else:
                    zero = words[0]
                    one = words[1]
                    two = words.pop()
                    print '"{0}.. ..{1}.." the voice struggles to understand your cruel riddles.'.format(zero + " " + one, two)
                
                print "The spear clatters as it hits the stone floor. The sound echoes through the room."
                print "The King emerges from the shadows, and collapses onto his knees."
                print '"I do not comprehend your sick games.. please.. just kill me.."'
                instakill = True
                continue
            elif x > 4:
                print '".."'
                continue




### Start of Actual Program ####################################################

start_rm(False)