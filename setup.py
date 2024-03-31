import setuptools

with open("README.md", "r", encoding='utf-8') as f:
    long_description = f.read()

__version__ = "0.0.0"

REPO_NAME = "Genomics-For-Alzheimer"
AUTHOR_USER_NAME = "MartinKalema"
SRC_REPO = "alzheimer"
AUTHOR_EMAIL = "kalema.martin@students.mak.ac.ug"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="Harnessing Genome Wide Association studies to identify biomarkers linked to the early onset of Alzheimer's disease and construct predictive models for the detection of these biomarkers within gene sequences.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues"
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)