from setuptools import setup, find_packages

setup(
      name='emojivote',
      packages=find_packages(include=['emojivote']),
      version='0.0.1',
      author='Andreas Grivas',
      author_email='andreasgrv@gmail.com',
      description='Propose papers for reading group using emoji voting',
      license='BSD',
      keywords=['papers', 'arxiv', 'emoji'],
      scripts=['bin/emojivote-slack'],
      classifiers=[],
      python_requires='>=3.5',
      tests_require=['pytest']
)
