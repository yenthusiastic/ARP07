import smbus
DEVICE_BUS = 1
DEVICE_ADDR = 0x48
bus = smbus.SMBus(DEVICE_BUS)

bus.write_i2c_block_data(DEVICE_ADDR, 0b00000001, [0b10000100, 0b10000011])
for i in range(10):
    print(i, bus.read_byte_data(DEVICE_ADDR, i))