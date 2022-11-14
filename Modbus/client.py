from pymodbus.client import ModbusSerialClient
client = ModbusSerialClient(method='rtu', port='COM6')
client.connect()

res = client.read_holding_registers(address=0, count=2, unit=1)
print(res.registers) # shows the result, type: list

client.close()