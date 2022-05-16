from setuptools import setup

NAME = "aspose-pdf-for-python-via-java"
VERSION = "22.5.0"
REQUIRES = ["JPype1==1.3.0"]

setup(
    name=NAME,
    version=VERSION,
    author="Aspose.PDF",
    description="",
    author_email="pdf@aspose.com",
    keywords=["aspose", "pdf", "java", "convert"],
    install_requires=REQUIRES,
    packages=['asposepdf'],
    include_package_data=True,
    long_description=open("README.md", encoding='utf-8').read(),
    long_description_content_type="text/markdown",
    classifiers=[
        'Programming Language :: Python :: 3.6',
        'License :: Other/Proprietary License'
    ],
    python_requires='>=3.6',
)