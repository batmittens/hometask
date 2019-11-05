paul = "When this film first came out in 1980, I remember going to see it on opening night. \
This movie just scared the life out of me, which is what still happens every time I rent the video for a re-watch. \
I have seen The Shining at least six or seven times, and I still believe it to be simultaneously and paradoxically one of the most \
frightening and yet funniest films I've ever seen. Frightening because of the extraordinarily effective use of long shots\
 to create feelings of isolation, convex lens shots to enhance surrealism, and meticulously scored music to bring tension levels to virtually\
  unbearable levels. And \"funny\" because of Jack Nicholson's outrageous and in many cases ad-libbed onscreen antics.\
   It never ceases to amaze me how The Shining is actually two films in one, both a comedy AND a horror flick. \
   Ghostly apparitions of a strikingly menacing nature haunt much of the first half of the film, which gradually \
   evolve into ever more serious physical threats as time progresses. Be that as it may, there is surprisingly little \
   violence given the apparent intensity, but that is little comfort for the feint of heart as much of the terror is more\
    implied than manifest. The Shining is a truly frightening movie that works symbolically on many levels, but is basically \
    about human shortcomings and the way they can be exploited by unconscious forces combined with weakness of will.\
     This film scares the most just by using suggestion to turn your own imagination against you. The Shining is a\
      brilliant cinematic masterpiece, the likes of which have never been seen before or since. Highly, highly recommended."
import string
paul = "".join(i for i in paul if i not in string.punctuation)
paul = paul.lower()
paul = paul.split()
new1 = []
for x in paul:
    if x not in new1:
        new1.append(x)
pauln = (len(new1))

jane = "Chilling, majestic piece of cinematic fright, this film combines all the great elements of an intellectual thriller,\
 with the grand vision of a director who has the instinctual capacity to pace a moody horror flick within the realm of his filmmaking\
  genius that includes an eye for the original shot, an ice-cold soundtrack and an overall sense of dehumanization. This movie cuts through\
  all the typical horror movies like a red-poker through a human eye, as it allows the viewer to not only feel the violence and psychosis of\
   its protagonist, but appreciate the seed from which the derangement stems. One of the scariest things for people to face is the unknown \
   and this film presents its plotting with just that thought in mind. The setting is perfect, in a desolate winter hideaway. The quietness\
    of the moment is a character in itself, as the fermenting aggressor in Jack Torrance's mind wallows in this idle time, and breeds the\
     devil's new playground. I always felt like the presence of evil was dormant in all of our minds, with only the circumstances \
     of the moment, and the reasons given therein, needed to wake its violent ass and pounce over its unsuspecting victims. \
     This film is a perfect example of this very thought. "
jane = "".join(a for a in jane if a not in string.punctuation)
jane = jane.lower()
jane = jane.split()
new2 = []
for y in jane:
    if y not in new2:
        new2.append(y)
janen = (len(new2))


kate = "What can I say about the scariest movie I have ever seen that has not already been said by others more articulate than yours truly? \
Do not view this film expecting to see a screen version of the Stephen King novel. Rather, this is a Stanley Kubrick film, \
and to fully appreciate it one should judge it within the context of Kubrick's entire body of work as a serious filmmaker. Thematically, \
THE SHINING relates most closely to 2001: A SPACE ODYSSEY, though flourishes of PATHS OF GLORY, A CLOCKWORK ORANGE and BARRY LYNDON \
do manage to figure prominently in the film's overall technique. In a nutshell (no pun intended), Jack Nicholson and Shelly Duvall\
 co-star with Oregon's Timberline Lodge - enlisted to portray the exterior of the Overlook Hotel - in a story that appears on the surface\
  to be about ghosts and insanity, but deals with issues of child abuse, immortality and duality. What the film might lack initially in\
   terms of coherence is more than made up for in technique. Garrett Brown (the male voice in those old Molson Golden commercials), \
   inventor of the Steadicam, chases young Danny Lloyd through hotel corridors and an amazing snow maze, providing magic-carpet-ride\
    fluidity to scenes that ten years earlier would have been impossible to accomplish. If the film starts off too slow, remember who \
    the director is. This man likes to take his time, and the results are well worth it: incredible aerial shots of the Overlook Hotel;\
     horrific Diane Arbus-inspired twins staring directly at us; portentous room 237 and its treasure trove of terrible secrets; \
     elevators that gush rivers of blood in slow-motion; Jack Torrance's immortality found via the hotel (akin to David \
     Bowman'\s journey through the Space Gate); and some of the best use of pre-existing music ever assembled for a motion picture."
kate = "".join(b for b in kate if b not in string.punctuation)
kate = kate.lower()
kate = kate.split()
new3 = []
for z in kate:
    if z not in new3:
        new3.append(z)
katen = (len(new3))


nick = "I was never a big fan of horror movies. They usually try cheap tricks to scare their audiences like loud noises and creepy children.\
 They usually lack originality and contain overacting galore. The only horror movie i like was Stir of Echoes with Kevin Bacon. \
 It was well-acted, and had a great story. But it has been joined and maybe even surpassed by Stanley Kubrick's The Shining, \
 quite possibly the scariest movie ever. The movie follows a writer (Jack Nicholson) and his family who agree to watch over a hotel\
  while it is closed for the winter. There were rumors of the place being haunted and the last resident went crazy and murdered his family.\
   But Jack is convinced it will be OK and he can use the quiet to overcome his writer's block. After months of solitude and silence however, \
   Jack becomes a grumpy and later violent. Is it cabin fever or is there something in the hotel that is driving him mad? \
   One of the creepiest parts about the movie is the feeling of isolation that Kubrick makes. The hotel is very silent, and the rooms are huge,\
yet always empty. It is also eerily calm when Jack's son is riding his bike through the barren hallways. Jack Nicholson's performance \
is also one of his very best, scaring the hell out of me and making me sure to get out once in awhile. My favorite scene is when he is \
talking to a ghost from inside a walk-in refrigerator. The Shining is tops for horror movies in my opinion, beating the snot out\
 of crap like the Ring and The Blair Witch Project. It may be a oldie, but is definitely a goodie. "
nick = "".join(c for c in nick if c not in string.punctuation)
nick = nick.lower()
nick = nick.split()
new4 = []
for f in nick:
    if f not in new4:
        new4.append(f)
nickn = (len(new4))


r = [pauln, katen, janen, nickn]
r=max(r)
if r == katen :
    print("kate has the best review")
elif r == pauln:
    print("paul has the best review")
elif r == janen:
    print("jane has the best review")
elif r == nickn:
    print("nick has the best review")
else :
    print("can't decide")
