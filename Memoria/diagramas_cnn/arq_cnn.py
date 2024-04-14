import sys
sys.path.append('./PlotNeuralNet/')
from pycore.tikzeng import *

arch = [
    to_head('./PlotNeuralNet'),
    to_cor(),
    to_begin(),
    to_Conv("conv1", 224, (3, 3), offset = "(0,0,0)", to = "(0,0,0)", height = 64, depth = 64, width = 3, caption = "Conv2D"), 
    to_Pool("pool1", offset = "(2,0,0)", to = "(conv1-east)", height = 32, depth = 32, width = 3, caption = "MaxPool2D"), 
    to_Conv("conv2", 109, (3, 3), offset = "(3.5,0,0)", to = "(pool1-east)", height = 31, depth = 31, width = 3),
    to_connection("pool1", "conv2"), 
    to_Pool("pool2", offset = "(2,0,0)", to = "(conv2-east)", height = 15, depth = 15, width = 3),
    to_Conv("conv3", 52, (3, 3), offset = "(2.5,0,0)", to = "(pool2-east)", height = 14, depth = 14, width = 3),
    to_connection("pool2", "conv3"), 
    to_Pool("pool3", offset = "(1.5,0,0)", to = "(conv3-east)", height = 7, depth = 7, width = 3),
    to_SoftMax("dense1", 43264 ,"(2.5,0,0)", "(pool3-east)", caption = "Flatten"),
    to_connection("pool3", "dense1"),  
    to_SoftMax("dense2", 8 ,"(2.5,0,0)", "(dense1-east)", depth = 20, caption = "Dense"),  
    to_connection("dense1", "dense2"),
    to_SoftMax("softmax", 4 ,"(2.5,0,0)", "(dense2-east)", depth = 10, caption = "Softmax"),
    to_connection("dense2", "softmax"),
    to_end()

    # \draw[densely dashed]
    # (conv1-nearnortheast) -- (pool1-nearnorthwest)
    # (conv1-nearsoutheast) -- (pool1-nearsouthwest)
    # (conv1-farsoutheast)  -- (pool1-farsouthwest)
    # (conv1-farnortheast)  -- (pool1-farnorthwest)

    # (conv2-nearnortheast) -- (pool2-nearnorthwest)
    # (conv2-nearsoutheast) -- (pool2-nearsouthwest)
    # (conv2-farsoutheast)  -- (pool2-farsouthwest)
    # (conv2-farnortheast)  -- (pool2-farnorthwest)

    # (conv3-nearnortheast) -- (pool3-nearnorthwest)
    # (conv3-nearsoutheast) -- (pool3-nearsouthwest)
    # (conv3-farsoutheast)  -- (pool3-farsouthwest)
    # (conv3-farnortheast)  -- (pool3-farnorthwest)
    # ;

    ]

def main():
    namefile = str(sys.argv[0]).split('.')[0]
    to_generate(arch, namefile + '.tex' )

if __name__ == '__main__':
    main()