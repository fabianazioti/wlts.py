#
# This file is part of Python Client Library for WLTS.
# Copyright (C) 2020-2021 INPE.
#
# Python Client Library for WLTS is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.
#
"""WLTS Python Client Examples."""
from lccs import LCCS

from wlts import WLTS

# Define Services
service_wlts = WLTS(url='https://brazildatacube.dpi.inpe.br/dev/wlts/', access_token='change-me')
service_lccs = LCCS(url='https://brazildatacube.dpi.inpe.br/dev/lccs/')

# Find the classification system of collections
collection_1 = service_wlts['terraclass_amazonia-v2'].classification_system
collection_2 = service_wlts['mapbiomas_amazonia-v5'].classification_system

# Show available classification system mappings
mp = service_lccs.available_mappings(f'{collection_1["classification_system_name"]}-{collection_1["classification_system_version"]}')
mp2 = service_lccs.available_mappings(f'{collection_2["classification_system_name"]}-{collection_2["classification_system_version"]}')

# Get a trajectory for a target system
tj = service_wlts.tj(latitude=-6.282295, longitude=-52.53655,
					collections='terraclass_amazonia-v2,mapbiomas_amazonia-v5',
					target_system=mp[0])
print(tj.df())