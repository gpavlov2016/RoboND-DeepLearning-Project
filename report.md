
### Network Architecture
The network has three downsampling encoders implemented using separable convolution with a stride of 2x2 with batch normalization between the layers. The fully connected layer is one by one convolution with deminsional reduction to 64 filters instead of 128 for the input layer. After the one by one convolutions there are 3 upsampling decoders implemented using bilinear upsampling with skip connections from the encoders between them and additional one by one convolutions to reduce depth after concatenation and introduce additional non-linearities.

```
_________________________________________________________________
Layer (type)                 Output Shape              Param #   
=================================================================
input_1 (InputLayer)         (None, 160, 160, 3)       0         
_________________________________________________________________
separable_conv2d_keras_1 (Se (None, 80, 80, 64)        283       
_________________________________________________________________
batch_normalization_1 (Batch (None, 80, 80, 64)        256       
_________________________________________________________________
separable_conv2d_keras_2 (Se (None, 40, 40, 128)       8896      
_________________________________________________________________
batch_normalization_2 (Batch (None, 40, 40, 128)       512       
_________________________________________________________________
separable_conv2d_keras_3 (Se (None, 20, 20, 128)       17664     
_________________________________________________________________
batch_normalization_3 (Batch (None, 20, 20, 128)       512       
_________________________________________________________________
conv2d_1 (Conv2D)            (None, 20, 20, 64)        73792     
_________________________________________________________________
batch_normalization_4 (Batch (None, 20, 20, 64)        256       
_________________________________________________________________
bilinear_up_sampling2d_1 (Bi (None, 40, 40, 64)        0         
_________________________________________________________________
concatenate_1 (Concatenate)  (None, 40, 40, 192)       0         
_________________________________________________________________
separable_conv2d_keras_4 (Se (None, 40, 40, 128)       26432     
_________________________________________________________________
batch_normalization_5 (Batch (None, 40, 40, 128)       512       
_________________________________________________________________
bilinear_up_sampling2d_2 (Bi (None, 80, 80, 128)       0         
_________________________________________________________________
concatenate_2 (Concatenate)  (None, 80, 80, 192)       0         
_________________________________________________________________
separable_conv2d_keras_5 (Se (None, 80, 80, 128)       26432     
_________________________________________________________________
batch_normalization_6 (Batch (None, 80, 80, 128)       512       
_________________________________________________________________
bilinear_up_sampling2d_3 (Bi (None, 160, 160, 128)     0         
_________________________________________________________________
conv2d_2 (Conv2D)            (None, 160, 160, 3)       387       
=================================================================
Total params: 156,446
Trainable params: 155,166
Non-trainable params: 1,280
```

### Hyperparameters
#### Epoch - 15 
After about 8 epochs the validation loss decreses very slow and after 15 epochs not at all.
#### Learning Rate - 0.001 
Higher learning rates tend to cause the validation error to be higher (overfitting) and lower learning rates do not produce better score but take longer to achieve it.
#### Batch Size - 32
Around the number of smaples ~6K divided by the number of steps in each epoch (200)

### One-by-one Convolutions
The main use of one-by-one convolutions in this project is to connect encoder part of the network to the decoder part of the network. It is the same as 2-d convolution with kernel size of 1. One of the nice features of one-by-one convolution is that it preserves spatial information such as the classified pixels can be overlaid on the original pixels. Another benefit of one-by-one transofrmation is reducing the number of filters (depth) going down the network. 

### Detecting other objects
During development the network was trained on labeled images with three types of objects (backgound, hero, other people) however the network can easily be trained to detect other people or even other objects. All is needed are labeled images with the person or object of interest labeled separately from other elements. 

## Future Enahancements
1. Data  - the number of samples in training data is hardly enough, especially when considering images that contain the hero. Amount of samples can be increased either by acquiring new samples or preforming data augmentation by, for example, horizontally flipping the images.
2. Network size - the current network is relatively small and is about the right size for the data available. With more data the network size can be increased by adding more layers, increasing the number of filters or adding more skip connections. Bigger networks with more data should be able to separate between increasingly small and similar classes.
3. Transferl learning - instead of training the whole network from scratch we can take a CNN such as VGG16 with weights trained on simialr database and replace the fully connected layer with decoders to upsample the data. In this case we will be able to freeze the convolutional parts of the network (original VGG16 weights) and train only the decoders.
