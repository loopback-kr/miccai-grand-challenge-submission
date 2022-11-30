# Grand Challenges ISLES 2022 Evaluation Container

## Instuctions
1. Clone this repository to the same root path as the nnUNet repository.
2. Define the `volumes` and `MODEL_PREDICTION_DIR` path in `docker-compose.yml`.
3. Run `docker compose up` to get the submission zip file with BIDS format.


## nnUNet original README

This repo contains the evaluation container for the ISLES 2022 challenge (e.g. [ATLAS](https://atlas.grand-challenge.org/)). The code presented here is not needed by participants for the challenge, but it is made available for transparency and to give participants a way to test the evaluations on their own machines.

The ground truth format must be a BIDS dataset.
  
The settings file (`settings.py`) can be used to control data loading, which scoring functions are used, and which summary statistics are returned.

Adapting this code to other BIDS datasets used in other challenges should require only the following settings:
- Updating `GroundTruthBIDSDerivativeName` and `PredictionBIDSDerivativeName` to your derivative names.
- Updating `GroundTruthEntities` and `PredictionEntities` to values matching your data. See the [BIDSIO documentation](https://github.com/npnl/bidsio)
  for more information on how to use these.
- Importing your desired metrics into `settings.py` and adding them to the `ScoringFunctions` dictionary.
