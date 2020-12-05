W = 25
H = 6

im = []

orbits = []

# assume one line
with open('inp8.txt', 'r') as f:
    for line in f:
        im = line

    im = [int(im[i]) for i in range(len(im)-1)]

'''
layers = []
for i in range(len(im)//(H*W)):
    layer = []
    im_ = im[i*(H*W):]
    for ind in range(H*W):
        layer.append(im_[ind])

    layers.append(layer)

zeros = []
for layer in layers:
    numzeros = len([i for i in layer if i == 0])
    zeros.append(numzeros)

mostest = layers[zeros.index(min(zeros))]
ones = len([i for i in mostest if i == 1])
twos = len([i for i in mostest if i == 2])

print(ones * twos)
'''


#im = [0,2,2,2,1,1,2,2,2,2,1,2,0,0,0,0] # let's call this a 3x3 im
#H, W = 2,2
layers = len(im) // (H*W)

spatial_im = []
offset = 0
for layer in range(layers):
    spatial = []
    for h in range(H):
        row = []
        for w in range(W):
            row.append(im[offset])
            offset += 1

        spatial.append(row)
    spatial_im.append(spatial)


def print_im(image):
    lp = 0

    for r, row in enumerate(image[lp]):
        str_ = ''
        for offset, elem in enumerate(row):
            llp = lp

            while(elem == 2):
                elem = image[llp][r][offset]
                llp += 1

            str_ = str_ + str(elem) + ' '
        print(str_)

print_im(spatial_im)
