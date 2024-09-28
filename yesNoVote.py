import json

# example vote data
votes_data = [
    '{"vote": "yes"}',
    '{"vote": "no"}',
    '{"vote": "yes"}',
    '{"vote": "yes"}',
    '{"vote": "no"}'
]


def _validate_vote(vote):
    return vote in ['yes', 'no']


class YesNoVoteProcessor:
    def __init__(self, vote_data):
        self.votes_data = vote_data
        self.yes_count = 0
        self.no_count = 0
        self.winner = None
        self.processVotes()

    def processVotes(self):
        for vote_str in self.votes_data:
            try:
                vote_data = json.loads(vote_str)
                vote = vote_data.get('vote').lower()

                if _validate_vote(vote):
                    if vote == 'yes':
                        self.yes_count += 1
                    elif vote == 'no':
                        self.no_count += 1

            except json.JSONDecodeError:
                print(f"Invalid vote data: {vote_str}")
        if self.yes_count > self.no_count:
            self.winner = "yes"
        elif self.yes_count < self.no_count:
            self.winner = "no"
        else:
            self.winner = "draw"

