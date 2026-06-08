# Automated Outreach Pipeline

A command-line Python application that automates B2B outreach by discovering similar companies, identifying decision makers, and sending personalized outreach emails.

## Overview

The pipeline accepts a seed company domain and performs the following workflow:

1. Discover similar companies
2. Find decision makers within those companies
3. Retrieve contact information
4. Generate personalized outreach messages
5. Send emails through Brevo after user confirmation

## Architecture

Seed Company Domain

↓

CompanyEnrich Lookalike Search API( Alternative To Ocean.io)

↓

Prospeo Search Person API

↓

Decision Maker Discovery

↓

Email Personalization

↓

Brevo Email API

↓

Email Delivery

## Features

* Company discovery using CompanyEnrich API
* Decision-maker discovery using Prospeo API
* Personalized outreach generation
* Real email delivery using Brevo API
* Environment variable configuration
* Modular service-based architecture
* User confirmation before sending emails

## APIs Used

### CompanyEnrich (Alternative to Ocean.io)

Used to discover companies similar to the seed company.

Example:

google.com

↓

youtube.com

↓

facebook.com

↓

x.com

### Prospeo

Used to discover decision makers and company contacts.

Returns:

* Name
* Job Title
* LinkedIn Profile
* Company Information

### Brevo

Used for transactional email delivery.

Verified functionality:

* API integration successful
* Email delivery successful
* Message IDs returned by Brevo

## Tech Stack

* Python
* Requests
* python-dotenv
* REST APIs
* Modular Service Architecture

## Project Structure

services/

├── ocean.py      # CompanyEnrich integration
├── prospeo.py    # Contact discovery
├── eazyreach.py  # Email enrichment layer
├── brevo.py      # Email delivery

main.py

config.py

.env

## How to Run

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python main.py



## Sample Execution

Input:

google.com

Output:

CompanyEnrich status: 200
Prospeo status: 200
Brevo status: 201

Companies found: 3
Contacts found: 3
Emails found: 3


## Notes

* Ocean.io was unavailable during testing due to account restrictions.
* CompanyEnrich was integrated as the company discovery provider.
* API keys are stored securely using environment variables.
* The pipeline requires user confirmation before sending emails.
