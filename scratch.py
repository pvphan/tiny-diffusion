"""
TODO:
- Train on GPU, measure experiment speed up for teapot.
- Catalog experiments more thoughtfully, visualize in rerun.
    - Dimensions to change: learning_rate, num_timesteps, embedding_size, hidden_size, hidden_layers
- Build catalog of experiments.
"""
import time

import numpy as np
import rerun as rr

import datasets


def main():
    teapot_dataset = datasets.get_dataset("teapot", 16_000)
    teapot_experiment_path = "exps/teapot_experiment/frames.npy"
    teapot_experiment_data = np.load(teapot_experiment_path)

    rr.init("scratch")
    rr.serve(open_browser=False)
    rr.log(
        "points",
        rr.Points3D(
            positions=teapot_dataset.tensors[0],
        ),
    )

    for data in teapot_experiment_data:
        rr.log(
            "points",
            rr.Points3D(
                positions=data,
            ),
        )

    while True:
        time.sleep(1)


if __name__ == "__main__":
    main()
