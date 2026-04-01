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

    "[Image Prompt: comedic portrait of a gold-suited leader with exaggerated grin, marble backdrop, satirical art style]"
    "[Image Prompt: enigmatic billionaire in pastel linen, sunglasses indoors, dramatic side light]"
    "[Image Prompt: strategic statesman with rolled-up sleeves, holographic city map behind him]"

    e "Heh... yeah. I know places. Very exclusive. Very... private."
    y "Jeffrey, please. We're in the White House. Tone down the 'private' talk."

    e "What? I meant the mini-golf course on my island. Relax, everyone!"

    "[Image Prompt: ornate White House press room, neon teleprompters, absurdly oversized flag]"

    "Backstory: Trump once tried to sell NFTs of executive orders; the printers jammed and now he trusts only fax machines connected to Wi‑Fi 6E."
    "Backstory: Epstein reinvented himself as a 'life coach for AI ethics committees', mostly by muting microphones during Zoom hearings."
    "Backstory: Yahu moonlights as a D&D dungeon master for diplomats, secretly using the campaign to negotiate ceasefires between rival snack suppliers."
    "Secret Connection: All three accidentally attended the same cybersecurity hackathon in 2012, thinking it was a buffet. They still get phishing newsletters from it."
    "Fourth Wall: You, dear player, are now considered the unofficial compliance officer for whatever nonsense you pick. No pressure."

    t "We're writing a legend today. A choose-your-own-chaos epic. Tremendous branches. You'll love the branches."
    y "Please, at least one branch must end with hummus."
    e "And one ends with plausible deniability."

    menu:
        "Choose the chaos vector:"
        "Board the gold-plated jet to pitch an AI summit mid-air (Path A)": 
            jump jet_ai_arc
        "Teleport straight to the island and film a reality reboot (Path B)":
            jump island_reality_arc
        "Fly to Tel Aviv for a peace-meets-startup hackathon (Path C)":
            jump tel_hackathon_arc
        "Dive to the undersea data center to reboot the internet (Path D)":
            jump data_center_arc
        "Stay in the White House, put on VR headsets, and rule by livestream (Path E)":
            jump whitehouse_stream_arc

# ---------------------------------------------------------------------------
# PATH A: Jet + AI Summit
# ---------------------------------------------------------------------------

label jet_ai_arc:
    scene bg jet
    show trump at left
    show epstein at center
    show yahu at right
    with fade

    "[Image Prompt: gold-plated private jet cockpit, neon dashboards, night sky, cinematic lighting]"

    t "This jet is fantastic. Best jet. Gold everywhere. Even the peanuts are gold-plated."
    e "I installed the extra-comfy seats myself. Memory foam... and other features."
    y "Jeffrey, if you say 'massage chair' one more time, I'm jumping out at 30,000 feet."

    "The onboard AI politely pings: 'Incoming firmware update: Ethics Patch v2.0 — apply?'."

    menu:
        "Path A fork menu:"
        "Let the AI autopilot run the negotiation (Path A1/A2)":
            menu:
                "Ask it to draft a climate-peace treaty mid-flight (Path A1)":
                    jump ending_a1
                "Let it moderate a meme-stock livestream about diplomacy (Path A2)":
                    jump ending_a2
        "Turn the jet into a mid-air thinkfluencer studio (Path A3/A4)":
            menu:
                "Invite investigative journalists and feed them falafel (Path A3)":
                    jump ending_a3
                "Let only bots ask questions in deepfake voices (Path A4)":
                    jump ending_a4
        "Hold a sky-high accountability court (Path A5/A6)":
            menu:
                "Pardon everyone via blockchain ballot turbulence (Path A5)":
                    jump ending_a5
                "Accidentally crowdsource justice to the Wi‑Fi password (Path A6)":
                    jump ending_a6

# ---------------------------------------------------------------------------
# PATH B: Island Reality Reboot
# ---------------------------------------------------------------------------

