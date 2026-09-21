RUN PGM=HIGHWAY
  ;------------------------------
  ; MiniCube – Minimal Assignment
  ;------------------------------

  ; Input network
  NETI = "..\INPUTS\minicube.net"

  ; Input demand matrix (single class)
  MATI[1] = "..\INPUTS\demand.mat"

  ; All-or-Nothing (change to UE later if needed)
  METHOD = AON

  ; Assign demand from matrix 1
  VOL[1] = 1

  ; Write assigned network
  NETO = "..\OUTPUTS\assigned.net"
ENDRUN