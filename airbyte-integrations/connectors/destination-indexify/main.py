#
# Copyright (c) 2024 Airbyte, Inc., all rights reserved.
#


import sys

from destination_indexify import DestinationIndexify

if __name__ == "__main__":
    DestinationIndexify().run(sys.argv[1:])
