# create_catalog.py
# Generates a combined CUBE Voyager catalog file for a simple 4-step model.

content = """CATALOG
    NAME = Simple4Step
    DESCRIPTION = "Combined Catalog for Simple 4-Step Model"

DATASET ZONES
    TYPE = DBF
    FILE = zones.dbf
    DESCRIPTION = "Traffic Analysis Zones"
ENDDATASET

DATASET HWYNET
    TYPE = NET
    FILE = highway.net
    DESCRIPTION = "Highway Input Network"
ENDDATASET

DATASET TRNET
    TYPE = PT
    FILE = transit.pt
    DESCRIPTION = "Transit Input Network"
ENDDATASET

DATASET TG_MAT
    TYPE = MAT
    FILE = tg_output.mat
    DESCRIPTION = "Trip Generation Matrix"
ENDDATASET

DATASET DIST_MAT
    TYPE = MAT
    FILE = distribution.mat
    DESCRIPTION = "Trip Distribution Matrix"
ENDDATASET

DATASET MC_MAT
    TYPE = MAT
    FILE = modechoice.mat
    DESCRIPTION = "Mode Choice Matrix"
ENDDATASET

DATASET ASSIGN_MAT
    TYPE = MAT
    FILE = assign_demand.mat
    DESCRIPTION = "Assignment Demand Matrix"
ENDDATASET

DATASET TIME_SKIM
    TYPE = MAT
    FILE = skim_time.mat
    DESCRIPTION = "Travel Time Skims"
ENDDATASET

DATASET DIST_SKIM
    TYPE = MAT
    FILE = skim_distance.mat
    DESCRIPTION = "Distance Skims"
ENDDATASET

ENDCATALOG
"""

with open("model.cat", "w") as f:
    f.write(content)

print("model.cat created successfully.")