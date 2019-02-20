import os

from conans import ConanFile, CMake, tools


class JmespathCppConan(ConanFile):
    name = "jmespath.cpp"
    version = "0.2.0"
    license = "MIT"
    author = "Robert Marki <gsmiko@gmail.com>"
    url = "https://github.com/robertmrk/conan-jmespath.cpp"
    repo_url = "https://github.com/robertmrk/jmespath.cpp"
    description = "C++ implementation of JMESPath, a query language for JSON"
    topics = ("<Put some tag here>", "<here>", "<and here>")
    settings = "os", "compiler", "build_type", "arch"
    generators = "cmake"

    exports_sources = ["CMakeLists.txt"]

    _source_subfolder = "source_subfolder"
    _build_subfolder = "build_subfolder"

    def requirements(self):
        self.requires("boost/1.65.1@conan/stable")
        self.requires("jsonformoderncpp/3.5.0@vthiery/stable")

    def source(self):
        self.run("git clone https://github.com/robertmrk/jmespath.cpp.git")
        self.run("cd jmespath.cpp && git checkout develop && cd ..")
        os.rename("jmespath.cpp", self._source_subfolder)

    def configure_cmake(self):
        cmake = CMake(self)
        cmake.definitions["JMESPATH_BUILD_TESTS"] = False
        cmake.configure(source_folder=self._source_subfolder,
                        build_folder=self._build_subfolder)
        return cmake

    def build(self):
        cmake = self.configure_cmake()
        cmake.build()

    def package(self):
        cmake = self.configure_cmake()
        cmake.install()

    def package_info(self):
        self.cpp_info.libdirs = ["lib", "lib/jmespath"]
        self.cpp_info.libs = tools.collect_libs(self)
