import setuptools

VERSION = "v1.0.0"
LONG_DESC = open("README.md").read()
DOWNLOAD = f"https://github.com/lulivi/dgp-lib/releases/tag/{VERSION}"
REQUIREMENTS = open("requirements/prod.txt").read().splitlines()

setuptools.setup(
    name="DeepGProp",
    version=VERSION,
    author="Luis Liñán",
    author_email="luislivilla@gmail.com",
    description="Train Multilayer Perceptrons with Genetic Algorithms.",
    long_description_content_type="text/markdown",
    long_description=LONG_DESC,
    license="GPLv3",
    url="https://github.com/lulivi/deep-g-prop",
    download_url=DOWNLOAD,
    classifiers=[
        "Environment :: X11 Applications",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ],
    packages=["dgp"],
    include_package_data=True,
    package_data={"datasets": ["dgp/datasets/proben1/*"]},
    entry_points={
        "console_scripts": [
            "dgp=dgp.__main__:cli",
            "d2p1=dgp.dataset_to_proben1:cli",
        ]
    },
    python_requires=">=3.6",
    install_requires=REQUIREMENTS,
    test_suite="tests",
)
