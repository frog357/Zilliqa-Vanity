import hashlib
from multiprocessing import Event, Queue
from typing import Callable, Dict, Optional
from pprint import pprint

from pyzil.crypto import zilkey
from pyzil.zilliqa import chain
from pyzil.zilliqa.units import Zil, Qa
from pyzil.account import Account, BatchTransfer


_BECH32_CHARSET = "023456789acdefghjklmnpqrstuvwxyzACDEFGHJKLMNPQRSTUVWXYZ"


def generate_wallet():
    account = Account.generate()
    #print(account.bech32_address)
    return account.bech32_address, account.public_key, account.private_key


def ends_with(suffix, bech_addr: str) -> bool:
    return bech_addr.endswith(suffix)


def starts_with(prefix, bech_addr: str) -> bool:
    return bech_addr[4:].startswith(prefix)


def contains(vanity, bech_addr: str) -> bool:
    return vanity in bech_addr


def letters(vanity, bech_addr: str) -> bool:
    return vanity <= sum(not c.isdigit() for c in bech_addr[4:])


def digits(vanity, bech_addr: str) -> bool:
    return vanity <= sum(c.isdigit() for c in bech_addr[4:])


def _is_valid_addr(predicates, candidate: str) -> Optional[str]:
    is_valid = set()
    for predicate, vanity in predicates.items():
        is_valid.add(predicate(vanity, candidate))
    if False in is_valid:
        return None
    return candidate


def find_vanity_addr(predicates: Dict[Callable, str], event: Event(), queue: Queue):
    while not event.is_set():
        candidate, pub, priv = generate_wallet()
        if _is_valid_addr(predicates, candidate):
            queue.put((candidate, pub, priv))
