from pre_process import *
import os
import shutil
import pytest


download_all_assignments = False  # Change to True only to download all files (long process)


class TestPreProcess(object):
    def test_initialize_canvas(self):
        edtech_course = initialize_canvas(26123)
        assert edtech_course.name == 'CS6460: Educational Technology'

    @pytest.mark.skip(reason="just saving time")
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

    @pytest.mark.skipif(not download_all_assignments, reason="only to download all files (long process)")
    def test_download_all_assignments(self):
        path = os.path.join(os.getcwd(), 'pdfs')
        if not os.path.exists(path):
            os.makedirs(path)

        edtech_course = initialize_canvas(26123)
        origin = "Class Assignment Library"
        destination = path
        download_from_canvas(origin, destination, edtech_course, log=False)
        assert len(os.listdir(path)) > 100
