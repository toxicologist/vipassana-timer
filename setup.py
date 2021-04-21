import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="vipassana-timer-toxicologist", # Replace with your own username
    version="0.1",
    author="toxicologist",
    author_email="toxiccologist@gmail.com",
    description="A small meditation timer for vipassana",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/toxicologist/vipassana-timer",
    project_urls={
        "Bug Tracker": "https://github.com/toxicologist/vipassana-timer/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=['vipassana_timer'],
    package_dir={"vipassana_timer": "src"},
    python_requires=">=3.6",
    install_requires=['simpleaudio'],
    package_data={'vipassana_timer': ['data/bell.wav']},
    entry_points = {'console_scripts': ['vipassana_timer = vipassana_timer:main']}
)
