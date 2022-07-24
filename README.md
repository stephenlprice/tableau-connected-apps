# Tableau Connected Apps

A collection of [Tableau Connected Apps](https://www.tableau.com/about/blog/2022/1/how-seamlessly-integrate-analytics-your-product-connected-apps) code samples. Connected Apps is the latest [JWT](https://jwt.io/) authentication and SSO method available on the Tableau platform. Authentication via this method is supported for both Tableau's [REST API](https://help.tableau.com/current/api/rest_api/en-us/REST/rest_api.htm) and for displaying visualization using the [Embedding API v3](https://help.tableau.com/current/api/embedding_api/en-us/index.html). To understand how these APIs and Connected Apps work together to extend the Tableau platform and add analytical capabilities to your application, refer to the [Embedded Analytics Playbook](https://tableau.github.io/embedding-playbook/).

![Tableau & JWT banner](assets/images/tableau+jwt.png)

</br>

## Table of Contents
- [Tableau Connected Apps](#tableau-connected-apps)
  - [Table of Contents](#table-of-contents)
  - [Requirements](#requirements)
  - [Installation](#installation)

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