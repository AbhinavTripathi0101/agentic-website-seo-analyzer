import re
from collections import Counter

STOPWORDS = set("""                                                         
the and is are was were to of in for on with as by from at that this it
""".split())                                                            #here removing Removes meaningless words

def extract_phrases(text, n=2):                                 #here Generates n-grams,SEO keywords are often phrases not single words
    words = [
        w.lower() for w in re.findall(r"[a-zA-Z]{3,}", text)
        if w.lower() not in STOPWORDS
    ]

    phrases = zip(*[words[i:] for i in range(n)])
    return [" ".join(p) for p in phrases]

def advanced_keyword(content, headings):                #it captures Single concepts,Compound ideas,Long-tail keywords
    unigrams = extract_phrases(content, 1)
    bigrams = extract_phrases(content, 2)
    trigrams = extract_phrases(content, 3)

    keyword_scores = Counter(unigrams + bigrams + trigrams)     #Counts importance signals, not literal matches

    # Boost heading keywords
    for phrase in extract_phrases(headings, 2):                 #as Headings matter more for SEO
        keyword_scores[phrase] += 3

    return keyword_scores.most_common(15)                       #Outputs ranked SEO topics
