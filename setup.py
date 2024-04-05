# Run/Used from command -> pip install -e . / pip install -e . --config-settings editable_mode=strict
from setuptools import setup, find_packages
# from toml import load

# #PEP 735 – Dependency Groups in pyproject.toml
# pyproject = load('pyproject.toml')

# base_dependencies = pyproject.get('dependency-groups', {}).get('base', [])
# optional_dependencies = pyproject.get('dependency-groups', {}).get('dev', [])

# setup(
#     name='editor',
#     version='0.1.0',
#     packages=find_packages("src/editor"),
#     package_dir={
#         '': 'src/editor',
#         'tests': 'src/editor/tests',
#         'components': 'src/editor/components',
#         'windows': 'src/editor/windows',
#     },
# )


# setup(
#     name='EBULA',
#     version='0.1.0',
#     packages=find_packages(
#         where='.',
#         include=['editor', 'editor.components']
#         ),
#     package_dir={
#         # '': '.',
#         # 'ebula': 'src',
#         # 'editor': 'src/editor',
#         'components': 'src/editor/components',
#         # 'windows': 'src/editor/windows',

#         # 'tests': 'src/editor/tests',
#         # 'components': 'src/editor/components',
#         # 'windows': 'src/editor/windows',
#     },
#     # install_requires=base_dependencies,
#     # extras_require={
#     #     'dev': optional_dependencies,
#     # },
# )

setup(
    # name="EBULA",
    # version="0.1",
    packages=
        # find_packages(where=".",
        #               include=["src"]) +
        # find_packages(where="src",
        #               include=["editor"]) +
        # find_packages(where='src/editor',
        #               include=["components", "windows"]),
        find_packages(where=".") +
        find_packages(where="src") +
        find_packages(where='src/editor', exclude=["tests"]),
    package_dir={
        '.': '.',       #? is needed because the src find overrides the src top level ??
        # 'src': 'src',   #? is not used ???
        # '': '.',
        # 'ebula': 'src',
        'editor': 'src/editor',
        # 'components': 'src/editor/components',
        # 'windows': 'src/editor/windows',

        # 'tests': 'src/editor/tests',
        'components': 'src/editor/components',
        'windows': 'src/editor/windows',
    },

)
