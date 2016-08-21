from coal import CoalFile
from util import git_clone, download, unzip, default_cmake_build, cp
from os import path

class SpdlogFile(CoalFile):
    url = "https://github.com/gabime/spdlog"
    exports = ["include"]
    def prepare(self):
        git_clone(self.url, 'master', 'src')
    def build(self):
        pass
    def package(self):
        cp('src/include', 'include')
    def info(self, generator):
        generator.add_include_dir('include/')
