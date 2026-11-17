from contextlib import nullcontext


def observed_items():
    observations = []
    for i in range(0, 6):
        observations.append(input("Enter observation"))
    return observations

def count(observations):
    data = set()
    for i in observations:
        if i in observations:
            data.add((i, 1))
        else:
            return

            