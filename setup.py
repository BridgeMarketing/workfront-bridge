from setuptools import setup, find_packages

setup(name='workfront-bridge',
      version='1.0.2',
      description='Workfront Bridge Project Library for Python',
      url='https://github.com/BridgeMarketing/workfront-bridge',
      author='Bridge',
      author_email='info@bridgecorp.com',
      license='bridgecorp',
      # packages=['workfront', 'workfront.wf', 'workfront.wf.objects'],
      long_description=open('README.md').read(),
      packages=find_packages(exclude=('tests')),
      install_requires=['requests==2.20.0'],
      tests_require=['mock', 'nose', 'requests-mock'],
      zip_safe=False)
