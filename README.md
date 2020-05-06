# V2Migration
A Python tool for migrating REP from Augur V1 to V2

* Python 3.6+ required
* USB Libs required: `sudo apt-get install libusb-1.0-0-dev libudev-dev`

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

Specifying this value script is run with the command:

```
ETHEREUM_PRIVATE_KEY=[PRIVATE_KEY] migrate
```

The script will wait for confirmation of the action it will take before signing and sending transactions.

## Future

Ledger support will be added in the next release