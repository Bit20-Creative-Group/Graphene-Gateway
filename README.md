# Graphene-Python-Gateway
An Open Source Gateway for BitShares/Graphene Blockchains

    ╔══════════════════════════╗
    ║ ╔═╗┬─┐┌─┐┌─┐┬ ┬┌─┐┌┐┌┌─┐ ║
    ║ ║ ╦├┬┘├─┤├─┘├─┤├┤ │││├┤  ║
    ║ ╚═╝┴└─┴ ┴┴  ┴ ┴└─┘┘└┘└─┘ ║
    ║ ╔═╗┬ ┬┌┬┐┬ ┬┌─┐┌┐┌       ║
    ║ ╠═╝└┬┘ │ ├─┤│ ││││       ║
    ║ ╩   ┴  ┴ ┴ ┴└─┘┘└┘       ║
    ║ ╔═╗┌─┐┌┬┐┌─┐┬ ┬┌─┐┬ ┬    ║
    ║ ║ ╦├─┤ │ ├┤ │││├─┤└┬┘    ║
    ║ ╚═╝┴ ┴ ┴ └─┘└┴┘┴ ┴ ┴     ║
    ╚══════════════════════════╝


WTFPL litepresence.com Jan 2021

The deposit gateway is a 24/7 www.falconframework.org API server,

which the client will approach via JSON.

Upon request for a deposit address,

it launches an foreign chain block operation listener.

The listener will await an incoming transfer of foreign chain coins from the client, until timeout.

Upon "hearing" the transfer, the BitShares/Graphene side auto issues a respective UIA.

The withdrawal side is a 24/7 BitShares/Graphene block operation listener,

which upon hearing an incoming UIA deposit -

with a memo containing a withdrawal address,

it automatically withdraws the matching foreign chain asset to the client's account.

Both Deposit and Withdrawal are built to handle multi client / multi asset concurrency.

Currently gateway tokenization of the following coins are supported:

- EOSIO - EOS
- Ripple - XRP

# This project has been sponsored by www.bitshares.org 

and peer reviewed by BitShares core developer Dr. Christopher Sanborn


    NON STANDARD MODULES WHICH REQUIRE INSTALLATION

- falcon 
- pybitshares 
- eosiopy 
- requests
- websocket-client
- secp256k1
- ecdsa
- aioxrpy
