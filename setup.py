from setuptools import find_packages, setup

setup(
    name="workfront-bridge",
    version="1.0.3",
    description="Workfront Bridge Project Library for Python",
    url="https://github.com/BridgeMarketing/workfront-bridge",
    author="Bridge",
    author_email="info@bridgecorp.com",
    license="bridgecorp",
    # packages=['workfront', 'workfront.wf', 'workfront.wf.objects'],
    long_description=open("README.md").read(),
    packages=find_packages(exclude=("tests")),
    install_requires=["requests==2.25.1"],
    tests_require=["mock", "nose", "requests-mock"],
    zip_safe=False,
)
