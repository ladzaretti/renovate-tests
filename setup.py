from setuptools import find_namespace_packages, setup

install_deps = [
    "requests~=2.24",
    "semver~=2.10",
]

extras_require = {
    "dev": [
        "pytest~=5.2",
    ],
}

with open("README.md") as f:
    description = f.read()

setup(
    name="pip-setup-root-test",
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
