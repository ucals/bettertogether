# bettertogether

This app uses Machine Learning NLP/topic modeling/document similarity techniques to group OMSCS CS-6460 Fall 2018 students by interests based on their essays/writing assignments.

With few clicks you will see a ranking of who's work is most similar of yours.

The objective is to help you find people with similar interests who are working in the same topics you are, to facilitate team formation and collaboration. After all, learning is better togehter. Have fun!

![screen\_shots][image-1]


## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

I built this on a *MacOS X* using *Python 3.7.0*. Check your Python version by running `python -V`. If you have an earlier version of Python installed, I suggest you upgrade it, downloading the [latest Python version][1].

On top of that, you will need [pip][2] for installing Python packages. pip is already installed if you are using downloaded from python.org. Just make sure to [upgrade pip][3].

### Installing

Clone this repository locally and install all requirements by running in terminal:

	git clone git@github.com:ucals/bettertogether.git
	cd bettertogether
	pip install -r requirements.txt

### Downloading corpora and preparing to use TextRazor

To run it properly you will have to download all PDFs with students' assignments. To do it, go to [Canvas][4], click on `Account -> Settings`, scroll to the bottom of the page, and click `+ New Access Token`. Copy the new token.

You will also have to get a [TextRazor free API Key][5]. After creating a free accoung, you will be redirected to a success page containing your API Key. Copy that as well.

Edit your `~/.bash_profile` and add the following line:
	export CANVAS_API_KEY="your new Canvas token"
	export TEXTRAZOR_API_KEY="your new TextRazor API key"
Replace `your new Canvas token` by the token you got from Canvas, and `your new TextRazor API key` by the API Key you got from TextRazor . Reload your profile by running `source ~/.bash_profile` from terminal.

Edit `pytest.ini` and set `download_all_assignments = True`. Now, to download all PDFs, just run:
	pytest -k TestPreProcess

This process will take some time. After it ends, you will have all PDFs from students' assignments downloaded in `pdfs/` folder. Finally, I recommend setting `download_all_assignments = False` back in `pytest.ini`.

## Running Tests and the Webserver

All main tests are located in `test_api.py`. To run them:
	pytest -k TestApi

To run the webserver locally, just:
	python main.py
You can access it by browsing to `http://localhost:8080`.

## Training Models

I have included the trained models in the repository as it takes \~10 minutes to train them. If you want to train them yourself, [install Jupyter Notebook][6] and run `tutorial.ipynb` 3 times. At the beginning of each time, alter `assignment` variable in 2nd cell to `"Assignment 2"`, `"Assignment 3"`, and `"Assignment 4"`. This procedure will generate the following files:
	doc2vec_model_assignment_2
	doc2vec_model_assignment_3
	doc2vec_model_assignment_4
They will be located in `models/` folder. 
 
## Build With

This code was built on top of the following code:
- [Gensim - Topic Modeling for Humans][7]
- [Canvas API][8]
- [TextRazor API][9]
- [Textract][10]
- [Bottle Python Web Framework][11]
- [JsonPickle][12]

## Author

I'm [Carlos Souza][13], and I did this side project as part of **Master of Science in Computer Science** [CS-6460 Education Technology][14] course from [Georgia Institute of Technology][15]. I'm accessible at [souza@gatech.edu][16] or [carlos@udacity.com][17].

## License

This project is licensed under the MIT License - see the [LICENSE.md][18] file for details.

## Acknowledgement

- [Quoc Le][19] & [Tomas Mikolov][20], thanks for this [fantastic article][21]!
- [RaRe Technologies][22], thanks for this [great tutorial][23]!
- [Skipgram][24], thanks for this [amazing tutorial][25]!

[1]:	https://www.python.org/downloads/
[2]:	https://pypi.org/project/pip/
[3]:	https://pip.pypa.io/en/stable/installing/#upgrading-pip
[4]:	https://gatech.instructure.com/
[5]:	https://www.textrazor.com/signup
[6]:	http://jupyter.org/install
[7]:	https://radimrehurek.com/gensim/
[8]:	https://github.com/ucfopen/canvasapi#documentation
[9]:	https://www.textrazor.com/
[10]:	https://textract.readthedocs.io/en/stable/
[11]:	http://bottlepy.org
[12]:	https://jsonpickle.github.io/
[13]:	https://www.linkedin.com/in/calsouza/
[14]:	http://omscs6460.gatech.edu/
[15]:	http://www.omscs.gatech.edu/
[16]:	mailto:souza@gatech.edu
[17]:	mailto:carlos@udacity.com
[18]:	https://github.com/ucals/bettertogether/blob/master/LICENSE.md
[19]:	mailto:QVL@GOOGLE.COM
[20]:	mailto:TMIKOLOV@GOOGLE.COM
[21]:	https://cs.stanford.edu/~quocle/paragraph_vector.pdf
[22]:	https://rare-technologies.com/
[23]:	https://github.com/RaRe-Technologies/gensim/blob/develop/docs/notebooks/doc2vec-lee.ipynb
[24]:	https://github.com/skipgram
[25]:	https://github.com/skipgram/modern-nlp-in-python/blob/master/executable/Modern_NLP_in_Python.ipynb

[image-1]:	https://github.com/ucals/bettertogether/raw/master/docs/screenshots.jpg "Screen shots"