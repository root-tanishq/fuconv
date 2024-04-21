# Fuconv
- uint and hex values converter for solidity CTFs
- and yes this tool is name after that word only because of my frustration of creating a `sol` file for basic conversion during CTF
---
# Installation
- pip
```
pip3 install fuconv
```
- setup tools
```
git clone https://github.com/root-tanishq/fuconv
cd fuconv
python3 setup.py install
```
---
# Usage
```
$ fuconv <CONVERSION TYPE> <INPUT> [-ui] [-uo] # ui / uo are optional params for some conversion's
```
- for conversion type use `--help`
```
❯ fuconv --help
😴 Fuccccccc²⁵⁶conv↴		@github.com/root-tanishq

usage: fuconv [-h] {u160,u128,u64,u32,u16,u8,b16,b8,b4,wei,eth,hex,uint} ...

conversion script for solidity ctfs

options:
  -h, --help            show this help message and exit

Subcommands:
  {u160,u128,u64,u32,u16,u8,b16,b8,b4,wei,eth,hex,uint}
    u160                convert a value to uint160
    u128                convert a value to uint128
    u64                 convert a value to uint64
    u32                 convert a value to uint32
    u16                 convert a value to uint16
    u8                  convert a value to uint8
    b16                 convert a value to bytes16
    b8                  convert a value to bytes8
    b4                  convert a value to bytes4
    wei                 convert ethers to wei
    eth                 convert wei to ethers
    hex                 convert a uint to bytes32 hex
    uint                convert a bytes hex value to uint
```