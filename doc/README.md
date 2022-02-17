# Journals2Data

### version

> Version 1.x.x (Synchronous, Selenium)

### description

This library is used to scrap automaticaly online newspapers, by providing a list of newspapers front page URLs.

> Since it is a library, you must call its objects to be able to use it. However, if you directly wants to run it, you can do so by creating a script (outside `journals2data`, not inside, but where it can access it), then `from journals2data import main`. Then run `main(<conf_filepath>)`. Finally, just run your script.
>
> Below, you will get more info on how to call `journals2data`.

## Installation

> Before everything, you will need to download the zipped build of the project as well as the zip containing BERT models. Find these on GitHub > Releases > Latest

[GitHub releases for Journals2Data](https://github.com/0nyr/python/releases) 

> WARN: Don't download the full zip of the project (Github > Code button), this contains everything and is not intended to be installed.

### step 1: unzip

1. Get the last version of `journals2data-<last_version>.zip`.
2. Put the zip in the directory where you plan to use `journals2data`.
3. Unzip it with the command `unzip journals2data-<last_version>.zip`. After that you can also remove the zip file.

```shell
(base) onyr@laerys:~/Documents/code/python/journals2data/releases$ ls
journals2data-0.1.1.zip
(base) onyr@laerys:~/Documents/code/python/journals2data/releases$ unzip journals2data-0.1.1.zip 
Archive:  journals2data-0.1.1.zip
   creating: journals2data/
   creating: journals2data/console/
  inflating: journals2data/console/ansictrlsequence.py  
[...]
  inflating: journals2data/configuration.py  
  inflating: journals2data/README.md  
(base) onyr@laerys:~/Documents/code/python/journals2data/releases$ ls
journals2data  journals2data-0.1.1.zip
```

### step 2: install dependencies in venv

1. Install conda. There is a script you can run at`cmd/install_conda.sh`
2. Install dependencies by creating a virtual environment using conda. Modify the `j2d.yml` file `prefix` param to match you `conda` path. Then use `conda env create --file j2d.yml` to create a venv from this file.

> You can also change the environment name if you wish. just make sure to modify both `name` and `prefix` params accordingly.

```yml
prefix: /home/florian/anaconda3/envs/j2d
```

> The `requirements.txt` file use is not recommanded since some modules are imported over `conda` and some others with `pip` from the conda venv.

Example:

```shell
(py39) florian@liris-livrons:~/code/testzone$ ls
journals2data  journals2data-0.1.1.zip
(py39) florian@liris-livrons:~/code/testzone$ cd journals2data/
(py39) florian@liris-livrons:~/code/testzone/journals2data$ ls
cli.py  configuration.py  exception    journals2data.py  README.md         setup.py
cmd     console           __init__.py  logs              requirements.txt  signalhandler.py
conf    data              j2d.yml      out               scraper           utils
(py39) florian@liris-livrons:~/code/testzone/journals2data$ ls
cli.py  configuration.py  exception    journals2data.py  README.md         setup.py
cmd     console           __init__.py  logs              requirements.txt  signalhandler.py
conf    data              j2d.yml      out               scraper           utils
(py39) florian@liris-livrons:~/code/testzone/journals2data$ conda env create --file j2d.yml
Collecting package metadata (repodata.json): done
Solving environment: done


==> WARNING: A newer version of conda exists. <==
  current version: 4.10.1
  latest version: 4.10.3

Please update conda by running

    $ conda update -n base -c defaults conda


Preparing transaction: done
Verifying transaction: done
Executing transaction: done
Installing pip dependencies: / Ran pip subprocess with arguments:
['/home/florian/anaconda3/envs/j2d/bin/python', '-m', 'pip', 'install', '-U', '-r', '/home/florian/code/testzone/journals2data/condaenv.9flbir4q.requirements.txt']
Pip subprocess output:
[...]
Collecting wrapt==1.12.1
  Using cached wrapt-1.12.1-cp39-cp39-linux_x86_64.whl
Requirement already satisfied: wheel<1.0,>=0.23.0 in /home/florian/anaconda3/envs/j2d/lib/python3.9/site-packages (from astunparse==1.6.3->-r /home/florian/code/testzone/journals2data/condaenv.9flbir4q.requirements.txt (line 2)) (0.36.2)
Requirement already satisfied: setuptools>=40.3.0 in /home/florian/anaconda3/envs/j2d/lib/python3.9/site-packages (from google-auth==1.32.1->-r /home/florian/code/testzone/journals2data/condaenv.9flbir4q.requirements.txt (line 13)) (52.0.0.post20210125)
Requirement already satisfied: certifi>=2017.4.17 in /home/florian/anaconda3/envs/j2d/lib/python3.9/site-packages (from requests==2.25.1->-r /home/florian/code/testzone/journals2data/condaenv.9flbir4q.requirements.txt (line 41)) (2021.5.30)
Installing collected packages: urllib3, pyasn1, idna, chardet, six, rsa, requests, pyasn1-modules, oauthlib, cachetools, soupsieve, requests-oauthlib, google-auth, werkzeug, tqdm, tensorboard-plugin-wit, tensorboard-data-server, sgmllib3k, requests-file, regex, pyparsing, protobuf, numpy, markdown, joblib, grpcio, google-auth-oauthlib, filelock, click, beautifulsoup4, absl-py, wrapt, typing-extensions, tokenizers, tldextract, tinysegmenter, threadpoolctl, termcolor, tensorflow-estimator, tensorboard, scipy, sacremoses, pyyaml, pytz, python-dateutil, pillow, packaging, opt-einsum, nltk, lxml, keras-preprocessing, keras-nightly, jieba3k, h5py, google-pasta, gast, flatbuffers, feedparser, feedfinder2, cssselect, astunparse, transformers, torch, tensorflow, selenium, scikit-learn, schedule, pandas, newspaper3k
Successfully installed absl-py-0.13.0 astunparse-1.6.3 beautifulsoup4-4.9.3 cachetools-4.2.2 chardet-4.0.0 click-8.0.1 cssselect-1.1.0 feedfinder2-0.0.4 feedparser-6.0.8 filelock-3.0.12 flatbuffers-1.12 gast-0.4.0 google-auth-1.32.1 google-auth-oauthlib-0.4.4 google-pasta-0.2.0 grpcio-1.34.1 h5py-3.1.0 idna-2.10 jieba3k-0.35.1 joblib-1.0.1 keras-nightly-2.5.0.dev2021032900 keras-preprocessing-1.1.2 lxml-4.6.3 markdown-3.3.4 newspaper3k-0.2.8 nltk-3.6.2 numpy-1.19.5 oauthlib-3.1.1 opt-einsum-3.3.0 packaging-20.9 pandas-1.2.5 pillow-8.3.0 protobuf-3.17.3 pyasn1-0.4.8 pyasn1-modules-0.2.8 pyparsing-2.4.7 python-dateutil-2.8.1 pytz-2021.1 pyyaml-5.4.1 regex-2021.4.4 requests-2.25.1 requests-file-1.5.1 requests-oauthlib-1.3.0 rsa-4.7.2 sacremoses-0.0.45 schedule-1.1.0 scikit-learn-0.24.2 scipy-1.7.0 selenium-3.141.0 sgmllib3k-1.0.0 six-1.15.0 soupsieve-2.2.1 tensorboard-2.5.0 tensorboard-data-server-0.6.1 tensorboard-plugin-wit-1.8.0 tensorflow-2.5.0 tensorflow-estimator-2.5.0 termcolor-1.1.0 threadpoolctl-2.1.0 tinysegmenter-0.3 tldextract-3.1.0 tokenizers-0.10.3 torch-1.9.0 tqdm-4.61.1 transformers-4.3.3 typing-extensions-3.7.4.3 urllib3-1.26.6 werkzeug-2.0.1 wrapt-1.12.1

done
#
# To activate this environment, use
#
#     $ conda activate j2d
#
# To deactivate an active environment, use
#
#     $ conda deactivate

(py39) florian@liris-livrons:~/code/testzone/journals2data$ conda info -e
# conda environments:
#
base                     /home/florian/anaconda3
j2d                      /home/florian/anaconda3/envs/j2d
py39                  *  /home/florian/anaconda3/envs/py39

(py39) florian@liris-livrons:~/code/testzone/journals2data$ conda activate j2d
(j2d) florian@liris-livrons:~/code/testzone/journals2data$ ls
cli.py  configuration.py  exception    journals2data.py  README.md         setup.py
cmd     console           __init__.py  logs              requirements.txt  signalhandler.py
conf    data              j2d.yml      out               scraper           utils
(j2d) florian@liris-livrons:~/code/testzone/journals2data$ cd ..
(j2d) florian@liris-livrons:~/code/testzone$ python3
Python 3.9.5 (default, Jun  4 2021, 12:28:51) 
[GCC 7.5.0] :: Anaconda, Inc. on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> fro
from        frozenset(  
>>> from journals2data import main
2021-07-12 11:48:13.290251: W tensorflow/stream_executor/platform/default/dso_loader.cc:64] Could not load dynamic library 'libcudart.so.11.0'; dlerror: libcudart.so.11.0: cannot open shared object file: No such file or directory
2021-07-12 11:48:13.290271: I tensorflow/stream_executor/cuda/cudart_stub.cc:29] Ignore above cudart dlerror if you do not have a GPU set up on your machine.
Python Current Working directory = /home/florian/code/testzone
>>> main("/home/florian/code/testzone/journals2data/conf/journals2data.florian.conf")
****** running J2D [--conf_path: /home/florian/code/testzone/journals2data/conf/journals2data.florian.conf]
****** config.params = [see below]
{
    "CONFIG_FILETYPE": "csv",
    "DEFAULT_OUTPUT_FILEPATH": "/home/florian/code/python/journals2data/out/out.json",
    "CONFIG_CSV_FILEPATH": "/home/florian/code/python/journals2data/src/journals2data/conf/csv/config_elod_long_test.csv",
    "GECKODRIVER_LOG_FILEPATH": "/home/florian/code/python/journals2data/logs/geckodriver.log",
    "BERT_MODEL_BASEPATH": "/home/florian/code/models/",
    "BERT_LANGUAGE_DIRS": {
        "en": "BERT_classifier_en/",
        "fr": "BERT_classifier_fr/"
    },
    "DEBUG": true,
    "VERBOSE": 2,
    "DEFAULT_TIMEOUT": 120,
    "SOURCE_TIMEOUT": 120,
    "ARTICLE_TIMEOUT": 120,
    "USER": null,
    "ARTICLE_SCORE_THRESHOLD": null,
    "NB_RUN_LIMIT": 2,
    "RUN_NUMBER": 0,
    "IS_J2D_RUNNING": true,
    "POTENTIAL_ARTICLE_LIMIT": 3,
    "SCHEDULE_SYNC_SCRAP_MIN": 1,
    "J2D_RUN_START_TIME": 1626083320.3937113,
    "ARTICLE_SAVING_OPTION": 1,
    "EMPTY_OUT_FILE": true
}
Default out file [/home/florian/code/python/journals2data/out/out.json] content has been erased.
****** SIGINT (CTRL + C) termination handled. ******

```

3. Install geckodriver. There is a script you can run at`cmd/install_gecko.sh`. Before that, make sure you have an available Firefox browser by running`firefox --version`. You should see something like what is shown below. If it is not the case, install firefox.

```shell
(base) onyr@laerys:~$ firefox --version
Mozilla Firefox 89.0.2
```

4. Switch to this virtual environment: `conda activate <venv_name>`.

## Configuration

### what to edit

The configuration process is important since it dictates how the library will work.

> WARN: Some functionality are not yet implemented and some parameters are not fully working yet.

1. Modify the list of article to scrap by modifying`conf/config.csv`. You can find examples inside`conf/example`.
2. Modify the conf params by making a`conf/journals2data.conf` file. You can find examples inside`conf/example` or check `conf/journals2data.example.conf`.

### conf params description

> All params are predefined and initialized by default inside `J2DConfiguration.py`.

> NOTE: All filepath are intended to be absolute.

> WARN: For now, since this version of the library is synchronous, the scraping frequency param from `config.csv` is not used. Use instead the conf param `SCHEDULE_SYNC_SCRAP_MIN`.

`CONFIG_FILETYPE`: Type of outfile. Default and only value possible for now is `csv`.

`DEFAULT_OUTPUT_FILEPATH`: Filepath of the default output file, in `.json` format.

`CONFIG_CSV_FILEPATH`: Filepath of the `config.csv` file containing the list of source URLs for scraping. You can find examples inside `conf/example`. NOTE: This params replaces for now what isFilepath of the

`GECKODRIVER_LOG_FILEPATH`: Filepath of the log file used by `selenium`.

`BERT_MODEL_BASEPATH`: Base filepath for BERT models directories

`BERT_LANGUAGE_DIRS`: Dictionnary containing keys as language letter codes like `en` and values being directory names containing BERT models.

`DEBUG`: Run in debug mode.

`VERBOSE`: Choose a verbosity level among what is possible: NONE, NO_COLOR, COLOR. Check `utils.enums` for details.

`DEFAULT_TIMEOUT`: Default max waiting time for any page loading.

`SOURCE_TIMEOUT`: Max waiting time for a souce loading.

`ARTICLE_TIMEOUT`: Max waiting time for article loading.

`USER`: This param is not intended to be used.

`ARTICLE_SCORE_THRESHOLD`: Not used yet. Allows to exclude articles whose scraping score is too low. Such a score is not computed yet. So don't use this param for now.

`NB_RUN_LIMIT`: Useful for debug. Set the library to stop itself after a certain number of source scraping runs.

`RUN_NUMBER`: Source scraping run number.

`IS_J2D_RUNNING`: Do no use this param by hand.

`POTENTIAL_ARTICLE_LIMIT`: Useful for debug. Limit the number of articles being scraped so as to speed the execution of the library.

`SCHEDULE_SYNC_SCRAP_MIN`: Important param! Set in minutes the time to wait between each source scraping run.

`J2D_RUN_START_TIME`: Do no use this param by hand.

`ARTICLE_SAVING_OPTION`: Set how the articles should be saved or not: NO_SAVING, SAVE_TO_FILE.

`EMPTY_OUT_FILE`: Wether or not to clear the out file when relaunching the library.

## Running

There are 3 ways to use and run the library.

1. **Intended way**: Use the library as any module and import it's top level object to use it. This is the intended way of using the library. See`cli.cpp` to get a basic example on how to use its internal objects.

It's pretty straightforward. `Journals2Data` is the main commanding objects that contains all necessary objects of the library. `J2DConfiguration` is an object to load the `.conf` file that contains several parameters on how to load the library.

> See conf param description below to get more info on them.

Example of scripts using `journals2data`:

```python
import journals2data
new_config = journals2data.J2DConfiguration(
    args.conf_path
)
j2d = journals2data.Journals2Data(
    config=new_config
)
j2d.master_scraper.scheduled_sync_scrap()
```

> See `cli.py` to get a real example of script using the library.

2. **Quick test**: Run`python3`, then`import journals2data` then try it `

```shell
(py39) onyr@laerys:~/Documents/code/python/journals2data/src$ python3
Python 3.9.5 (default, Jun  4 2021, 12:28:51) 
[GCC 7.5.0] :: Anaconda, Inc. on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import journals2data
Python Current Working directory = /home/onyr/Documents/code/python/journals2data/src
>>> journals2data.main("D:\PFE\Dev\Journal2data\src\journals2data\conf\journals2data.conf")
****** running J2D [--conf_path: /home/onyr/Documents/code/python/journals2data/src/journals2data/conf/journals2data.onyr.conf]
****** config.params = [see below]
{
    "CONFIG_FILETYPE": "csv",
    "DEFAULT_OUTPUT_FILEPATH": "/home/onyr/Documents/code/python/journals2data/out/out.json",
    "CONFIG_CSV_FILEPATH": "/home/onyr/Documents/code/python/journals2data/src/journals2data/conf/csv/config_3_journals.csv",
    "GECKODRIVER_LOG_FILEPATH": "/home/onyr/Documents/code/python/journals2data/logs/geckodriver.log",
    "BERT_MODEL_BASEPATH": "/home/onyr/Documents/code/models/",
    "BERT_LANGUAGE_DIRS": {
        "en": "BERT_classifier_en/",
        "fr": "BERT_classifier_fr/"
    },
    "DEBUG": true,
    "VERBOSE": 2,
    "DEFAULT_TIMEOUT": 120,
    "SOURCE_TIMEOUT": 120,
    "ARTICLE_TIMEOUT": 120,
    "USER": "onyr",
    "ARTICLE_SCORE_THRESHOLD": null,
    "NB_RUN_LIMIT": 2,
    "RUN_NUMBER": 0,
    "IS_J2D_RUNNING": true,
    "POTENTIAL_ARTICLE_LIMIT": 3,
    "SCHEDULE_SYNC_SCRAP_MIN": 2,
    "J2D_RUN_START_TIME": 1625763583.9314969,
    "ARTICLE_SAVING_OPTION": 1,
    "EMPTY_OUT_FILE": true
}
Default out file [/home/onyr/Documents/code/python/journals2data/out/out.json] content has been erased.
****** SIGINT (CTRL + C) termination handled. ******
^C!!!!!! SIGINT or CTRL-C detected. Trying to exit gracefully !!!!!!
(py39) onyr@laerys:~/Documents/code/python/journals2data/src$ 
```

3. **Quick script test**: Similarly to step 2, create a script like`try_j2d.py`, then execute it:

```python
from journals2data import main
main("/home/onyr/Documents/code/python/journals2data/src/journals2data/conf/journals2data.onyr.conf")
```

Example:

```shell
(py39) florian@liris-livrons:~/code/testzone$ ls /home/florian/code/testzone/journals2data/conf/journals2data.florian.conf 
/home/florian/code/testzone/journals2data/conf/journals2data.florian.conf
(py39) florian@liris-livrons:~/code/testzone$ python3
Python 3.9.5 (default, Jun  4 2021, 12:28:51) 
[GCC 7.5.0] :: Anaconda, Inc. on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> from journals2data import main
2021-07-12 11:03:15.752140: W tensorflow/stream_executor/platform/default/dso_loader.cc:64] Could not load dynamic library 'libcudart.so.11.0'; dlerror: libcudart.so.11.0: cannot open shared object file: No such file or directory
2021-07-12 11:03:15.752158: I tensorflow/stream_executor/cuda/cudart_stub.cc:29] Ignore above cudart dlerror if you do not have a GPU set up on your machine.
Python Current Working directory = /home/florian/code/testzone
>>> main("/home/florian/code/testzone/journals2data/conf/journals2data.florian.conf")
****** running J2D [--conf_path: /home/florian/code/testzone/journals2data/conf/journals2data.florian.conf]
****** config.params = [see below]
{
    "CONFIG_FILETYPE": "csv",
    "DEFAULT_OUTPUT_FILEPATH": "/home/florian/code/python/journals2data/out/out.json",
    "CONFIG_CSV_FILEPATH": "/home/florian/code/python/journals2data/src/journals2data/conf/csv/config_elod_long_test.csv",
    "GECKODRIVER_LOG_FILEPATH": "/home/florian/code/python/journals2data/logs/geckodriver.log",
    "BERT_MODEL_BASEPATH": "/home/florian/code/models/",
    "BERT_LANGUAGE_DIRS": {
        "en": "BERT_classifier_en/",
        "fr": "BERT_classifier_fr/"
    },
    "DEBUG": true,
    "VERBOSE": 2,
    "DEFAULT_TIMEOUT": 120,
    "SOURCE_TIMEOUT": 120,
    "ARTICLE_TIMEOUT": 120,
    "USER": null,
    "ARTICLE_SCORE_THRESHOLD": null,
    "NB_RUN_LIMIT": 2,
    "RUN_NUMBER": 0,
    "IS_J2D_RUNNING": true,
    "POTENTIAL_ARTICLE_LIMIT": 3,
    "SCHEDULE_SYNC_SCRAP_MIN": 1,
    "J2D_RUN_START_TIME": 1626080626.7153962,
    "ARTICLE_SAVING_OPTION": 1,
    "EMPTY_OUT_FILE": true
}
Default out file [/home/florian/code/python/journals2data/out/out.json] content has been erased.
****** SIGINT (CTRL + C) termination handled. ******
{"url": "https://www.leprogres.fr/e-services/ForgotPassword", "title_from_a_tag": "mot de passe oublié ?", "scraped_nb_times": "0"}
{"url": "https://www.leprogres.fr/edition-ain-est/a-la-une", "title_from_a_tag": "Ain Est", "scraped_nb_times": "0"}
{"url": "https://www.leprogres.fr/edition-ain-ouest/a-la-une", "title_from_a_tag": "Ain Ouest", "scraped_nb_times": "0"}
{"url": "https://www.leprogres.fr/edition-est-lyonnais/a-la-une", "title_from_a_tag": "Est Lyonnais", "scraped_nb_times": "0"}
{"url": "https://www.leprogres.fr/edition-haute-loire/a-la-une", "title_from_a_tag": "Haute-Loire", "scraped_nb_times": "0"}
[...]
```

## Troubleshooting

### change tmp/ to a bigger folder and install conda venv named py39

> WARN: Firefox cannot be run as `root`. Hence, install `conda` and run the project from a non-root user like `ssh_user`.

1. Use`mkdir tmp` to create a`tmp` directory inside for instance`/home/ssh_user`.
2. `export TEMP=/home/ssh_user/tmp`: export a new variable so as to change the`tmp` directory for the current terminal sessions.
3. Install venv named`py39`. Inside`python/journals2data/conf/`, run`conda venv create --file environment.yml`.
4. WARN: Make sure to`rm -rf ~/tmp/` after that! Else, if trying to reuse it, it could make errors.

### send bert models/ directory over SSH

`scp -r -P 22 models/ florian@134.214.108.151:/home/florian/code/`: Adapt this command to copy over SSH. Note the use of `-r` since it is a directory.
