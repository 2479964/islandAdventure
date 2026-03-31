# The Golden Trio's Wild Ride
# A ridiculous satirical comedy


define t = Character("Trump", color="#FF4500", who_color="#FFD700", image="trump")
define e = Character("Epstein", color="#4B0082", who_color="#9370DB", image="epstein")
define y = Character("Yahu", color="#006400", who_color="#32CD32", image="yahu")

# Declare images
image bg white:
    "bg white.png"
    xysize (1920, 1080)

image bg island:
    "island.png"
    xysize (1920, 1080)

image bg jet:
    "jet.png"
    xysize (1920, 1080)

image bg tel:
    "tel.png"
    xysize (1920, 1080)

image trump = "trump.png"
image epstein = "epstein1.png"
image yahu = "yahu.png"

label start:
    scene bg white
    show trump at center
    with fade

    t "Folks, we're gonna make this the greatest little adventure in history. Tremendous. Believe me."
    t "I just got off the phone with my good friend Yahu. And Jeffrey here... well, he knows all the best islands."

    show epstein at right
    show yahu at left
    with dissolve

    e "Heh... yeah. I know places. Very exclusive. Very... private."
    y "Jeffrey, please. We're in the White House. Tone down the 'private' talk."

    e "What? I meant the mini-golf course on my island. Relax, everyone!"

    menu:
        "What should we do first?"
        "Fly on the private jet for a 'business meeting'":
            jump jet_scene
        "Teleport straight to the island for some 'relaxation'":
            jump island_scene
        "Go to Tel Aviv for falafel and strategy":
            jump tel_scene

label jet_scene:
    scene bg jet
    show trump at left
    show epstein at center
    show yahu at right
    with fade

    t "This jet is fantastic. The best jet. Gold everywhere. Even the peanuts are gold-plated."
    e "I installed the extra-comfy seats myself. Memory foam... and other features."
    y "Jeffrey, if you say 'massage chair' one more time, I'm jumping out at 30,000 feet."

    t "Relax, Yahu! We're gonna solve world peace. Or at least make a killer deal on it."
    t "Epstein, you got the little black book with all the contacts?"

    e "Uh... it's more of a 'little friendly network' these days."

    y "Gentlemen, focus. We need a plan. Big plan."

    menu:
        "What next?"
        "Land on the island":
            jump island_scene
        "Divert to Tel Aviv":
            jump tel_scene

label island_scene:
    scene bg island
    show trump at center
    show epstein at right
    show yahu at left
    with fade

    t "Beautiful! Look at this island. Perfect. Ten out of ten. I could build the greatest resort here."
    e "It's... uh... very peaceful. No paparazzi. Ever."
    y "Why do I feel like I've seen this place in a documentary I definitely didn't watch?"

    t "We're here to discuss the ultimate deal: Trump Tower Tel Aviv, with a private Epstein... I mean, luxury spa wing!"
    e "And I'll handle the guest list. Very selective."

    y "As long as there's good hummus and no surprises, I'm in."

    "Suddenly, a parrot flies by squawking: 'Little black book! Little black book!'"

    t "See? Even the birds love the plan!"

    menu:
        "End the adventure with a group selfie":
            jump ending
        "Fly to Tel Aviv to celebrate":
            jump tel_scene

label tel_scene:
    scene bg tel
    show yahu at center
    show trump at left
    show epstein at right
    with fade

    y "Ah, Tel Aviv. Beautiful city. Great food. No weird islands nearby."
    t "This place is yuge! We're gonna make the best deals here. Falafel peace treaty!"
    e "I know a guy who knows a guy who can get us the best table... discreetly."

    y "Jeffrey, you're banned from 'knowing guys' for the rest of the trip."

    t "We're unstoppable, folks. The trio that can't be beat. Trump, Epstein, and Yahu — the dream team!"

    "The three strike a ridiculous pose as the sun sets over the city."

    jump ending

label ending:
    scene bg white
    show trump at left
    show epstein at center
    show yahu at right
    with fade

    t "What a day! We solved nothing, but we had tremendous fun."
    e "And no one got... you know... in trouble."
    y "Miracles do happen."

    t "You're the best. Both of you. We're gonna do this again. Soon. Huge success."

    "The screen fades to black with big gold text: 'The End... or is it?'"

    "Thanks for playing this silly satirical ride!"

    return