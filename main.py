from rankedChoiceVote import RankedChoiceVoteProcessor
from sampleVoteData import rc_votes1000_7, rc_candidates7
from bigSampleVoteData import votes30000, candidates9



processor = RankedChoiceVoteProcessor(votes30000, candidates9, 3)

print(processor.finalize_results())
