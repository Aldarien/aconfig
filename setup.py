from setuptools import setup

setup(name='aconfig',
      version='1.0.0',
      description='Config Files Manager for JSON and YAML files',
      url='http://github.com/aldarien/aconfig',
      author='Aldarien',
      author_email='aldarien85@gmail.com',
      license='MIT',
      packages=['pyconfig'],
      zip_safe=False,
      install_requires=[
          "pyyaml>=3.0, <6.0"
          ])
