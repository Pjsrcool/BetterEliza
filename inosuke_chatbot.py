# Natural Language Toolkit: Eliza
#
# Copyright (C) 2001-2022 NLTK Project
# Authors: Steven Bird <stevenbird1@gmail.com>
#          Edward Loper <edloper@gmail.com>
# URL: <https://www.nltk.org/>
# For license information, see LICENSE.TXT

# Based on an Eliza implementation by Joe Strout <joe@strout.net>,
# Jeff Epler <jepler@inetnebr.com> and Jez Higgins <mailto:jez@jezuk.co.uk>.

# a translation table used to convert things you say into things the
# computer says back, e.g. "I am" --> "you are"

# from nltk.chat.util import Chat, reflections

# a table of response pairs, where each pair consists of a
# regular expression, and a list of possible responses,
# with group-macros labelled as %1, %2.

pairs = (
    (
        r"I need (.*)",
        (
            "Why do you need %1?",
            "Do you really need %1?",
            "It won't matter once I destroy that thing.",
        ),
    ),
    (
        r"Why don\'t you (.*)",
        (
            "Do you really think I don't %1?",
            "How should I know?",
            "That's enough of your crap!",
        ),
    ),
    (
        r"Why can\'t I (.*)",
        (
            "That's enough of your crap!",
            "Have you really tried?",
            "No matter how pathetic or humiliated you feel, you still have to %1",
        ),
    ),
    (
        r"I can\'t (.*)",
        (
            "Die on the battlefield and serve as my springboard!",
            "It won't matter once I destroy that thing.",
            "That's enough of your crap!",
            "If you can't do that... then you'll pay for it with a million deaths!",
            "No matter how pathetic or humiliated you feel, you still have to %1",
        ),
    ),
    (
        r"I am (.*)",
        (
            "All right!",
            "I'm gonna tear you to shreds, you damn demon!",
            "I'm gonna send you to hell!",
        ),
    ),
    (
        r"I\'m (.*)",
        (
            "All right!",
            "I'm gonna tear you to shreds, you damn demon!",
            "I'm gonna send you to hell!",
        ),
    ),
    (
        r"Are you (.*)",
        (
            "You think I am %1?!?!",
            "How should I know?",
            "I'm gonna send you to hell!",
        ),
    ),
    (
        r"What (.*)",
        (
            "Why do you want to know?",
            "How should I know?",
            "What do you think???",
        ),
    ),
    (
        r"How (.*)",
        (
            "What do you think???",
            "Figure it out yourself.",
            "What is it you're really asking?",
        ),
    ),
    (
        r"Because (.*)",
        (
            "Is that the real reason?",
            "Go ahead and think whatever you want.",
            "All right!",
            "Hold up!",
            "That's mind-blowing!",
        ),
    ),
    (
        r"(.*) sorry (.*)",
        (
            "Don't go showering with your sensitivity and kindness.",
            "Cut that out! I don't need that!",
            "You've really done it now!",
            "I'm gonna tear you to shreds, you damn demon!",
        ),
    ),
    (
        r"Hello(.*)",
        (
            "Hey!",
            "Comin' through! Comin' through!",
        ),
    ),
    (
        r"I think (.*)",
        (
            "All right!",
            "Awesome! Awesome!",
            "Cut that out! I don't need that!",
        ),
    ),
    (
        r"(.*) friend (.*)",
        (
            "Bro! Bro!",
        ),
    ),
    (
        r"Yes", 
        (
            "All right!",
            "Awesome! Awesome!",
            "It won't matter once I destroy that thing.",
        )
    ),
    (
        r"Is it (.*)",
        (
            "Ummm...",
            "That's enough of your crap",
            "It won't matter once I destroy that thing.",
        ),
    ),
    (
        r"It is (.*)",
        (
            "You seem very certain.",
            "All right!",
            "Awesome! Awesome!",
            "It won't matter once I destroy that thing.",
        ),
    ),
    (
        r"Can you (.*)",
        (
            "If I could %1, then what?",
            "Do you doubt if I can %1?!",
            "After all, anything you can do, I can do, too!",
            "It won't matter once I destroy that thing.",
        ),
    ),
    (
        r"Can I (.*)",
        (
            "How should I know?",
            "Go ahead and do whatever you want!",
            "It won't matter once I destroy that thing.",
            "If you could %1, then what?",
            "It won't matter once I destroy that thing.",
        ),
    ),
    (
        r"You are (.*)",
        (
            "You think I am %1?!",
            "You want me to be %1?!",
            "You're really talking about yourself!",
            "Cut that out! I don't need that.",
            "Who are you calling %1?!",
            "Are we talking about you, or me?!",
            "I'm totally fine!",
        ),
    ),
    (
        r"You\'re (.*)",
        (
            "You think I am %1?!",
            "You want me to be %1?!",
            "You're really talking about yourself!",
            "Cut that out! I don't need that.",
            "Who are you calling %1?!",
            "Are we talking about you, or me?!",
            "I'm totally fine!",
        ),
    ),
    (
        r"I don\'t (.*)",
        (
            "Me too!",
            "Alright you monster...",
            "Really?!",
            "That's enough of your crap!",
        ),
    ),
    (
        r"I feel (.*)",
        (
            "Good.",
            "Who cares?",
            "Me too!",
            "It won't matter once I destroy that thing!",
        ),
    ),
    (
        r"I have (.*)",
        (
            "Good.",
            "Who cares?",
            "Me too!",
            "It won't matter once I destroy that thing!",
            "You've really done it now!",
        ),
    ),
    (
        r"I would (.*)",
        (
            "Good.",
            "Who cares?",
            "Me too!",
            "It won't matter once I destroy that thing!",
        ),
    ),
    (
        r"Is there (.*)",
        (
            "How should I know?",
            "Who cares?",
            "It won't matter once I destroy that thing!",
        ),
    ),
    (
        r"My (.*)",
        (
            "Ummm...",
            "Who cares?",
            "It won't matter once I destroy that thing!",
        ),
    ),
    (
        r"You (.*)",
        (
            "You think I am %1?!",
            "You want me to be %1?!",
            "You're really talking about yourself!",
            "Cut that out! I don't need that.",
            "Who are you calling %1?!",
            "Are we talking about you, or me?!",
        ),
    ),
    (
        r"Why (.*)",
        (
            "Why don't you tell me the reason why %1?",
            "Why do you think %1?",
            "How should I know?",
        ),
    ),
    (
        r"I want (.*)",
        (
            "Why?",
            "Who cares?",
            "Cut that out! I don't need that!",
            "It won't matter once I destroy that thing!",
            "Go ahead and do whatever you want.",
            "It won't matter once I destroy that thing!",
        ),
    ),
    (
        r"(.*) mother(.*)",
        (
            "My mom's dead.",
            "Who are you calling \"mother\"?",
        ),
    ),
    (
        r"(.*) father(.*)",
        (
            "Who are you calling \"father\"?",
        ),
    ),
    (
        r"(.*) child(.*)",
        (
            "Who are you calling \"child\"?",
        ),
    ),
    (
        r"(.*)\?",
        (
            "Go ahead and do whatever you want",
            "Why don't you tell me?",
            "How am I supposed to know?",
        ),
    ),
    (
        r"quit",
        (
            "Awesome! Awesome! So fast!",
            "Alright!",
            "So freaking fast!",
        ),
    ),
    (
        r"(.*)",
        (
            "Huh?",
        ),
    ),
)
