import requests
import pandas as pd

def fetch_fasta(uniprot_id):
    url = f"https://rest.uniprot.org/uniprotkb/{uniprot_id}.fasta"
    response = requests.get(url)
    if response.status_code == 200:
        print(f"Response for {uniprot_id}: {response.text[:100]}")
        sequence_parts = response.text.split('\n')
        if len(sequence_parts) > 1:
            sequence = ''.join(sequence_parts[1:])
            return sequence
        else:
            print(f"No sequence parts found after split for {uniprot_id}")
            return None
    else:
        print(f"Failed to download FASTA for {uniprot_id} with status code {response.status_code}")
        return None

def write_to_excel(file_path, output_file):
    with open(file_path, 'r') as file:
        uniprot_ids = [line.strip() for line in file if line.strip()]

    data = []
    for uniprot_id in uniprot_ids:
        sequence = fetch_fasta(uniprot_id)
        if sequence:
            data.append({'UniProt ID': uniprot_id, 'Sequence': sequence})
        else:
            print(f"No sequence fetched for {uniprot_id}")

    if data:
        df = pd.DataFrame(data)
        df.to_excel(output_file, index=False)
        print(f"Data written to {output_file}")
    else:
        print("No data to write.")

input_file = "Path\\ecoli.txt"
output_file = "Path\\uniprot_sequences.xlsx"
write_to_excel(input_file, output_file)
