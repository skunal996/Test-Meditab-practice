import pytest

from selenium import webdriver


@pytest.fixture()
def open_browser():
    driver = webdriver.Edge()
    driver.maximize_window()
    return driver


def pytest_metadata(metadata):
    # To Add
    metadata["Class"] = "Credence"
    metadata["Batch"] = "CT#14"
    metadata["Site"] = "Meditab Demo Site"
    metadata["URL"] = "https://iemodemoindia.meditab.com/#/login"
    # To Remove
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Packages", None)
    metadata.pop("Platform", None)
