import gradio as gr
from PIL import Image
from transformers import BlipProcessor, BlipForConditionalGeneration

model_path = r"C:\Users\prbt3\OneDrive\Desktop\Finetuning-BLIP-Transformer-Model\blip_flickr8k_finetuned"
processor = BlipProcessor.from_pretrained(model_path)
model = BlipForConditionalGeneration.from_pretrained(model_path)

def generate_caption(image):
    raw_image = Image.open(image).convert("RGB")
    text = "a photography of"
    inputs = processor(raw_image, text, return_tensors="pt")
    output = model.generate(**inputs)
    caption = processor.decode(output[0], skip_special_tokens=True)
    return caption

iface = gr.Interface(
    fn=generate_caption,
    inputs=gr.Image(type="filepath"),
    outputs=gr.Textbox(label="Generated Caption"),
    title="Image Captioning with Fine-Tuned BLIP",
    description="Upload an image and generate a caption using the fine-tuned BLIP model."
)

if __name__ == "__main__":
    iface.launch()
