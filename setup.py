from setuptools import setup, find_packages

VERSION = "1.0.5"
LONG_DESC = open("README.md", encoding="utf-8").read()
DOWNLOAD = f"https://github.com/lulivi/dgp-lib/releases/tag/v{VERSION}"

setup(
    name="DeepGProp",
    version=VERSION,
    author="Luis Liñán",
    author_email="luislivilla@gmail.com",
    description="Train Multilayer Perceptrons with Genetic Algorithms.",
    long_description_content_type="text/markdown",
    long_description=LONG_DESC,
    license="GPLv3",
    url="https://github.com/lulivi/dgp-lib",
    download_url=DOWNLOAD,
    classifiers=[
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: POSIX :: Linux",
        "Development Status :: 4 - Beta",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Intended Audience :: Education",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: Artificial Intelligence"
    ],
    packages=find_packages(),
    include_package_data=True,
    package_data={"datasets": ["dgp/datasets/proben1/*"]},
    entry_points={
        "console_scripts": [
            "dgp=dgp.__main__:cli",
            "d2p1=dgp.dataset_to_proben1:cli",
        ]
    },
    python_requires=">=3.6",
    install_requires=[
        "numpy==1.18.2",
        "pandas==1.0.3",
        "deap==1.3.1",
        "scikit-learn==0.22.2.post1",
        "Theano-PyMC==1.0.10",
        "Keras==2.3.1",
        "click==7.1.2",
        "tabulate==0.8.7",
    ],
    test_suite="tests",
)
