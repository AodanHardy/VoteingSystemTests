import json
import random as rand


def generateRankedChoiceVotes(numVotes, candidate_names):
    candidatesDict = {i + 1: name for i, name in enumerate(candidate_names)}

    random_votes = []
    for i in range(0, numVotes):
        numChoices = rand.randint(1, len(candidatesDict))


        shuffled_candidates = rand.sample(list(candidatesDict.keys()), numChoices)


        vote_dict = {"rankings": shuffled_candidates}


        vote_json = json.dumps(vote_dict)


        random_votes.append(vote_json)

    formatted_candidates = {id: name for id, name in candidatesDict.items()}
    finalCandidates = f"candidates{len(candidate_names)} = {formatted_candidates}"

    formatted_votes = f"votes{numVotes} = " + str(random_votes)
    return finalCandidates, formatted_votes


candidates, voteData = generateRankedChoiceVotes(500, ['Amy', 'Luke', 'John', 'Paul', 'Ellie', 'Anna'])

print(candidates)
print(voteData)


def generateFPTPVotes(numVotes, candidates):
    pass


def generateYesNoVotes(numVotes):
    pass


