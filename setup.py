from pathlib import Path
from typing import Any, cast

from setuptools import setup  # pyright: ignore[reportUnknownVariableType]

version: dict[str, Any] = {}
with open("genanki/version.py") as fp:
  exec(fp.read(), version)

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
  name="genanki",
  version=cast(str, version["__version__"]),
  description="Generate type-safe Anki decks programmatically",
  long_description=long_description,
  long_description_content_type="text/markdown",
  url="http://github.com/kerrickstaley/genanki",
  author="Kerrick Staley",
  author_email="k@kerrickstaley.com",
  license="MIT",
  packages=["genanki"],
  zip_safe=False,
  include_package_data=True,
  python_requires=">=3.10",
  install_requires=[
    "cached-property>=1.5.2",
    "frozendict>=2.4.4",
    "chevron>=0.14.0",
    "pydantic>=2.9.2",
    "pyyaml>=6.0.2",
    "typing_extensions>=4.12.2",
  ],
  setup_requires=["pytest-runner"],
  tests_require=["pytest>=6.0.2"],
  keywords=["anki", "flashcards", "memorization"],
)
