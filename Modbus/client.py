from pymodbus.client import ModbusTcpClient

client = ModbusTcpClient('172.30.248.239')
# client.write_coil(1, True)
result = client.read_holding_registers(0,10,1)
print(result.registers)
print(result.getRegister(2))
client.close()