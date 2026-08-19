from pathlib import Path

from setuptools import find_packages, setup


ROOT = Path(__file__).resolve().parent


def read_readme() -> str:
    readme = ROOT / "sparkplug_b" / "readme.md"
    return readme.read_text(encoding="utf-8")


setup(
    name="sparkplug-b",
    version="1.0.0",
    description="Sparkplug B Python helpers and protobuf bindings",
    long_description=read_readme(),
    long_description_content_type="text/markdown",
    package_dir={"": "."},
    packages=find_packages(include=["sparkplug_b", "sparkplug_b.*"]),
    include_package_data=True,
    zip_safe=False,
)

