# release3_inspection
This repository contains data, code and documentation related to manual inspection of [HPLT v3](https://hplt-project.org/datasets/v3.0).  

## Purpose of inspection
We want to get a rough idea about the actual content of the cleaned version of the 3rd data release. More specifically, for each language L we want to estimate the proportion of documents that are:
1) not in the language L,
2) contain undesirable artifacts, 
3) fully undesirable because they are mostly unnatural,
4) undesirable porn texts.

## Data for round 1 of HPLT 3.0 (cleaned) inspection: 
* samples stratified by language,
*  5 batches of random documents per language,
*  200 documents per batch,
*  full text for texts shorter than 1500 characters, otherwise the first 500 characters, the last 500 characters and 500 characters from the middle of the text.


## Inspection
Inspection is performed by volunteers who were mostly the members of the HPLT project. Volunteers inspect languages 
which they are native or fluent speakers of following the [guidelines](GUIDELINES.md).

## Results
Data:
- [the original sample](sample)
- [the sample converted to a format appropriate for annotation, partially annotated](annot_round1)
- [observations provided by the annotators](observations/README.md)
- [all annotated documents in one file along with annotations](annotated.tsv)

Analysis:
- [summary table](results_per_lang.tsv)
- [detailed analysis](Proportions-HPLTv3.ipynb)

# Acknowledgements

This project has received funding from the European Union’s Horizon Europe research and innovation programme under grant agreement No 101070350 and from UK Research and Innovation (UKRI) under the UK government’s Horizon Europe funding guarantee [grant number 10052546]
