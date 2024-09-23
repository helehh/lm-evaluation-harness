from lm_eval.filters.extraction import Filter

def doc_to_text(doc):
    if doc["question"] == "cause":
        question = "What might be the cause of " + '"' + doc["premise"] + '"' + "?"
    else:
        question = "What might have happened as a result of " + '"' + doc["premise"] + '"' + "?"
    
    question = question + "\n" + "Options:" + "\n" + "- " + '"' + doc["choice1"] + '"' + "\n" + "- " + '"' + doc["choice2"] + '"'
    return question + "\n" + "Answer:"

def doc_to_choice(doc):
    return [doc["choice1"],  doc["choice2"]]


class QuotesFilter(Filter):
    """ """

    def __init__(self) -> None:
        pass

    def apply(self, resps, docs):
        def filter_set(inst):
            filtered_resp = []
            for resp in inst:
                if resp.startswith('"') and resp.endswith('"'):
                    resp = resp[1:-1]

                filtered_resp.append(resp)

            return filtered_resp

        filtered_resps = [filter_set(resp) for resp in resps]

        return filtered_resps