import time

import rerun as rr

import datasets


def main():
    teapot_dataset = datasets.get_dataset("teapot")

    rr.init("scratch")
    rr.serve(open_browser=False)
    rr.log(
        "points",
        rr.Points3D(
            positions=teapot_dataset.tensors[0],
        ),
    )

    while True:
        time.sleep(1)


if __name__ == "__main__":
    main()
