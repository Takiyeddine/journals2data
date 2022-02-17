# Journals2Data

## Objectif

Development of a deployable Python library allowing the use of online  scraping functions at regular intervals, through the use of pre-trained models.

##### Input: CSV (or JSON?) config file

* URLs of journals to scrap
* Scraping frequency, interval durations
* Path for out files
* Language of journals, used to select the correct pre-trained model.

##### Output: JSON file containing articles

* URL of the journal
* URL of the article
* Timestamp of scaping
* (if available) date of publication of the article
* Title
* Full text

### Input

inside `conf/`, a .csv file with a list of source URLs, language and scraping frequency associated with each URL.

### Output

A big JSON file containing unique scraped articles with metadata and full text.

## commands

### conda

> NB: [activate conda venv in VSCode](https://medium.com/@udiyosovzon/how-to-activate-conda-environment-in-vs-code-ce599497f20d).

`source /home/onyr/Downloads/yes/bin/activate`:

`conda activate venv1`: activate `venv1` virtual environment.

`conda install <package>`: install a package into a conda environment. Make sure to be inside the right environment.

`conda list`: list installed packaged.

`~/Downloads/yes/envs/venv1/bin/pip3 install <package_name>`: install a package using pip from virtual environment. Ex:

```shell
(venv1) onyr@laerys:~/Documents/code/python/scripts/requests$ ~/Downloads/yes/envs/venv1/bin/pip3 install transformers
Collecting transformers
  Downloading transformers-4.8.1-py3-none-any.whl (2.5 MB)
     |████████████████████████████████| 2.5 MB 7.5 MB/s 
Collecting packaging
```

`conda -V`: display the version of `conda` installed.

## Notes

##### long strings in json file

On JSON files with long string, use `ALT`+`Z` to change between word vrap mode or not. The long string can either be displayed entirely or be troncated only visualy by VSCode and ended with `...`.
