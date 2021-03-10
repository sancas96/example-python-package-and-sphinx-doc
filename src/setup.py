from setuptools import setup, find_packages

setup(name="opt2",
      version="0.1",
      description=u"Small package for example",
      url="",
      author="itam",
      author_email="",
      license="MIT",
      packages=find_packages(),
      install_requires = [
                          "numpy",
                          "pandas",
                          "nose"
                          ],
      )
