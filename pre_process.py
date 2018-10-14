import os
from canvasapi import Canvas
import gensim
import textract
from gensim.parsing.preprocessing import preprocess_string, remove_stopwords


def initialize_canvas(course_id):
    api_key = os.environ['CANVAS_API_KEY']
    return Canvas("https://gatech.instructure.com", api_key).get_course(course_id)


def download_from_canvas(origin, destination, canvas_course):
    folders = canvas_course.get_folders()
    for folder in folders:
        if origin in str(folder):
            files = folder.get_files()
            for file in files:
                if not os.path.isfile(os.path.join(destination, str(file))):
                    file.download(os.path.join(destination, str(file)))


def train_model(assignment_number, save_model=False):
    path_cache = os.path.join(os.getcwd(), '.cache')
    if not os.path.exists(path_cache):
        os.makedirs(path_cache)

    assignment = "Assignment " + str(assignment_number)
    assignment_code = assignment.lower().replace(' ', '_')
    path_pdfs = os.path.join(os.getcwd(), "pdfs")
    path_models = os.path.join(os.getcwd(), "models")

    # Preprocess Unigrams
    unigram_sentences_filepath = os.path.join(path_cache, 'unigram_sentences_all_' + assignment_code + '.txt')
    with open(unigram_sentences_filepath, 'w', encoding='utf_8') as f:
        for file in os.listdir(path_pdfs):
            if assignment in str(file):
                text = textract.process(os.path.join(path_pdfs, file)).decode("utf-8")
                for sent in gensim.summarization.textcleaner.get_sentences(text):
                    processed = preprocess_string(sent)
                    if len(processed) > 0:
                        f.write(" ".join(processed) + "\n")

    unigram_sentences = gensim.models.word2vec.LineSentence(unigram_sentences_filepath)

    # Preprocess Bigrams
    bigram_model_filepath = os.path.join(path_cache, 'bigram_model_all_' + assignment_code)
    bigram_model = gensim.models.Phrases(unigram_sentences)
    bigram_model.save(bigram_model_filepath)
    bigram_sentences_filepath = os.path.join(path_cache, 'bigram_sentences_all_' + assignment_code + '.txt')
    with open(bigram_sentences_filepath, 'w', encoding='utf_8') as f:
        for unigram_sentence in unigram_sentences:
            bigram_sentence = " ".join(bigram_model[unigram_sentence])
            f.write(bigram_sentence + "\n")

    bigram_sentences = gensim.models.word2vec.LineSentence(bigram_sentences_filepath)

    # Preprocess Trigrams
    trigram_model_filepath = os.path.join(path_cache, 'trigram_model_all_' + assignment_code)
    trigram_model = gensim.models.Phrases(bigram_sentences)
    trigram_model.save(trigram_model_filepath)
    trigram_sentences_filepath = os.path.join(path_cache, 'trigram_sentences_all_' + assignment_code + '.txt')
    with open(trigram_sentences_filepath, 'w', encoding='utf_8') as f:
        for bigram_sentence in bigram_sentences:
            trigram_sentence = " ".join(trigram_model[bigram_sentence])
            f.write(trigram_sentence + "\n")

    trigram_sentences = gensim.models.word2vec.LineSentence(trigram_sentences_filepath)

    # Preprocess all assignments
    trigram_assignments_filepath = os.path.join(path_cache,
                                                'trigram_transformed_assignments_all_' + assignment_code + '.txt')
    with open(trigram_assignments_filepath, 'w', encoding='utf_8') as f:
        for file in os.listdir(path_pdfs):
            if assignment in str(file):
                text = textract.process(os.path.join(path_pdfs, file)).decode("utf-8")
                unigram_assignment = preprocess_string(text)
                bigram_assignment = bigram_model[unigram_assignment]
                trigram_assignment = trigram_model[bigram_assignment]
                f.write(" ".join(trigram_assignment) + "\n")

    # Define functions to help training
    file_list = []
    for file in os.listdir(path_pdfs):
        if assignment in str(file):
            file_list.append(file)

    def read_corpus(fname, tokens_only=False):
        with open(fname, encoding="utf-8") as f:
            for i, line in enumerate(f):
                if tokens_only:
                    yield gensim.utils.simple_preprocess(line)
                else:
                    # For training data, add tags
                    yield gensim.models.doc2vec.TaggedDocument(gensim.utils.simple_preprocess(line), [get_student_name(i)])

    def get_student_name(file_index):
        return file_list[file_index].split(" -")[0]

    # Train Doc2Vec model
    train_corpus = list(read_corpus(trigram_assignments_filepath))
    test_corpus = list(read_corpus(trigram_assignments_filepath, tokens_only=True))
    model = gensim.models.doc2vec.Doc2Vec(vector_size=300, min_count=5, epochs=100)
    model.build_vocab(train_corpus)
    model.train(train_corpus, total_examples=model.corpus_count, epochs=model.epochs)
    doc2vec_model_filepath = os.path.join(path_models, 'doc2vec_model_' + assignment_code)
    if save_model:
        model.save(doc2vec_model_filepath)

    return model
