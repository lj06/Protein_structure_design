import requests

def download_pdb(file_path):
    base_url = "https://alphafold.ebi.ac.uk/files/AF-{uni_id}-F1-model_v4.pdb"
    
    # Read UniProt IDs from file
    with open(file_path, 'r') as file:
        uniprot_ids = [line.strip() for line in file]
    
    for uni_id in uniprot_ids:
        url = base_url.format(uni_id=uni_id)
        response = requests.get(url)
        if response.status_code == 200:
            file_path = f"D:\\Users\\Zzz\\Desktop\\CX4803\\{uni_id}.pdb"  # specify your directory here
            with open(file_path, 'wb') as f:
                f.write(response.content)
            print(f"Downloaded: {file_path}")
        else:
            print(f"Failed to download {uni_id}: Status code {response.status_code}")

# Path to the file with UniProt IDs
file_path = "D:\\Users\\Zzz\\Desktop\\CX4803\\ecoli.txt"

download_pdb(file_path)
