
# Accumulated JaccardMax: Unsupervised Effectiveness Estimation Measure Based on Rank Correlation for Image Retrieval

**Authors:** Thiago César Castilho Almeida, [Lucas Pascotti Valem](https://lucasvalem.com), [Daniel Carlos Guimarães Pedronette](https://www.ic.unicamp.br/~dcarlos/)

Department of Statistics, Applied Mathematics, and Computing, São Paulo State University ([UNESP](http://www.rc.unesp.br/)), Rio Claro, Brazil

----------------------
* [Overview](#overview)
* [Installation and Dependencies](#installation-and-dependencies)
* [Project Structure](#project-structure)
* [Running the Code](#running-the-code)
* [Contact](#contact)
* [Acknowledgments](#acknowledgments)

## Overview

The *Accumulated JaccardMax* (AccJacMax) measure is a novel unsupervised effectiveness estimation method based on rank correlation, designed for image retrieval tasks. It provides robust estimations without the need for training or labeled data.

If you use this code, please cite our [paper](https://isvc.net):

```latex
@inproceedings{Almeida2024AccJacMax,
  author    = {Thiago César Castilho Almeida and Lucas Pascotti Valem and Daniel Carlos Guimarães Pedronette},
  title     = {Unsupervised Effectiveness Estimation Measure Based on Rank Correlation for Image Retrieval},
  booktitle = {19th International Symposium on Visual Computing (ISVC)},
  year      = {2024},
  address   = {Lake Tahoe, NV, USA},
}
```

## Installation and Dependencies

This project depends on two main libraries: `scipy` and `pyUDLF`. Follow the steps below to install the dependencies.

### Installation Steps

1. **Clone the repository:**

   ```bash
   git clone https://github.com/thcastilho/AccumulatedJacMax.git
   cd AccumulatedJacMax
   ```

2. **Create a virtual environment (optional, but recommended):**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Linux/MacOS
   venv\Scripts\activate   # On Windows
   ```

3. **Install the dependencies:**

   ```bash
   pip install scipy
   git clone https://github.com/UDLF/pyUDLF.git
   ```

For pyUDLF installation, please follow the instructions on [pyUDLF repository](https://github.com/UDLF/pyUDLF/).

## Project Structure

```bash
├── accumulatedJacMax.py        # Functions to compute Accumulated JaccardMax
├── datasets                    # Directory containing example datasets
│   └── oxford17flowers          # Dataset: OxfordFlowers-17
│       ├── flowers_classes.txt  # Class labels for the flowers
│       ├── flowers_lists.txt    # Image list for the flowers
│       └── ranked_lists         # Ranked lists for the flowers dataset
│           └── CNN-ResNet.txt   # Example of a ranked list using ResNet
├── main.py                     # Main script to compute Accumulated JaccardMax and evaluate the results
└── README.md                   # This README file
```

### File Descriptions

- **accumulatedJacMax.py**: Contains the core functions to compute Accumulated JaccardMax.
- **main.py**: The main script that runs the entire pipeline, from loading the data, calculating MAP (Mean Average Precision), and Accumulated JaccardMax to correlating the results.
- **datasets/oxford17flowers**: Directory containing the OxfordFlowers-17 dataset and precomputed ranked lists.

## Running the Code

To run the Accumulated JacMax code, execute the following command:

```bash
python main.py
```

This will calculate the Accumulated JaccardMax metric and evaluate it based on the OxfordFlowers-17 dataset, provided in the repository.

## Contact

**Thiago César Castilho Almeida**: `tc.almeida@unesp.br`

**Lucas Pascotti Valem**: `lucaspascottivalem@gmail.com` or `lucas.valem@unesp.br`

**Daniel Carlos Guimarães Pedronette**: `daniel.pedronette@unesp.br`

## Acknowledgments

The authors are grateful to the São Paulo Research Foundation - FAPESP (grant \#2018/15597-6), the Brazilian National Council for Scientific and Technological Development - CNPq (grants \#313193/2023-1 and \#422667/2021-8), and Petrobras (grant \#2023/00095-3) for their financial support.
