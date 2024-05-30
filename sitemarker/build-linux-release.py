#!/usr/bin/python3

def get_flutter():
    # TODO: Download flutter if NOT in $PATH
    pass

def create_build_option(args: List<str>):
    # TODO: Create flutter build options from commandline args
    pass

def create_archive(path: str):
    # TODO: Create .tar.xz archive on Linux and .zip on Windows
    pass

def run_command(command: List<str>):
    # TODO: Run a command on shell
    pass

def get_target_platform():
    # TODO: Get option for building the commandline for `flutter build`. Return a list of values
    # Possible combos:
    # Android:                  ["apk", "appbundle"]
    # Linux:                    ["linux"]
    # Windows:                  ["windows"]
    # Web (UNSUPPORTED):        ["web"]
    pass

def get_target_arch():
    # TODO: Get target platform architecture
    # Possible values:
    # 64-bit:           "x86_64"
    # Arm64:            "arm64"
    pass

def run_patchelf():
    # Returns the pathchelf command on Linux.
    if os.name.lower() == 'linux':
        return [
            {
                "cd": ["cd", "build/linux/x64/release/bundle/lib"],
                "patchelf_url_launcher": ["patchelf", "--set-rpath", "'$ORIGIN'", "liburl_launcher_linux_plugin.so"],
                "patchelf_sqlite3": ["patchelf", "--set-rpath", "'$ORIGIN'", "libsqlite3_flutter_libs_plugin.so"]
            }
        ]
    else:
        return [{}]

