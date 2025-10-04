def bank_transaction(balance: int, transaction_type:str, amount:int) -> int:
    """
    Perform a bank transaction (deposit or withdrawal) on the current amount.

    Parameters:
    balance (int): The current amount in the bank account.
    transaction_type (str): The type of transaction ('deposit' or 'withdrawal').
    amount (int): The amount to deposit or withdraw.

    Returns:
    float: The new amount in the bank account after the transaction.
    """
    if amount < 0 or balance < 0:
        raise ValueError("Amount and balance must be non-negative.")
    if amount == 0:
        return balance
    if amount > 1000000:
        raise ValueError("Amount exceeds the maximum limit of 1,000,000.")
    if transaction_type == 'deposit':
        balance = balance + amount
    elif transaction_type == 'withdrawal':
        if amount > balance:
            raise ValueError("Insufficient funds for withdrawal.")
        balance = balance - amount
    else:
        raise ValueError("Invalid transaction type. Use 'deposit' or 'withdrawal'.")
    return balance
    

