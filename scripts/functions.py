# ----------------------------------
# Import libraries
# ----------------------------------
import pandas as pd
from pathlib import Path


# ----------------------------------
# Configure files and directories
# ----------------------------------
# We assume a top-level project directory containing the following
# subdirectories:
#   /scripts
#   /data
#   /data/processed
# This Python script resides in the /scripts subdirectory

# Define directory locations
dir_scripts = Path()
dir_raw = Path("../data")
dir_processed = Path("../data/processed")

# Check directories
assert dir_scripts.cwd().stem == "scripts", \
    "Execute this script from the /scripts directory"

assert dir_raw.exists(), \
    "/data directory does not exist"

if not dir_processed.exists():
    dir_processed.mkdir()
    print("Created", dir_processed.absolute())


# ----------------------------------
# Define functions
# ----------------------------------
def norm_data(filename, index_col=None):
    """Calculate the mean Z score for each country over time and append to the data frame as a new column."""

    # Import the data
    data = pd.read_csv(filename, index_col=index_col)

    # Calculate individual Z scores
    z = (data - data.values.mean()) / data.values.std(ddof=1)

    # Mean Z score for each country
    mean_z = z.mean(axis=1)    # alternatively, `z.T.mean()`

    # Add new column to data frame
    data["mean_z"] = mean_z

    return data


# ----------------------------------
# Process data
# ----------------------------------
filename = dir_raw.joinpath("gapminder_gdp_europe.csv")

if filename.is_file():
    df = norm_data(filename, index_col="country")
    df.to_csv(dir_processed.joinpath("".join([filename.stem, "_processed", ".csv"])))
