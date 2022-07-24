# Tableau Connected Apps

A collection of [Tableau Connected Apps](https://www.tableau.com/about/blog/2022/1/how-seamlessly-integrate-analytics-your-product-connected-apps) code samples. Connected Apps is the latest [JWT](https://jwt.io/) authentication and SSO method available on the Tableau platform. Authentication via this method is supported for both Tableau's [REST API](https://help.tableau.com/current/api/rest_api/en-us/REST/rest_api.htm) and for displaying visualization using the [Embedding API v3](https://help.tableau.com/current/api/embedding_api/en-us/index.html). To understand how these APIs and Connected Apps work together to extend the Tableau platform and add analytical capabilities to your application, refer to the [Embedded Analytics Playbook](https://tableau.github.io/embedding-playbook/).

![Tableau & JWT banner](assets/images/tableau+jwt.png)

</br>

## Table of Contents
- [Tableau Connected Apps](#tableau-connected-apps)
  - [Table of Contents](#table-of-contents)
  - [Requirements](#requirements)
  - [Installation](#installation)
  - [Dependencies](#dependencies)

</br>

![Tableau Connected Apps Diagram](assets/images/connectedapp_how.png)

## Requirements

This list covers requirements for local development and deployment to Heroku (note that you are free to deploy this server on other platforms).

- [Python](https://www.python.org/) version 3.8.8
- [Anaconda](https://www.anaconda.com/) or some other Python environment manager (optional but recommended)
- Tableau Server or Tableau Online site (a developer site is available for free by signing up for the [developer program](https://www.tableau.com/developer))

</br>

## Installation

1. Clone this repository
```bash
git clone git@github.com:stephenlprice/tableau-connected-apps.git
# or
git clone https://github.com/stephenlprice/tableau-connected-apps.git

# navigate inside the project directory
cd tableau-connected-apps
```
1. Create a `conda` environment to install all dependencies and activate it (see [Dependencies](#dependencies) for more info.)
```bash
# will create an environment called tableau-webhooks
conda env create -f environment.yml

# activates the environment
conda activate tableau-connected-apps
```
> ##### *__NOTE__: if you are not using `conda` you can create a `requirements.txt` file or install the dependencies listed in the `environment.yml` file manually with `pip3`.*
</br>

3. Create a `.env` file in the project's root directory and add values for each environment variable described in the [example file](#environment-variables) (`example-env`)
```bash
# create the .env file
touch .env
```
> ##### *__NOTE__: the script will raise a `RuntimeError` if these environment variables are not declared.*
</br>

4. Run the script
```bash
# enter the repo's python folder
cd python
# run the script
python index.py
```

</br>

## Dependencies

This project was built with [Anaconda](https://www.anaconda.com/), therefore the development environment can be cloned from the `environment.yml` file. Most dependencies are installed with `conda` while the last three are installed with `pip3`. 

If you are new to `conda` I recommend keeping the [conda cheatsheet](https://docs.conda.io/projects/conda/en/4.6.0/_downloads/52a95608c49671267e40c689e0bc00ca/conda-cheatsheet.pdf) nearby for reference.

```yaml
name: tableau-connected-apps
channels:
  - defaults
dependencies:
  - python=3.8.8
  - requests=2.28.1
  - pip=21.2.4
  - pip:
    - python-dotenv==0.19.2
    - pyjwt[crypto]==2.4.0
```

It is possible to recreate this environment without Anaconda, using something like [virtualenvwrapper](https://virtualenvwrapper.readthedocs.io/en/latest/). In that case you can install all dependencies with `pip3` and write a `requirements.txt` file to document your dependencies.

</br>