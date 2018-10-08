from api import *
import pytest
import shutil


# TODO put these flags in pytest.ini
# Look here: https://docs.python.org/3/library/configparser.html
download_all_top_entities = True  # Change to True only to download all files (long process)
remove_textrazor_cache = False


class TestApi(object):
    @pytest.mark.skip(reason="just saving time")
    def test_get_students(self):
        students = get_students()
        assert len(students) > 0
        assert "Carlos Souza" in students

    @pytest.mark.skip(reason="just saving time")
    def test_models_exist(self):
        model_path = os.path.join(os.getcwd(), 'models')
        for assignment in range(2, 6):
            model_file = os.path.join(model_path, 'doc2vec_model_assignment_' + str(assignment))
            assert os.path.isfile(model_file)

    @pytest.mark.skip(reason="just saving time")
    def test_load_models(self):
        for assignment in range(2, 6):
            model = load_model(assignment)
            assert type(model) is gensim.models.doc2vec.Doc2Vec

    @pytest.mark.skip(reason="just saving time")
    def test_get_similar_docs(self):
        student = "Carlos Souza"
        assignment = 4
        assert len(get_similar_docs(student, assignment)) > 0

    @pytest.mark.skip(reason="just saving time")
    def test_initialize_textrazor(self):
        client = initialize_textrazor()
        assert type(client) is textrazor.TextRazor

    @pytest.mark.skip(reason="just saving time")
    def test_get_top_entities(self):
        student = "Carlos Souza"
        assignment = 4
        entities = get_top_entities(student, assignment, force_api=False)
        assert len(entities) > 0

    @pytest.mark.skipif(not download_all_top_entities, reason="only to download all files (long process)")
    def test_download_all_top_entities(self):
        path = os.path.join(os.getcwd(), 'models', 'textrazor_cache')
        if remove_textrazor_cache:
            if os.path.exists(path):
                shutil.rmtree(path)

        for student in get_students():
            for assignment in [2, 3, 4]:
                get_top_entities(student, assignment, force_api=remove_textrazor_cache)

        assert len(os.listdir(path)) > 100
