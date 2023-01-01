tcp = 1
serial = 0
if(serial == True):
    from pymodbus.client import ModbusSerialClient
    client = ModbusSerialClient(method='rtu', port='COM6')
    client.connect()
    # client.write_register(0x10,00,1)
    # result = client.read_holding_registers(0x10,1,1)
    # print(result.registers)
    # print(result.getRegister(0))
    res = client.read_holding_registers(address=0, count=2, unit=1)
    print(res.registers) # shows the result, type: list

if(tcp ==True):
    from pymodbus.client import ModbusTcpClient as ModbusClient
    client = ModbusClient('192.168.137.63',5020)
    client.connect()

    result = client.read_holding_registers(0x00,1,0)
    print(result.registers)
    # client.write_register(0x10,00,1)
    client.close()