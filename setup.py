from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="image_processing_package",
    version="0.0.1",
    author="Gutembergue",
    author_email="gutemberguemartins@gmail.com",
    description="Este programa tem como propósito renderizar uma imagem com base no histograma de uma imagem referência.",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/gutembergue-martins/image-processing-package.git"
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.8',
)
