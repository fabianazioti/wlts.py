#
# This file is part of Python Client Library for WLTS.
# Copyright (C) 2020-2021 INPE.
#
# Python Client Library for WLTS is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.
#
"""WLTS Python Client Examples."""
from wlts import WLTS

# Specify the URL of the WLTS instance to be used
service = WLTS(url='https://brazildatacube.dpi.inpe.br/wlts/', access_token='change-me')

# Example of trajectory operation
# Make sure the collection is available in service
tj = service.tj(latitude=-12.0, longitude=-54.0, collections='prodes_amazonia_legal')

print(tj.trajectory)

# # Example of trajectory operation passing a list of latitude and longitude
# Make sure the collection is available in service
tj_m = service.tj(latitude=[-12.0, -10.3378], longitude=[-47.3200, -54.0],
                  collections='prodes_amazonia_legal,mapbiomas_amazonia-v5', start_date='2010')
for tj in tj_m['trajectories']:
    print(tj.trajectory)
#
# Example of trajectory operation with geometry
# The collection name may not be same.
# Make sure the collection is available in service
tj_two = service.tj(latitude=-10.3378, longitude=-47.3200, collections='prodes_cerrado', geometry=True)
print(tj_two.trajectory)
