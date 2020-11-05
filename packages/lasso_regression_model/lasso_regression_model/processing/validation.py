from lasso_regression_model.config import config

import pandas as pd


def validate_inputs(input_data):

    validated_data = input_data.copy()

    # check for numerical NA values not seen during training
    if input_data[config.NUMERICAL_NA_NOT_ALLOWED].isnull().any().any():
        validated_data = validated_data.dropna(
            axis=0, subset=config.NUMERICAL_NA_NOT_ALLOWED
        )

    # check for categorical NA values not seen during training
    if input_data[config.CATEGORICAL_NA_NOT_ALLOWED].isnull().any().any():
        validated_data = validated_data.dropna(
            axis=0, subset=config.CATEGORICAL_NA_NOT_ALLOWED
        )

    # check for values <= 0 for the log transformed variables
    if (input_data[config.NUMERICAL_LOG_VARS] <= 0).any().any():
        vars_with_neg_values = config.NUMERICAL_LOG_VARS[
            (input_data[config.NUMERICAL_LOG_VARS] <= 0).any()
        ]
        validated_data = validated_data[validated_data[vars_with_neg_values] > 0]

    return validated_data
