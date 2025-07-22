from typing import List

class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:

        # Sort both lists so we can perform a linear sweep.
        players.sort()
        trainers.sort()

        trainer_idx: int = 0
        matches: int = 0

        for player_capability in players:
            # Advance to the first trainer who can handle this player's capability.
            while trainer_idx < len(trainers) and trainers[trainer_idx] < player_capability:
                trainer_idx += 1

            # If we've exhausted the trainers list, no further matches are possible.
            if trainer_idx == len(trainers):
                break

            # Match the current player with the found trainer and move to the next trainer.
            matches += 1
            trainer_idx += 1  # The matched trainer is no longer available.

        return matches