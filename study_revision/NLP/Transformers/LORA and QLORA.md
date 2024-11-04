# Understanding LoRA and QLoRA in LLMs

## 1. LoRA (Low-Rank Adaptation) Basics

### Core Concept
- Instead of fine-tuning all parameters, decompose weight updates into low-rank matrices
- Original weight matrix W → W + BA where:
  - B is matrix of size (r × d)
  - A is matrix of size (d × r)
  - r is the rank (hyperparameter, typically 8, 16, or 32)

### Key Components
- Pre-trained weights (W): Frozen during training
- LoRA matrices (A & B): Only parameters updated
- Rank (r): Controls compression ratio
- Alpha (α): Scaling factor, typically set equal to rank

### Memory Efficiency
```
Original parameters: d × d
LoRA parameters: 2 × d × r
Compression ratio: 2r/d
```

### Training Process
1. Load pre-trained model (W)
2. Initialize random A and B matrices
3. Compute W + (α/r)BA during forward pass
4. Update only A and B during backprop
5. Original weights W remain frozen

## 2. Alpha Parameter Deep Dive

### Purpose
- Controls update magnitude
- Helps stabilize training
- Makes updates rank-independent when α = r

### Common Settings
- Default: α = r
- Conservative: α = r/2
- Aggressive: α = r × 2

### When to Adjust
- Increase if: changes too subtle, slow convergence
- Decrease if: training unstable, model diverging

## 3. QLoRA (Quantized LoRA)

### Key Innovations
1. 4-bit quantization of base model
2. NormalFloat (NF4) quantization
3. Double quantization
4. Paged optimizer (CPU offloading)

### Memory Comparison (7B Model Example)
```
Regular LoRA:
- Base model: ~14GB (16-bit)
- Total needed: ~17GB

QLoRA:
- Base model: ~3.5GB (4-bit)
- Total needed: ~6GB
```

### Implementation Components
1. 4-bit base model quantization
2. 16-bit LoRA matrices
3. Paged AdamW optimizer
4. Double quantization for constants

## 4. Practical Implementation Guide

### LoRA Setup
```python
# Key hyperparameters
rank = 8
alpha = 8
learning_rate = 3e-4

# Final weight computation
final_weights = W + (alpha/rank) * BA
```

### QLoRA Setup
```python
config = BitsAndBytesConfig(
    load_in_4bit=True,
    bnb_4bit_quant_type="nf4",
    bnb_4bit_use_double_quant=True
)
```

## 5. When to Use What

### Use LoRA When
- Limited computational resources
- Need parameter-efficient fine-tuning
- Want to maintain multiple adaptations

### Use QLoRA When
- Very limited GPU memory (<24GB)
- Can trade training speed for memory
- Need extreme memory efficiency

## 6. Best Practices

### LoRA
1. Start with r=8, α=8
2. Monitor training stability
3. Adjust α if needed
4. Target attention layers first

### QLoRA
1. Use NF4 quantization
2. Enable double quantization
3. Use paged optimizers
4. Keep LoRA modules in 16-bit

## 7. Common Issues & Solutions

### Training Issues
- Unstable training → Reduce α
- Slow convergence → Increase α
- Memory errors → Switch to QLoRA
- Loss spikes → Check learning rate

### Inference Issues
- Memory spikes → Use merged weights
- Slow inference → Pre-merge W + BA
- Quality degradation → Increase rank

## 8. Performance Monitoring

### Key Metrics
1. Training loss convergence
2. Memory usage
3. Inference speed
4. Model quality metrics
5. Update magnitude: ||BA|| / ||W||

## 9. Advanced Tips

### Combining Multiple LoRAs
- Can merge multiple adaptations
- Need to manage scaling carefully
- Consider task relationships

### Memory Optimization
1. Use gradient checkpointing
2. Implement efficient attention
3. Optimize batch size
4. Use mixed precision training