import google.generativeai as genai


#GOOGLE_API_KEY --> Obter no site https://aistudio.google.com/ --> Get API Key
google_api_key = ""
genai.configure(api_key=google_api_key)

#Setando parâmetros
var_generation_config = {
    "candidate_count": 1, 
    "temperature": 0.5,
}

#Configurações de segurança
#Valores disponíveis [BLOCK_NONE, BLOCK_FEW, BLOCK_SOME, BLOCK_MOST]
var_safety_settings = {
   "HARASSMENT": "BLOCK_NONE", 
   "HATE": "BLOCK_NONE",
   "SEXUAL": "BLOCK_NONE",
   "DANGEROUS": "BLOCK_NONE",
}

#Escolha do modelo
var_model_name = "gemini-1.0-pro"

model = genai.GenerativeModel(model_name=var_model_name,
                              generation_config=var_generation_config,
                              safety_settings=var_safety_settings)


#Criando um chat
chat = model.start_chat(history=[])

prompt = input("Esperando prompt: ")

while(prompt != "sair"):
    response = chat.send_message(prompt)
    print("Resposta: " , response.text, "\n")
    prompt = input("Esperando prompt: ")