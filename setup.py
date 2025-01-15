import setuptools

#README.md yi okuyalım
with open("README.md", "r", encoding = "utf-8") as f:
    long_description = f.read()

#Versiyon numarası
__version__ = "0.0.0"

#Proje ve yazar bilgileri diyorum
REPO_NAME = "Text-Summarizer-Project"
AUTHOR_USER_NAME = "entbappy"
SRC_REPO = "textSummarizer"
AUTHOR_EMAIL = "entbappy73@gmail.com"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="Python package",
    long_description= long_description,
    long_description_content_type= "text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls = {
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues", 
    },
    package_dir={"":"src"},
    packages=setuptools.find_packages(where = "src")#src dizinindeki tüm paketleri bulur ve dahil eder.
)