import streamlit as st
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM, BitsAndBytesConfig

# Configuración para carga en 4-bit (BitsAndBytes)
bnb_config = BitsAndBytesConfig(
    load_in_4bit=True,
    bnb_4bit_use_double_quant=True,
    bnb_4bit_quant_type="nf4",
    bnb_4bit_compute_dtype=torch.float16
)

# Ruta al modelo ya mergeado (modelo completo con LoRA fusionado)
model_path = "./tinyllama_merged"

# Cargar tokenizer y modelo
tokenizer = AutoTokenizer.from_pretrained(model_path, use_fast=True)
model = AutoModelForCausalLM.from_pretrained(
    model_path,
    device_map="auto",
    quantization_config=bnb_config,
    trust_remote_code=False
)

model.eval()  # Para desactivar el cálculo de gradientes

# Función para generar respuestas
def generar_respuesta(prompt, max_tokens=200, temperature=0.7):
    inputs = tokenizer(prompt, return_tensors="pt").to(model.device)
    with torch.no_grad():
        output = model.generate(
            **inputs,
            max_new_tokens=max_tokens,
            do_sample=True,
            temperature=temperature,
            top_p=0.95,
            top_k=50,
            repetition_penalty=1.1,
            pad_token_id=tokenizer.eos_token_id
        )
    respuesta = tokenizer.decode(output[0], skip_special_tokens=True)
    return respuesta

# Interfaz Streamlit
st.title("Asistente TinyLlama para SQL, Python y Finanzas")

user_input = st.text_area("Escribe tu pregunta aquí:", height=150)

if st.button("Generar respuesta"):
    if user_input.strip():
        prompt = f"### Human: {user_input}\n### Assistant:"
        respuesta = generar_respuesta(prompt)
        st.markdown("**Respuesta:**")
        st.write(respuesta)
    else:
        st.warning("Por favor, ingresa una pregunta válida.")