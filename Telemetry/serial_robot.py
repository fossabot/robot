import serial, sys, os, struct, time
import serial.tools.list_ports as list_ports

COMMANDS = {
    'CHANGEMODE'  : b'\x00',
    'MOVE'        : b'\x01',
    'STOP_TIMER'  : b'\x02',
    'SET_P'       : b'\x03',
    'SET_D'       : b'\x04',
    'SENSOR_DATA' : b'\x05',
    'SET_HEIGHT'  : b'\x06',
    'ROTATION'    : b'\x07',
    'PD_DATA'     : b'\x08',
    'SET_SPEED'   : b'\x09',
}

def find_com_port():
    DEVICE_HEX = 'D47F'
    comport = None

    print "Searching for device {}".format(DEVICE_HEX)
    for port in list_ports.comports():
        # Knasig lista
        search = port[2].split('\\')[2]
        if DEVICE_HEX + '_' in search:
            print "Using " + port[0]
            comport = port[0]
    if not comport:
        print "Device not found in com ports"
        return None
    else:
        return comport

def create_changemode_command(mode):
    ret = COMMANDS['CHANGEMODE']
    ret += struct.pack('B', mode)
    return ret

def create_move_command(forward, side, rotation):
    ret = COMMANDS['MOVE']
    for x in [forward, side, rotation]:
        ret += struct.pack('f', x)
    return ret

def create_p_command(p):
    ret = COMMANDS['SET_P']
    ret += struct.pack('f', p)
    return ret

def create_d_command(p):
    ret = COMMANDS['SET_D']
    ret += struct.pack('f', p)
    return ret

def create_height_command(height):
    ret = COMMANDS['SET_HEIGHT']
    ret += struct.pack('f', height)
    return ret

def create_rotation_command(xrot, yrot):
    ret = COMMANDS['ROTATION']
    for x in [xrot, yrot]:
        ret += struct.pack('f', x)
    return ret

def create_speed_command(p):
    ret = COMMANDS['SET_SPEED']
    ret += struct.pack('f', p)
    return ret

def print_raw(raw):
    print "".join(["{:02x}".format(ord(c)) for c in raw])

def printer(txt):
    print txt

def connect_to_robot(_printer=printer):
    con = None

    if os.name == 'nt':
        comport = find_com_port()
    elif len(sys.argv) < 2:
        comport = '/dev/rfcomm0'
    else:
        comport = sys.argv[1]

    _printer(str(comport))

    while not con:
        try:
            con = serial.Serial(
                comport,
                baudrate=115200,
                parity=serial.PARITY_NONE,
                bytesize=serial.EIGHTBITS,
                stopbits=serial.STOPBITS_ONE)
        except Exception as e:
            _printer(str(e))
            _printer("Trying to connect...")
            time.sleep(5)
        
    _printer("Connected to {}".format(con.name))
    return con
