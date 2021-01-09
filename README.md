# Graphene-Python-Gateway
An Open Source Gateway for Graphene Blockchains

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

The deposit gatewau is a 24/7 Falcon API server,

which the client will approach via JSON.

Upon request for a deposit address,

it will trigger EOSIO or Ripple block operation listeners run by the gateway admin.

The listeners will await an incoming transfer from the client until timeout.

Upon "hearing" the transfer, the BitShares side auto issues a respective UIA.

The withdrawal side is a 24/7 BitShares block operation listener,

which upon hearing an incoming UIA deposit -

with a memo containing a withdrawal address,

automatically withdraws the matching foreign chain asset to the client's account.

Both Deposit and Withdrawal are built to handle multi client / multi asset concurrency.

This project has been sponsored by bitshares.org 

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




