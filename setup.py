import setuptools

setuptools.setup(
    name="mro_filter_wheel",
    version="1.0.0",
    license="BSD3",
    install_requires=["Phidget22", "twisted"],
    packages=setuptools.find_packages(where="src"),
    package_dir={"": "src"},
    include_package_data=True,
    entry_points={
        "console_scripts": [
            "filter_wheel = filter_wheel.server:main",
        ]
    },
)
