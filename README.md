# bettertogether
[![Build Status](https://travis-ci.org/ucals/bettertogether.svg?branch=master)](https://travis-ci.org/ucals/bettertogether)

This app uses Machine Learning NLP/topic modeling/document similarity techniques to group OMSCS CS-6460 Fall 2018 students by interests based on their essays/writing assignments.

With few clicks you will see a ranking of who's work is most similar of yours.

The objective is to help you find people with similar interests who are working in the same topics you are, to facilitate team formation and collaboration. After all, learning is better togehter. Have fun!

![screen_shots](https://github.com/ucals/bettertogether/raw/master/docs/screenshots.jpg "Screen shots")


## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

I built this on a *MacOS X* using *Python 3.7.0*. Check your Python version by running `python -V`. If you have an earlier version of Python installed, I suggest you upgrade it, downloading the [latest Python version](https://www.python.org/downloads/).

On top of that, you will need [pip](https://pypi.org/project/pip/) for installing Python packages. pip is already installed if you are using downloaded from python.org. Just make sure to [upgrade pip](https://pip.pypa.io/en/stable/installing/#upgrading-pip).

### Installing

Clone this repository locally and install all requirements by running in terminal:

```
git clone git@github.com:ucals/bettertogether.git
cd bettertogether
pip install -r requirements.txt
```

### Downloading corpora and preparing to use TextRazor

To run it properly you will have to download all PDFs with students' assignments. To do it, go to [Canvas](https://gatech.instructure.com/), click on `Account -> Settings`, scroll to the bottom of the page, and click `+ New Access Token`. Copy the new token.

You will also have to get a [TextRazor free API Key](https://www.textrazor.com/signup). After creating a free accoung, you will be redirected to a success page containing your API Key. Copy that as well.

Edit your `~/.bash_profile` and add the following line:
```
export CANVAS_API_KEY="your new Canvas token"
export TEXTRAZOR_API_KEY="your new TextRazor API key"
```
Replace `your new Canvas token` by the token you got from Canvas, and `your new TextRazor API key` by the API Key you got from TextRazor . Reload your profile by running `source ~/.bash_profile` from terminal.

Edit `pytest.ini` and set `download_all_assignments = True`. Now, to download all PDFs, just run:
```
pytest -k TestPreProcess
```

This process will take some time. After it ends, you will have all PDFs from students' assignments downloaded in `pdfs/` folder. Finally, I recommend setting `download_all_assignments = False` back in `pytest.ini`.

## Running Tests and the Webserver

All main tests are located in `test_api.py`. To run them:
```
pytest -k TestApi
```

To run the webserver locally, just:
```
python main.py
```
You can access it by browsing to `http://localhost:8080`.

## Training Models

I have included the trained models in the repository as it takes ~10 minutes to train them. If you want to train them yourself, [install Jupyter Notebook](http://jupyter.org/install) and run `tutorial.ipynb` 3 times. At the beginning of each time, alter `assignment` variable in 2nd cell to `"Assignment 2"`, `"Assignment 3"`, and `"Assignment 4"`. This procedure will generate the following files:
```
doc2vec_model_assignment_2
doc2vec_model_assignment_3
doc2vec_model_assignment_4
```
They will be located in `models/` folder. 
 
## Build With

This code was built on top of the following code:
- [Gensim - Topic Modeling for Humans](https://radimrehurek.com/gensim/)
- [Canvas API](https://github.com/ucfopen/canvasapi#documentation)
- [TextRazor API](https://www.textrazor.com/)
- [Textract](https://textract.readthedocs.io/en/stable/)
- [Bottle Python Web Framework](http://bottlepy.org)
- [JsonPickle](https://jsonpickle.github.io/)

## Author

I'm [Carlos Souza](https://www.linkedin.com/in/calsouza/), and I did this side project as part of **Master of Science in Computer Science** [CS-6460 Education Technology](http://omscs6460.gatech.edu/) course from [Georgia Institute of Technology](http://www.omscs.gatech.edu/). I'm accessible at [souza@gatech.edu](mailto:souza@gatech.edu) or [carlos@udacity.com](mailto:carlos@udacity.com).

## License

This project is licensed under the MIT License - see the [LICENSE.md](https://github.com/ucals/bettertogether/blob/master/LICENSE.md) file for details.

## Acknowledgement

- [Quoc Le](mailto:QVL@GOOGLE.COM) & [Tomas Mikolov](mailto:TMIKOLOV@GOOGLE.COM), thanks for this [fantastic article](https://cs.stanford.edu/~quocle/paragraph_vector.pdf)!
- [RaRe Technologies](https://rare-technologies.com/), thanks for this [great tutorial](https://github.com/RaRe-Technologies/gensim/blob/develop/docs/notebooks/doc2vec-lee.ipynb)!
- [Skipgram](https://github.com/skipgram), thanks for this [amazing tutorial](https://github.com/skipgram/modern-nlp-in-python/blob/master/executable/Modern_NLP_in_Python.ipynb)!