'''
Runs the CLI for hash-it
'''

from __future__ import absolute_import, print_function
from hashit.core.hash_data import HashData
from hashit.core.hash_it import HashIt
from hashit.core.hash_type import HashType
from hashit.service.validate_hash import ValidateHash

def extract_args(args):
    hash_type = HashType.CRC16
    if args['--hash-type']:
        hash_type = HashType[args['--hash-type'].upper()]
    return hash_type

def verify_data(args, ht):
    if args['-f']:
        validate = ValidateHash(
            result=args['--verify'],
            hash_type=ht,
            data=HashData(args['<input>'])
        )
        if not validate.is_vaild():
            return 2
    return 0

def run_hash(hash_type, args=None):
    if args['--verify']:
        return verify_data(args, hash_type)
    else:
        hash_str = ''
        if args['-f']:
            hash_str = HashIt(hash_type=hash_type,
                hash_data=HashData(args['<input>'])
            ).hash_it()
            print('file: %s hash: %s'%(args['<input>'], hash_str))

    return 0

def cli_main(args=None):
    try:
        hash_type = extract_args(args)
    except KeyError:
        print("Unknown hash type %s"%args['--hash-type'])
        return 1
    except TypeError:
        return 1

    return run_hash(hash_type, args)
