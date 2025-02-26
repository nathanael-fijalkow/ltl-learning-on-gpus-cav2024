## LTL learning on GPUs

This repo contains all the code and benchmarks for reproducing the paper

- *LTL learning on GPUs*, by [M. Valizadeh](https://www.linkedin.com/in/mojtaba-valizadeh-phd-3b98b67a/), [N. Fijalkow](https://games-automata-play.com/) and [M. Berger](https://martinfriedrichberger.net/). Draft: https://arxiv.org/abs/2402.12373, publisher's version: https://link.springer.com/chapter/10.1007/978-3-031-65633-0_10.

This work builds on https://github.com/MojtabaValizadeh/paresy and addresses scalability issues. The paper  appeared at CAV 2024 (36th International Conference on Computer Aided Verification) in July 2024. The file 

- `cav-2024-submission-5511.zip`

contains all the code. The code has been tested on Google Colab. We will add a detailed description of how to run it on Colab before CAV.

The directory `benchmarks` contains all the benchmarks used in the paper. The construction of our benchmarks is described in Section 7. Our benchmarks use the  trace format described in 

- https://github.com/rajarshi008/Scarlet

## Colab Notebook
This work is presented on a Google Colab notebook platform, which automatically clones this GitHub repository and comes fully equipped with all necessary dependencies and libraries, eliminating the need for additional installations. You can run the scripts by clicking on the designated buttons and adjusting inputs as needed.

To access the notebook, please use the link below and follow the instructions provided.
- https://colab.research.google.com/github/MojtabaValizadeh/ltl-learning-on-gpus/blob/main/LTL_Learning_on_GPUs.ipynb

## Citations

```
@inproceedings{ValizadehM:ltlleaog,
	address = {Cham},
	author = {Valizadeh, Mojtaba and Fijalkow, Nathana{\"e}l and Berger, Martin},
	booktitle = {Computer Aided Verification},
	doi = {10.1007/978-3-031-65633-0_10},
	editor = {Gurfinkel, Arie and Ganesh, Vijay},
	isbn = {978-3-031-65633-0},
	pages = {209--231},
	publisher = {Springer Nature Switzerland},
	title = {{LTL Learning on GPUs}},
	url = {https://doi.org/10.1007/978-3-031-65633-0_10},
	year = {2024},
	bdsk-url-1 = {https://doi.org/10.1007/978-3-031-65633-0_10}}
```

```
@misc{ValizadehM:ltlleaog_software,
	author = {Valizadeh, Mojtaba and Fijalkow, Nathana{\"e}l and Berger, Martin},
	title = {{Software for: LTL Learning on GPUs}}, 
	year={2024},
	howpublished = {\url{https://github.com/MojtabaValizadeh/ltl-learning-on-gpus}}
}
