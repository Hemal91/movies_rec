import spacy
nlp = spacy.load('en_core_web_md')

word1 = nlp("cat")
word2 = nlp("monkey")
word3 = nlp("banana")

print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))


tokens = nlp('cat apple monkey banana dog bone chimp')
for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))

'''
similarities between cat, monkey and banana
cat banana 0.2235882580280304
monkey banana 0.4041501581668854

similarity between monkey and banana is much higher than cat banana -
this makes sense as generally monkeys seen as being likely to eat banana
where cats are not

amending cat to dog and banana to bone - results in similarities of a similar value
however dog bone has slightly more similarities between monkey bone.

dog bone 0.25421422719955444
monkey bone 0.23434987664222717

adding chimp - there is a greater similarity between chimp and monkey vs chimp and cat or dog.
chimp monkey 0.8372925519943237
chimp cat 0.513255774974823
chimp dog 0.4221893548965454

when using ‘en_core_web_sm’ vs 'en_core_web_md':

an error is shown to advise no word vectors are loaded for the simpler model
There also seem to be differences in the similarities between the same two words
with some also being negative
'''
