cmake_minimum_required(VERSION 2.8.11)
project(cmake_wrapper)

include(conanbuildinfo.cmake)
conan_basic_setup()

include("${CMAKE_CURRENT_BINARY_DIR}/conan_paths.cmake")

add_subdirectory("source_subfolder")
