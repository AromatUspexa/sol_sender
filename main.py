from solders.keypair import Keypair
from solana.rpc.api import Client
from pathlib import Path
from solders.pubkey import Pubkey
from solana.transaction import Transaction
from solders.system_program import TransferParams, transfer
from solana.rpc.core import RPCException

print('Не отправляйте на биржи меньше 0.01 SOL')

client = Client("https://api.mainnet-beta.solana.com")

keypair_list = [w for w in Path('from_wallets.txt').read_text(encoding="utf-8").replace("\n", " ").split()]
where_send_money = [w for w in Path('to_address.txt').read_text(encoding="utf-8").replace("\n", " ").split()]


for keypair, address in zip(keypair_list, where_send_money):
    resp = client.get_balance(Keypair.from_base58_string(keypair).pubkey())
    wallet_address = Keypair.from_base58_string(keypair).pubkey()
    remainder = resp.value - 900_000
    if remainder < 950_000:
      print('Не хватет на комиссию...')
    else:
        try:
            transaction = Transaction().add(transfer(TransferParams(
                from_pubkey=wallet_address,
                to_pubkey=Pubkey.from_string(address),
                lamports=remainder)
            ))
            keypair_sender = Keypair.from_base58_string(keypair)
            client.send_transaction(transaction, keypair_sender)
            print(f"{Keypair.from_base58_string(keypair).pubkey()} ==[ {resp.value / 1000000000} SOL ]==> {address}")
        except RPCException:
            print("Недстаточно комиссии")


