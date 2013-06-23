"""Account object.

These account objects are rather simple and dumb; they do not contain the list
of their associated postings. This is achieved by building a realization; see
realization.py for details.
"""
import re
from collections import namedtuple


# A type used to represent an account read in.
Account = namedtuple('Account', 'name type')

def account_from_name(account_name):
    "Create a new account solely from its name."
    return Account(account_name, account_type(account_name))

def account_parent_name(name):
    """Return the name of the parent account of the given account."""
    components = name.split(':')
    components.pop(-1)
    return ':'.join(components)

def account_leaf_name(name):
    """Get the name of the leaf of this account."""
    return name.split(':')[-1]

def account_sortkey(account):
    """Sort a list of accounts, taking into account the type of account.
    Assets, Liabilities, Equity, Income and Expenses, in this order, then
    in the order of the account's name."""
    return (TYPES_ORDER[account.type], account.name)

def account_names_sortkey(account_name):
    """Sort a list of accounts, taking into account the type of account.
    Assets, Liabilities, Equity, Income and Expenses, in this order, then
    in the order of the account's name."""
    account_type = account_name.split(':')[0]
    return (TYPES_ORDER[account_type], account_name)

# FIXME: This may not be hard-coded, needs to be read from options.
TYPES_ORDER = dict((x,i) for (i,x) in enumerate('Assets Liabilities Equity Income Expenses'.split()))

def account_type(name):
    """Return the type of this account's name."""
    return name.split(':')[0]

def is_account_name(string):
    """Return true if the given string is an account name."""
    return re.match('(Asset|Liabilities|Equity|Income|Expenses)', string)

def is_account_root(account_name):
    """Return true if the account name is one of the root accounts."""
    return ':' not in account_name

def is_balance_sheet_account(account):
    return account.type in ('Assets', 'Liabilities', 'Equity')
    # FIXME: Remove these hardcoded strings; use the options instead.

def is_balance_sheet_account_name(account_name, options):
    return account_type(account_name) in (
        options[x] for x in ('name_assets',
                             'name_liabilities',
                             'name_equity'))

def is_income_statement_account(account):
    return account.type in ('Income', 'Expenses')
    # FIXME: Remove these hardcoded strings; use the options instead.
