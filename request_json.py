import requests
import json
import csv


url = "https://api.suthubservice.com/v0/sales"
headers = {'Content-Type': 'application/json', 'api-key': 'eb9484921d678843bbfdd6bf460a1df7'}
response = requests.get(url, headers=headers).content
r_dict = json.loads(response)
cachorros = {}

def main():
    try:
        for resp in r_dict["response"]:
            for policies in resp["policies"]:
                for covered_goods in policies["covered_goods"]:
                    if covered_goods.get("Nome"):
                        if covered_goods.get("Nome") in cachorros:
                            cachorros[covered_goods.get("Nome")] += 1
                        else:
                            cachorros[covered_goods.get("Nome")] = 1

        with open("data.csv", "w", newline='') as csvFile:

            coluns = ['nome_pet', 'contador']
            writer = csv.DictWriter(csvFile, fieldnames=coluns)
            writer.writeheader()
            for nm, ct in cachorros.items():
                writer.writerow({'nome_pet': nm, 'contador': ct})
            print("Arquivo Data.Csv Criado com Sucesso!")
    except Exception as e:
        print("Error"+ e)


if __name__ == '__main__':
    main()
