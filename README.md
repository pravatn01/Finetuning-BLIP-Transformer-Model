# **Finetuning-BLIP-Transformer-Model**

This project demonstrates **how to fine-tune the BLIP (Bootstrapped Language-Image Pretraining) Transformer model** using a **subset of the Flickr8K dataset**. The fine-tuning process is implemented with the **Hugging Face Trainer**, showcasing a structured approach to adapting BLIP for **image captioning**.

## 🚀 **Project Overview**
- **Model:** BLIP Transformer  
- **Dataset:** Subset of Flickr8K (custom selection)  
- **Objective:** Fine-tune BLIP for improved image captioning  
- **Training Method:** Hugging Face Trainer API  
- **Large File Handling:** Git LFS for managing large model files  

## 🏋️ **Fine-Tuning Process**
- Training was conducted in **Google Colab** for efficient GPU access  
- Dataset preprocessing for BLIP compatibility  
- **Comparison between the pre-trained BLIP and fine-tuned BLIP** models to evaluate improvements  
- Hugging Face's Trainer API was used for training and evaluation  

## 🎯 **Results**
- The fine-tuned model **produces more context-aware and accurate captions**  
- A **direct comparison** with the original BLIP model was conducted in the Colab notebook  
- Fine-tuned BLIP shows improved generalization on unseen images  

## 🌐 **Web App Demo**
The trained model was used in a webapp **made using Gradio**, allowing users to input images and receive generated captions.

Below is a preview of the **web application demo**:  

![Web App Demo](image.png)
