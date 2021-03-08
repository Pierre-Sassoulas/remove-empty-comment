from setuptools import setup

with open("README.md", "r", encoding="utf-8") as r:
    README = r.read()

setup(
    author="Pierre Sassoulas",
    author_email="pierre.sassoulas@gmail.com",
    long_description=README,
    long_description_content_type="text/markdown",
    name="remove-empty-comment",
    version="1.0.2",
    packages=["remove_empty_comment"],
    entry_points={"console_scripts": ["remove-empty-comment=remove_empty_comment.__main__:main"]},
    install_requires=[],
    url="https://github.com/Pierre-Sassoulas/remove-empty-comment/",
    zip_safe=True,
)
