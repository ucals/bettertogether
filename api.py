import os
import logging
import gensim
import textrazor
import textract


def get_students():
    path = os.path.join(os.getcwd(), "pdfs")
    students = []
    for file in sorted(os.listdir(path)):
        student = str(file).split(" -")[0]
        if student not in students:
            students.append(student)
            logging.debug(student)

    return students


def load_model(assignment):
    doc2vec_model_filepath = os.path.join(os.getcwd(), 'models', 'doc2vec_model_assignment_' + str(assignment))
    return gensim.models.doc2vec.Doc2Vec.load(doc2vec_model_filepath)


def get_similar_docs(student, assignment, model=None):
    if model is None:
        model = load_model(assignment)

    similar_doc = model.docvecs.most_similar(student)
    if logging.getLogger().getEffectiveLevel() == logging.DEBUG:
        logging.debug("Most similar documents of " + student + " for Assignment " + str(assignment))
        for item in similar_doc:
            logging.debug(str(item[1]) + " \t" + str(item[0]))

    return similar_doc


def initialize_textrazor():
    textrazor.api_key = os.environ['TEXTRAZOR_API_KEY']
    return textrazor.TextRazor(extractors=["entities", "topics"])


def get_top_entities(student, assignment, limit=15, textrazor_client=None):
    if textrazor_client is None:
        textrazor_client = initialize_textrazor()

    path_pdfs = os.path.join(os.getcwd(), "pdfs")
    text = textract.process(os.path.join(path_pdfs, student + " - Assignment " + str(assignment) + ".pdf"))\
        .decode("utf-8")
    response = textrazor_client.analyze(text)
    entities = list(response.entities())
    entities.sort(key=lambda x: x.relevance_score, reverse=True)

    top_entities = []
    logging.debug("\n")
    logging.debug("Top entities from " + student + "'s Assignment " + str(assignment))
    seen = set()
    index = 0
    for entity in entities:
        if entity.id not in seen:
            top_entities.append(entity)
            logging.debug(str(entity.relevance_score) + '\t' + str(entity.confidence_score) + '\t' + entity.id)
            seen.add(entity.id)
            index += 1
            if index >= limit:
                break

    return top_entities


