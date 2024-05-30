from setuptools import setup

setup(
    name="checkbox",
    version="0.1",
    description="Neovim plugin to add checkboxes to markdown documents",
    author="4thel00z",
    author_email="4thel00z@gmail.com",
    url="https://github.com/4thel00z/checkbox.vim",
    packages=["checkbox"],
    install_requires=["pynvim"],
)
