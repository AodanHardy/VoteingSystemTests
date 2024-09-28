from rankedChoiceVote import RankedChoiceVoteProcessor
from sampleVoteData import rc_candidates6, rc_votes500_6




processor = RankedChoiceVoteProcessor(rc_votes500_6, rc_candidates6, 3)

print(processor.finalize_results())
