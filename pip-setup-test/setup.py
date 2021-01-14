from setuptools import find_namespace_packages, setup

install_deps = [
    "bugsnag~=3.0",
]

extras_require = {
    "dev": [
        "behave~=1.2",
        "cookiecutter~=1.7"
    ],
}

with open("README.md") as f:
    description = f.read()

setup(
    name="pip-setup-test",
    version="0.0.1",
    description="pip setup.py test",
    long_description=description,
    long_description_content_type="text/markdown",
    package_dir={"": "src"},
    packages=find_namespace_packages(where="src"),
    install_requires=install_deps,
    extras_require=extras_require,
    namespace_packages=["package"],
)