import hashlib as hasher
import datetime as date
import numpy as np
#%%
# Define what a Snakecoin block is
class Block:
  def __init__(self, patient_uid, timestamp, ids, previous_hash):
    self.patient_uid = patient_uid
    self.timestamp = timestamp
    self.ids = ids
    self.previous_hash = previous_hash
    self.hash = self.hash_block()
  
  def hash_block(self):
    sha = hasher.sha256()
    sha.update(str(self.patient_uid) + str(self.timestamp) + str(self.ids) + str(self.previous_hash))
    return sha.hexdigest()

# Generate genesis block
def create_genesis_block():
  # Manually construct a block with
  # patient_uid zero and arbitrary previous hash
  return Block(0, date.datetime.now(), "Genesis Block", "0")

# Generate all later blocks in the blockchain
def next_block(last_block,patient_uid,ids):
  this_patient_uid = patient_uid
  this_timestamp = date.datetime.now()
  this_ids = ids
  this_hash = last_block.hash
  return Block(this_patient_uid, this_timestamp, this_ids, this_hash)

def fetch_block(blockchain,patient_uid):
    for block in blockchain:
        if block.patient_uid == patient_uid:
            print "Printing Patient IDS Record"
            print "Total IDS Score: ",block.ids[7]
            print "N1: ",block.ids[0]
            print "N2: ",block.ids[1]
            print "N3: ",block.ids[2]
            print "N4: ",block.ids[3]
            print "N5: ",block.ids[4]
            print "N6: ",block.ids[5]
            print "N7: ",block.ids[6]
#%% 
# Create the blockchain and add the genesis block
blockchain = [create_genesis_block()]
previous_block = blockchain[0]
#%% 
# How many blocks should we add to the chain
# after the genesis block
num_of_blocks_to_add = 20
#%% 
# Add blocks to the chain
for i in range(0, num_of_blocks_to_add):
  patient_uid = np.random.randint(100000000,999999999)
  ids = np.random.randint(2, size=7)
  ids = np.append(ids,np.sum(ids))  
  block_to_add = next_block(previous_block,patient_uid,ids)
  blockchain.append(block_to_add)
  previous_block = block_to_add
  # Tell everyone about it!
  print "Block #{} has been added to the blockchain!".format(block_to_add.patient_uid)
  print "Hash: {}\n".format(block_to_add.hash) 

#%%
fetch_block(blockchain,709927446)
fetch_block(blockchain,955003839)
#%%   