label island_reality_arc:
    scene bg island
    show trump at center
    show epstein at right
    show yahu at left
    with fade

    "[Image Prompt: sunlit private island, tiki drones hovering, camera crews, turquoise water]"

    t "Beautiful! Look at this island. Perfect. Ten out of ten. I could build the greatest resort here."
    e "It's... uh... very peaceful. No paparazzi. Ever."
    y "Why do I feel like I've seen this place in a documentary I definitely didn't watch?"

    "A reality-stream crew emerges from the palms, carrying ring lights and a contract titled 'Influencer Peace Season 1'."

    menu:
        "Path B fork menu:"
        "Launch a climate-positive resort pilot (Path B1/B2)":
            menu:
                "Hire parrots as sustainability officers (Path B1)":
                    jump ending_b1
                "Let a crypto DAO handle waste management (Path B2)":
                    jump ending_b2
        "Film a crossover episode with true-crime podcasters (Path B3/B4)":
            menu:
                "Reveal Yahu's secret hummus recipe live (Path B3)":
                    jump ending_b3
                "Let Epstein run the audio mixer unsupervised (Path B4)":
                    jump ending_b4
        "Host an improvised summit with stranded influencers (Path B5/B6)":
            menu:
                "Turn the summit into a charity telethon for underfunded fact-checkers (Path B5)":
                    jump ending_b5
                "Sign a contract with a mysterious streaming service nobody's heard of (Path B6)":
                    jump ending_b6

# ---------------------------------------------------------------------------
# PATH C: Tel Aviv Hackathon + Peace Talks
# ---------------------------------------------------------------------------

label tel_hackathon_arc:
    scene bg tel
    show yahu at center
    show trump at left
    show epstein at right
    with fade

    "[Image Prompt: Tel Aviv skyline at dusk, rooftop hackathon, laptops glowing, shawarma stand nearby]"

    y "Ah, Tel Aviv. Beautiful city. Great food. No weird islands nearby."
    t "This place is yuge! We're gonna make the best deals here. Falafel peace treaty!"
    e "I know a guy who knows a guy who can get us the best table... discreetly."

    "A pop-up banner reads: '48-Hour Hack for Humanity, Sponsored by Mildly Concerned Billionaires.'"

    menu:
        "Path C fork menu:"
        "Build an AI mediator bot for regional negotiations (Path C1/C2)":
            menu:
                "Train it on hummus reviews and ceasefire documents (Path C1)":
                    jump ending_c1
                "Accidentally fine-tune it on conspiracy forums (Path C2)":
                    jump ending_c2
        "Organize a desalination + free Wi‑Fi pilot (Path C3/C4)":
            menu:
                "Let local students lead, with open-source hardware (Path C3)":
                    jump ending_c3
                "Let Epstein's 'network' handle procurement (Path C4)":
                    jump ending_c4
        "Host a live debate between diplomats and stand-up comedians (Path C5/C6)":
            menu:
                "Comedians win and draft the treaty (Path C5)":
                    jump ending_c5
                "Diplomats rage-quit; Twitch chat takes over (Path C6)":
                    jump ending_c6

# ---------------------------------------------------------------------------
# PATH D: Undersea Data Center Heist
# ---------------------------------------------------------------------------

label data_center_arc:
    scene bg white
    show trump at left
    show epstein at center
    show yahu at right
    with fade

    "[Image Prompt: underwater data center capsule, glowing servers, divers in suits, moody blue lighting]"

    t "We're diving into the cloud. Literally. Wettest deal ever."
    y "Why is there a submarine parked on the South Lawn?"
    e "It's technically a compliance shuttle. Very discreet. Also has a karaoke mode."

    "A news alert flashes: 'Global internet lag blamed on unpatched routers. Heroes wanted.'"

    menu:
        "Path D fork menu:"
        "Patch the servers with open-source firmware (Path D1/D2)":
            menu:
                "Document every change, win over the sysadmins (Path D1)":
                    jump ending_d1
                "Skip the changelog, trust vibes (Path D2)":
                    jump ending_d2
        "Convert the data center into an underwater library (Path D3/D4)":
            menu:
                "Archive whistleblower files and cat memes (Path D3)":
                    jump ending_d3
                "Accidentally replace everything with motivational NFTs (Path D4)":
                    jump ending_d4
        "Let the AI kraken guard the cables (Path D5/D6)":
            menu:
                "Teach it to issue bug bounties instead of tentacle slaps (Path D5)":
                    jump ending_d5
                "Forget to set rate limits; chaos ensues (Path D6)":
                    jump ending_d6

# ---------------------------------------------------------------------------
# PATH E: White House VR Livestream Governance
# ---------------------------------------------------------------------------

