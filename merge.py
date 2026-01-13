import pandas as pd
from pandas.api.types import is_numeric_dtype
from pathlib import Path
import seaborn as sns
import numpy as np


dfs = []
for d in Path('annot_round1').glob('*'):
    for i, sdf in enumerate(pd.read_json(f'sample/per_lang_1000/{d.name}.shuf.zst', lines=True, chunksize=200)):
        p = d / f'batch{i}.tsv'
        if not p.exists(): break  # all batches for a language in d are processed
        df = pd.read_csv(p, sep='\t').dropna(subset='id').set_index('id')
        sdf = sdf.set_index('id')
        assert (df.index==sdf.index).all()
        outdir = Path('sample_with_annots')/d.name
        outdir.mkdir(parents=True,exist_ok=True)
        pd.concat([sdf,df]).to_json(outdir / f'batch{i}.jsonl.zst',orient='records',lines=True)
        print(p)

