# NFT Sniffer

A Python tool that monitors network traffic and captures NFT data from responses to https://portals-market.com/api/market/actions/, storing the data in MongoDB.

## Requirements

- Python 3.6+
- pyshark
- pymongo
- Admin/root privileges (required for packet sniffing)
- MongoDB server running

## Installation

Ensure you have the required packages installed:

```bash
pip install pyshark pymongo
```

Additionally, you need:
- Wireshark/TShark installed on your system (required by pyshark)
- MongoDB server running (default: localhost:27017)

## Configuration

Edit `nft_sniffer.py` to modify these settings if needed:

```python
# MongoDB configuration
MONGO_URI = "mongodb://localhost:27017/"
DB_NAME = "nft_data"
COLLECTION_NAME = "nfts"

# Target URL pattern to match
TARGET_URL = "portals-market.com/api/market/actions/"
```

## Usage

Run the script with administrative privileges:

```bash
# On Windows
# Run Command Prompt/PowerShell as Administrator
python nft_sniffer.py

# On Linux/Mac
sudo python nft_sniffer.py
```

The script will:
1. Connect to MongoDB
2. Start capturing network traffic 
3. Filter for HTTP/HTTPS traffic
4. Process packets that match the target URL
5. Extract NFT data and store it in MongoDB with the NFT id as the key

Press `Ctrl+C` to stop the capture.

## Data Structure

Each NFT is stored in MongoDB with the following structure:

```
{
  "id": "<nft_id>",
  "name": "<nft_name>",
  "photo_url": "<url_to_photo>",
  "collection_id": "<collection_id>",
  "external_collection_number": <number>,
  "price": "<price>",
  "status": "<status>",
  "animation_url": "<url_to_animation>",
  "has_animation": <boolean>,
  "attributes": [
    {
      "type": "<attribute_type>",
      "value": "<attribute_value>",
      "rarity_per_mille": <rarity_value>
    },
    ...
  ],
  "emoji_id": "<emoji_id>",
  "is_owned": <boolean>,
  "floor_price": "<floor_price>",
  "captured_at": "<timestamp>",
  "action_type": "<action_type>",
  "action_amount": "<action_amount>",
  "action_created_at": "<action_timestamp>"
}
```

## Notes

- The script creates a unique index on the `id` field to prevent duplicates
- When an NFT with an existing ID is captured, its data is updated in the database
- This script requires administrative privileges to capture packets
- This tool is for educational purposes only
