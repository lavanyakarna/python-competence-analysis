from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="python-competence-analysis",
    version="0.1.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="Open source model evaluation for Python student competence analysis",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/YOUR_USERNAME/python-competence-analysis",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Education",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Topic :: Education",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
    python_requires=">=3.8",
    install_requires=requirements,
    keywords="education, python, code-analysis, ai, competence-assessment",
    project_urls={
        "Bug Reports": "https://github.com/YOUR_USERNAME/python-competence-analysis/issues",
        "Source": "https://github.com/YOUR_USERNAME/python-competence-analysis",
        "Documentation": "https://github.com/YOUR_USERNAME/python-competence-analysis#readme",
    },
)
