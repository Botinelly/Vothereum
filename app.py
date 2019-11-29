import json
from web3 import Web3


#Conexao com smartContract do remix-ide
ganache_url = "http://localhost:7545"
web3 = Web3(Web3.HTTPProvider(ganache_url))
address = web3.toChecksumAddress("0x722E1Dd982Bb57ec31bB0d977Fe3633Ec64930e4")

web3.eth.defaultAccount = web3.eth.accounts[0]

abi = json.loads('[{"constant":false,"inputs":[{"name":"_greeting","type":"string"}],"name":"setGreeting","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"greet","outputs":[{"name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"greeting","outputs":[{"name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"inputs":[],"payable":false,"stateMutability":"nonpayable","type":"constructor"}]')

contract = web3.eth.contract(address = address, abi = abi)


print(contract.functions.greet().call())

tx_hash = contract.functions.setGreeting("DROGA, EH O BRAIA").transact()

print(tx_hash)

web3.eth.waitForTransactionReceipt(tx_hash)

print('Updated greeting: {}'.format(
    contract.functions.greet().call()



#Conexao com a blockchain e transacao

"""
print(web3.isConnected())

account1 = "0xC8f137a60d4DF7dF5eFA6a612Ef0b2a7495672B2"
account2 = "0x7B9346fF44380D454C2D01821109B901e76Ae09F"

private_key = "1d3843182cbf4931978c5b6a5f84f75f3428e274a2d6bdd583616b293217c147"

#nonce
nonce = web3.eth.getTransactionCount(account1)

#Transacao
tx = {
    'nonce': nonce,
    'to': account2,
    'from': account1,
    #preco da transacao
    'value': web3.toWei(1, 'ether'),
    #gas = taxa da transacao
    'gas': 2000000,
    'gasPrice': web3.toWei('50', 'gwei')
}

#Assinar a transacao

signed_tx = web3.eth.account.signTransaction(tx, private_key)
tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)
print(web3.toHex(tx_hash))
#Enviar a transacao
#pegar o hash da transacao

"""