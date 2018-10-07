import os
from canvasapi import Canvas


def initialize_canvas(course_id):
    api_key = os.environ['CANVAS_API_KEY']
    return Canvas("https://gatech.instructure.com", api_key).get_course(course_id)


def download_from_canvas(origin, destination, canvas_course, log):
    folders = canvas_course.get_folders()
    for folder in folders:
        if origin in str(folder):
            files = folder.get_files()
            for file in files:
                if not os.path.isfile(os.path.join(destination, str(file))):
                    file.download(os.path.join(destination, str(file)))


