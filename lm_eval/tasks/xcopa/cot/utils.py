from functools import partial

CoT_examples_et = ['''What might have happened as a result of "Mees keeras kraani lahti."?
Options:
- "Tualett täitus veega."
- "Tilast voolas vett."
Answer: Let's think step by step.
The premise "Mees keeras kraani lahti." can be translated from Estonian into English as "The man turned on the faucet."
The first option "Tualett täitus veega." can be translated as "The toilet filled with water.", whereas the second option "Tilast voolas vett." can be translated as "Water flowed from the spout."
If the man turned on the faucet then it makes sense that water flowed from the spout as a result.
Therefore, the answer is "Tilast voolas vett.".'''
,
'''What might be the cause of "Hamburgeri liha pruunistus."?
Options:
- "Kokk külmutas selle."
- "Kokk grillis seda."
Answer: Let's think step by step.
The premise "Hamburgeri liha pruunistus." can be translated from Estonian into English as "e": "The hamburger meat broqwned."
The first option "Kokk külmutas selle." can be translated as "The cook froze it.", whereas the second option "Kokk grillis seda." can be translated as "The cook grilled it."
It makes sense that the hamburger meat browned because the cook grilled it.
Therefore, the answer is "Kokk grillis seda.".'''
,
'''What might have happened as a result of "Tüdruk leidis oma helveste seest putuka."?
Options:
- "Ta kallas piima kaussi."
- "Ta kaotas oma isu."
Answer: Let's think step by step.
The premise "Tüdruk leidis oma helveste seest putuka." can be translated from Estonian into English as "The girl found a bug in her cereal."
The first option "Ta kallas piima kaussi." can be translated as "She poured milk in the bowl.", whereas the second option "Ta kaotas oma isu." can be translated as "She lost her appetite."
If the girl found a bug in her cereal then it makes sense that she lost her appetite as a result.
Therefore, the answer is "Ta kaotas oma isu.".'''
,
'''What might be the cause of "Ma otsustasin ööseks koju jääda."?
Options:
- "Ilmateade ennustas tormi."
- "Mu sõbrad käisid peale, et läheksin välja."
Answer: Let's think step by step.
The premise "Ma otsustasin ööseks koju jääda." can be translated from Estonian into English as "I decided to stay home for the night."
The first option "Ilmateade ennustas tormi." can be translated as "The forecast called for storms.", whereas the second option "Mu sõbrad käisid peale, et läheksin välja." can be translated as "My friends urged me to go out."
It makes sense that I decided to stay home for the night because the forecast called for storms.
Therefore, the answer is "Ilmateade ennustas tormi.".'''
,
'''What might have happened as a result of "Naine jäi pensionile."?
Options:
- "Ta sai oma pensioni kätte."
- "Ta maksis oma hüpoteegi ära."
Answer: Let's think step by step.
The premise "Naine jäi pensionile." can be translated from Estonian into English as "The woman retired."
The first option "Ta sai oma pensioni kätte." can be translated as "She received her pension.", whereas the second option "Ta maksis oma hüpoteegi ära." can be translated as "She paid off her mortgage."
If the woman retired then it makes sense that she received her pension as a result.
Therefore, the answer is "Ta sai oma pensioni kätte".'''
]