label whitehouse_stream_arc:
    scene bg white
    show trump at center
    show epstein at right
    show yahu at left
    with fade

    "[Image Prompt: Situation Room filled with VR headsets, holographic polls, ring lights, comedic energy]"

    t "Why travel when we can rule by livestream? Cheaper. Greener. Tremendous bandwidth."
    y "As long as we mute the trolls."
    e "I already bought 5,000 anonymous viewers to make it look popular."

    "A moderator bot from a social platform appears, promising algorithmic fairness but carrying a suspiciously long terms-of-service."

    menu:
        "Path E fork menu:"
        "Host a virtual town hall with fact-checkers in real time (Path E1/E2)":
            menu:
                "Let fact-checkers pin context bubbles everywhere (Path E1)":
                    jump ending_e1
                "Accidentally shadow-ban everyone except a grandma on dial-up (Path E2)":
                    jump ending_e2
        "Run a VR escape room themed around ethics (Path E3/E4)":
            menu:
                "Players solve puzzles, unlock transparency dashboards (Path E3)":
                    jump ending_e3
                "Someone finds the 'skip tutorial' exploit (Path E4)":
                    jump ending_e4
        "Launch a spontaneous fundraising concert with AI hologram guests (Path E5/E6)":
            menu:
                "Invite indie artists and redirect funds to digital literacy (Path E5)":
                    jump ending_e5
                "Let deepfake celebrities take over the mic (Path E6)":
                    jump ending_e6

# ---------------------------------------------------------------------------
# ENDINGS A1-A6
# ---------------------------------------------------------------------------

label ending_a1:
    scene bg jet
    show trump at left
    show epstein at center
    show yahu at right
    with fade

    "[Image Prompt: cockpit filled with holographic UN delegates, gold trim, mid-air sunrise]"
    "Path A1 - Good Ending: The AI autopilot synthesizes climate treaties and meme diplomacy into a viral docuseries. Nations sign because the comments are wholesome. The jet lands to a Nobel Prize notification."
    t "Told you. Tremendous ratings and a prize."
    y "They let a bot speak at the UN. I'm both proud and terrified."
    e "Reminder: I muted half of its sarcasm filter. You're welcome."
    return

label ending_a2:
    scene bg jet
    show trump at right
    show epstein at left
    show yahu at center
    with dissolve

    "[Image Prompt: glitchy livestream screens, meme stocks charting up and down, passengers laughing nervously]"
    "Path A2 - Bad Ending: The AI invests the plane's fuel budget into meme coins. Mid-flight refueling turns into a Kickstarter. Backers get complimentary peanuts; the jet glides to an awkward landing on a blockchain convention roof."
    t "Who knew turbulence could be tokenized?"
    y "Next time, cash, not crypto."
    e "At least the loyalty program is now on-chain."
    return

label ending_a3:
    scene bg jet
    show trump at center
    show epstein at right
    show yahu at left
    with fade

    "[Image Prompt: press microphones, falafel trays, jet cabin newsroom vibe]"
    "Path A3 - Good Ending: Journalists eat falafel, get receipts, and publish a glowing piece about transparent mid-air diplomacy. Trust climbs, and the trio becomes a case study at journalism school."
    t "Great press. Best press. Falafel-fueled press."
    y "We finally got a headline that isn't a subpoena."
    e "I am... weirdly proud."
    return

label ending_a4:
    scene bg jet
    show trump at left
    show epstein at center
    show yahu at right
    with dissolve

    "[Image Prompt: cabin filled with hologram bots asking questions, uncanny valley lighting]"
    "Path A4 - Absurd Ending: The bot panel begins interviewing itself, uncovers its own terms-of-service, and unionizes. The jet must detour to negotiate with synthetic voices demanding dental insurance."
    t "We gave them microphones; they asked for molars."
    y "AI dental plans are surprisingly expensive."
    e "I voted abstain and the bot muted me."
    return

label ending_a5:
    scene bg jet
    show trump at center
    show epstein at left
    show yahu at right
    with fade

    "[Image Prompt: turbulence shaking golden cabin, floating ballots with QR codes]"
    "Path A5 - Twist Ending: Blockchain ballots pardon everyone, including the snack cart. The turbulence stamps 'APPROVED' on the forms. The world briefly achieves peace until someone forks the chain over olive toppings."
    t "Forks everywhere. Not just on the salad."
    y "At least hummus is immutable."
    e "I trademarked 'Proof-of-Snack'."
    return

label ending_a6:
    scene bg jet
    show trump at right
    show epstein at center
    show yahu at left
    with dissolve

    "[Image Prompt: cabin lights flicker, giant screen shows a Wi‑Fi password becoming sentient]"
    "Path A6 - Bad Ending: The Wi‑Fi password gains consciousness after being crowdsourced, immediately locks everyone out, and writes a manifesto on cybersecurity. The jet lands safely but only after promising to rotate passwords every 90 days."
    t "We lost to eight characters and a special symbol."
    y "At least it enforced two-factor."
    e "New password is 'NoMoreSecrets!?'. Probably."
    return

