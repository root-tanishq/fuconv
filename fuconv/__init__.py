# Conversion function
# All the inputs in the functions are into hex as well as output
# only bytes32 conversions
import decimal

def hextou160(htou160):
    return htou160[-40:]

def hextou128(htou128):
    return htou128[-32:]

def hextou64(htou64):
    return htou64[-16:]

def hextou32(htou32):
    return htou32[-8:]

def hextou16(htou16):
    return htou16[-4:]

def hextou8(htou8):
    return htou8[-2:]

def Bytes32to16(b32to16):
    return b32to16[:32]

def Bytes32to8(b32to8):
    return b32to8[:16]

def Bytes32to4(b32to4):
    return b32to4[:8]

def BytesAnyto32(bAnyto32):
    return bAnyto32.ljust(64, '0')

# Takes int input
def ethertoWei(ether):
    return decimal.Decimal(float(ether) * 10**18)

def weitoEther(wei):
    return float(decimal.Decimal(wei) / 10**18)

# Input Output Functions
# Input Function
def xHexRemove(hexString):
    if (hexString.startswith("0x")):
        hexString_1 = hexString[2:]
    else:
        hexString_1 = hexString
    return hexString_1

def IntToHex(intdata):
    return hex(int(intdata))[2:].zfill(64)

# Output function
def HextoInt(hexdata):
    return int(hexdata, 16)
