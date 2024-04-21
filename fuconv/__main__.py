#!/usr/bin/env python3
import fuconv
import argparse

# Banner
print('😴 Fuccccccc²⁵⁶conv↴\t\t@github.com/root-tanishq\n')

parser = argparse.ArgumentParser(description="conversion script for solidity ctfs")
subparsers = parser.add_subparsers(title="Subcommands", dest="subcommand", required=True)

parser_1 = subparsers.add_parser("u160", help="convert a value to uint160")
parser_1.add_argument('input', help="input value for the conversion")
parser_1.add_argument('-ui','--uinput', help="provided value is uint",action='store_true',default=False)
parser_1.add_argument('-uo','--uoutput', help="print uint value as output",action='store_true',default=False)

parser_2 = subparsers.add_parser("u128", help="convert a value to uint128")
parser_2.add_argument('input', help="input value for the conversion")
parser_2.add_argument('-ui','--uinput', help="provided value is uint",action='store_true',default=False)
parser_2.add_argument('-uo','--uoutput', help="print uint value as output",action='store_true',default=False)

parser_3 = subparsers.add_parser("u64", help="convert a value to uint64")
parser_3.add_argument('input', help="input value for the conversion")
parser_3.add_argument('-ui','--uinput', help="provided value is uint",action='store_true',default=False)
parser_3.add_argument('-uo','--uoutput', help="print uint value as output",action='store_true',default=False)

parser_4 = subparsers.add_parser("u32", help="convert a value to uint32")
parser_4.add_argument('input', help="input value for the conversion")
parser_4.add_argument('-ui','--uinput', help="provided value is uint",action='store_true',default=False)
parser_4.add_argument('-uo','--uoutput', help="print uint value as output",action='store_true',default=False)

parser_5 = subparsers.add_parser("u16", help="convert a value to uint16")
parser_5.add_argument('input', help="input value for the conversion")
parser_5.add_argument('-ui','--uinput', help="provided value is uint",action='store_true',default=False)
parser_5.add_argument('-uo','--uoutput', help="print uint value as output",action='store_true',default=False)

parser_6 = subparsers.add_parser("u8", help="convert a value to uint8")
parser_6.add_argument('input', help="input value for the conversion")
parser_6.add_argument('-ui','--uinput', help="provided value is uint",action='store_true',default=False)
parser_6.add_argument('-uo','--uoutput', help="print uint value as output",action='store_true',default=False)

parser_7 = subparsers.add_parser("b16", help="convert a value to bytes16")
parser_7.add_argument('input', help="input value for the conversion")
parser_7.add_argument('-ui','--uinput', help="provided value is uint",action='store_true',default=False)
parser_7.add_argument('-uo','--uoutput', help="print uint value as output",action='store_true',default=False)

parser_8 = subparsers.add_parser("b8", help="convert a value to bytes8")
parser_8.add_argument('input', help="input value for the conversion")
parser_8.add_argument('-ui','--uinput', help="provided value is uint",action='store_true',default=False)
parser_8.add_argument('-uo','--uoutput', help="print uint value as output",action='store_true',default=False)

parser_9 = subparsers.add_parser("b4", help="convert a value to bytes4")
parser_9.add_argument('input', help="input value for the conversion")
parser_9.add_argument('-ui','--uinput', help="provided value is uint",action='store_true',default=False)
parser_9.add_argument('-uo','--uoutput', help="print uint value as output",action='store_true',default=False)

parser_10 = subparsers.add_parser("wei", help="convert ethers to wei")
parser_10.add_argument('input', help="input value for the conversion")

parser_11 = subparsers.add_parser("eth", help="convert wei to ethers")
parser_11.add_argument('input', help="input value for the conversion")

parser_12 = subparsers.add_parser("hex", help="convert a uint to bytes32 hex")
parser_12.add_argument('input', help="input value for the conversion")

parser_13 = subparsers.add_parser("uint", help="convert a bytes hex value to uint")
parser_13.add_argument('input', help="input value for the conversion")

args = parser.parse_args()

def main():
    if args.subcommand == "u160":
        inputVal = args.input
        if args.uinput:
            inputVal = fuconv.IntToHex(args.input)
        resultVal = fuconv.hextou160(inputVal)
        if args.uoutput:
            print(fuconv.HextoInt(resultVal))
        else:
            print('0x'+resultVal)

    elif args.subcommand == "u128":
        inputVal = args.input
        if args.uinput:
            inputVal = fuconv.IntToHex(args.input)
        resultVal = fuconv.hextou128(inputVal)
        if args.uoutput:
            print(fuconv.HextoInt(resultVal))
        else:
            print('0x'+resultVal)

    elif args.subcommand == "u64":
        inputVal = args.input
        if args.uinput:
            inputVal = fuconv.IntToHex(args.input)
        resultVal = fuconv.hextou64(inputVal)
        if args.uoutput:
            print(fuconv.HextoInt(resultVal))
        else:
            print('0x'+resultVal)

    elif args.subcommand == "u32":
        inputVal = args.input
        if args.uinput:
            inputVal = fuconv.IntToHex(args.input)
        resultVal = fuconv.hextou32(inputVal)
        if args.uoutput:
            print(fuconv.HextoInt(resultVal))
        else:
            print('0x'+resultVal)

    elif args.subcommand == "u16":
        inputVal = args.input
        if args.uinput:
            inputVal = fuconv.IntToHex(args.input)
        resultVal = fuconv.hextou16(inputVal)
        if args.uoutput:
            print(fuconv.HextoInt(resultVal))
        else:
            print('0x'+resultVal)

    elif args.subcommand == "u8":
        inputVal = args.input
        if args.uinput:
            inputVal = fuconv.IntToHex(args.input)
        resultVal = fuconv.hextou8(inputVal)
        if args.uoutput:
            print(fuconv.HextoInt(resultVal))
        else:
            print('0x'+resultVal)

    elif args.subcommand == "b16":
        inputVal = args.input
        if args.uinput:
            inputVal = fuconv.IntToHex(args.input)
        resultVal = fuconv.Bytes32to16(inputVal)
        if args.uoutput:
            print(fuconv.HextoInt(resultVal))
        else:
            print('0x'+resultVal)

    elif args.subcommand == "b8":
        inputVal = args.input
        if args.uinput:
            inputVal = fuconv.IntToHex(args.input)
        resultVal = fuconv.Bytes32to8(inputVal)
        if args.uoutput:
            print(fuconv.HextoInt(resultVal))
        else:
            print('0x'+resultVal)

    elif args.subcommand == "b4":
        inputVal = args.input
        if args.uinput:
            inputVal = fuconv.IntToHex(args.input)
        resultVal = fuconv.Bytes32to4(inputVal)
        if args.uoutput:
            print(fuconv.HextoInt(resultVal))
        else:
            print('0x'+resultVal)

    elif args.subcommand == "wei":
        inputVal = args.input
        print(fuconv.ethertoWei(inputVal))

    elif args.subcommand == "eth":
        inputVal = args.input
        print(fuconv.weitoEther(inputVal))

    elif args.subcommand == "hex":
        inputVal = int(args.input)
        print('0x'+fuconv.IntToHex(inputVal))

    elif args.subcommand == "uint":
        inputVal = fuconv.xHexRemove(args.input)
        print(fuconv.HextoInt(inputVal))

if __name__ == '__main__':
    main()