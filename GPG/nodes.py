"""
nodes.py
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

public api endpoints

SECURITY ADVISORY: best to use a "personal node" in production
"""


def eosio_nodes():
    """
    EOSIO https rest api endpoints tested MAY 2020
    """
    # alternatively you can use single private node in list
    # if using more than 1 node it is best to use at least 5
    return ["https://api.eosdetroit.io"]

    # tested as of July 2020
    
    # "https://api.tokenika.io",
    # "https://api1.eosasia.one",
    # "https://eos.greymass.com",
    # "https://api.eosdetroit.io",
    # "https://bp.cryptolions.io",
    # "https://mainnet.eoscannon.io",
    # "https://user-api.eoseoul.io",
    # "https://node.eosflare.io",
    # "https://api.eossweden.se",
    # "https://eosbp.atticlab.net",
    # "https://node1.eosphere.io",
    # "https://node2.eosphere.io",



def bitshares_nodes():
    """
    Bitshares websocket endpoints tested MAY 2020
    """
    # alternatively you can use single private node in list
    # if using more than 1 node it is best to use at least 5
    return [
        "wss://node3.deexnet.org/ws",
        "wss://api.bitshares.bhuz.info/wss",
        "wss://node5.deexnodes.net/ws",
        "wss://kimziv.com/wss",
        "wss://ru-kha.walldex.pro/ws",
        "wss://ru-msk.walldex.pro/wss",
        "wss://france.walldex.pro/wss",
        "wss://spain.walldex.pro/wss",
        "wss://node6.deexnet.org/wss",
        "wss://node1.deex.exchange/wss",
        "wss://api.bts.mobi/wss",
        "wss://api.61bts.com/wss",
        "wss://korea.walldex.pro/ws",
        "wss://singapore.walldex.pro/wss",
        "wss://ca-bc.walldex.pro/wss",
        "wss://bitshares.openledger.info/ws",
        "wss://node2.deexnodes.net/ws",
        "wss://uk.walldex.pro/ws",
        "wss://node.bitshares.eu",
        "wss://node6.deexnet.com/wss",
        "wss://poland.walldex.pro/wss",
        "wss://india.walldex.pro/ws",
        "wss://ru-nsk.walldex.pro/wss",
        "wss://node4.deexnet.org/ws",
        "wss://node1.deexnodes.net/wss",
        "wss://netherlands.walldex.pro/wss",
        "wss://node4.deexnodes.net/wss",
        "wss://germany.walldex.pro/ws",
        "wss://blockzms.xyz/ws",
        "wss://eu.nodes.bitshares.ws/wss",
        "wss://brazil.walldex.pro/ws",
        "wss://node3.deexnet.com/wss",
        "wss://btsws.roelandp.nl/wss",
        "wss://ukraine.walldex.pro/wss",
        "wss://btsfullnode.bangzi.info/wss",
        "wss://sg.nodes.bitshares.ws/ws",
        "wss://eu.openledger.info/wss",
        "wss://us-tx.walldex.pro/ws",
        "wss://node7.deexnet.com/wss",
        "wss://us-va.walldex.pro/ws",
        "wss://bts.open.icowallet.net/wss",
        "wss://citadel.li/node/wss",
        "wss://dex.iobanker.com:9090/ws",
        "wss://api.dex.trading/wss",
        "wss://node5.deexnet.org/wss",
        "wss://node1.deexnet.com/ws",
        "wss://node6.deexnodes.net/ws",
        "wss://us-mo.walldex.pro/wss",
        "wss://node7.deexnet.org/ws",
        "wss://node7.deexnodes.net/wss",
        "wss://node3.deexnodes.net/ws",
        "wss://hongkong.walldex.pro/ws",
        "wss://japan.walldex.pro/wss",
        "wss://chile.walldex.pro/ws",
        "wss://node5.deexnet.com/ws",
        "wss://node1.deexnet.org/wss",
        "wss://node2.deexnet.com/wss",
        "wss://australia.walldex.pro/wss",
        "wss://israel.walldex.pro/ws",
        "wss://us-fl.walldex.pro/wss",
        "wss://ru-spb.walldex.pro/wss",
        "wss://node2.deexnet.org/wss",
        "wss://node4.deexnet.com/ws",
        "wss://moscow.walldex.pro/ws",
        "wss://turkey.walldex.pro/wss",
        "wss://ca-qc.walldex.pro/wss",
        "wss://ru-ekb.walldex.pro/wss",
    ]


def eosio_universe():
    """
    all public api endpoints I could find; some in this list do not connect though
    """
    # https://github.com/greymass/anchor/blob/
    #    c29b5665083c854f0d7b27281587cfb3b2ffb398/nodes.md
    return [
        "https://api.tokenika.io",
        "https://api1.eosasia.one",
        "https://eos.greymass.com",  # operated by greymass
        "https://mainnet.eoscalgary.io",  # operated by EOS Cafe
        "https://api.eosnewyork.io",  # operated by EOS New York
        "https://api.eosdetroit.io",  # operated by EOS Detroit
        "http://api.hkeos.com",  # operated by HK EOS
        "https://bp.cryptolions.io",  # operated by CryptoLions
        "http://dc1.eosemerge.io:8888",  # operated by EOS Emerge Poland
        "https://dc1.eosemerge.io:5443",  # operated by EOS Emerge Poland
        "https://api1.eosdublin.io",  # operated by EOS Dublin
        "https://api2.eosdublin.io",  # operated by EOS Dublin
        "https://mainnet.eoscannon.io",  # operated by EOS Cannon
        "https://eos-api.privex.io",  # operated by Privex
        "https://eosapi.blockmatrix.network",  # operated by Block Matrix
        "https://user-api.eoseoul.io",  # operated by EOSeoul
        "https://api.eos.bitspace.no",  # operated by Bitspace
        "https://node.eosflare.io",  # operated by EOS Flare
        "https://api-eos.blckchnd.com",  # operated by BLCKCHND
        "https://mainnet.eosimpera.com",  # operated by EOS IMPERA
        "https://api.franceos.fr",  # operated by franceos
        "http://api.cypherglass.com",  # operated by Cypherglass
        "https://api.eossweden.se",  # operated by Sw/eden
        "https://nodes.eos42.io",  # operated by EOS42
        "http://api-mainnet.starteos.io",  # operated by Starteos
        "https://eosbp.atticlab.net",  # opeated by AtticLab
        "https://api1.eosdublin.io",  # operated by eosDublin
        "https://node1.eosphere.io",  # operated by EOSphere
        "https://node2.eosphere.io",  # operated by EOSphere
    ]


def unit_test_nodes():
    """
    print the list of nodes in use by the Gateway
    """
    print("bitshares nodes\n", bitshares_nodes(), "\n\n")
    print("bitshares nodes\n", eosio_nodes(), "\n\n")


if __name__ == "__main__":

    unit_test_nodes()
