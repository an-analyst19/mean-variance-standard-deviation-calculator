import numpy as np

def calculate(list):
    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")

    numbers = np.array(list).reshape(3, 3)

    calculations = {
        'mean' : [
            np.mean(numbers, axis=0).tolist(),
            np.mean(numbers, axis=1).tolist(),
            np.mean(numbers).item()
        ],

        'variance' : [
            np.var(numbers, axis=0).tolist(),
            np.var(numbers, axis=1).tolist(),
            np.var(numbers).item()
        ],

        'standard deviation':[
            np.std(numbers, axis=0).tolist(),
            np.std(numbers, axis=1).tolist(),
            np.std(numbers).item()
        ],

        'max' : [
            np.max(numbers, axis=0).tolist(),
            np.max(numbers, axis=1).tolist(),
            np.max(numbers).item()
        ],

        'min' : [
            np.min(numbers, axis=0).tolist(),
            np.min(numbers, axis=1).tolist(),
            np.min(numbers).item()
        ],

        'sum' : [
            np.sum(numbers, axis=0).tolist(),
            np.sum(numbers, axis=1).tolist(),
            np.sum(numbers).item()
        ]
    }

    return calculations