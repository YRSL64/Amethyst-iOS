"""Validate the real packaged upstream app, without claiming it runs on iOS."""
import plistlib
import sys
import zipfile
from pathlib import Path


def verify(path):
    with zipfile.ZipFile(path) as archive:
        damaged = archive.testzip()
        if damaged:
            raise ValueError(f"ZIP CRC failed: {damaged}")
        root = "Payload/AngelAuraAmethyst.app/"
        info = plistlib.loads(archive.read(root + "Info.plist"))
        executable = root + info["CFBundleExecutable"]
        if archive.getinfo(executable).file_size == 0:
            raise ValueError("Empty executable")
        if archive.read(executable)[:4] not in (
            b"\xcf\xfa\xed\xfe", b"\xfe\xed\xfa\xcf", b"\xca\xfe\xba\xbe"
        ):
            raise ValueError("Executable is not Mach-O")
        required = [root + "libs/launcher.jar", root + "libs/lwjgl.jar"]
        for version in (8, 17, 21, 25):
            runtime = root + f"java_runtimes/java-{version}-openjdk/"
            required += [runtime + "release", runtime + "lib/server/libjvm.dylib"]
        for name in required:
            if archive.getinfo(name).file_size == 0:
                raise ValueError(f"Empty required payload: {name}")
        print(f"Verified archive: {path.name}; bundle={info['CFBundleIdentifier']}")
        print("This is an ad-hoc sideload package, not an Apple-signed install or device test.")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit("Usage: verify_ipa.py path/to/app.ipa")
    try:
        for argument in sys.argv[1:]:
            verify(Path(argument))
    except (OSError, ValueError, KeyError, zipfile.BadZipFile) as error:
        sys.exit(f"IPA verification failed: {error}")
