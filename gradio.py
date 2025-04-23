import gradio as gr

# Assuming you have your model loaded (e.g., some NLP model)
def process_input(input_text):
    # Your model processing code (like entity extraction, etc.)
    return "Processed output here"

# Define Gradio interface
iface = gr.Interface(fn=process_input, inputs="text", outputs="text")

# Launch the interface
iface.launch()
