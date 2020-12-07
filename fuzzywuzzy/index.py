from fuzzywuzzy import fuzz 
from fuzzywuzzy import process 
  
frase1 = "frase sem sentido"
frase2 = "outra frase sem sentido"
print("Ratio: ", fuzz.ratio(frase1, frase2))
print("PartialRatio: ", fuzz.partial_ratio(frase1, frase2))
print("TokenSortRatio: ", fuzz.token_sort_ratio(frase1, frase2))
print("TokenSetRatio: ", fuzz.token_set_ratio(frase1, frase2))
print("WRatio: ", fuzz.WRatio(frase1, frase2),'\n')

query = 'rafael brito'
choices = ['r. brito', 'rafael b.', 'rafa brito']  
print("Lista: ")
print(process.extract(query, choices), '\n')
print("Melhor da lista: ",process.extractOne(query, choices))