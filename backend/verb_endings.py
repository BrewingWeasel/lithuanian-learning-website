PREFIXES = [
    "ne",
    "be",
    "te",
    "par",
    "per",
    "pra",
    "pri",
    "pa",
    "su",
    "nu",
    "at",
    "iš",
    "ap",
    "at",
    "už",
    "si",
    "į",
]


with open("data/verbs", "r") as f:
    VERB_VALS = {i.split(", ")[0]: i.split(", ")[1:] for i in f.read().splitlines()}


def get_endings(verb):
    for possible_verb in VERB_VALS.keys():
        if verb.endswith(possible_verb):
            trimmed_verb = verb
            verbs_prefixes = ""
            success = True
            while trimmed_verb != possible_verb:
                for prefix in PREFIXES:
                    if trimmed_verb.startswith(prefix):
                        trimmed_verb = trimmed_verb.lstrip(prefix)
                        verbs_prefixes += prefix
                        break
                else:
                    success = False
                    break
            if success:
                orig_vals = VERB_VALS[possible_verb]
                return (
                    verbs_prefixes + possible_verb,
                    verbs_prefixes + orig_vals[0],
                    verbs_prefixes + orig_vals[1],
                )
