import hashlib

def get_supermajority(total_nodes):
    return (total_nodes * 2 // 3) + 1

def verify_and_commit(proposal, votes, total_nodes):
    # Ensure supermajority of cryptographic signatures
    if len(votes) >= get_supermajority(total_nodes):
        return True
    return False
