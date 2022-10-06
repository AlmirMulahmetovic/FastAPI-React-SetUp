from glob import glob

pytest_plugins = [
    fixture.replace("/", ".").replace("\\", ".").replace(".py", "")
    for fixture in glob("tests/fixtures/**/*.py", recursive=True)
    if "__" not in fixture
]
