<span style="font-family: helvetica, arial, sans-serif; font-size: 10pt;">
import numpy as np
from PIL import Image</span>
<span style="font-family: helvetica, arial, sans-serif; font-size: 10pt;">images_list = ['HeroKnight(2).jpg', 'HeroKnight(2).jpg', 'HeroKnight(2).jpg']
imgs = [ Image.open(i) for i in images_list ]</span>

<span style="font-family: helvetica, arial, sans-serif; font-size: 10pt;">img_merge = Image.fromarray(img_merge)
img_merge.save( 'terracegarden_h.jpg' )</span>
