from frameworks.decision_tree_learning import *
from frameworks.document_classification import *
from frameworks.tfidf import *

import operator
train_data = [
    ("""I like Rhythm and Blue music.""", 'formal'),
    ("""Back in my day Emo was a comedian :/""", 'informal'),
    ("""Why sit and listen to Locke, Jack, or Syead?""", 'informal'),
    ("""There's nothing he needs to change.""", 'formal'),
    ("""It does not exist.""", 'formal'),
    ("""I like when the Prime Minister goes door to door to find the girl!""", 'informal'),
    ("""Mine is book by Steve Martin called 'The Pleasure of my Company'.""", 'formal'),
    ("""What differentiates a mosquitoo from a blonde?""", 'formal'),
    ("""They're pretty good. Also, that's a good song.""", 'formal'),
    ("""And every time I hear that song I get butterflies in my stomach!""", 'informal'),
    ("""It's the biggest load of crap I've seen for ages.""", 'informal'),
    ("""I do not think Beyonce can sing, dance, or act. You mentioned Rihanna, who is that?""", 'formal'),
    ("""as i lay dying is far far away from christ definitaly!""", 'informal'),
    ("""I was unaware that you were in law enforcement, as well.""", 'formal'),
    ("""I might be seeing them in a few months!""", 'informal'),
    ("""I called to say 'I Love You""", 'formal'),
    ("""that´s why they needed to open that hatch so much!""", 'informal'),
    ("""I would most likely not vote for him, although I believe Melania would be the most attractive First Lady in our country's history.""", 'formal'),
    ("""I do not hate him.""", 'formal'),
    ("""He's supposed to be in jail!""", 'informal'),
    ("""i thought that she did an outstanding job in the movie""", 'informal'),
    ("""Nicole Kidman, I love her eyes""", 'informal'),
    ("""Youtube.com also features many of the current funny ads.""", 'formal'),
    ("""I enjoy watching my companion attempt to role-play with them.""", 'formal'),
    ("""omg i love that song im listening to it right now""", 'informal'),
    ("""Some of my favorite television series are Monk, The Dukes of Hazzard, Miami Vice, and The Simpsons.""", 'formal'),
    ("""I have a desire to produce videos on Full Metal Alchemist.""", 'formal'),
    ("""tell him you want a 3 way with another hot girl""", 'informal'),
    ("""I would travel to that location and physically assault you at this very moment, however, I am unable to swim.""", 'formal'),
    ("""No, no, no that was WITNESS...""", 'informal'),
    ("""aneways shonenjump.com is cool and yeah narutos awsum""", 'informal'),
    ("""Your mother is so unintelligent that she was hit by a cup and told the police that she was mugged.""", 'formal'),
    ("""You must be creative and find something to challange us.""", 'formal'),
    ("""i think they would have, quite a shame isn't it""", 'informal'),
    ("""I am watching it right now.""", 'formal'),
    ("""I do not know; the person who invented the names had attention deficit disorder.""", 'formal'),
    ("""im a huge green day fan!!!!!""", 'informal'),
    ("""I believe, rather, that they are not very smart on this topic.""", 'formal'),
    ("""Of course it is Oprah, because she has been providing better advice for a longer time.""", 'formal'),
    ("""Chicken Little my son loves that movie I have to watch at least 4 times a day!""", 'informal'),
    ("""That is the key point, that you fell asleep.""", 'formal'),
    ("""A brunette female, a blonde, and person with red hair walked down a street.""", 'formal'),
    ("""who is your best bet for american idol season five""", 'informal'),
    ("""That is funny.  Girls need to be a part of everything.""", 'formal'),
    ("""In point of fact, Chris's performance looked like the encoure performed at a Genesis concert.""", 'formal'),
    ("""In my time, Emo was a comedian.""", 'formal'),
    ("""my age gas prices and my blood pressure  LOL""", 'informal'),
    ("""Moriarty and so forth, but what character did the Peruvian actor portray?""", 'formal'),
    ("""What did the beaver say to the log?""", 'formal'),
    ("""Where in the world do you come up with these questions????""", 'informal'),
    ("""even though i also agree that the girls on Love Hina are pretty scrumptious""", 'informal'),
    ("""I miss Aaliyah, she was a great singer.""", 'formal'),
    ("""and the blond says Great they already put me on my first murder mystery case""", 'informal'),
]


if __name__ == '__main__':
    sample = input()

    klasifikator = NaiveBayes(get_words)
    for item in train_data:
        klasifikator.train(item[0], item[1])

    klasa_baesov = klasifikator.classify_document(sample)

    documents  = [ item[0] for item in train_data]
    labels = [item[1] for item in train_data]

    dataset, df, N, vocab = create_dataset(documents, labels)
    drvo = build_tree(dataset)

    sample_vector = process_document(sample, df, N, vocab)
    klasa_drvo  = classify(sample_vector, drvo)

    klasa_drvo=max(klasa_drvo.items(), key = operator.itemgetter(1))[0]

    if klasa_drvo == klasa_baesov:
        print(klasa_drvo)
    else:
        print("unknown")




