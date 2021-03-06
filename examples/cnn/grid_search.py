from examples.cnn.cifar10.cifar10 import get_data
from examples.cnn.cnn import cnn

x0=[50, 50, 50, 50, 50, 50, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.01, 0.01, 0.01, 0.01],  # default configuration
bounds=[(10, 500), (10, 500), (10, 500), (10, 500), (10, 500), (10, 500), (0, 1), (0, 1), (0, 1), (0, 1), (0, 1), (0, 1),
        (0.0001, 0.1), (0.0001, 0.1), (0.0001, 0.1), (0.0001, 0.1)]  # limits

for width in [64, 128, 256]:
    for dropout in [0.25, 0.5]:
        for regularizer in [0.01, 0.001]:
            params = [width * 1.0] * 6 + [dropout] * 6 + [regularizer] * 4
            print(params)
            cnn(params, get_data())
