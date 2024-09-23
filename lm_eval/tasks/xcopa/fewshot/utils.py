from functools import partial

def doc_to_text(doc):
    if doc["question"] == "cause":
        question = "What might be the cause of " + '"' + doc["premise"] + '"' + "?"
    else:
        question = "What might have happened as a result of " + '"' + doc["premise"] + '"' + "?"
    
    question = question + "\n" + "Options:" + "\n" + "- " + '"' + doc["choice1"] + '"' + "\n" + "- " + '"' + doc["choice2"] + '"'
    return question + "\n" + "Answer:"

def doc_to_choice(doc):
    """
    Let's use quotes (log likelihood evaluation).
    """
    return ['"' + doc["choice1"] + '"', '"' + doc["choice2"] + '"']
 