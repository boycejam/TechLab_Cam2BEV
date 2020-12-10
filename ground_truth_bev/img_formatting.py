from PIL import Image

imgs = './images-2-23-14-04-04'

SIZE = 1169
a = ["%04d" % x for x in range(SIZE)]
b = ["%07d" % x for x in range(SIZE)]
c = ["%07d" % x for x in range(1000, 1000 + SIZE * 500, 500)]

for i in range(0, SIZE):

    img_num = a[i]
    new_num = c[i]

    # for training
    im = Image.open('./images-2-23-14-07-23/frame' + img_num + '.jpg')
    im.save('./images-2-23-14-07-23/new_imgs/t_0_0_' + new_num + '.png')

    # for validation
    im = Image.open('./images-2-23-14-07-23/frame' + img_num + '.jpg')
    im.save('./images-2-23-14-07-23/new_imgs/v_0_' + new_num + '.png')
    