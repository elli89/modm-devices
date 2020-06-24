from pathlib import Path
import urllib.request
import zipfile
import shutil
import io
import glob
import os



# nordic offers svd and linker files in their microcontroller developnemt kit (MDK)
packurl = "https://www.nordicsemi.com/-/media/Software-and-other-downloads/Desktop-software/nRF-MDK/sw/8-33-0/nRF_MDK_8_33_0_GCC_BSDLicense.zip"

# remove existing files and make sure the target directory exists
shutil.rmtree("../raw-device-data/nrf-devices", ignore_errors=True)
Path("../raw-device-data/nrf-devices/nrf").mkdir(exist_ok=True, parents=True)

if __name__ == "__main__":

    dest = "../raw-device-data/nrf-devices/nrf"

    print("Downloading...")
    with urllib.request.urlopen(packurl) as content:
        z = zipfile.ZipFile(io.BytesIO(content.read()))

        print("Extracting...")
        for zi in z.infolist():
            # only extract svd files and linker scripts. The CMSIS C headers are not needed
            if zi.filename.endswith(".svd") or zi.filename.endswith(".ld"):
                zi.filename = os.path.basename(zi.filename)
                print(zi.filename)
                z.extract(zi, dest)

    # dirty hack because af inconsistent part names in .svd files
    os.rename(dest + '/nrf51.svd', dest + '/nrf51822.svd')
    os.rename(dest + '/nrf52.svd', dest + '/nrf52832.svd')

    # we only need the linker files which contain the available
    # memory regions and their sizes
    for f in glob.glob(dest + '/nrf51_*.ld'):
        os.remove(f)
    for f in glob.glob(dest + '/nrf52_*.ld'):
        os.remove(f)
    for f in glob.glob(dest + '/nrf_common.ld'):
        os.remove(f)
