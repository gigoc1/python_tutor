from pymodbus.client import ModbusSerialClient
client = ModbusSerialClient(method='rtu', port='COM6')
client.connect()

res = client.read_holding_registers(address=0, count=2, unit=1)
print(res.registers) # shows the result, type: list

<<<<<<< Updated upstream
=======
client = ModbusTcpClient('172.16.11.222',502)
# client.write_register(0x10,00,1)
result = client.read_holding_registers(0x10,1,1)
print(result.registers)
print(result.getRegister(0))
>>>>>>> Stashed changes
client.close()