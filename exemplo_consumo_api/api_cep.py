import requests


def consultar_cep(cep: str):
    # Remove caracteres não numéricos (como traços ou pontos)
    cep_limpo = cep.replace("-", "").replace(".", "").strip()

    # Validação estrutural básica: CEP no Brasil deve ter 8 dígitos
    if len(cep_limpo) != 8 or not cep_limpo.isdigit():
        print("Erro: O CEP informado deve conter exatamente 8 dígitos numéricos.")
        return

    url = f"https://viacep.com.br/ws/{cep_limpo}/json/"

    try:
        # Faz a requisição HTTP GET
        resposta = requests.get(url, timeout=5)
        
        # Dispara exceção se o status code HTTP for de erro (4xx ou 5xx)
        resposta.raise_for_status()

        dados = resposta.json()

        # A ViaCEP retorna {"erro": "true"} quando o CEP tem 8 dígitos mas não existe
        if dados.get("erro"):
            print("Erro: CEP não encontrado na base de dados.")
            return

        # Exibição dos dados
        print("\n--- Endereço Encontrado ---")
        print(f"Logradouro:  {dados.get('logradouro')}")
        print(f"Bairro:      {dados.get('bairro')}")
        print(f"Cidade/UF:   {dados.get('localidade')}/{dados.get('uf')}")
        print(f"DDD:         {dados.get('ddd')}")

    except requests.exceptions.RequestException as e:
        print(f"Erro na conexão com o serviço: {e}")


if __name__ == "__main__":
    cep_digitado = input("Digite o CEP para consulta: ")
    consultar_cep(cep_digitado)
