from setuptools import setup

with open("README.md", "r") as fh:
    readme = fh.read()

setup(name='pyeon',
      version='1.0.1',
      url='https://github.com/delvidioneto/PyEon',
      license='MIT License',
      author='Delvidio Demarchi Neto',
      long_description=readme,
      long_description_content_type="text/markdown",
      author_email='delvidio.neto@dqexp.com.br',
      keywords='Pacote',
      description=u'This package was developed to simplify date manipulation.',
      packages=['pyeon'],
      install_requires=['dateutil', 'holidays', 'calendar'],)
