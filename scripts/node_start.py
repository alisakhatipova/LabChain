import argparse
import logging
import os
import sys

# append project dir to python path
from labchain.blockchainNode import BlockChainNode

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
if parent_dir not in sys.path:
    sys.path.append(parent_dir)

# set TERM environment variable if not set
if 'TERM' not in os.environ:
    os.environ['TERM'] = 'xterm-color'

CONFIG_FILE = os.path.join(os.path.dirname(__file__), '../labchain/resources/node_configuration.ini')

"""
def create_config_directory():
    os.makedirs(CONFIG_DIRECTORY, exist_ok=True)
"""


def create_node(node_port, peer_list):
    return BlockChainNode(CONFIG_FILE, node_port, peer_list)


def setup_logging(verbose):
    if verbose:
        logging.basicConfig(level=logging.DEBUG)
    else:
        logging.basicConfig(level=logging.WARNING)


def parse_args():
    parser = argparse.ArgumentParser(description='CLI node for Labchain.')
    parser.add_argument('--node_port', default=8080, help='The port address of the Labchain node')
    parser.add_argument('--peer_list', default='{}', help='The peer list address of the Labchain node')
    parser.add_argument('--verbose', '-v', action='store_true')
    return parser.parse_args()


if __name__ == '__main__':
    args = parse_args()
    setup_logging(args.verbose)
    node = create_node(args.node_port, args.peer_list)
