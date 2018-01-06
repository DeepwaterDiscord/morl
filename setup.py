from setuptools import setup

setup(name="morl",
      version="0.1",
      description="Multi-objective reinforcement learning optimized using filter methods.",
      url="http://github.com/DeepwaterDiscord/morl",
      author="DeepwaterDiscord",
      author_email="deepwater.discord@gmail.com",
      license="MIT",
      packages=["morl"],
      install_requires=[
          'matplotlib',
          'numpy',
          'pandas',
          'pyspark'
      ],
      dependency_links=["https://github.com/openai/gym/tarball/master"],
      zip_safe=False)
