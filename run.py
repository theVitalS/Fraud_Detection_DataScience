import kagglehub
import pandas as pd


# Download/access latest version
path_to_csv_dataset = kagglehub.dataset_download("nelgiriyewithana/credit-card-fraud-detection-dataset-2023") + '/creditcard_2023.csv'
print("Path to dataset files:", path_to_csv_dataset)

# Load the dataset into a pandas DataFrame
df_tr = pd.read_csv(path_to_csv_dataset)

