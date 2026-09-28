from fastapi import FastAPI

# app. Representa a nossa aplicação inteira
app = FastAPI()

# O símbolo @ é uma etiqueta especial. Estamos dizendo: quando alguém acessar o endereço principal
# da nossa API (/) pedindo para ler dados (get), acione a função abaixo.
@app.get("/")

# Essa função fará as manipulações em nossa aplicação
def pagina_inicial():
    # Esse dicionário será convertido para json e disponibilizado em nossa api (tela)
    return {"mensagem": "Sei lá!"}





# uvicorn main:app --reload # Ele inicia e gerencia o nosso servidor local
