# V2Migration
A Python tool for migrating REP from Augur V1 to V2

* Python 3.6+ **required**

## RUN STEPS

```
1. git clone git@github.com:augurproject/V2Migration.git
2. cd V2Migration
3. virtualenv venv
4. . venv/bin/activate
5. pip install -e .
6. ETHEREUM_HTTP=[YOUR_ETHEREUM_HTTP_ENDPOINT] ETHEREUM_PRIVATE_KEY=[YOUR_PRIVATE_KEY] migrate
```

## Setup

```sh
git clone git@github.com:augurproject/V2Migration.git
cd V2Migration
```

Then run these install commands:

```sh
virtualenv venv
. venv/bin/activate
pip install -e .
```

## Running The Script

When run the script will convert all V1 REP owned by an account into V2 REP.

To run the private key of the account must be available as an environment variable `ETHEREUM_PRIVATE_KEY`.

If a local Ethereum endpoint is not running you will also need to specify one with the enviornment variable `ETHEREUM_HTTP`.

Specifying this value script is run with the command:

```
ETHEREUM_PRIVATE_KEY=[PRIVATE_KEY] migrate
```

The script will wait for confirmation of the action it will take before signing and sending transactions.
