import os
from kaggle.api.kaggle_api_extended import KaggleApi

def download_data(dataset, output_dir="data"):
    api = KaggleApi()
    api.authenticate()
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    api.dataset_download_files(dataset, path=output_dir, unzip=True)

if __name__ == "__main__":
    dataset = "mlg-ulb/creditcardfraud"
    download_data(dataset)
    print("Datos descargados en la carpeta data")
