## Conan package recipe for [*jmespath.cpp*](https://github.com/robertmrk/jmespath.cpp)
[![Download](https://api.bintray.com/packages/robertmrk/conan/jmespath.cpp%3Arobertmrk/images/download.svg) ](https://bintray.com/robertmrk/conan/jmespath.cpp%3Arobertmrk/_latestVersion)
[![Build Status Travis](https://travis-ci.org/robertmrk/conan-jmespath.cpp.svg?branch=master)](https://travis-ci.org/robertmrk/conan-jmespath.cpp)
[![Build Status AppVeyor](https://ci.appveyor.com/api/projects/status/wtchojaiohn3f6nt?svg=true)](https://ci.appveyor.com/project/robertmrk/conan-jmespath-cpp)

jmespath.cpp is a C++ implementation of [JMESPath](http://jmespath.org/), a query language for JSON. It can be used to extract and transform elements of a JSON document.

The packages generated with this **conanfile** can be found on [Bintray](https://bintray.com/robertmrk/conan/jmespath.cpp%3Arobertmrk).

## Issues
If you wish to report an issue or make a request for a package, please do so here:
[Issues Tracker](https://github.com/robertmrk/conan-jmespath.cpp/issues)

## For Users

### Basic setup
    $ conan install jmespath.cpp/0.2.0@robertmrk/testing

### Project setup
If you handle multiple dependencies in your project is better to add a *conanfile.txt*

    [requires]
    jmespath.cpp/0.2.0@robertmrk/testing

    [generators]
    cmake

Complete the installation of requirements for your project running:

    $ mkdir build && cd build && conan install ..

Note: It is recommended that you run conan install from a build directory and not the root of the project directory.  This is because conan generates *conanbuildinfo* files specific to a single build configuration which by default comes from an autodetected default profile located in ~/.conan/profiles/default.  If you pass different build configuration options to conan install, it will generate different *conanbuildinfo* files.  Thus, they should not be added to the root of the project, nor committed to git.

### Add Remote
    $ conan remote add robertmrk https://api.bintray.com/conan/robertmrk/conan
