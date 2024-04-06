# Run/Used from command -> pip install -e . / pip install -e . --config-settings editable_mode=strict
from setuptools import setup, find_packages

setup(
    # name="EBULA",     #* -> from toml file automatically
    # version="0.1",    #* -> from toml file automatically
    packages=
        #* Include all that is specified
        find_packages(where=".",
                      include=["src","src.*"]) +
        find_packages(where="src",
                      include=["editor", "editor.*"]) +
        find_packages(where='src/editor',
                      include=["components", "components.*", "windows", "windows.*"]),
        #* Include all that is found
        # find_packages(where=".") +
        # find_packages(where="src") +
        # find_packages(where='src/editor', exclude=["tests"]),
    package_dir={
        #* Declarations for top levels and their paths
        '.': '.',       #? is needed because the src find overrides the src top level ??
        # 'src': 'src',   #? is not used ???
        'editor': 'src/editor',
        'components': 'src/editor/components',
        'windows': 'src/editor/windows',
    },
)