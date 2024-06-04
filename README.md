# Output Files

## Articles

Currently, articles are fetched using the euroPMC API. 
https://europepmc.org/RestfulWebService

We also use the same API to fetch papers which cite each paper from Blue Brain Project.

##### articles.csv

Each line here will correspond to exactly one article.
We have the following properties:
* uid: unique identifier for this paper. Right now this is the same as the "europmc_id".
* title: title of the paper.
* publication date
* source: the API used to fetch metadata for this paper. Currently we only use "europmc".
* is_bbp: will be True if this article was in the input csv for the script "gather_articles.py"
* abstract
* doi
* pmid: PubMed identifier: https://pubmed.ncbi.nlm.nih.gov/
* europmc_id: unique identifier used by EuroPMC for this article
* url: link to the full text

Example:

| uid       | title                                                | publication_date | source  | is_bbp | abstract                                                                                                   | doi                           | pmid     | europmc_id | url                                                                                                      |
|-----------|------------------------------------------------------|------------------|---------|--------|------------------------------------------------------------------------------------------------------------|-------------------------------|----------|------------|----------------------------------------------------------------------------------------------------------|
| 31121126  | The Scientific Case for Brain Simulations            | 2019-05-22       | europmc | True   | A key element of the European Union’s Human Brain Project (HBP)...                                         | 10.1016/j.neuron.2019.03.027  | 31121126 | 31121126   | https://www.sciencedirect.com/science/article/pii/S0896627319302909?via%3Dihub                           |
| 38645618  | Neurobiological Causal Models of Language Processing | 2024-04-01       | europmc | False  | The language faculty is physically realized in the neurobiological infrastructure of the human brain...   | 10.1162/nol_a_00133           | 38645618 | 38645618   |                                                                                                          |

##### article_cites_article.csv

Each line will contain a "source" and a "target" article, where target is the cited article while source is the
article citing it. The id is the same as the uid in articles.csv.

Example:

| article_uid_source | article_uid_target |
|--------------------|--------------------|
| 31121126           | 31121126           |
| 38645618           | 31121126           |
| 38470935           | 31121126           |
| 38408099           | 31121126           |
| 38410682           | 31121126           |

##### authors.csv

A list of unique authors found in any of the articles.
The author information is fetched using the Orcid API: https://info.orcid.org/documentation/features/public-api/
It is possible that some article's authors are not found in this public database,
in which case they will not be included here.

Example:

| orcid_id           | author_name         |
|--------------------|---------------------|
| 0000-0001-9080-8502 | Torbjørn V Ness     |
| 0000-0002-8251-8860 | Viktor Jirsa        |
| 0000-0002-2915-720X | Werner Van Geit     |
| 0000-0001-5157-247X | Elisabetta Iavarone |
| 0000-0002-3149-4934 | Christian O'Reilly  |
| 0000-0002-8245-0392 | Karl Magnus Petersson |


##### institutions.csv

This table contains the institutions recorded by Orcid that any of the authors were affiliated to
at one point. 

Example:

| name                                 | organization_id                      | organization_id_source | 
|--------------------------------------|--------------------------------------|------------------------|
| University of Stuttgart              | grid.5719.a                          | GRID                   | 
| The University of Manchester         | 5292                                 | RINGGOLD               |
| Aix-Marseille Université             | http://dx.doi.org/10.13039/100007586 | FUNDREF                |
| CNRS Marseille                       |                                      |                        |
| Florida Atlantic University          | http://dx.doi.org/10.13039/100008778 | FUNDREF                |
| University of Ghent                  |                                      |                        |

##### author_wrote_article.csv

This table represents the author-article relationship where
an author took part in the writing of the article. 
It contains all authors, not just first authors.

Example:

| author_uid        | article_uid                     |
|-------------------|---------------------------------|
| 0000-0001-7162-4425 | 10.1016/j.neuron.2019.03.027    |
| 0000-0001-9080-8502 | 10.1016/j.neuron.2019.03.027    |
| 0000-0002-8251-8860 | 10.1016/j.neuron.2019.03.027    |
| 0009-0000-8821-2312 | 10.1162/nol_a_00133             |
| 0000-0002-8245-0392 | 10.1162/nol_a_00133             |
| 0000-0002-4247-0356 | 10.1371/journal.pbio.3002539    |
| 0000-0003-0358-0074 | 10.1371/journal.pcbi.1011108    |
| 0000-0003-3848-914X | 10.3389/fninf.2024.1156683      |
| 0000-0001-6173-1884 | 10.1038/s41380-023-02337-z      |

##### author_affiliated_with_institution.csv

This table contains author-institution relationships and when
each author was part of an institution.

Example:

| author_uid        | institution_uid                      | start_date | end_date   |
|-------------------|--------------------------------------|------------|------------|
| 0000-0001-9080-8502 | a20b5b81                             | 2011-02-01 | 2014-12-18 |
| 0000-0001-9080-8502 | a20b5b81                             | 2014-12-18 |            |
| 0000-0002-8251-8860 | grid.5719.a                          |            |            |
| 0000-0002-8251-8860 | 5292                                 |            |            |
| 0000-0002-8251-8860 | http://dx.doi.org/10.13039/100007586 |            |            |
| 0000-0002-8251-8860 | c167e3fa                             |            |            |
| 0000-0002-8251-8860 | http://dx.doi.org/10.13039/100008778 |            |            |
| 0000-0002-8245-0392 | 27106                                |            |            |
