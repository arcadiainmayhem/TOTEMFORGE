from adafruit_pn532.i2c import PN532_I2C
from adafruit_pn532.uart import PN532_UART


from config import DEV_MODE

if not DEV_MODE:
    import busio
    import board

    i2c = busio.I2C(board.SCL , board.SDA)
    #creating PN532 object
    pn532 = PN532_I2C(i2c , debug = False)
    #call before reading tags
    pn532.SAM_configuration()

def read_uid():

    uid_bytes = pn532.read_passive_target(timeout = 0.5)

    if uid_bytes is None:
        print("No UID Bytes")
        return None

    #hex converts raw bytes to string
    uid_hex = uid_bytes.hex()
    return uid_hex

#writes chunks so that phone can read
def write_chunks_to_pages(chunks):

    start_page = 4

    for i , chunk in enumerate(chunks):
        page_number = start_page + i
        pn532.ntag2xx_write_block(page_number,chunk)


def wait_for_removal():
    while pn532.read_passive_target(timeout=0.5) is not None:
        pass