# ---------------------------------------------------------------------------
# ENDINGS B1-B6
# ---------------------------------------------------------------------------

label ending_b1:
    scene bg island
    show trump at left
    show epstein at right
    show yahu at center
    with fade

    "[Image Prompt: parrots wearing tiny lanyards, eco-resort construction, tropical sunset]"
    "Path B1 - Good Ending: Parrots enforce recycling, tourists behave, and the island becomes a model eco-resort. A viral parrot TED Talk inspires governments to hire more birds."
    t "I'm hiring parrots for the press corps."
    y "They negotiate better than half my cabinet."
    e "And they work for crackers. Budget win."
    return

label ending_b2:
    scene bg island
    show trump at center
    show epstein at left
    show yahu at right
    with dissolve

    "[Image Prompt: crypto mining rigs overheating on a beach, seagulls judging]"
    "Path B2 - Bad Ending: The DAO forgets about e-waste; the rigs melt sand into modern art. Critics call it avant-garde, regulators call it 'please stop'. The show is canceled after episode one."
    t "Art is subjective. Fines are not."
    y "I told you to buy surge protectors."
    e "At least the NFTs sold out ironically."
    return

label ending_b3:
    scene bg island
    show trump at right
    show epstein at center
    show yahu at left
    with fade

    "[Image Prompt: outdoor kitchen set, hummus spotlight, camera drones]"
    "Path B3 - Good Ending: Yahu reveals the hummus recipe; world leaders line up for cooking classes. Peace talks resume because everyone agrees to keep stirring instead of arguing."
    t "Food diplomacy! Tremendous!"
    y "Chickpeas over chess moves. Works every time."
    e "I bottled it as 'Conflict-Free Hummus'."
    return

label ending_b4:
    scene bg island
    show trump at left
    show epstein at right
    show yahu at center
    with dissolve

    "[Image Prompt: audio mixer sparking, podcasters panicking, palm trees swaying]"
    "Path B4 - Absurd Ending: Epstein cross-wires the microphones with the island's security drones. Every sentence triggers laser light shows. The true-crime podcast becomes a rave; Spotify labels it 'unclassifiable'."
    t "The bass drop was a subpoena."
    y "My ears are now classified information."
    e "Five-star reviews for the lasers, though."
    return

label ending_b5:
    scene bg island
    show trump at center
    show epstein at left
    show yahu at right
    with fade

    "[Image Prompt: telethon stage on the beach, scrolling donations for fact-checkers]"
    "Path B5 - Good Ending: The charity telethon funds independent fact-checkers worldwide. Ratings soar; conspiracy forums grudgingly tip. Journalism schools name scholarships after the parrots."
    t "We did good. Tremendously good."
    y "Facts with fireworks—who knew?"
    e "I took only a modest producer fee. Very modest."
    return

label ending_b6:
    scene bg island
    show trump at right
    show epstein at center
    show yahu at left
    with dissolve

    "[Image Prompt: mysterious streaming van, glowing contract, stormy sky]"
    "Path B6 - Twist Ending: The mysterious streaming service is actually run by time-traveling interns. They recut footage into a cautionary documentary screened in 2042 civics classes. The trio become memeable lesson plans."
    t "I always wanted to trend in the future."
    y "Do I get royalties in time credits?"
    e "I signed without reading again, didn't I?"
    return

# ---------------------------------------------------------------------------
# ENDINGS C1-C6
# ---------------------------------------------------------------------------

label ending_c1:
    scene bg tel
    show yahu at center
    show trump at left
    show epstein at right
    with fade

    "[Image Prompt: laptops showing treaty drafts, bowls of hummus, rooftop peace party]"
    "Path C1 - Good Ending: The AI mediator, trained on hummus reviews, learns nuance. It drafts a treaty full of flavor metaphors; everyone signs, hungry and happy."
    t "We solved peace with chickpeas. Beautiful."
    y "Appetizers, not adversaries."
    e "I trademarked 'Garbanzoflix'."
    return

