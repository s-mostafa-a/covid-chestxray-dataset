# Explanation
They have collected all the information about patients in the rows of [metadata.csv](./metadata.csv), which easily can be turn into pandas dataframe.

## scripts
#### [hannover.ipynb](./scripts/hannover.ipynb)
This is just for adding some new data to the metadata.csv file.
#### [metadata_visualization.ipynb](./scripts/metadata_visualization.ipynb)
This notebook reads metadata.csv and draws some diagrams based on csv's columns.
#### [select_covid_patient_X_ray_images.py](./scripts/select_covid_patient_X_ray_images.py)
This scripts selects all covid-19 data and puts them somewhere else.
#### [verify_and_modify_dataset.ipynb](./scripts/verify_and_modify_dataset.ipynb)
This is just for shaping the metadata.csv file.
#### [radiopedia.ipynb](./scripts/radiopedia.ipynb)
This is just for adding some new data to the metadata.csv file from radiopedia.
#### [test_dataloader.py](./scripts/test_dataloader.py)
This file tests an interesting data loader which loads data from csv but also have got the images.
