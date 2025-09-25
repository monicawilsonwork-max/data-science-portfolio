# GPU Setup & Verification

This folder contains a simple notebook (`gpu_verification.ipynb`) that verifies GPU availability in Google Colab.  
GPU access is an important prerequisite for training and testing machine learning models efficiently.

## Notebook Overview
- **Check GPU Availability**: Confirms if a GPU is accessible in Colab.  
- **Display GPU Details**: Uses `nvidia-smi` to show type, memory, and CUDA version.  
- **Framework Integration**: Verifies CUDA support in PyTorch.

## Why This Matters
Many machine learning workflows rely on GPU acceleration for training deep learning models.  
This notebook provides a quick way to ensure that your Colab environment is ready for ML experiments.

## How to Use
1. Open the notebook in Google Colab.  
2. Run all cells to verify GPU access.  
3. If a GPU is not available, change runtime type:  
   - Go to **Runtime > Change runtime type**  
   - Select **GPU** as the hardware accelerator  
   - Save and re-run the notebook  
