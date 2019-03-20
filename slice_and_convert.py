import pandas as pd

# dataset: http://observatorio.ministeriodesarrollosocial.gob.cl/casen-multidimensional/casen/basedatos.php

name = 'Casen 2017'
encoding = 'latin-1'

reader = pd.read_stata( f"{name}.dta", chunksize=100000, convert_categoricals=False, encoding=encoding )
df = pd.DataFrame()
c = 0
for chunk in reader:
    c += 1
    chunk.to_csv( f"{name}_{c}.csv", index=False, encoding=encoding )
    chunk.to_stata( f"{name}_{c}.dta", write_index=False, encoding=encoding )
    df = df.append( chunk )
df.to_csv( f"{name}.csv", index=False, encoding=encoding )
df.to_stata( f"{name}_new.dta", write_index=False, encoding=encoding )