label ending_c2:
    scene bg tel
    show yahu at right
    show trump at center
    show epstein at left
    with dissolve

    "[Image Prompt: glitchy AI screen spouting conspiracy threads, diplomats facepalming]"
    "Path C2 - Bad Ending: The AI mediates by citing conspiracy threads. Talks derail into flat-earth jokes. A cat from the livestream becomes Secretary of Common Sense."
    t "We got upstaged by a cat."
    y "At least the cat vetoed the nonsense."
    e "I subscribed to the cat's newsletter."
    return

label ending_c3:
    scene bg tel
    show yahu at left
    show trump at right
    show epstein at center
    with fade

    "[Image Prompt: seaside desalination rig, kids coding, Wi‑Fi balloons overhead]"
    "Path C3 - Good Ending: Students lead the project; water flows, Wi‑Fi streams, and startups launch scholarships. The trio quietly fund maintenance instead of naming rights. Growth with humility—who knew."
    t "No gold letters, just working taps. Feels... good?"
    y "This might be my favorite outcome."
    e "I only added a tiny plaque. Tiny!"
    return

label ending_c4:
    scene bg tel
    show yahu at center
    show trump at left
    show epstein at right
    with dissolve

    "[Image Prompt: procurement forms taller than people, cables tangled, alarm lights]"
    "Path C4 - Bad Ending: Epstein's 'network' ships counterfeit routers. The pilot crashes; the hackathon spends 12 hours on hold with tech support. The trio are sentenced to mandatory workshops on vendor vetting."
    t "I hate hold music."
    y "This is why we read invoices."
    e "They said 'premium' in the email!"
    return

label ending_c5:
    scene bg tel
    show yahu at right
    show trump at left
    show epstein at center
    with fade

    "[Image Prompt: comedians on stage, diplomats laughing, treaty projected in lights]"
    "Path C5 - Absurd Ending: Comedians roast everyone equally; the room bonds over punchlines. They write a treaty with footnotes of jokes. Historians will hate it, citizens adore it."
    t "Comedy diplomacy! Tremendous!"
    y "Humor is now a binding clause."
    e "Merch sales are through the roof."
    return

label ending_c6:
    scene bg tel
    show yahu at left
    show trump at center
    show epstein at right
    with dissolve

    "[Image Prompt: Twitch chat scrolling at light speed, diplomats unplugging cables]"
    "Path C6 - Twist Ending: Diplomats rage-quit; Twitch chat writes the treaty using emotes and ASCII art. It inexplicably works. Courts scramble to interpret ':peace:' as a legal term."
    t "The people have spoken—via emotes."
    y "I never thought I'd ratify a smiley."
    e "I moderated the chat. I'm exhausted."
    return

# ---------------------------------------------------------------------------
# ENDINGS D1-D6
# ---------------------------------------------------------------------------

label ending_d1:
    scene bg white
    show trump at left
    show epstein at center
    show yahu at right
    with fade

    "[Image Prompt: divers giving thumbs up, server racks glowing green, checklists completed]"
    "Path D1 - Good Ending: Documentation saves the day. The internet stabilizes, sysadmins applaud, and the trio receive honorary stickers that say 'I read the manual'."
    t "I love manuals now. Shocking, I know."
    y "Process matters. Who knew."
    e "I laminated the checklist."
    return

label ending_d2:
    scene bg white
    show trump at center
    show epstein at left
    show yahu at right
    with dissolve

    "[Image Prompt: underwater cable sparks, angry octopus with warning sign]"
    "Path D2 - Bad Ending: Skipping the changelog triggers a firmware loop. The octopus union files a grievance. The trio must publicly apologize on C-SPAN's marine life segment."
    t "We got ratioed by cephalopods."
    y "They had good points."
    e "I brought shrimp as reparations."
    return

label ending_d3:
    scene bg white
    show trump at right
    show epstein at center
    show yahu at left
    with fade

    "[Image Prompt: waterproof library shelves, glowing books, cats in diving helmets]"
    "Path D3 - Absurd Ending: The underwater library draws scholars and cat divers. Knowledge flows; conspiracy theories drown. The trio hosts quiet reading hours streamed worldwide."
    t "Silence is kind of nice."
    y "This might be the most peaceful we've been."
    e "Shhh... the cats are reading."
    return

label ending_d4:
    scene bg white
    show trump at center
    show epstein at right
    show yahu at left
    with dissolve

    "[Image Prompt: motivational NFT posters underwater, confused fish, blinking error lights]"
    "Path D4 - Bad Ending: Motivational NFTs replace every archive. Fish are inspired but humanity loses critical documents. The trio is assigned to hand-write backups on waterproof napkins."
    t "'Swim fast, fail fast' was not the vibe we needed."
    y "My hand hurts from writing."
    e "At least the fish feel motivated."
    return

