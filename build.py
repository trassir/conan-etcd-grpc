from os import environ
from cpt.packager import ConanMultiPackager


if __name__ == "__main__":
    builder = ConanMultiPackager(
	remotes="https://api.bintray.com/conan/inexorgame/inexor-conan",
	build_policy="missing")
    builder.add_common_builds(pure_c=False)
    builder.run()
