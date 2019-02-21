import os
import os.path

from conans import ConanFile, CMake, tools
from conans.model.version import Version
from conans.errors import ConanInvalidConfiguration


class JmespathCppConan(ConanFile):
    name = "jmespath.cpp"
    version = "0.2.0"
    description = "C++ implementation of JMESPath, a query language for JSON"
    homepage = "https://github.com/robertmrk/jmespath.cpp"
    url = "https://github.com/robertmrk/conan-jmespath.cpp"
    license = "MIT"
    author = "Robert Marki (gsmiko@gmail.com)"
    topics = ("jmespath", "json")
    settings = "os", "compiler", "build_type", "arch"    
    generators = ("cmake", "cmake_paths")
    default_options = "boost:header_only=True"
    exports_sources = ["CMakeLists.txt"]

    _source_subfolder = "source_subfolder"
    _build_subfolder = "build_subfolder"

    def requirements(self):
        self.requires("boost/1.65.1@conan/stable")
        self.requires("jsonformoderncpp/3.5.0@vthiery/stable")

    def source(self):
        self.run("git clone https://github.com/robertmrk/jmespath.cpp.git")
        self.run("cd jmespath.cpp && git checkout 0.2.0 && cd ..")
        os.rename("jmespath.cpp", self._source_subfolder)

    def configure_cmake(self):
        compiler_version = Version(self.settings.compiler.version.value)
        if self.settings.compiler == "Visual Studio" and compiler_version < "15":
            raise ConanInvalidConfiguration("jmespath.cpp requires Visual Studio 2017 or higher")
        if self.settings.compiler == "gcc" and compiler_version < "6.0":
            raise ConanInvalidConfiguration("jmespath.cpp requires gcc 6.0 or higher")
        if self.settings.compiler == "clang" and compiler_version < "4.0":
            raise ConanInvalidConfiguration("jmespath.cpp requires clang 4.0 or higher")
        if self.settings.compiler == "apple-clang" and compiler_version < "9.0":
            raise ConanInvalidConfiguration("jmespath.cpp requires apple-clang 9.0 or higher")

        cmake = CMake(self)
        cmake.definitions["JMESPATH_BUILD_TESTS"] = False
        cmake.configure(build_folder=self._build_subfolder)
        return cmake

    def build(self):
        cmake = self.configure_cmake()
        cmake.build()

    def package(self):
        self.copy("LICENSE", src=self._source_subfolder, dst="licenses")
        cmake = self.configure_cmake()
        cmake.install()

    def package_info(self):
        self.cpp_info.libdirs = ["lib", "lib/jmespath"]
        self.cpp_info.libs = tools.collect_libs(self)
