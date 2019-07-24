from distutils.core import setup


"""Run setup.py file:
pip install -e ."""


desc = """
Flask project outline:
- Create a REST API for website
- Create a light weight website fits to the API
- Add web content
- Convert to web application
"""

setup(name='Flask_project',
      author='Max K., Chris V.',
      author_email='max.koutouzov@outlook.com',
      version='0.1',
      long_description=desc,
      url=['https://github.com/TestPern1',
           'https://github.com/elmaxk'],
      packages=['flask',
                'requests'])
