# SALTSTACK TTP

Repository to store TTP based SALTSTACK modules:

- salt-tto execution module
- salt-tto runner module

TTP modules [pull request](https://github.com/saltstack/salt/pull/58754)

## Motivation

TTP is a library for parsing semi structured text using templates. 

TTP execution and runner modules allow to run commands against minions to obtain text output, parse it using TTP templates and return structured data.

Sample use cases that TTP can help to address:

- reporting across several minions by parsing text output and returning text tables
- transforming text data in structured format for storing in mine
- time series data can be produced using TTP templates and pushed to databases using returners
- compliance testing by parsing text into structured data with further processing and analysis to detect deviations
- Given that text data can be transformed into structured data of arbitrary hierarchy, this modules can significantly expand functionality in the area of minions state analysis and processing.

## Installation

To use TTP execution module make sure to install salt-ttp on minion, to use TTP runner module make sure to install salt-ttp on master. From [PyPi distribution](https://pypi.org/project/salt-ttp/0.1.0/)

```
pip install salt_ttp
```

To use templates from [TTP templates collection](https://github.com/dmulyalin/ttp_templates), need to install them as well:

```
pip install ttp_templates
```

# How to use

Run commands to explore doc strings for further usage:

```
salt minion-id sys.doc ttp
```
