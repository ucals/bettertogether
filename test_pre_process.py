from pre_process import *
import os
import shutil
import pytest
import configparser


config = configparser.ConfigParser()
config.read(os.path.join(os.getcwd(), 'pytest.ini'))
download_all_assignments = (config['pre_process']['download_all_assignments'] == 'True')
is_travis = 'TRAVIS' in os.environ


class TestPreProcess(object):
    def test_initialize_canvas(self):
        edtech_course = initialize_canvas(26123)
        assert edtech_course.name == 'CS6460: Educational Technology'

    # @pytest.mark.skip(reason="just saving time")
    def test_download_from_canvas(self):
        path = os.path.join(os.getcwd(), '.pytest_cache', 'pdfs')
        if os.path.exists(path):
            shutil.rmtree(path)

        os.makedirs(path)

        edtech_course = initialize_canvas(26123)
        origin = "Carlos Souza"
        destination = path
        download_from_canvas(origin, destination, edtech_course)
        assert len(os.listdir(path)) > 0

    @pytest.mark.skipif((not download_all_assignments) and (not is_travis),
                        reason="only to download all files (long process)")
    def test_download_all_assignments(self):
        path = os.path.join(os.getcwd(), 'pdfs')
        if not os.path.exists(path):
            os.makedirs(path)

        edtech_course = initialize_canvas(26123)
        origin = "Class Assignment Library"
        destination = path
        download_from_canvas(origin, destination, edtech_course)
        assert len(os.listdir(path)) > 100
