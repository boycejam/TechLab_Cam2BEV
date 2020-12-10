import numpy as np
import utils
palette = utils.parse_convert_xml("one_hot_conversion/convert_new.xml")
dist = utils.get_class_distribution("../data/our_data/val/bev+occlusion", (256, 512), palette)
weights = np.log(np.reciprocal(list(dist.values())))
print(weights)