CoT_examples_it = ['''What might have happened as a result of "L'uomo aprì il rubinetto."?
Options:
- "Il gabinetto si riempì d'acqua."
- "Dell'acqua fluì dal beccuccio."
Answer: Let's think step by step.
The premise "L'uomo aprì il rubinetto." can be translated from Estonian into English as "The man turned on the faucet."
The first option "Il gabinetto si riempì d'acqua." can be translated as "The toilet filled with water.", whereas the second option "Dell'acqua fluì dal beccuccio." can be translated as "Water flowed from the spout."
If the man turned on the faucet then it makes sense that water flowed from the spout as a result.
Therefore, the answer is "Dell'acqua fluì dal beccuccio.".'''
,
'''What might be the cause of "La carne dell'hamburger si è abbrustolita."?
Options:
- "Il cuoco lo ha congelato."
- "Il cuoco l'ha grigliato."
Answer: Let's think step by step.
The premise "La carne dell'hamburger si è abbrustolita." can be translated from Estonian into English as "The hamburger meat broqwned."
The first option "Il cuoco lo ha congelato." can be translated as "The cook froze it.", whereas the second option "Il cuoco l'ha grigliato." can be translated as "The cook grilled it."
It makes sense that the hamburger meat browned because the cook grilled it.
Therefore, the answer is "Il cuoco l'ha grigliato.".'''
,
'''What might have happened as a result of "La ragazza trovò un insetto nei cereali."?
Options:
- "Versò il latte nella ciotola."
- "Perse l'appetito."
Answer: Let's think step by step.
The premise "La ragazza trovò un insetto nei cereali." can be translated from Estonian into English as "The girl found a bug in her cereal."
The first option "Versò il latte nella ciotola." can be translated as "She poured milk in the bowl.", whereas the second option "Perse l'appetito." can be translated as "She lost her appetite."
If the girl found a bug in her cereal then it makes sense that she lost her appetite as a result.
Therefore, the answer is "Perse l'appetito.".'''
,
'''What might be the cause of "Ho deciso di stare a casa per la notte."?
Options:
- "Il meteo annunciava tempesta."
- "I miei amici insistevano per uscire."
Answer: Let's think step by step.
The premise "Ho deciso di stare a casa per la notte." can be translated from Estonian into English as "I decided to stay home for the night."
The first option "Il meteo annunciava tempesta." can be translated as "The forecast called for storms.", whereas the second option "I miei amici insistevano per uscire." can be translated as "My friends urged me to go out."
It makes sense that I decided to stay home for the night because the forecast called for storms.
Therefore, the answer is "Il meteo annunciava tempesta.".'''
,
'''What might have happened as a result of "La donna andò in pensione."?
Options:
- "Ricevette la sua pensione."
- "Ripagò il suo mutuo."
Answer: Let's think step by step.
The premise "La donna andò in pensione." can be translated from Estonian into English as "The woman retired."
The first option "Ricevette la sua pensione." can be translated as "She received her pension.", whereas the second option "Ripagò il suo mutuo." can be translated as "She paid off her mortgage."
If the woman retired then it makes sense that she received her pension as a result.
Therefore, the answer is "Ricevette la sua pensione.".'''
]

def _doc_to_text(doc):
    if doc["question"] == "cause":
        question = "What might be the cause of " + '"' + doc["premise"] + '"' + "?"
    else:
        question = "What might have happened as a result of " + '"' + doc["premise"] + '"' + "?"
    
    question = question + "\n" + "Options:" + "\n" + "- " + '"' + doc["choice1"] + '"' + "\n" + "- " + '"' + doc["choice2"] + '"'
    return question + "\n" + "Answer:"


def doc_to_text_cot_oneshot_et(doc):
    question = _doc_to_text(doc)
    return CoT_examples_et[0] + "\n\n" + question


def doc_to_text_cot_threeshot_et(doc):
    question = _doc_to_text(doc)
    return "\n\n".join(CoT_examples_et[0:3]) + "\n\n" + question


def doc_to_text_cot_fiveshot_et(doc):
    question = _doc_to_text(doc)
    return "\n\n".join(CoT_examples_et) + "\n\n" + question


def doc_to_text_cot_oneshot_it(doc):
    question = _doc_to_text(doc)
    return CoT_examples_it[0] + "\n\n" + question


def doc_to_text_cot_threeshot_it(doc):
    question = _doc_to_text(doc)
    return "\n\n".join(CoT_examples_it[0:3]) + "\n\n" + question


def doc_to_text_cot_fiveshot_it(doc):
    question = _doc_to_text(doc)
    return "\n\n".join(CoT_examples_it) + "\n\n" + question


def doc_to_choice(doc):
    return [doc["choice1"], doc["choice2"]]
