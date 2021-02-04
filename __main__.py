import argparse
import multiprocessing as mp
from multiprocessing import Manager, Pool

from zilliqavanity.zilliqavanity import (
    _BECH32_CHARSET,
    contains,
    digits,
    ends_with,
    find_vanity_addr,
    letters,
    starts_with,
)


def main():
    parser = argparse.ArgumentParser(
        description="ZilliqaVanity - Create custom Zilliqa addresses."
    )
    parser.add_argument(
        "--startswith",
        type=str,
        help="Find an address ending with the provided argument.",
    )
    parser.add_argument(
        "--endswith",
        type=str,
        help="Find an address starting with the provided argument.",
    )
    parser.add_argument(
        "--contains", type=str, help="Find an address containing the provided argument."
    )
    parser.add_argument(
        "--letters",
        type=int,
        help="Find an address containing the provided number of letters.",
    )
    parser.add_argument(
        "--digits",
        type=int,
        help="Find an address containing the provided number of digits.",
    )
    parser.add_argument(
        "-n", type=int, help="Number of addresses to search for.", default=1
    )
    args = parser.parse_args()

    vanity_args = {}
    if args.startswith and _is_valid_bech32(args.startswith):
        vanity_args[starts_with] = str(args.startswith)
    if args.endswith and _is_valid_bech32(args.endswith):
        vanity_args[ends_with] = str(args.endswith)
    if args.contains and _is_valid_bech32(args.contains):
        vanity_args[contains] = args.contains
    if args.letters and args.letters:
        vanity_args[letters] = args.letters
    if args.digits and args.digits:
        vanity_args[digits] = args.digits

    with Pool(processes=mp.cpu_count()) as pool:
        manager = Manager()
        event = manager.Event()
        queue = manager.Queue()
        for i in range(args.n):
            for _ in range(mp.cpu_count()):
                pool.apply_async(find_vanity_addr, args=(vanity_args, event, queue))

        vanity_addresses = []
        address = None
        while not address:
            address = queue.get()
            vanity_addresses.append(address)
            address = None
            if len(vanity_addresses) >= args.n:
                event.set()
                break
        for address in vanity_addresses:
            print(address)


def _is_valid_bech32(vanity: str):
    if not all(c in _BECH32_CHARSET for c in vanity):
        print(f"Not valid bech32 vanity input for {vanity}")
        exit(1)
    return True


if __name__ == "__main__":
    main()
