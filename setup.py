from setuptools import setup
with open("README.md", "r", encoding='utf-16') as fh:
    long_description = fh.read()

author = 'Shanmukh Mundra'
src_repo = 'src'
requirements = ['streamlit']

setup(
    name = src_repo,
    version = '0.1',
    author = author,
    email = 'shanmukhamundra@yahoo.com',
    description = 'Movie Recommender system with Streamlit web interface',
    long_description = long_description,
    long_description_content_type = 'text/markdown',
    url = 'https://github.com/shanmukha/Recommender_System',
    packages = ['src'],
    python_requires = '>=3.9',
    install_requires = requirements,
)