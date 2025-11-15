```python
import gradio as gr
from transformers import pipeline, set_seed

generator = pipeline("text-generation", model="distilgpt2")
set_seed(42)

description = """
🚨 *Attention* : Les exemples générés sont uniquement à des *fins éducatives* sur le hacking éthique.  
L’objectif est de sensibiliser, pas de promouvoir l’usage malveillant.

👨‍💻 Pose une question ou un thème, comme :
- Comment fonctionne un test d'intrusion ?
- Exemples d'ingénierie sociale
- C’est quoi un hacker éthique ?
"""

def generate_text(prompt):
    result = generator(prompt, max_length=100, num_return_sequences=1)
    return result[0]["generated_text"]

demo = gr.Interface(
    fn=generate_text,
    inputs=gr.Textbox(lines=2, placeholder="Pose ta question ici...", label="Prompt"),
    outputs="text",
    title="Générateur éducatif - Hacking éthique",
    description=description,
    examples=[
        ["Explique le rôle d'un hacker éthique"],
        ["Qu'est-ce qu'une injection SQL ?"],
        ["Comment protéger un réseau Wi-Fi ?"]
    ]
)

if _name_ == "_main_":
    demo.launch()
```
