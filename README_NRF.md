Nordic has a portfolio of [RF enabled microcontrollers](https://www.nordicsemi.com/Products). They feature 2.4 GHz Technologies like Bluetooth, ZigBee and ANT as well as a proprietary protocol called Enhanced Shock Burst or Gazell which is used by many Logitech and Microsoft Mice and Keyboards. Though the chips are rated for a supply voltage of 3.3 V some of the newer ones accept 1.7-5.5 V and can be directly powered by a Li-Ion cell.

Nordic offers a [microcontroller development kit](https://www.nordicsemi.com/Software-and-Tools/Development-Tools/nRF-MDK) which consists of CMSIS svd files for hardware and register description, linkerfiles, startup code and C headers. This MDK is sufficient to generate the a modm device tree.

The linkerfiles are used to extract the available memory sections and their sizes. The GPIOs, peripherals and provided signals are gathered from the CMSIS svd files. The nrf microcontrollers have a crossbar switch and allow to connect the signals of a peripheral to an arbitrary GPIO.

# Extractor

The extractor script `extract-nrf.py` downloads the zip file containing the MDK. Then it extracts each svd file and the linker scripts. It also performs some renaming since the svd file names are not consistent. For example the file containing the description for the nrf52832 is called nrf52.svd

# Device tree generator