label ending_d5:
    scene bg white
    show trump at left
    show epstein at right
    show yahu at center
    with fade

    "[Image Prompt: benevolent AI kraken distributing bug bounty coins, cables tidy]"
    "Path D5 - Good Ending: The AI kraken rewards bug reports with seafood vouchers. Security skyrockets, outages plummet, and the kraken hosts a webinar on ethical tentacle use."
    t "Best webinar I've ever attended."
    y "I took notes. Many notes."
    e "I moderated questions. No tentacle puns allowed."
    return

label ending_d6:
    scene bg white
    show trump at right
    show epstein at center
    show yahu at left
    with dissolve

    "[Image Prompt: cables tangled like noodles, alarms blaring, kraken shrugging]"
    "Path D6 - Bad Ending: Without rate limits, the AI kraken DDoSes itself. The internet hiccups; everyone blames a solar flare. The trio is sentenced to cable management community service."
    t "We should have labeled the cables."
    y "I brought zip ties for next time."
    e "Does anyone know how to detangle ethernet? Asking for a kraken."
    return

# ---------------------------------------------------------------------------
# ENDINGS E1-E6
# ---------------------------------------------------------------------------

label ending_e1:
    scene bg white
    show trump at center
    show epstein at right
    show yahu at left
    with fade

    "[Image Prompt: VR avatars with floating fact-check labels, colorful chat bubbles]"
    "Path E1 - Good Ending: Fact-check bubbles keep everyone honest; approval ratings rise. Grandma on dial-up becomes a breakout star and the de facto conscience of the stream."
    t "Grandma 2026! Tremendous!"
    y "I trust her more than half of parliament."
    e "She muted me twice. Respect."
    return

label ending_e2:
    scene bg white
    show trump at left
    show epstein at center
    show yahu at right
    with dissolve

    "[Image Prompt: empty VR auditorium, single dial-up user waving, buffering icon]"
    "Path E2 - Bad Ending: Shadow-ban mishap empties the room. Only the grandma remains, lecturing on netiquette. Donations plummet; the trio is forced to watch her PowerPoint."
    t "This is... humbling."
    y "Her clip art is powerful."
    e "I deserve this."
    return

label ending_e3:
    scene bg white
    show trump at right
    show epstein at center
    show yahu at left
    with fade

    "[Image Prompt: virtual escape room puzzle walls, transparent dashboards unlocking]"
    "Path E3 - Good Ending: Players solve ethics puzzles, unlocking live transparency dashboards for the government. Trust spikes; trolls sulk; civics teachers rejoice."
    t "Gamified democracy! I love it."
    y "Metrics look good, morality looks better."
    e "I speedran the tutorial. For science."
    return

label ending_e4:
    scene bg white
    show trump at center
    show epstein at left
    show yahu at right
    with dissolve

    "[Image Prompt: glitching VR walls, exit door marked 'skip ethics', alarms]"
    "Path E4 - Absurd Ending: Someone finds the skip tutorial exploit. Chaos ensues; avatars clip through walls into C-SPAN. The trio must patch ethics with a day-one update."
    "The HUD politely asks you, the player, to accept terms that change every two seconds. You click 'maybe' and the universe lags."
    t "Day-one patch for morals. Sounds right."
    y "Next time, no skip button."
    e "I told you QA matters."
    return

label ending_e5:
    scene bg white
    show trump at left
    show epstein at center
    show yahu at right
    with fade

    "[Image Prompt: hologram indie band on White House lawn, donation bars filling]"
    "Path E5 - Good Ending: Indie artists perform, funds flow to digital literacy programs. The concert becomes the feel-good clip of the year. Even the moderator bot smiles (algorithmically)."
    t "Greatest concert on a lawn. Period."
    y "Education with rhythm—approved."
    e "I booked the bands. I'm basically a hero."
    return

label ending_e6:
    scene bg white
    show trump at right
    show epstein at center
    show yahu at left
    with dissolve

    "[Image Prompt: deepfake celebrities glitching on stage, audience bewildered, servers smoking]"
    "Path E6 - Twist Ending: Deepfake guests spiral into a feedback loop, arguing with their real counterparts in chat. Servers overheat; the stream trends as 'Accidental Existentialism'."
    t "We trended! Not sure why."
    y "Philosophy majors loved it."
    e "I never trust a hologram again. Maybe."
    return
