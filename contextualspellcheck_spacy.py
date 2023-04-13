import spacy
import contextualSpellCheck
nlp = spacy.load('fr_core_news_lg')
contextualSpellCheck.add_to_pipe(nlp)
doc = nlp('Ce n etoit pas feulement en rems de guerre que la petite Eusèbe exerçat ses talents, elle était fort confidérée au château, elle avait assez - souvent l honneur de manger, à la table de Monseigneur, servie par son frère ; et quand ce galant seigneur allait à la ville,, il ne revenait jamaissans lui rapporter quelque chapeau élégant, ou quelques paires de gans à la Figaro..')

print(doc._.performed_spellCheck) #Should be True
print(doc._.outcome_spellCheck) 