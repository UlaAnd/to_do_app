import os


class Config:
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))

    TEXT_FILE_DIR = os.path.join(BASE_DIR, "saved_files")

    if not os.path.exists(TEXT_FILE_DIR):
        os.makedirs(TEXT_FILE_DIR)


class TestConfig:
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))

    # Use a temporary directory for testing
    TEXT_FILE_DIR = os.path.join(BASE_DIR, "test_saved_files")

    if not os.path.exists(TEXT_FILE_DIR):
        os.makedirs(TEXT_FILE_DIR)
