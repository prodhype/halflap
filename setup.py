from distutils.core import setup

setup(
    name="halflap",
    packages=["halflap"],
    version="0.1",
    license="MIT",
    description="Halflap is a simple, easy-to-use, easy-to-enhance RPC library that uses RabbitMQ and JSON-serializable payloads.",
    author="John Perkins",
    author_email="johndperkins+halflap@gmail.com",
    url="https://github.com/prodhype/halflap",
    download_url="https://github.com/prodhype/halflap/archive/refs/tags/v_01.tar.gz",
    keywords=[
        "halflap",
        "rpc",
        "rabbitmq",
        "distributed",
    ],
    install_requires=[
        "pika",
    ],
    classifiers=[
        "Development Status :: 3 - Alpha",  # "3 - Alpha", "4 - Beta" or "5 - Production/Stable"
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: System :: Distributed Computing",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
)
